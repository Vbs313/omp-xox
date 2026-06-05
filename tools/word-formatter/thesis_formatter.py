#!/usr/bin/env python3
"""Thesis Formatter — recovered from Word-Formatter-Pro v2.7.4, adapted for thesis specs.

Usage: python thesis_formatter.py input.docx [output.docx]
"""
import sys, os, re, logging
from pathlib import Path
from docx import Document
from docx.document import Document as _Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, Cm

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
log = logging.getLogger(__name__)

# ── Thesis Spec ──
SPEC = {
    "paper": "A4",
    "margin_top": Cm(2.54), "margin_bottom": Cm(2.54),
    "margin_left": Cm(3.17), "margin_right": Cm(3.17),
    "margin_left_even": Cm(2.54), "margin_right_even": Cm(3.17),
    "body_font_cn": "宋体", "body_font_en": "Times New Roman",
    "body_size": Pt(12),          # 小四号 = 12pt
    "body_line_spacing": 1.5,
    "h1_size": Pt(16),            # 三号 = 16pt, bold, center
    "h2_size": Pt(14),            # 四号 = 14pt, bold, left
    "h3_size": Pt(12),            # 小四号 = 12pt, bold, left
    "chart_font_size": Pt(10.5),  # 五号 = 10.5pt
    "page_num_size": Pt(9),       # 小五号 = 9pt
}

RE_H1 = re.compile(r"^(第[一二三四五六七八九十百千]+章|\d+)[、\.\s]\s*(.+)")
RE_H2 = re.compile(r"^(\d+\.\d+)\s+(.+)")
RE_H3 = re.compile(r"^(\d+\.\d+\.\d+)\s+(.+)")
RE_HAS_CHINESE = re.compile(r"[\u4e00-\u9fff]")
RE_FIGURE = re.compile(r"^(图|Fig|Figure)\s*\d+")
RE_TABLE = re.compile(r"^(表|Table)\s*\d+")


class ThesisFormatter:
    """Apply thesis formatting specs to a .docx file."""

    def __init__(self):
        self.page = 0

    def _set_margins(self, section, is_even=False):
        section.top_margin = SPEC["margin_top"]
        section.bottom_margin = SPEC["margin_bottom"]
        section.left_margin = SPEC["margin_left_even"] if is_even else SPEC["margin_left"]
        section.right_margin = SPEC["margin_right_even"] if is_even else SPEC["margin_right"]
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)

    def _apply_font(self, run, cn_font=None, en_font=None, size=None, bold=False):
        cn = cn_font or SPEC["body_font_cn"]
        en = en_font or SPEC["body_font_en"]
        sz = size or SPEC["body_size"]
        run.font.size = sz
        run.font.bold = bold
        run.font.name = cn
        r = run._element
        rPr = r.get_or_add_rPr()
        rFonts = rPr.find(qn("w:rFonts"))
        if rFonts is None:
            rFonts = OxmlElement("w:rFonts")
            rPr.insert(0, rFonts)
        rFonts.set(qn("w:eastAsia"), cn)
        rFonts.set(qn("w:ascii"), en)
        rFonts.set(qn("w:hAnsi"), en)

    def _set_line_spacing(self, para):
        pf = para.paragraph_format
        pf.line_spacing = SPEC["body_line_spacing"]
        pf.space_before = Pt(0)
        pf.space_after = Pt(0)

    def _is_chart_caption(self, para):
        text = para.text.strip()
        if not text:
            return False
        if RE_FIGURE.match(text) or RE_TABLE.match(text):
            return True
        if text.startswith(("图", "Fig", "Table", "表")) and len(text) < 120:
            return True
        return False

    def _is_page_number_para(self, para, section_idx, para_idx):
        """Heuristic: footer paragraph with short numeric text."""
        text = para.text.strip()
        if len(text) <= 3 and text.isdigit():
            return True
        return False

    def _detect_heading_level(self, text):
        """Detect heading level from text pattern."""
        t = text.strip()
        m1 = RE_H1.match(t)
        if m1:
            return 1, m1.group(0)
        m2 = RE_H2.match(t)
        if m2:
            return 2, m2.group(0)
        m3 = RE_H3.match(t)
        if m3:
            return 3, m3.group(0)
        # Heuristic: bold + short + numeric prefix
        return 0, t

    def _format_paragraph(self, para, level=0):
        """Format a single paragraph according to thesis spec."""
        text = para.text.strip()
        self._set_line_spacing(para)

        # Chart/table captions
        if self._is_chart_caption(para):
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in para.runs:
                self._apply_font(run, size=SPEC["chart_font_size"], bold=False)
            return

        # Headings
        if level == 1:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            self._set_line_spacing(para)
            # Add blank line above/below
            pf = para.paragraph_format
            pf.space_before = Pt(12)
            pf.space_after = Pt(12)
            for run in para.runs:
                self._apply_font(run, size=SPEC["h1_size"], bold=True)
            return

        if level == 2:
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for run in para.runs:
                self._apply_font(run, size=SPEC["h2_size"], bold=True)
            return

        if level == 3:
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for run in para.runs:
                self._apply_font(run, size=SPEC["h3_size"], bold=True)
            return

        # Body text
        para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        para.paragraph_format.first_line_indent = Pt(24)  # 两个中文字符缩进
        for run in para.runs:
            self._apply_font(run, size=SPEC["body_size"], bold=False)

    def format(self, input_path, output_path=None):
        """Main entry: read .docx, apply formatting, save."""
        output_path = output_path or input_path.replace(".docx", "_formatted.docx")

        log.info(f"读取: {input_path}")
        doc = Document(input_path)

        # ── Page setup ──
        sections = doc.sections
        for i, sec in enumerate(sections):
            # Odd/even page margins for duplex printing
            if i == 0:
                self._set_margins(sec, is_even=False)
            elif i > 0 and i % 2 == 1:
                self._set_margins(sec, is_even=True)
            else:
                self._set_margins(sec, is_even=False)
            # Footer — page numbers
            footer = sec.footer
            if footer and footer.paragraphs:
                for fp in footer.paragraphs:
                    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    for run in fp.runs:
                        self._apply_font(run, size=SPEC["page_num_size"], cn="Times New Roman", en="Times New Roman")

        # ── Detect body start (after abstract/table of contents) ──
        body_started = False
        para_count = 0

        for para in doc.paragraphs:
            text = para.text.strip()

            # Detect first chapter/section → start body
            if not body_started and (RE_H1.match(text) or text.startswith("第")):
                body_started = True
                # Add page break before first chapter
                run = para.runs[0] if para.runs else para.add_run("")
                run._element.get_or_add_rPr().append(
                    OxmlElement("w:br") if False else None
                )

            if not body_started:
                # Front matter (abstract, TOC) — minimal formatting
                self._set_line_spacing(para)
                for run in para.runs:
                    self._apply_font(run, size=SPEC["body_size"])
                continue

            para_count += 1
            level, _ = self._detect_heading_level(text)
            self._format_paragraph(para, level=level)

        log.info(f"正文段落: {para_count}")
        log.info(f"保存: {output_path}")
        doc.save(output_path)
        return output_path


def main():
    if len(sys.argv) < 2:
        print("Usage: python thesis_formatter.py input.docx [output.docx]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    if not os.path.exists(input_path):
        log.error(f"文件不存在: {input_path}")
        sys.exit(1)

    formatter = ThesisFormatter()
    result = formatter.format(input_path, output_path)
    print(f"\n✅ Done: {result}")


if __name__ == "__main__":
    main()
