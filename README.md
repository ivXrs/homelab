# Homelab

Source for **[ivxrs.github.io/homelab](https://ivxrs.github.io/homelab/)**, a bilingual (English / Spanish) documentation site about my homelab: a mini PC running Proxmox VE that I use to learn systems administration and self-host a few services.

The site covers the hardware and the services running on it. All the content lives there; this repository only holds its source.

## Stack

- [Zensical](https://zensical.org) static site generator, one site per language
- Deployed to GitHub Pages with GitHub Actions on every push to `main`

## Repository layout

| Path | Contents |
|---|---|
| `docs_en/`, `docs_es/` | Page content, one tree per language with the same filenames |
| `zensical.en.toml`, `zensical.es.toml` | Site config for each language |
| `shared/` | Custom CSS, JavaScript and images, copied into each language at build time |
| `scripts/build.py` | Builds both languages into `site/` |

## Build locally

Requires Python 3.13 and [uv](https://docs.astral.sh/uv/).

```powershell
uv venv --python 3.13 .venv
uv pip install --python .venv\Scripts\python.exe -r requirements.txt

.venv\Scripts\python scripts\build.py --strict      # build both languages into site/
.venv\Scripts\python scripts\build.py --serve en    # live preview of one language at http://localhost:8000
```

## License

[MIT](LICENSE.txt)
