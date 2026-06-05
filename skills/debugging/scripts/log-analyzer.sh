#!/usr/bin/env bash
# log-analyzer.sh — Parse log files for errors, stack traces, and patterns
#
# Usage: bash scripts/log-analyzer.sh <log-file> [options]
#
# Options:
#   --errors-only   Show only lines with ERROR/CRITICAL/FATAL/Exception
#   --stats         Show per-level message counts
#   --stacktraces   Extract Java/Python/JS stack traces
#   --since <time>  Filter lines after a timestamp (grep-compatible)
#   --help          Show this help

set -euo pipefail

show_help() {
  head -20 "$0" | grep -E "^#" | sed 's/^# //; s/^#$//'
  exit 0
}

# ----- parse flags -----
ERRORS_ONLY=false
SHOW_STATS=false
STACKTRACES=false
SINCE_FILTER=""

POSITIONAL=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --errors-only) ERRORS_ONLY=true; shift ;;
    --stats)       SHOW_STATS=true; shift ;;
    --stacktraces) STACKTRACES=true; shift ;;
    --since)       SINCE_FILTER="$2"; shift 2 ;;
    --help)        show_help ;;
    -*)
      echo "Unknown option: $1"
      show_help
      ;;
    *) POSITIONAL+=("$1"); shift ;;
  esac
done

LOG_FILE="${POSITIONAL[0]:-}"
if [[ -z "$LOG_FILE" ]]; then
  echo "Usage: bash scripts/log-analyzer.sh <log-file> [options]"
  echo "Try --help for details."
  exit 1
fi

if [[ ! -f "$LOG_FILE" ]]; then
  echo "Error: File not found: $LOG_FILE"
  exit 1
fi

# ---- filter lines if --since provided ----
INPUT="$LOG_FILE"
if [[ -n "$SINCE_FILTER" ]]; then
  TEMP=$(mktemp)
  # awk: print lines where $0 >= since_filter (string comparison works for ISO timestamps)
  awk -v since="$SINCE_FILTER" '{ if ($0 >= since || NR == 1) print }' "$LOG_FILE" > "$TEMP"
  INPUT="$TEMP"
fi

# ---- summary header ----
echo "========================================"
echo " Log Analysis: $(basename "$LOG_FILE")"
echo "========================================"
echo ""

# ---- level counts (always computed for stats) ----
ERROR_COUNT=$(grep -ciE '\b(error|critical|fatal|exception|traceback)\b' "$INPUT" 2>/dev/null || echo 0)
WARN_COUNT=$(grep -ciE '\b(warn|warning)\b' "$INPUT" 2>/dev/null || echo 0)
INFO_COUNT=$(grep -ciE '\binfo\b' "$INPUT" 2>/dev/null || echo 0)
DEBUG_COUNT=$(grep -ciE '\bdebug\b|\[DBG\]' "$INPUT" 2>/dev/null || echo 0)

if [[ "$SHOW_STATS" == true ]]; then
  echo "--- Log Level Stats ---"
  printf "  ERROR/WARN/INFO/DEBUG lines: %s / %s / %s / %s\n" "$ERROR_COUNT" "$WARN_COUNT" "$INFO_COUNT" "$DEBUG_COUNT"
  echo ""
fi

# ---- errors only mode ----
if [[ "$ERRORS_ONLY" == true ]]; then
  echo "--- Errors & Exceptions ---"
  grep -inE '\b(error|critical|fatal|exception|traceback)\b' "$INPUT" || echo "  (none)"
  echo ""
fi

# ---- stack trace extraction ----
if [[ "$STACKTRACES" == true ]]; then
  echo "--- Stack Traces ---"
  # Python/Java/.NET style: an error line followed by indented "at"/"File"/"  " lines
  awk '
    /Exception|Traceback|Error/ { capture=1; buf=$0; next }
    capture && /^[[:space:]]+(at |File |from |\.\.\.)/ { buf = buf ORS $0; next }
    capture { print buf; print ""; capture=0; buf="" }
    END { if (capture) print buf }
  ' "$INPUT" || echo "  (none)"
  echo ""
fi

# ---- if no flag, show a useful default view ----
if [[ "$ERRORS_ONLY" == false && "$SHOW_STATS" == false && "$STACKTRACES" == false ]]; then
  echo "--- Errors & Exceptions ---"
  grep -inE '\b(error|critical|fatal|exception|traceback)\b' "$INPUT" | head -40 || echo "  (none)"
  echo ""
  echo "--- Warnings ---"
  grep -inE '\b(warn|warning)\b' "$INPUT" | head -20 || echo "  (none)"
  echo ""
  echo "--- Stats ---"
  printf "  ERROR/WARN/INFO/DEBUG lines: %s / %s / %s / %s\n" "$ERROR_COUNT" "$WARN_COUNT" "$INFO_COUNT" "$DEBUG_COUNT"
fi

# ---- cleanup ----
if [[ -n "$SINCE_FILTER" ]]; then
  rm -f "$INPUT"
fi
