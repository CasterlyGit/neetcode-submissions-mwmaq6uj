#!/usr/bin/env python3
"""
Regenerate docs/index.html and docs/data.json from the current set of submissions
in this repo. Runs on every push (via .github/workflows/build-dashboard.yml) so
the live dashboard at https://casterlygit.github.io/neetcode-submissions-mwmaq6uj/
stays in sync with auto-pushed NeetCode submissions.

Usage:  python3 scripts/build-dashboard.py

Reads:
  Data Structures & Algorithms/<problem-slug>/submission-N.<ext>
  git log (for solve dates and heatmap)

Writes:
  docs/data.json
  docs/index.html  (data inlined for offline / file:// support)
"""
import json
import os
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOCS = REPO / "docs"

EXT_LANG = {
    ".py": "Python",
    ".ts": "TypeScript",
    ".js": "JavaScript",
    ".java": "Java",
    ".cpp": "C++",
    ".cs": "C#",
    ".go": "Go",
    ".rs": "Rust",
    ".kt": "Kotlin",
    ".swift": "Swift",
    ".sql": "SQL",
}

# Best-effort difficulty by slug (NeetCode 150-ish). Unknown defaults to Medium.
EASY = {
    "two-integer-sum", "concatenation-of-array", "contains-duplicate", "contains-duplicate-ii",
    "is-anagram", "majority-element", "is-palindrome", "reverse-string", "merge-strings-alternately",
    "longest-common-prefix", "remove-element", "remove-duplicates-from-sorted-array",
    "merge-sorted-array", "search-insert-position", "binary-search",
    "guess-number-higher-or-lower", "sqrtx", "number-of-one-bits", "counting-bits",
    "reverse-a-linked-list", "invert-a-binary-tree", "depth-of-binary-tree",
    "same-binary-tree", "subtree-of-a-binary-tree",
    "lowest-common-ancestor-in-binary-search-tree", "duplicate-integer", "rotate-array",
    "reverse-bits", "missing-number", "climbing-stairs", "single-number", "valid-parentheses",
    "validate-parentheses", "baseball-game",
}
MEDIUM = {
    "three-integer-sum", "anagram-groups", "top-k-elements-in-list",
    "products-of-array-discluding-self", "valid-sudoku", "longest-consecutive-sequence",
    "buy-and-sell-crypto", "find-target-in-rotated-sorted-array",
    "find-minimum-in-rotated-sorted-array", "search-2d-matrix", "koko-eating-bananas",
    "time-based-key-value-store", "daily-temperatures", "generate-parentheses", "car-fleet",
    "minimum-stack", "evaluate-reverse-polish-notation", "reorder-linked-list",
    "remove-node-from-end-of-linked-list", "copy-linked-list-with-random-pointer",
    "add-two-numbers", "linked-list-cycle-detection", "find-the-duplicate-number", "lru-cache",
    "level-order-traversal-of-binary-tree", "binary-tree-right-side-view",
    "count-good-nodes-in-binary-tree", "valid-binary-search-tree",
    "kth-smallest-integer-in-bst", "binary-tree-from-preorder-and-inorder-traversal",
    "sort-an-array", "valid-palindrome-ii", "two-integer-sum-ii", "3sum",
    "container-with-most-water", "encode-and-decode-strings",
}
HARD = {
    "trapping-rain-water", "median-of-two-sorted-arrays", "reverse-nodes-in-k-group",
    "merge-k-sorted-linked-lists", "binary-tree-maximum-path-sum",
    "serialize-and-deserialize-binary-tree", "word-search-ii",
}


def git(*args: str) -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(REPO), *args],
            stderr=subprocess.DEVNULL,
        ).decode()
    except subprocess.CalledProcessError:
        return ""


def collect():
    problems = []
    topic_dirs = [d for d in REPO.iterdir() if d.is_dir() and not d.name.startswith(".")]
    for topic_dir in topic_dirs:
        for prob_dir in sorted(topic_dir.iterdir()):
            if not prob_dir.is_dir():
                continue
            slug = prob_dir.name
            submission_files = sorted(
                f for f in prob_dir.iterdir() if f.is_file() and not f.name.startswith(".")
            )
            if not submission_files:
                continue

            # Folder-level dates
            first_lines = [
                ln for ln in git(
                    "log", "--diff-filter=A", "--follow", "--format=%ad",
                    "--date=short", "--", f"{prob_dir.relative_to(REPO)}/",
                ).strip().split("\n") if ln
            ]
            first_solved = first_lines[-1] if first_lines else ""
            last_updated = git(
                "log", "-1", "--format=%ad", "--date=short", "--",
                f"{prob_dir.relative_to(REPO)}/",
            ).strip()

            files = []
            langs = set()
            for f in submission_files:
                ext = f.suffix
                lang = EXT_LANG.get(ext, ext.lstrip(".") or "unknown")
                langs.add(lang)
                code = f.read_text(errors="replace")
                date_lines = [
                    ln for ln in git(
                        "log", "--diff-filter=A", "--follow", "--format=%ad",
                        "--date=short", "--", str(f.relative_to(REPO)),
                    ).strip().split("\n") if ln
                ]
                fdate = date_lines[-1] if date_lines else first_solved
                files.append({
                    "name": f.name,
                    "lang": lang,
                    "date": fdate,
                    "code": code,
                    "loc": sum(1 for ln in code.split("\n") if ln.strip()),
                })
            diff = "Easy" if slug in EASY else "Hard" if slug in HARD else (
                "Medium" if slug in MEDIUM else "Medium"
            )
            problems.append({
                "slug": slug,
                "title": slug.replace("-", " ").title(),
                "firstSolved": first_solved,
                "lastUpdated": last_updated,
                "difficulty": diff,
                "languages": sorted(langs),
                "submissions": files,
            })

    dates = [
        ln for ln in git("log", "--format=%ad", "--date=short").strip().split("\n") if ln
    ]
    date_counts = defaultdict(int)
    for d in dates:
        date_counts[d] += 1

    languages = sorted({lang for p in problems for lang in p["languages"]})
    return {
        "problems": problems,
        "totalProblems": len(problems),
        "totalSubmissions": sum(len(p["submissions"]) for p in problems),
        "commitDates": dict(date_counts),
        "languages": languages,
    }


def main():
    DOCS.mkdir(exist_ok=True)
    data = collect()

    with (DOCS / "data.json").open("w") as f:
        json.dump(data, f, indent=2)

    tmpl_path = DOCS / "_template.html"
    if not tmpl_path.exists():
        print(
            "warning: docs/_template.html not found — skipping HTML regen.\n"
            "         (data.json was still updated.)",
            file=sys.stderr,
        )
        return

    tmpl = tmpl_path.read_text()
    out = tmpl.replace("__DATA__", json.dumps(data, ensure_ascii=False))
    (DOCS / "index.html").write_text(out)
    print(
        f"built docs/index.html  ·  {data['totalProblems']} problems, "
        f"{data['totalSubmissions']} submissions, "
        f"{len(data['commitDates'])} active days"
    )


if __name__ == "__main__":
    main()
