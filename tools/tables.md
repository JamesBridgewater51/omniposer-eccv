# OmniPoser ECCV 2026 camera-ready: quantitative tables (web-ready JSON)

Source of truth: `/tmp/eccv_cr/experiments.tex` (LaTeX table code); cross-checked against `/tmp/eccv_paper.txt` (PDF text extraction).

Every cell was transcribed by hand and then mechanically re-verified by an independent parser (`/tmp/eccv_site_gather/build_and_verify.py`) that re-reads `experiments.tex` and diffs every value string, best/second flag, row order, caption, benchmark list and metric sub-header against this JSON. Verification result: **0 mismatches across 283 data cells.**

`best` = printed in `\textbf{}` (best result); `second` = printed in `\underline{}` (second-best); per the paper: "Bold and underlined values indicate the best and second-best results, respectively." Cell values `v` are verbatim digit strings (e.g. `"0.230"`, `"88.0"` keep their trailing zeros); `"-"` denotes the printed dash (unavailable metric, per "For Nymeria, dashes denote unavailable metrics").

## JSON

```json
{
  "tables": [
    {
      "id": "tab:setting1_upper_body",
      "number": "Table 1",
      "setting": "Setting 1 (Sparse Observation) - upper-body joint positions",
      "caption": "Quantitative results of Setting 1: Sparse Observation (Upper-body joint positions).",
      "caption_latex": "\\caption{Quantitative results of Setting 1: Sparse Observation (Upper-body joint positions).}",
      "layout": "methods_as_rows",
      "benchmarks": [
        "AMASS",
        "Nymeria (In-the-wild)"
      ],
      "metrics": {
        "AMASS": [
          {
            "key": "JPE",
            "label": "JPE↓",
            "label_latex": "JPE$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "Acc",
            "label": "Acc↓",
            "label_latex": "Acc$\\downarrow$",
            "unit": "m/s^2",
            "direction": "lower"
          },
          {
            "key": "Con",
            "label": "Con↑",
            "label_latex": "Con$\\uparrow$",
            "unit": null,
            "direction": "higher"
          },
          {
            "key": "Ska",
            "label": "Ska↓",
            "label_latex": "Ska$\\downarrow$",
            "unit": null,
            "direction": "lower"
          },
          {
            "key": "Pen",
            "label": "Pen↓",
            "label_latex": "Pen$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          }
        ],
        "Nymeria (In-the-wild)": [
          {
            "key": "JPE",
            "label": "JPE↓",
            "label_latex": "JPE$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "Acc",
            "label": "Acc↓",
            "label_latex": "Acc$\\downarrow$",
            "unit": "m/s^2",
            "direction": "lower"
          },
          {
            "key": "Con",
            "label": "Con↑",
            "label_latex": "Con$\\uparrow$",
            "unit": null,
            "direction": "higher"
          },
          {
            "key": "Ska",
            "label": "Ska↓",
            "label_latex": "Ska$\\downarrow$",
            "unit": null,
            "direction": "lower"
          }
        ]
      },
      "rows": [
        {
          "method": "HuMoR",
          "method_bold": false,
          "block": "specialist",
          "cells": {
            "AMASS": {
              "JPE": {
                "v": "88.0",
                "best": false,
                "second": false
              },
              "Acc": {
                "v": "3.3",
                "best": false,
                "second": false
              },
              "Con": {
                "v": "0.68",
                "best": false,
                "second": false
              },
              "Ska": {
                "v": "0.230",
                "best": false,
                "second": false
              },
              "Pen": {
                "v": "2.59",
                "best": false,
                "second": false
              }
            },
            "Nymeria (In-the-wild)": {
              "JPE": {
                "v": "88.5",
                "best": false,
                "second": false
              },
              "Acc": {
                "v": "8.26",
                "best": false,
                "second": false
              },
              "Con": {
                "v": "0.78",
                "best": false,
                "second": false
              },
              "Ska": {
                "v": "0.685",
                "best": false,
                "second": false
              }
            }
          }
        },
        {
          "method": "RoHM",
          "method_bold": false,
          "block": "specialist",
          "cells": {
            "AMASS": {
              "JPE": {
                "v": "34.8",
                "best": false,
                "second": true
              },
              "Acc": {
                "v": "2.3",
                "best": true,
                "second": false
              },
              "Con": {
                "v": "0.95",
                "best": true,
                "second": false
              },
              "Ska": {
                "v": "0.078",
                "best": false,
                "second": true
              },
              "Pen": {
                "v": "0.69",
                "best": true,
                "second": false
              }
            },
            "Nymeria (In-the-wild)": {
              "JPE": {
                "v": "59.3",
                "best": false,
                "second": true
              },
              "Acc": {
                "v": "7.2",
                "best": false,
                "second": true
              },
              "Con": {
                "v": "0.91",
                "best": false,
                "second": true
              },
              "Ska": {
                "v": "0.610",
                "best": false,
                "second": true
              }
            }
          }
        },
        {
          "method": "Ours-S",
          "method_bold": true,
          "block": "specialist",
          "cells": {
            "AMASS": {
              "JPE": {
                "v": "32.1",
                "best": true,
                "second": false
              },
              "Acc": {
                "v": "2.7",
                "best": false,
                "second": true
              },
              "Con": {
                "v": "0.94",
                "best": false,
                "second": true
              },
              "Ska": {
                "v": "0.031",
                "best": true,
                "second": false
              },
              "Pen": {
                "v": "1.84",
                "best": false,
                "second": true
              }
            },
            "Nymeria (In-the-wild)": {
              "JPE": {
                "v": "21.1",
                "best": true,
                "second": false
              },
              "Acc": {
                "v": "1.39",
                "best": true,
                "second": false
              },
              "Con": {
                "v": "0.95",
                "best": true,
                "second": false
              },
              "Ska": {
                "v": "0.033",
                "best": true,
                "second": false
              }
            }
          }
        },
        {
          "method": "RoHM-U",
          "method_bold": false,
          "block": "unified",
          "cells": {
            "AMASS": {
              "JPE": {
                "v": "158.7",
                "best": false,
                "second": false
              },
              "Acc": {
                "v": "2.9",
                "best": false,
                "second": false
              },
              "Con": {
                "v": "0.75",
                "best": false,
                "second": true
              },
              "Ska": {
                "v": "0.190",
                "best": false,
                "second": false
              },
              "Pen": {
                "v": "1.48",
                "best": false,
                "second": true
              }
            },
            "Nymeria (In-the-wild)": {
              "JPE": {
                "v": "-",
                "best": false,
                "second": false
              },
              "Acc": {
                "v": "-",
                "best": false,
                "second": false
              },
              "Con": {
                "v": "-",
                "best": false,
                "second": false
              },
              "Ska": {
                "v": "-",
                "best": false,
                "second": false
              }
            }
          }
        },
        {
          "method": "RoHM++-U",
          "method_bold": false,
          "block": "unified",
          "cells": {
            "AMASS": {
              "JPE": {
                "v": "39.9",
                "best": false,
                "second": true
              },
              "Acc": {
                "v": "2.3",
                "best": true,
                "second": false
              },
              "Con": {
                "v": "0.95",
                "best": true,
                "second": false
              },
              "Ska": {
                "v": "0.081",
                "best": false,
                "second": true
              },
              "Pen": {
                "v": "0.56",
                "best": true,
                "second": false
              }
            },
            "Nymeria (In-the-wild)": {
              "JPE": {
                "v": "-",
                "best": false,
                "second": false
              },
              "Acc": {
                "v": "-",
                "best": false,
                "second": false
              },
              "Con": {
                "v": "-",
                "best": false,
                "second": false
              },
              "Ska": {
                "v": "-",
                "best": false,
                "second": false
              }
            }
          }
        },
        {
          "method": "Ours-U",
          "method_bold": true,
          "block": "unified",
          "cells": {
            "AMASS": {
              "JPE": {
                "v": "36.7",
                "best": true,
                "second": false
              },
              "Acc": {
                "v": "2.7",
                "best": false,
                "second": true
              },
              "Con": {
                "v": "0.95",
                "best": true,
                "second": false
              },
              "Ska": {
                "v": "0.025",
                "best": true,
                "second": false
              },
              "Pen": {
                "v": "9.32",
                "best": false,
                "second": false
              }
            },
            "Nymeria (In-the-wild)": {
              "JPE": {
                "v": "-",
                "best": false,
                "second": false
              },
              "Acc": {
                "v": "-",
                "best": false,
                "second": false
              },
              "Con": {
                "v": "-",
                "best": false,
                "second": false
              },
              "Ska": {
                "v": "-",
                "best": false,
                "second": false
              }
            }
          }
        }
      ]
    },
    {
      "id": "tab:setting1_random",
      "number": "Table 2",
      "setting": "Setting 1 (Sparse Observation) - random joint masking",
      "caption": "Quantitative results of Setting 1: Sparse Observation (Random joint masking) on AMASS.",
      "caption_latex": "\\caption{Quantitative results of Setting 1: Sparse Observation (Random joint masking) on AMASS.}",
      "layout": "transposed_in_print (metrics are rows, methods are columns); normalized here to method rows. Single benchmark (AMASS) per caption.",
      "benchmarks": [
        "AMASS"
      ],
      "metrics": {
        "AMASS": [
          {
            "key": "JPE (mm)",
            "label": "JPE (mm) ↓",
            "label_latex": "JPE (mm) $\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "Accel. (m/s$^2$)",
            "label": "Accel. (m/s²) ↓",
            "label_latex": "Accel. (m/s$^2$) $\\downarrow$",
            "unit": "m/s^2",
            "direction": "lower"
          },
          {
            "key": "Contact",
            "label": "Contact ↑",
            "label_latex": "Contact $\\uparrow$",
            "unit": null,
            "direction": "higher"
          },
          {
            "key": "Skating",
            "label": "Skating ↓",
            "label_latex": "Skating $\\downarrow$",
            "unit": null,
            "direction": "lower"
          }
        ]
      },
      "rows": [
        {
          "method": "HuMoR",
          "method_bold": false,
          "block": null,
          "cells": {
            "AMASS": {
              "JPE (mm)": {
                "v": "80.5",
                "best": false,
                "second": false
              },
              "Accel. (m/s$^2$)": {
                "v": "3.3",
                "best": false,
                "second": false
              },
              "Contact": {
                "v": "0.78",
                "best": false,
                "second": false
              },
              "Skating": {
                "v": "0.184",
                "best": false,
                "second": false
              }
            }
          }
        },
        {
          "method": "RoHM",
          "method_bold": false,
          "block": null,
          "cells": {
            "AMASS": {
              "JPE (mm)": {
                "v": "38.2",
                "best": false,
                "second": true
              },
              "Accel. (m/s$^2$)": {
                "v": "1.9",
                "best": true,
                "second": false
              },
              "Contact": {
                "v": "0.95",
                "best": false,
                "second": true
              },
              "Skating": {
                "v": "0.024",
                "best": false,
                "second": true
              }
            }
          }
        },
        {
          "method": "Ours-S",
          "method_bold": true,
          "block": null,
          "cells": {
            "AMASS": {
              "JPE (mm)": {
                "v": "35.7",
                "best": true,
                "second": false
              },
              "Accel. (m/s$^2$)": {
                "v": "2.2",
                "best": false,
                "second": true
              },
              "Contact": {
                "v": "0.97",
                "best": true,
                "second": false
              },
              "Skating": {
                "v": "0.018",
                "best": true,
                "second": false
              }
            }
          }
        },
        {
          "method": "Ours-U",
          "method_bold": true,
          "block": null,
          "cells": {
            "AMASS": {
              "JPE (mm)": {
                "v": "49.3",
                "best": false,
                "second": false
              },
              "Accel. (m/s$^2$)": {
                "v": "2.6",
                "best": false,
                "second": false
              },
              "Contact": {
                "v": "0.93",
                "best": false,
                "second": false
              },
              "Skating": {
                "v": "0.019",
                "best": false,
                "second": false
              }
            }
          }
        }
      ]
    },
    {
      "id": "tab:setting2_head_only",
      "number": "Table 3",
      "setting": "Setting 2 (Egocentric Head 6D Pose)",
      "caption": "Quantitative results of Setting 2: Egocentric Head 6D Pose.",
      "caption_latex": "\\caption{Quantitative results of Setting 2: Egocentric Head 6D Pose.}",
      "layout": "methods_as_rows",
      "benchmarks": [
        "AMASS",
        "RICH (Cross-domain)",
        "Nymeria (Wild)"
      ],
      "metrics": {
        "AMASS": [
          {
            "key": "JPE",
            "label": "JPE↓",
            "label_latex": "JPE$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "PA",
            "label": "PA↓",
            "label_latex": "PA$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "Con",
            "label": "Con↑",
            "label_latex": "Con$\\uparrow$",
            "unit": null,
            "direction": "higher"
          },
          {
            "key": "T_h",
            "label": "T_h↓",
            "label_latex": "$T_h\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          }
        ],
        "RICH (Cross-domain)": [
          {
            "key": "JPE",
            "label": "JPE↓",
            "label_latex": "JPE$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "PA",
            "label": "PA↓",
            "label_latex": "PA$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "Con",
            "label": "Con↑",
            "label_latex": "Con$\\uparrow$",
            "unit": null,
            "direction": "higher"
          },
          {
            "key": "T_h",
            "label": "T_h↓",
            "label_latex": "$T_h\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          }
        ],
        "Nymeria (Wild)": [
          {
            "key": "JPE",
            "label": "JPE↓",
            "label_latex": "JPE$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "PA",
            "label": "PA↓",
            "label_latex": "PA$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "Con",
            "label": "Con↑",
            "label_latex": "Con$\\uparrow$",
            "unit": null,
            "direction": "higher"
          }
        ]
      },
      "rows": [
        {
          "method": "EgoEgo",
          "method_bold": false,
          "block": "specialist",
          "cells": {
            "AMASS": {
              "JPE": {
                "v": "167.4",
                "best": false,
                "second": false
              },
              "PA": {
                "v": "145.8",
                "best": false,
                "second": false
              },
              "Con": {
                "v": "0.92",
                "best": false,
                "second": true
              },
              "T_h": {
                "v": "54.9",
                "best": false,
                "second": false
              }
            },
            "RICH (Cross-domain)": {
              "JPE": {
                "v": "207.8",
                "best": false,
                "second": false
              },
              "PA": {
                "v": "187.8",
                "best": false,
                "second": false
              },
              "Con": {
                "v": "0.88",
                "best": false,
                "second": true
              },
              "T_h": {
                "v": "66.5",
                "best": false,
                "second": false
              }
            },
            "Nymeria (Wild)": {
              "JPE": {
                "v": "135.8",
                "best": false,
                "second": false
              },
              "PA": {
                "v": "117.2",
                "best": false,
                "second": false
              },
              "Con": {
                "v": "0.57",
                "best": false,
                "second": false
              }
            }
          }
        },
        {
          "method": "EgoAllo",
          "method_bold": false,
          "block": "specialist",
          "cells": {
            "AMASS": {
              "JPE": {
                "v": "119.7",
                "best": false,
                "second": true
              },
              "PA": {
                "v": "101.1",
                "best": false,
                "second": true
              },
              "Con": {
                "v": "1.00",
                "best": true,
                "second": false
              },
              "T_h": {
                "v": "6.2",
                "best": true,
                "second": false
              }
            },
            "RICH (Cross-domain)": {
              "JPE": {
                "v": "176.2",
                "best": false,
                "second": true
              },
              "PA": {
                "v": "160.1",
                "best": false,
                "second": true
              },
              "Con": {
                "v": "0.96",
                "best": true,
                "second": false
              },
              "T_h": {
                "v": "8.9",
                "best": true,
                "second": false
              }
            },
            "Nymeria (Wild)": {
              "JPE": {
                "v": "103.0",
                "best": false,
                "second": true
              },
              "PA": {
                "v": "89.3",
                "best": false,
                "second": true
              },
              "Con": {
                "v": "0.63",
                "best": false,
                "second": true
              }
            }
          }
        },
        {
          "method": "Ours-S",
          "method_bold": true,
          "block": "specialist",
          "cells": {
            "AMASS": {
              "JPE": {
                "v": "83.2",
                "best": true,
                "second": false
              },
              "PA": {
                "v": "73.5",
                "best": true,
                "second": false
              },
              "Con": {
                "v": "0.92",
                "best": false,
                "second": true
              },
              "T_h": {
                "v": "17.1",
                "best": false,
                "second": true
              }
            },
            "RICH (Cross-domain)": {
              "JPE": {
                "v": "131.6",
                "best": true,
                "second": false
              },
              "PA": {
                "v": "111.5",
                "best": true,
                "second": false
              },
              "Con": {
                "v": "0.71",
                "best": false,
                "second": false
              },
              "T_h": {
                "v": "25.7",
                "best": false,
                "second": true
              }
            },
            "Nymeria (Wild)": {
              "JPE": {
                "v": "40.7",
                "best": true,
                "second": false
              },
              "PA": {
                "v": "36.2",
                "best": true,
                "second": false
              },
              "Con": {
                "v": "0.94",
                "best": true,
                "second": false
              }
            }
          }
        },
        {
          "method": "RoHM-U",
          "method_bold": false,
          "block": "unified",
          "cells": {
            "AMASS": {
              "JPE": {
                "v": "124.3",
                "best": false,
                "second": false
              },
              "PA": {
                "v": "101.5",
                "best": false,
                "second": false
              },
              "Con": {
                "v": "0.94",
                "best": false,
                "second": true
              },
              "T_h": {
                "v": "36.7",
                "best": false,
                "second": false
              }
            },
            "RICH (Cross-domain)": {
              "JPE": {
                "v": "195.0",
                "best": false,
                "second": false
              },
              "PA": {
                "v": "115.4",
                "best": false,
                "second": false
              },
              "Con": {
                "v": "0.62",
                "best": false,
                "second": false
              },
              "T_h": {
                "v": "56.8",
                "best": false,
                "second": false
              }
            },
            "Nymeria (Wild)": {
              "JPE": {
                "v": "-",
                "best": false,
                "second": false
              },
              "PA": {
                "v": "-",
                "best": false,
                "second": false
              },
              "Con": {
                "v": "-",
                "best": false,
                "second": false
              }
            }
          }
        },
        {
          "method": "RoHM++-U",
          "method_bold": false,
          "block": "unified",
          "cells": {
            "AMASS": {
              "JPE": {
                "v": "94.5",
                "best": false,
                "second": true
              },
              "PA": {
                "v": "92.5",
                "best": false,
                "second": true
              },
              "Con": {
                "v": "0.96",
                "best": true,
                "second": false
              },
              "T_h": {
                "v": "19.5",
                "best": true,
                "second": false
              }
            },
            "RICH (Cross-domain)": {
              "JPE": {
                "v": "126.3",
                "best": true,
                "second": false
              },
              "PA": {
                "v": "112.3",
                "best": false,
                "second": true
              },
              "Con": {
                "v": "0.72",
                "best": true,
                "second": false
              },
              "T_h": {
                "v": "44.8",
                "best": true,
                "second": false
              }
            },
            "Nymeria (Wild)": {
              "JPE": {
                "v": "-",
                "best": false,
                "second": false
              },
              "PA": {
                "v": "-",
                "best": false,
                "second": false
              },
              "Con": {
                "v": "-",
                "best": false,
                "second": false
              }
            }
          }
        },
        {
          "method": "Ours-U",
          "method_bold": true,
          "block": "unified",
          "cells": {
            "AMASS": {
              "JPE": {
                "v": "86.2",
                "best": true,
                "second": false
              },
              "PA": {
                "v": "69.8",
                "best": true,
                "second": false
              },
              "Con": {
                "v": "0.92",
                "best": false,
                "second": false
              },
              "T_h": {
                "v": "33.2",
                "best": false,
                "second": true
              }
            },
            "RICH (Cross-domain)": {
              "JPE": {
                "v": "134.8",
                "best": false,
                "second": true
              },
              "PA": {
                "v": "106.4",
                "best": true,
                "second": false
              },
              "Con": {
                "v": "0.65",
                "best": false,
                "second": true
              },
              "T_h": {
                "v": "50.7",
                "best": false,
                "second": true
              }
            },
            "Nymeria (Wild)": {
              "JPE": {
                "v": "-",
                "best": false,
                "second": false
              },
              "PA": {
                "v": "-",
                "best": false,
                "second": false
              },
              "Con": {
                "v": "-",
                "best": false,
                "second": false
              }
            }
          }
        }
      ]
    },
    {
      "id": "tab:setting3_6imu_with_kpt_pos",
      "number": "Table 4",
      "setting": "Setting 3 (Mocap data from 6 IMUs with keypoint positions)",
      "caption": "Quantitative results of Setting 3: Mocap Data from 6 IMUs with Keypoint Positions.",
      "caption_latex": "\\caption{Quantitative results of Setting 3: Mocap Data from 6 IMUs with Keypoint Positions.}",
      "layout": "methods_as_rows (full-width table*)",
      "benchmarks": [
        "AIST++",
        "TotalCapture",
        "Nymeria (In-the-wild)"
      ],
      "metrics": {
        "AIST++": [
          {
            "key": "PA",
            "label": "PA↓",
            "label_latex": "PA$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "JPE",
            "label": "JPE↓",
            "label_latex": "JPE$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "PVE",
            "label": "PVE↓",
            "label_latex": "PVE$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "TE",
            "label": "TE↓",
            "label_latex": "TE$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "HS",
            "label": "HS↓",
            "label_latex": "HS$\\downarrow$",
            "unit": "deg",
            "direction": "lower"
          },
          {
            "key": "Jrk",
            "label": "Jrk↓",
            "label_latex": "Jrk$\\downarrow$",
            "unit": "km/s^3",
            "direction": "lower"
          },
          {
            "key": "FS",
            "label": "FS↓",
            "label_latex": "FS$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          }
        ],
        "TotalCapture": [
          {
            "key": "PA",
            "label": "PA↓",
            "label_latex": "PA$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "JPE",
            "label": "JPE↓",
            "label_latex": "JPE$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "PVE",
            "label": "PVE↓",
            "label_latex": "PVE$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "TE",
            "label": "TE↓",
            "label_latex": "TE$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "HS",
            "label": "HS↓",
            "label_latex": "HS$\\downarrow$",
            "unit": "deg",
            "direction": "lower"
          },
          {
            "key": "Jrk",
            "label": "Jrk↓",
            "label_latex": "Jrk$\\downarrow$",
            "unit": "km/s^3",
            "direction": "lower"
          },
          {
            "key": "FS",
            "label": "FS↓",
            "label_latex": "FS$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          }
        ],
        "Nymeria (In-the-wild)": [
          {
            "key": "PA",
            "label": "PA↓",
            "label_latex": "PA$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "JPE",
            "label": "JPE↓",
            "label_latex": "JPE$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "PVE",
            "label": "PVE↓",
            "label_latex": "PVE$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "TE",
            "label": "TE↓",
            "label_latex": "TE$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          },
          {
            "key": "HS",
            "label": "HS↓",
            "label_latex": "HS$\\downarrow$",
            "unit": "deg",
            "direction": "lower"
          },
          {
            "key": "Jrk",
            "label": "Jrk↓",
            "label_latex": "Jrk$\\downarrow$",
            "unit": "km/s^3",
            "direction": "lower"
          },
          {
            "key": "FS",
            "label": "FS↓",
            "label_latex": "FS$\\downarrow$",
            "unit": "mm",
            "direction": "lower"
          }
        ]
      },
      "rows": [
        {
          "method": "SIP",
          "method_bold": false,
          "block": "specialist",
          "cells": {
            "AIST++": {
              "PA": {
                "v": "23.1",
                "best": false,
                "second": false
              },
              "JPE": {
                "v": "29.8",
                "best": false,
                "second": false
              },
              "PVE": {
                "v": "39.0",
                "best": false,
                "second": false
              },
              "TE": {
                "v": "11.31",
                "best": true,
                "second": false
              },
              "HS": {
                "v": "8.91",
                "best": false,
                "second": true
              },
              "Jrk": {
                "v": "1.50",
                "best": false,
                "second": true
              },
              "FS": {
                "v": "0.57",
                "best": false,
                "second": true
              }
            },
            "TotalCapture": {
              "PA": {
                "v": "28.6",
                "best": false,
                "second": false
              },
              "JPE": {
                "v": "46.5",
                "best": false,
                "second": false
              },
              "PVE": {
                "v": "54.3",
                "best": false,
                "second": false
              },
              "TE": {
                "v": "5.42",
                "best": true,
                "second": false
              },
              "HS": {
                "v": "10.6",
                "best": true,
                "second": false
              },
              "Jrk": {
                "v": "0.94",
                "best": false,
                "second": true
              },
              "FS": {
                "v": "0.69",
                "best": true,
                "second": false
              }
            },
            "Nymeria (In-the-wild)": {
              "PA": {
                "v": "15.2",
                "best": false,
                "second": false
              },
              "JPE": {
                "v": "17.0",
                "best": false,
                "second": true
              },
              "PVE": {
                "v": "16.8",
                "best": false,
                "second": true
              },
              "TE": {
                "v": "4.13",
                "best": true,
                "second": false
              },
              "HS": {
                "v": "5.22",
                "best": true,
                "second": false
              },
              "Jrk": {
                "v": "0.059",
                "best": false,
                "second": true
              },
              "FS": {
                "v": "0.25",
                "best": true,
                "second": false
              }
            }
          }
        },
        {
          "method": "RobCap",
          "method_bold": false,
          "block": "specialist",
          "cells": {
            "AIST++": {
              "PA": {
                "v": "24.0",
                "best": false,
                "second": false
              },
              "JPE": {
                "v": "33.1",
                "best": false,
                "second": false
              },
              "PVE": {
                "v": "43.2",
                "best": false,
                "second": false
              },
              "TE": {
                "v": "19.92",
                "best": false,
                "second": false
              },
              "HS": {
                "v": "9.34",
                "best": false,
                "second": false
              },
              "Jrk": {
                "v": "2.49",
                "best": false,
                "second": false
              },
              "FS": {
                "v": "0.61",
                "best": false,
                "second": false
              }
            },
            "TotalCapture": {
              "PA": {
                "v": "33.5",
                "best": false,
                "second": false
              },
              "JPE": {
                "v": "48.7",
                "best": false,
                "second": false
              },
              "PVE": {
                "v": "63.4",
                "best": false,
                "second": false
              },
              "TE": {
                "v": "23.5",
                "best": false,
                "second": false
              },
              "HS": {
                "v": "13.4",
                "best": false,
                "second": false
              },
              "Jrk": {
                "v": "2.09",
                "best": false,
                "second": false
              },
              "FS": {
                "v": "1.40",
                "best": false,
                "second": false
              }
            },
            "Nymeria (In-the-wild)": {
              "PA": {
                "v": "16.5",
                "best": false,
                "second": false
              },
              "JPE": {
                "v": "19.5",
                "best": false,
                "second": false
              },
              "PVE": {
                "v": "19.4",
                "best": false,
                "second": false
              },
              "TE": {
                "v": "4.52",
                "best": false,
                "second": false
              },
              "HS": {
                "v": "7.51",
                "best": false,
                "second": false
              },
              "Jrk": {
                "v": "1.56",
                "best": false,
                "second": false
              },
              "FS": {
                "v": "0.54",
                "best": false,
                "second": false
              }
            }
          }
        },
        {
          "method": "RobCap3D",
          "method_bold": false,
          "block": "specialist",
          "cells": {
            "AIST++": {
              "PA": {
                "v": "21.8",
                "best": false,
                "second": true
              },
              "JPE": {
                "v": "28.5",
                "best": false,
                "second": true
              },
              "PVE": {
                "v": "37.6",
                "best": false,
                "second": true
              },
              "TE": {
                "v": "15.82",
                "best": false,
                "second": true
              },
              "HS": {
                "v": "8.95",
                "best": false,
                "second": false
              },
              "Jrk": {
                "v": "2.31",
                "best": false,
                "second": false
              },
              "FS": {
                "v": "0.59",
                "best": false,
                "second": false
              }
            },
            "TotalCapture": {
              "PA": {
                "v": "27.9",
                "best": false,
                "second": true
              },
              "JPE": {
                "v": "42.3",
                "best": false,
                "second": true
              },
              "PVE": {
                "v": "52.8",
                "best": false,
                "second": true
              },
              "TE": {
                "v": "9.74",
                "best": false,
                "second": true
              },
              "HS": {
                "v": "12.8",
                "best": false,
                "second": true
              },
              "Jrk": {
                "v": "1.87",
                "best": false,
                "second": false
              },
              "FS": {
                "v": "1.22",
                "best": false,
                "second": false
              }
            },
            "Nymeria (In-the-wild)": {
              "PA": {
                "v": "15.0",
                "best": false,
                "second": true
              },
              "JPE": {
                "v": "17.8",
                "best": false,
                "second": false
              },
              "PVE": {
                "v": "17.5",
                "best": false,
                "second": false
              },
              "TE": {
                "v": "4.25",
                "best": false,
                "second": true
              },
              "HS": {
                "v": "7.18",
                "best": false,
                "second": true
              },
              "Jrk": {
                "v": "1.41",
                "best": false,
                "second": false
              },
              "FS": {
                "v": "0.48",
                "best": false,
                "second": false
              }
            }
          }
        },
        {
          "method": "Ours-S",
          "method_bold": true,
          "block": "specialist",
          "cells": {
            "AIST++": {
              "PA": {
                "v": "19.4",
                "best": true,
                "second": false
              },
              "JPE": {
                "v": "26.0",
                "best": true,
                "second": false
              },
              "PVE": {
                "v": "32.9",
                "best": true,
                "second": false
              },
              "TE": {
                "v": "16.54",
                "best": false,
                "second": false
              },
              "HS": {
                "v": "7.40",
                "best": true,
                "second": false
              },
              "Jrk": {
                "v": "0.29",
                "best": true,
                "second": false
              },
              "FS": {
                "v": "0.22",
                "best": true,
                "second": false
              }
            },
            "TotalCapture": {
              "PA": {
                "v": "26.5",
                "best": true,
                "second": false
              },
              "JPE": {
                "v": "36.2",
                "best": true,
                "second": false
              },
              "PVE": {
                "v": "51.2",
                "best": true,
                "second": false
              },
              "TE": {
                "v": "15.9",
                "best": false,
                "second": false
              },
              "HS": {
                "v": "13.3",
                "best": false,
                "second": false
              },
              "Jrk": {
                "v": "0.16",
                "best": true,
                "second": false
              },
              "FS": {
                "v": "0.81",
                "best": false,
                "second": true
              }
            },
            "Nymeria (In-the-wild)": {
              "PA": {
                "v": "14.5",
                "best": true,
                "second": false
              },
              "JPE": {
                "v": "16.6",
                "best": true,
                "second": false
              },
              "PVE": {
                "v": "16.6",
                "best": true,
                "second": false
              },
              "TE": {
                "v": "6.83",
                "best": false,
                "second": false
              },
              "HS": {
                "v": "7.50",
                "best": false,
                "second": false
              },
              "Jrk": {
                "v": "0.048",
                "best": true,
                "second": false
              },
              "FS": {
                "v": "0.39",
                "best": false,
                "second": true
              }
            }
          }
        },
        {
          "method": "RoHM-U",
          "method_bold": false,
          "block": "unified",
          "cells": {
            "AIST++": {
              "PA": {
                "v": "123.5",
                "best": false,
                "second": false
              },
              "JPE": {
                "v": "157.5",
                "best": false,
                "second": false
              },
              "PVE": {
                "v": "185.9",
                "best": false,
                "second": false
              },
              "TE": {
                "v": "76.3",
                "best": false,
                "second": false
              },
              "HS": {
                "v": "38.1",
                "best": false,
                "second": false
              },
              "Jrk": {
                "v": "0.21",
                "best": true,
                "second": false
              },
              "FS": {
                "v": "9.49",
                "best": false,
                "second": true
              }
            },
            "TotalCapture": {
              "PA": {
                "v": "78.6",
                "best": false,
                "second": false
              },
              "JPE": {
                "v": "95.3",
                "best": false,
                "second": false
              },
              "PVE": {
                "v": "100.4",
                "best": false,
                "second": false
              },
              "TE": {
                "v": "22.8",
                "best": false,
                "second": false
              },
              "HS": {
                "v": "19.5",
                "best": false,
                "second": false
              },
              "Jrk": {
                "v": "0.19",
                "best": false,
                "second": false
              },
              "FS": {
                "v": "0.95",
                "best": false,
                "second": true
              }
            },
            "Nymeria (In-the-wild)": {
              "PA": {
                "v": "-",
                "best": false,
                "second": false
              },
              "JPE": {
                "v": "-",
                "best": false,
                "second": false
              },
              "PVE": {
                "v": "-",
                "best": false,
                "second": false
              },
              "TE": {
                "v": "-",
                "best": false,
                "second": false
              },
              "HS": {
                "v": "-",
                "best": false,
                "second": false
              },
              "Jrk": {
                "v": "-",
                "best": false,
                "second": false
              },
              "FS": {
                "v": "-",
                "best": false,
                "second": false
              }
            }
          }
        },
        {
          "method": "RoHM++-U",
          "method_bold": false,
          "block": "unified",
          "cells": {
            "AIST++": {
              "PA": {
                "v": "89.5",
                "best": false,
                "second": true
              },
              "JPE": {
                "v": "136.5",
                "best": false,
                "second": true
              },
              "PVE": {
                "v": "128.5",
                "best": false,
                "second": true
              },
              "TE": {
                "v": "56.1",
                "best": false,
                "second": true
              },
              "HS": {
                "v": "32.1",
                "best": false,
                "second": true
              },
              "Jrk": {
                "v": "0.21",
                "best": true,
                "second": false
              },
              "FS": {
                "v": "9.51",
                "best": false,
                "second": false
              }
            },
            "TotalCapture": {
              "PA": {
                "v": "18.7",
                "best": true,
                "second": false
              },
              "JPE": {
                "v": "29.0",
                "best": true,
                "second": false
              },
              "PVE": {
                "v": "26.3",
                "best": true,
                "second": false
              },
              "TE": {
                "v": "17.5",
                "best": false,
                "second": true
              },
              "HS": {
                "v": "8.3",
                "best": true,
                "second": false
              },
              "Jrk": {
                "v": "0.07",
                "best": true,
                "second": false
              },
              "FS": {
                "v": "2.06",
                "best": false,
                "second": false
              }
            },
            "Nymeria (In-the-wild)": {
              "PA": {
                "v": "-",
                "best": false,
                "second": false
              },
              "JPE": {
                "v": "-",
                "best": false,
                "second": false
              },
              "PVE": {
                "v": "-",
                "best": false,
                "second": false
              },
              "TE": {
                "v": "-",
                "best": false,
                "second": false
              },
              "HS": {
                "v": "-",
                "best": false,
                "second": false
              },
              "Jrk": {
                "v": "-",
                "best": false,
                "second": false
              },
              "FS": {
                "v": "-",
                "best": false,
                "second": false
              }
            }
          }
        },
        {
          "method": "Ours-U",
          "method_bold": true,
          "block": "unified",
          "cells": {
            "AIST++": {
              "PA": {
                "v": "21.4",
                "best": true,
                "second": false
              },
              "JPE": {
                "v": "29.3",
                "best": true,
                "second": false
              },
              "PVE": {
                "v": "40.4",
                "best": true,
                "second": false
              },
              "TE": {
                "v": "17.5",
                "best": true,
                "second": false
              },
              "HS": {
                "v": "7.9",
                "best": true,
                "second": false
              },
              "Jrk": {
                "v": "1.73",
                "best": false,
                "second": true
              },
              "FS": {
                "v": "1.05",
                "best": true,
                "second": false
              }
            },
            "TotalCapture": {
              "PA": {
                "v": "23.4",
                "best": false,
                "second": true
              },
              "JPE": {
                "v": "35.5",
                "best": false,
                "second": true
              },
              "PVE": {
                "v": "47.2",
                "best": false,
                "second": true
              },
              "TE": {
                "v": "15.7",
                "best": true,
                "second": false
              },
              "HS": {
                "v": "11.1",
                "best": false,
                "second": true
              },
              "Jrk": {
                "v": "0.15",
                "best": false,
                "second": true
              },
              "FS": {
                "v": "0.86",
                "best": true,
                "second": false
              }
            },
            "Nymeria (In-the-wild)": {
              "PA": {
                "v": "-",
                "best": false,
                "second": false
              },
              "JPE": {
                "v": "-",
                "best": false,
                "second": false
              },
              "PVE": {
                "v": "-",
                "best": false,
                "second": false
              },
              "TE": {
                "v": "-",
                "best": false,
                "second": false
              },
              "HS": {
                "v": "-",
                "best": false,
                "second": false
              },
              "Jrk": {
                "v": "-",
                "best": false,
                "second": false
              },
              "FS": {
                "v": "-",
                "best": false,
                "second": false
              }
            }
          }
        }
      ]
    }
  ],
  "metrics_legend": {
    "latex_verbatim": "We report MPJPE and PA-MPJPE (mm), Acceleration Error (m/s$^2$), Jerk (km/s$^3$), Per-vertex Error (mm), Contact Accuracy, Foot Skating (FS, mm), Ground Penetration (mm), Translation Error ($T_\\text{head}$, mm), and Hips \\& Shoulders Rotation Error (deg). In all tables in this section, $\\downarrow$ means lower is better, while $\\uparrow$ means higher is better.",
    "rendered": "We report MPJPE and PA-MPJPE (mm), Acceleration Error (m/s²), Jerk (km/s³), Per-vertex Error (mm), Contact Accuracy, Foot Skating (FS, mm), Ground Penetration (mm), Translation Error (T_head, mm), and Hips & Shoulders Rotation Error (deg). In all tables in this section, ↓ means lower is better, while ↑ means higher is better.",
    "best_second_convention": "Bold and underlined values indicate the best and second-best results, respectively."
  }
}
```

