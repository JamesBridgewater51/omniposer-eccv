# OmniPoser (ECCV 2026) — Project Page

Project website for **OmniPoser: Flexible Human Motion Recovery in the Wild with
Masked Flow Matching** (ECCV 2026), built on the
[nerfies](https://github.com/nerfies/nerfies.github.io) project-page template.

## Preview locally

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Update the results tables

The four quantitative tables are rendered by a small script so the numbers never
drift when edited:

```bash
python3 tools/build_tables.py
# paste the <!-- TABLE_n --> blocks from tools/tables_fragment.html
# into index.html at the matching markers
```

Table data lives in `tools/tables.md` (transcribed from the paper's
`experiments.tex`).

## Deploy (GitHub Pages)

1. Create a repository (e.g. `omniposer-eccv`) and push this directory.
2. Repo **Settings → Pages → Deploy from branch → main / (root)**.
3. The page goes live at `https://<username>.github.io/omniposer-eccv/`.
4. The og:image URL in `index.html` is absolute and points at this domain —
   update it if the site ever moves.

Every `git push` to `main` re-publishes automatically — edit `index.html`,
commit, push.

## Assets

| File | Source |
|---|---|
| `static/images/teaser.jpg` | paper Fig. 1 |
| `static/images/pipeline.jpg` | paper Fig. 2 |
| `static/images/qualitative.png` | paper Fig. 3 |

## Credits

- Template: [nerfies.github.io](https://nerfies.github.io) — footer credit kept,
  analytics removed.
- Fonts/icons: Google Fonts (Google Sans / Noto Sans / Castoro), FontAwesome,
  Academicons.
