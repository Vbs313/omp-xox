#!/usr/bin/env bash
# detect-framework.sh — Detect test framework used by a project
#
# Usage: bash scripts/detect-framework.sh [project-directory]
#   Defaults to current directory if not specified.
#
# Returns: Name of the detected test framework (or "unknown") and key details.

set -euo pipefail

PROJECT_DIR="${1:-.}"
PROJECT_DIR="$(cd "$PROJECT_DIR" && pwd)"

detect_node() {
  local pkg="$PROJECT_DIR/package.json"
  [[ ! -f "$pkg" ]] && return 1

  # Check scripts first (most reliable signal), then devDependencies
  local scripts
  scripts=$(jq -r '(.scripts // {}) | to_entries[] | "\(.value)"' "$pkg" 2>/dev/null || echo "")

  local deps
  deps=$(jq -r '(.devDependencies // {}) + (.dependencies // {}) | keys[]' "$pkg" 2>/dev/null || echo "")

  # Vitest (check first — it may also have jest installed)
  if echo "$deps" | grep -q 'vitest'; then
    echo "vitest"
    return 0
  fi

  # Jest
  if echo "$deps" | grep -q 'jest'; then
    echo "jest"
    return 0
  fi

  # Mocha
  if echo "$deps" | grep -q 'mocha'; then
    local framework="mocha"
    echo "$deps" | grep -q 'chai' && framework+="+chai"
    echo "$deps" | grep -q 'sinon' && framework+="+sinon"
    echo "$framework"
    return 0
  fi

  # Ava
  if echo "$deps" | grep -q 'ava'; then
    echo "ava"
    return 0
  fi

  # Node test (built-in)
  if echo "$scripts" | grep -qE '\bnode --test\b'; then
    echo "node:test"
    return 0
  fi

  return 1
}

detect_python() {
  local cfg_dir="$PROJECT_DIR"
  # Check for pytest config files
  if [[ -f "$cfg_dir/pyproject.toml" ]] && grep -q '\[tool.pytest' "$cfg_dir/pyproject.toml" 2>/dev/null; then
    echo "pytest"
    return 0
  fi
  if [[ -f "$cfg_dir/pytest.ini" ]] || [[ -f "$cfg_dir/setup.cfg" ]] && grep -q '\[tool:pytest\]' "$cfg_dir/setup.cfg" 2>/dev/null; then
    echo "pytest"
    return 0
  fi
  if [[ -f "$cfg_dir/tox.ini" ]] && grep -q '\[pytest\]' "$cfg_dir/tox.ini" 2>/dev/null; then
    echo "pytest"
    return 0
  fi
  # Check if pytest is installed in the environment
  if command -v pytest &>/dev/null && [[ -f "$cfg_dir/requirements*.txt" || -f "$cfg_dir/Pipfile" || -f "$cfg_dir/pyproject.toml" ]]; then
    echo "pytest"
    return 0
  fi
  # Check for unittest (standard library — no config file)
  local test_files
  test_files=$(find "$PROJECT_DIR" -maxdepth 3 -name 'test_*.py' 2>/dev/null | head -5)
  if [[ -n "$test_files" ]] && grep -q 'import unittest' "$test_files" 2>/dev/null; then
    echo "unittest"
    return 0
  fi

  return 1
}

detect_go() {
  local go_mod="$PROJECT_DIR/go.mod"
  [[ ! -f "$go_mod" ]] && return 1
  echo "go-test"
  return 0
}

detect_rust() {
  local cargo="$PROJECT_DIR/Cargo.toml"
  [[ ! -f "$cargo" ]] && return 1
  echo "cargo-test"
  return 0
}

detect_ruby() {
  local gemfile="$PROJECT_DIR/Gemfile"
  [[ ! -f "$gemfile" ]] && return 1
  if grep -q 'rspec' "$gemfile" 2>/dev/null; then
    echo "rspec"
  else
    echo "minitest"
  fi
  return 0
}

detect_java() {
  local pom="$PROJECT_DIR/pom.xml"
  local gradle="$PROJECT_DIR/build.gradle"
  if [[ -f "$pom" ]]; then
    echo "maven+junit"
    return 0
  fi
  if [[ -f "$gradle" ]]; then
    grep -q 'junit' "$gradle" 2>/dev/null && echo "gradle+junit" || echo "gradle"
    return 0
  fi
  return 1
}

# ----- main -----
echo "Scanning project: $PROJECT_DIR"
echo ""

framework=""

detect_node && framework=$(detect_node)
if [[ -z "$framework" ]]; then detect_python && framework=$(detect_python); fi
if [[ -z "$framework" ]]; then detect_go && framework=$(detect_go); fi
if [[ -z "$framework" ]]; then detect_rust && framework=$(detect_rust); fi
if [[ -z "$framework" ]]; then detect_ruby && framework=$(detect_ruby); fi
if [[ -z "$framework" ]]; then detect_java && framework=$(detect_java); fi

if [[ -n "$framework" ]]; then
  echo "✅ Detected framework: $framework"
else
  echo "❌ Unknown test framework"
  echo ""
  echo "Could not detect a test framework. Common locations checked:"
  echo "  - package.json (Node.js: jest, vitest, mocha, ava)"
  echo "  - pyproject.toml / pytest.ini / setup.cfg (Python: pytest, unittest)"
  echo "  - go.mod (Go)"
  echo "  - Cargo.toml (Rust)"
  echo "  - Gemfile (Ruby: rspec, minitest)"
  echo "  - pom.xml / build.gradle (Java: JUnit)"
fi
