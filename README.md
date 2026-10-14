# OmniPoser (ECCV 2026) Project Page

Static project website for **OmniPoser: Flexible Human Motion Recovery in the Wild
with Masked Flow Matching** (ECCV 2026 camera-ready).

- **Strictly the [nerfies](https://github.com/nerfies/nerfies.github.io) template** —
  plain white, bulma, no effects; the only custom CSS (`static/css/eccv-site.css`)
  is structural (table overflow, the paper's midrule, caption spacing).
- **All figure/table material is static** — teaser, pipeline, Tables 1–4, and the
  qualitative figure, exactly as in the camera-ready.
- Independent from the TPAMI-extension site.

## Content policy: extraction, not summary

The page's prose is **extracted verbatim** from the camera-ready LaTeX
(`/home/liuminghao/ECCV26_OmniPoser_CameraReady.zip`), following a sentence-level
extraction graph: the paper's sentences are nodes, its hidden transitions
(起承转合, callbacks, mechanism→evidence edges) are edges, and the site keeps a
**connected sub-graph** — every connective on the page ("however", "We therefore",
"To address this", "This design", "We attribute this", "those baselines", "four
settings") has its antecedent earlier on the page or in a caption.

The full extraction graph (25 kept sentences + abstract + captions, named edges,
gap audit, and the log of sanctioned trims/grammar fixes) lives in the build
record; deviations from verbatim are limited to that log:

| Where | Change | Reason |
|---|---|---|
| Teaser caption | "msaked" → "masked" | camera-ready typo |
| Method §dual-stream | "network v_θ are two streams" → "comprises two streams" | grammar |
| Results §Setting 2 | "Ours-U achieve 86.2mm MPJPE, (~30%…" → "achieves 86.2 mm MPJPE (~30%…" | grammar |
| Qualitative | "mocap dataset generalize" → "datasets"; "AR/VR capture scene" → "scenes" | grammar |
| Abstract | "Ego-Exo4D dataset" → "datasets" | grammar |
| Protocol | "stated in Sec. 3.2" → "stated above" | section numbers do not exist on the page |
| Acknowledgements | block added (beyond the extraction plan); "Commitee" → "Committee"; "Grant No." spacing | funding credit, standard section; typos |
| Table footnote | "Bold and underlined values indicate the best and second-best results, respectively." restored from the dropped EP8 tail | tables are unreadable without the key; sanctioned scaffolding |
| Head | `og:` meta tags kept (not in nerfies) | invisible sharing metadata; deliberate deviation — set the **absolute** og:image URL at deploy time |

Tables were transcribed from `experiments.tex` and double-verified (283 cells,
0 mismatches) before rendering.

## Rebuilding the tables

`tools/build_tables.py` regenerates the four tables from the verified JSON:

```bash
python3 tools/build_tables.py   # reads /tmp/eccv_site_gather/tables.md by default
```

If the JSON path has moved, edit `SRC` in the script. The generated fragment is
substituted into `index.html` at the `{{TABLE_n}}` placeholders.

## Local preview & deploy

```bash
python3 -m http.server 8000    # preview
# GitHub Pages: push to a repo, Settings → Pages → main / root
```

All asset paths are relative; a `.nojekyll` file is included.

## Assets

| File | Source | Notes |
|---|---|---|
| `static/images/teaser.jpg` | `fig/teaser.png` downscaled to 2000px | Fig. 1 |
| `static/images/pipeline.jpg` | `fig/pipeline.png` downscaled to 2000px | Fig. 2 |
| `static/images/qualitative.png` | `fig/qualitative.pdf` rasterized @150dpi | Fig. 3 |

## Credits

Template: [nerfies.github.io](https://nerfies.github.io) (footer credit kept;
Google Analytics removed as their license requests for forks).
