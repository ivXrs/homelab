# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Documentation for a personal homelab (a Blackview MP100 mini PC running Proxmox VE), published as a bilingual (English/Spanish) static site built with [Zensical](https://zensical.org) and deployed to GitHub Pages at https://ivxrs.github.io/homelab/. The repo is public: never commit real IPs, hostnames, credentials or keys. Use placeholders or example values instead.

`README.md` is a short English description of the repo (what the site is, stack, layout, how to build). It does not duplicate site content, so hardware or service changes only go in `docs_en/` and `docs_es/`. Update the README only when the stack, layout or build commands change.

## Commands

The toolchain is pinned in `requirements.txt` (Zensical 0.1.2). Use a Python 3.13 venv: pyyaml has no wheel for newer Pythons on Windows, and CI also uses 3.13.

```powershell
uv venv --python 3.13 .venv
uv pip install --python .venv\Scripts\python.exe -r requirements.txt

.venv\Scripts\python scripts\build.py --strict      # build both languages into site/ (same as CI)
.venv\Scripts\python scripts\build.py --serve es    # live preview of ONE language at http://localhost:8000
.venv\Scripts\python scripts\build.py --sync-only   # only copy shared/ assets into docs_*/assets/
```

There are no tests or linters. `build.py --strict` is the check, and it must finish with "No issues found" for both languages.

`--serve` previews a single language, so the language switcher and the root redirect don't work there. To test the full site as Pages serves it, build, copy `site/` into a folder named `homelab/`, and serve its parent directory (for example `python -m http.server`), then open `/homelab/`.

## Architecture

Zensical 0.1.2 has no native i18n, so each language is its own Zensical site:

- **`zensical.en.toml` / `zensical.es.toml`**: near-identical configs that differ only in language strings, `docs_dir`, `site_dir` (`site/en`, `site/es`), `site_url` and nav labels. Any change to theme, features, markdown extensions, palette, `extra_css`/`extra_javascript` or `nav` must be made in **both** files.
- **`docs_en/` / `docs_es/`**: page content. The two trees mirror each other with the same filenames, and every page must exist in both. A new page must also be added to `nav` in both configs.
- **`shared/{css,js,img}`**: the single source for custom assets. `scripts/build.py` copies them into `docs_<lang>/assets/` before each build, and that folder is gitignored and regenerated on every build. Edit `shared/`, never `docs_*/assets/`. Pages reference assets relatively (e.g. `../assets/img/mini_pc.png`).
- **`scripts/build.py`**: syncs assets, builds each language, then writes `site/index.html` and `site/.nojekyll`. The root page redirects to `en/` or `es/` by browser language.
- **Language switcher**: `extra.alternate` in each config holds absolute links (`/homelab/en/`, `/homelab/es/`). `shared/js/extra.js` rewrites them so switching keeps the current page, which depends on both trees having the same paths.
- **Animations**: `shared/css/extra.css` (hero gradient title, card hover, reveal classes) and `shared/js/extra.js` (IntersectionObserver scroll reveal). The JS re-initialises through Zensical's `document$` observable because `navigation.instant` swaps pages without a full reload. All motion must stay behind `prefers-reduced-motion`.
- **Home page hero**: `docs_*/index.md` uses `<div class="hero" markdown>` with `.hero__title` and `.hero__lead`. The permalink `¶` is deliberately hidden on the hero title only.

Known Zensical 0.1.2 quirk: a nested `docs_dir` such as `docs/en` panics on Windows ("URL reference is a valid IRI"). That is why the content folders are top-level `docs_en` / `docs_es`.

## Deployment

`.github/workflows/docs.yml` runs on pushes to `main` that touch `docs_*/`, `shared/`, `scripts/`, `zensical.*.toml`, `requirements.txt` or the workflow file, and on `workflow_dispatch`. It builds with `--strict` and deploys `site/` via `actions/deploy-pages` (Pages source is set to "GitHub Actions"). Pull requests run no checks, so build locally with `--strict` before opening one.

## Conventions

- Branch names, commit messages, PR titles and PR bodies are in English and follow Conventional Commits (e.g. `feat(docs): ...`, `ci(docs): ...`). Changes go through a branch and a squash-merged PR, never direct pushes to `main`.
- Site content is written in both languages. Spanish is a proper translation, not machine-literal, and keeps common technical terms (Proxmox VE, homelab, DNS, VPN) as is.