## Verification notes (second pass)

- **Second independent audit** (separate script, different technique): re-read the JSON out of this very file, freshly regex-extracted every numeric token and every `\textbf{}/\underline{}` occurrence from the four tabular bodies of `experiments.tex` (after stripping structural digits from `\cmidrule`/`\multicolumn` spans, unit exponents like `$^2$`, and mixed tokens like `RobCap3D`), and compared multisets per table. Result: 241 numeric values + 42 dash cells = 283 cells match exactly; per-table bold counts (15/4/19/36) and underline counts (14/4/20/35) match the JSON flags exactly; metrics legend confirmed verbatim in the tex.
- All 283 data cells, 4 captions, 4 benchmark header groups, all metric sub-header labels (with arrows), and the printed method-row order were re-parsed from the LaTeX and diffed against the JSON above: 0 value mismatches, 0 flag mismatches, 0 order mismatches.
- Cross-check vs `/tmp/eccv_paper.txt` (rendered PDF text): every number in the four tables was located and matched (Tables 1-4, including the dash blocks for Nymeria).
- PDF text extraction concatenates cells, so the LaTeX source was treated as authoritative; the PDF text was used as a redundant read of the digit strings only.

### Structural notes
- **Table 2 layout**: printed transposed (metrics as rows, methods as columns: HuMoR, RoHM, Ours-S, Ours-U). Normalized here to method-rows for a uniform site schema; the `layout` field records this. Benchmark is AMASS per the caption ("on AMASS"); there is no benchmark header row in the printed table.
- **Blocks**: Tables 1, 3 and 4 print a `\midrule` between the specialist block (top: baselines + Ours-S) and the unified block (bottom: RoHM-U, RoHM++-U, Ours-U). Best/second bold+underline markings are computed **within each block** (and within each benchmark column). The `block` field on each row records this. Table 2 has a single block.
- **Method names** are verbatim table labels: Table 4 prints `RobCap` / `RobCap3D` (the prose calls them RobustCap / RobustCap3D). `method_bold` records the `\textbf` on Ours-S / Ours-U row labels.
- **Dashes**: Table 1 Nymeria cells for RoHM-U / RoHM++-U / Ours-U are four separate `-` cells; in Table 4 the Nymeria cells of those rows are a single `\multicolumn{7}{c}{-}` span, expanded here to one `-` per metric cell.

