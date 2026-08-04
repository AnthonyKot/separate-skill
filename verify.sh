#!/usr/bin/env bash
# Winning Is a Separate Skill — standing verification. Run from anywhere: ./verify.sh
#
# Ports the machinery of the earlier books and changes what it is allowed to
# promise. Counts are COMPUTED, never typed.
#
#   * checks/patchnotes.py  registered strings vs Valve's own datafeed   (GATING)
#   * checks/matches.py     registered events vs committed snapshots     (GATING)
#   * checks/data.py        bracket figures recomputed from their sample (GATING)
#   * checks/privacy.py     no identifiers in public or bracket snapshots     (GATING)
#   * checks/coverage.py    numbers in prose that match no claim            (ADVISORY)
#   * checks/register.py    banned vocabulary in chapter prose             (GATING)
#   * internal links        entirely inside this repository              (GATING)
#
# One check is advisory — coverage — because prose legitimately contains numbers
# that are not claims. Everything else is gating, which is deliberate for this
# series: every source above is either committed to this repository or is Valve's
# structured JSON. Live drift against the current game is a SEPARATE, non-failing
# run — see --drift — because a number moving is the game changing rather than the
# book being wrong.
#
# What a green build proves: every registered figure is present in the record it
# is attributed to, checked by something that could actually see that record. It
# does NOT prove the advice is right. Book 4 shipped a chapter whose every claim
# passed while its central causal arrow pointed backwards.
set -u
cd "$(dirname "$0")"
fail=0

case "${1:-}" in
  --links) only_links=1 ;;
  *) only_links=0 ;;
esac

if [ "$only_links" = "0" ]; then
  echo "== patch claims vs dota2.com datafeed (gating) =="
  python3 checks/patchnotes.py || fail=1

  echo "== match claims vs committed snapshots (gating) =="
  python3 checks/matches.py || fail=1

  echo "== bracket claims recomputed from their samples (gating) =="
  python3 checks/data.py || fail=1

  echo "== player identifiers in snapshots (gating) =="
  python3 checks/privacy.py || fail=1

  echo "== figures in prose vs registered claims (advisory) =="
  python3 checks/coverage.py

  echo "== banned vocabulary (gating) =="
  python3 checks/register.py || fail=1
fi

echo "== count sync (computed, not typed) =="
files=$(ls docs/chapters/*.html 2>/dev/null | wc -l | tr -d ' ')
links=$(grep -oE 'href="chapters/[0-9][^"]*\.html"' docs/index.html 2>/dev/null | sort -u | wc -l | tr -d ' ')
echo "  $files chapter files on disk; $links distinct chapter links on the contents page"
if [ "$files" != "$links" ]; then
  echo "  FAIL: contents page ($links) != chapter files ($files)"; fail=1
fi

echo "== internal links (gating) =="
python3 - <<'PY' || fail=1
import glob, os, re, sys
bad = 0
for path in glob.glob("docs/**/*.html", recursive=True):
    base = os.path.dirname(path)
    with open(path, encoding="utf-8") as f:
        html = f.read()
    for href in re.findall(r'href="([^"#?]+)', html):
        if href.startswith(("http://", "https://", "mailto:", "#", "//")):
            continue
        target = os.path.normpath(os.path.join(base, href))
        if not os.path.exists(target):
            print(f"  FAIL: {path} -> {href} (no such file)")
            bad += 1
print(f"  {bad} broken internal links")
sys.exit(1 if bad else 0)
PY

echo "== transcripts must never be committed =="
# data/transcripts/ is gitignored before it ever existed. This check exists because
# a .gitignore protects only against accident, not against `git add -f`, and the
# rule it enforces is a licensing one: caster commentary is someone else's
# expression and supplies no number in this book. See CONTEXT.md 5.
leaked=$(git ls-files 2>/dev/null | grep -cE '^data/transcripts/|\.(vtt|srt|json3)$' || true)
if [ "${leaked:-0}" != "0" ]; then
  echo "  FAIL: $leaked transcript file(s) are tracked by git"; fail=1
else
  echo "  none tracked"
fi

echo
if [ "$fail" = "0" ]; then
  echo "PASS"
else
  echo "FAIL"
fi
exit $fail
