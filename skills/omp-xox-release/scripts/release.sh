#!/usr/bin/env bash
# omp-xox release script — bump version, commit, tag, push
#
# Usage:
#   ./scripts/release.sh patch    # 2.0.0 → 2.0.1
#   ./scripts/release.sh minor    # 2.0.1 → 2.1.0
#   ./scripts/release.sh major    # 2.1.0 → 3.0.0
#   ./scripts/release.sh 2.5.0    # explicit version

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../../.." && pwd)"
cd "$ROOT_DIR"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

info()  { echo -e "${GREEN}[INFO]${NC} $*"; }
warn()  { echo -e "${YELLOW}[WARN]${NC} $*"; }
error() { echo -e "${RED}[ERROR]${NC} $*" >&2; }
step()  { echo -e "${CYAN}[STEP]${NC} $*"; }

# ── Step 1: Validate ──

step "1/6 Validating..."

# Check git clean
if [[ -n "$(git status --porcelain)" ]]; then
    warn "Working tree has uncommitted changes"
    git status --short
fi

# Check TypeScript compiles
if ! bun --eval 'import("./index.ts").then(m=>console.log("OK:",typeof m.default))' 2>/dev/null; then
    error "TypeScript compilation failed"
    exit 1
fi

# Check extension count
EXT_COUNT=$(find extensions -name "index.ts" -maxdepth 2 | wc -l)
if [[ "$EXT_COUNT" -ne 9 ]]; then
    error "Expected 9 extensions, found $EXT_COUNT"
    exit 1
fi

info "Validation passed ($EXT_COUNT extensions)"

# ── Step 2: Determine version ──

step "2/6 Determining version..."

CURRENT_VERSION=$(python3 -c "import json; print(json.load(open('package.json'))['version'])")
info "Current version: $CURRENT_VERSION"

BUMP="${1:-patch}"

if [[ "$BUMP" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    NEW_VERSION="$BUMP"
else
    IFS='.' read -r MAJOR MINOR PATCH <<< "$CURRENT_VERSION"
    case "$BUMP" in
        major) NEW_VERSION="$((MAJOR + 1)).0.0" ;;
        minor) NEW_VERSION="${MAJOR}.$((MINOR + 1)).0" ;;
        patch) NEW_VERSION="${MAJOR}.${MINOR}.$((PATCH + 1))" ;;
        *) error "Invalid bump: $BUMP (use major|minor|patch or x.y.z)"; exit 1 ;;
    esac
fi

info "New version: $NEW_VERSION"

# ── Step 3: Update package.json ──

step "3/6 Updating package.json..."

python3 << PYEOF
import json

with open('package.json', 'r') as f:
    pkg = json.load(f)

pkg['version'] = '$NEW_VERSION'

with open('package.json', 'w') as f:
    json.dump(pkg, f, indent=2)
    f.write('\n')

print(f"package.json: {pkg['version']}")
PYEOF

# ── Step 4: Update marketplace.json ──

step "4/6 Updating marketplace.json..."

python3 << PYEOF
import json

with open('.claude-plugin/marketplace.json', 'r') as f:
    mkt = json.load(f)

mkt['plugins'][0]['version'] = '$NEW_VERSION'

with open('.claude-plugin/marketplace.json', 'w') as f:
    json.dump(mkt, f, indent=2)
    f.write('\n')

print(f"marketplace.json: {mkt['plugins'][0]['version']}")
PYEOF

# ── Step 5: Commit and tag ──

step "5/6 Committing and tagging..."

git add package.json .claude-plugin/marketplace.json
git commit -m "release: v$NEW_VERSION"
git tag -a "v$NEW_VERSION" -m "Release v$NEW_VERSION"

info "Tagged v$NEW_VERSION"

# ── Step 6: Push ──

step "6/6 Pushing..."

git push origin main --tags

info "Pushed to https://github.com/Vbs313/omp-xox"

# ── Summary ──

echo ""
echo -e "${GREEN}═══════════════════════════════════════════${NC}"
echo -e "${GREEN}  omp-xox v$NEW_VERSION released!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════${NC}"
echo ""
echo "Install: omp plugin install github:Vbs313/omp-xox"
echo "Or:      git clone https://github.com/Vbs313/omp-xox.git && cd omp-xox && ./install.sh"
echo ""