### Ambiguities and how they were resolved
1. **Skating units differ between tables.** The metrics legend defines "Foot Skating (FS, mm)", whose abbreviation and value range (0.22-9.51) match Table 4's `FS` column only. Tables 1-2 print `Ska`/`Skating` with values 0.018-0.685, and the prose calls 0.031 "the lowest skating ratio". Resolution: `unit: null` for Table 1 `Ska` and Table 2 `Skating` (dimensionless ratio); `unit: "mm"` for Table 4 `FS` per the legend.
2. **Jerk unit on Nymeria (Table 4).** The legend says Jerk is km/s^3 (and the AIST++ prose uses km/s^3 for 0.29), but the Nymeria prose says "jerk (0.048 m/s^3)". Resolution: kept `unit: "km/s^3"` from the legend/table-wide definition and transcribed the value 0.048 as printed; the prose inconsistency is flagged here, not silently resolved.
3. **TE vs T_head.** The legend's "Translation Error (T_head, mm)" maps to Table 3's `T_h` column (HMD head translation). Table 4's `TE` is a different translation metric (global/root translation; prose: "global translation (5.42 vs. 15.9 mm)"). Both recorded with unit mm, keys kept distinct (`T_h` vs `TE`).
4. **Tie in Table 3 AMASS Con**: EgoEgo 0.92 and Ours-S 0.92 are *both* underlined (tie for second). Both carry `second: true`, exactly as printed.
5. **Table 2 Skating underline**: RoHM 0.024 is underlined although Ours-U 0.019 is numerically second-lowest; the paper's marking is preserved as printed (0.024 `second: true`, 0.019 plain) - transcription, not correction.
6. **Contact Accuracy** has no unit in the paper; recorded `unit: null`, direction `higher` from the `Con\uparrow` arrow.

