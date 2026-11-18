#!/usr/bin/env python3
"""Build the bilingual docs: sync shared assets, build each language, write root redirect.

Usage:
    python scripts/build.py [--strict]     build everything into site/
    python scripts/build.py --serve en     live preview of one language (en or es)
    python scripts/build.py --sync-only    only copy shared assets
"""
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = ["en", "es"]
SITE = ROOT / "site"

REDIRECT = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Homelab</title>
<link rel="canonical" href="en/">
<link rel="alternate" hreflang="en" href="en/">
<link rel="alternate" hreflang="es" href="es/">
<noscript><meta http-equiv="refresh" content="0; url=en/"></noscript>
<script>
  var langs = navigator.languages || [navigator.language || "en"];
  var target = "en";
  for (var i = 0; i < langs.length; i++) {
    var l = String(langs[i]).slice(0, 2).toLowerCase();
    if (l === "es" || l === "en") { target = l; break; }
  }
  location.replace(target + "/" + location.search + location.hash);
</script>
</head>
<body><p><a href="en/">English</a> &middot; <a href="es/">Espa&ntilde;ol</a></p></body>
</html>
"""


def sync_assets() -> None:
    """Copy shared/{css,js,img} into docs_<lang>/assets (gitignored)."""
    for lang in LANGS:
        dest = ROOT / f"docs_{lang}" / "assets"
        if dest.exists():
            shutil.rmtree(dest)
        for sub in ("css", "js", "img"):
            shutil.copytree(ROOT / "shared" / sub, dest / sub)


def main() -> int:
    sync_assets()
    if "--sync-only" in sys.argv:
        return 0
    if "--serve" in sys.argv:
        lang = sys.argv[sys.argv.index("--serve") + 1]
        return subprocess.call(
            [sys.executable, "-m", "zensical", "serve", "-f", f"zensical.{lang}.toml"], cwd=ROOT
        )
    if SITE.exists():
        shutil.rmtree(SITE)
    for lang in LANGS:
        cmd = [sys.executable, "-m", "zensical", "build", "-c", "-f", f"zensical.{lang}.toml"]
        if "--strict" in sys.argv:
            cmd.append("-s")
        print(f"==> Building {lang}", flush=True)
        if subprocess.call(cmd, cwd=ROOT) != 0:
            return 1
    (SITE / "index.html").write_text(REDIRECT, encoding="utf-8")
    (SITE / ".nojekyll").write_text("", encoding="utf-8")
    print("==> Done: site/ (en, es, index.html)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
