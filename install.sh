#!/usr/bin/env bash
# omp-xox v2: Install script for OMP extension package
#
# Usage:
#   ./install.sh              # Link to user-level OMP extensions
#   ./install.sh --project    # Link to project-level OMP extensions
#   ./install.sh --uninstall  # Remove link

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACKAGE_NAME="omp-xox"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

info() { echo -e "${GREEN}[INFO]${NC} $*"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $*"; }
error() { echo -e "${RED}[ERROR]${NC} $*" >&2; }

usage() {
    cat <<EOF
omp-xox v2 Installer

Usage:
  ./install.sh              Link to user-level (~/.omp/agent/settings.json)
  ./install.sh --project    Link to project-level (.omp/settings.json)
  ./install.sh --uninstall  Remove from settings
  ./install.sh --check      Verify installation

This script registers omp-xox as an OMP extension package via settings.json.
OMP will automatically discover skills, prompts, agents, and the unified
extension entry point from this directory.
EOF
}

# ── Detect OMP config path ──

get_settings_path() {
    local scope="${1:-user}"
    if [[ "$scope" == "project" ]]; then
        echo "$(pwd)/.omp/settings.json"
    else
        echo "${HOME}/.omp/agent/settings.json"
    fi
}

# ── Ensure settings.json exists with valid JSON ──

ensure_settings() {
    local settings_path="$1"
    local settings_dir
    settings_dir="$(dirname "$settings_path")"

    if [[ ! -d "$settings_dir" ]]; then
        mkdir -p "$settings_dir"
    fi

    if [[ ! -f "$settings_path" ]]; then
        echo '{}' > "$settings_path"
    fi

    # Validate JSON
    if ! python3 -c "import json; json.load(open('$settings_path'))" 2>/dev/null; then
        warn "Invalid JSON in $settings_path, resetting to {}"
        echo '{}' > "$settings_path"
    fi
}

# ── Add extension path to settings.json ──

add_extension() {
    local settings_path="$1"
    local ext_path="$2"

    python3 << PYEOF
import json
import sys

settings_path = "$settings_path"
ext_path = "$ext_path"

with open(settings_path, 'r') as f:
    settings = json.load(f)

extensions = settings.get("extensions", [])
if not isinstance(extensions, list):
    extensions = []

if ext_path not in extensions:
    extensions.append(ext_path)
    settings["extensions"] = extensions
    with open(settings_path, 'w') as f:
        json.dump(settings, f, indent=2)
    print(f"Added: {ext_path}")
else:
    print(f"Already registered: {ext_path}")
PYEOF
}

# ── Remove extension path from settings.json ──

remove_extension() {
    local settings_path="$1"
    local ext_path="$2"

    python3 << PYEOF
import json

settings_path = "$settings_path"
ext_path = "$ext_path"

with open(settings_path, 'r') as f:
    settings = json.load(f)

extensions = settings.get("extensions", [])
if ext_path in extensions:
    extensions.remove(ext_path)
    settings["extensions"] = extensions
    with open(settings_path, 'w') as f:
        json.dump(settings, f, indent=2)
    print(f"Removed: {ext_path}")
else:
    print(f"Not found: {ext_path}")
PYEOF
}

# ── Check installation ──

check_install() {
    local settings_path="$1"
    local ext_path="$2"

    if [[ ! -f "$settings_path" ]]; then
        error "Settings not found: $settings_path"
        return 1
    fi

    python3 << PYEOF
import json

settings_path = "$settings_path"
ext_path = "$ext_path"

with open(settings_path, 'r') as f:
    settings = json.load(f)

extensions = settings.get("extensions", [])
if ext_path in extensions:
    print(f"OK: {ext_path} is registered")
else:
    print(f"NOT REGISTERED: {ext_path}")
    print(f"Current extensions: {extensions}")
PYEOF
}

# ── Main ──

main() {
    local action="install"
    local scope="user"

    for arg in "$@"; do
        case "$arg" in
            --project) scope="project" ;;
            --uninstall) action="uninstall" ;;
            --check) action="check" ;;
            --help|-h) usage; exit 0 ;;
            *) error "Unknown argument: $arg"; usage; exit 1 ;;
        esac
    done

    local settings_path
    settings_path="$(get_settings_path "$scope")"
    local ext_path="$SCRIPT_DIR"

    case "$action" in
        install)
            info "Installing omp-xox v2 ($scope scope)"
            ensure_settings "$settings_path"
            add_extension "$settings_path" "$ext_path"
            info "Settings: $settings_path"
            info "Extension: $ext_path"
            echo ""
            info "Installation complete. Restart OMP to load extensions."
            info "Quick test: omp -e $ext_path/index.ts --max-turns 1 --print 'list omp-xox tools'"
            ;;
        uninstall)
            info "Uninstalling omp-xox v2 ($scope scope)"
            ensure_settings "$settings_path"
            remove_extension "$settings_path" "$ext_path"
            info "Done. Restart OMP to unload extensions."
            ;;
        check)
            info "Checking omp-xox v2 installation ($scope scope)"
            check_install "$settings_path" "$ext_path"
            ;;
    esac
}

main "$@"
