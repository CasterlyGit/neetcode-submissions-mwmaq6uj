# neetcode-submissions

Auto-synced [NeetCode](https://neetcode.io) solutions for [@CasterlyGit](https://github.com/CasterlyGit).

**Live dashboard:** https://casterlygit.github.io/neetcode-submissions-mwmaq6uj/

The dashboard shows total problems solved, language breakdown, difficulty mix, recent solves with expandable syntax-highlighted code, and a GitHub-style activity heatmap. It rebuilds itself on every push.

## Pipeline

```
neetcode.io  →  GitHub Sync (auto-commits on each accepted submission)
             →  push to main
             →  .github/workflows/build-dashboard.yml runs
             →  scripts/build-dashboard.py regenerates docs/index.html + docs/data.json
             →  GitHub Pages serves the dashboard
```

The dashboard is always live with the latest data. No manual updates needed.

## Layout

```
Data Structures & Algorithms/<problem-slug>/submission-N.<ext>
                                  the solutions themselves
docs/index.html                   the dashboard (data inlined)
docs/data.json                    same data, standalone
docs/_template.html               template build-dashboard.py fills in
scripts/build-dashboard.py        regenerate the dashboard from current state
.github/workflows/build-dashboard.yml
                                  rebuild on every relevant push
```

## Manual rebuild

```
python3 scripts/build-dashboard.py
```

Reads the submissions directory and `git log`, writes `docs/data.json` and `docs/index.html`.

## NeetCode GitHub Sync

Sync is configured at [neetcode.io/profile/github](https://neetcode.io/profile/github):

- Auto-commit on each accepted submission
- Bulk-sync of historical submissions
- Per-language file extensions

This repo is the data layer. The dashboard is the view.
