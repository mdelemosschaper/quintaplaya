# py4dgeo analysis — pulled for quintaplaya

Pulled from [3dgeo-heidelberg/py4dgeo](https://github.com/3dgeo-heidelberg/py4dgeo) (MIT
licensed, see `LICENSE_py4dgeo.md`) on 2026-09-10, for the Quinta Playa beach-morphology
change-detection work.

## What's here

- **`official_tutorials/`** — the "Basic usage tutorials" notebooks from the docs
  (https://py4dgeo.readthedocs.io/en/latest/basic.html), the ones flagged as relevant
  earlier: `m3c2.ipynb`, `registration.ipynb`, `m3c2ep.ipynb`, the three `4dobc-*.ipynb`,
  plus `c2c.ipynb` and `outlier_removal.ipynb` for context/preprocessing. These run on
  small synthetic/toy data (planes, not real terrain) — good for learning the API, not
  representative of real beach data volume or noise.

- **`demo_workflows/`** — fuller, published worked examples from py4dgeo's `demo/`
  folder, run on **real terrain point clouds** (a rock-glacier monitoring study) rather
  than toy data: `m3c2-change_analysis.ipynb`, `registration_standard_ICP.ipynb`,
  `m3c2ep_change_analysis.ipynb`, `4dobc-change_analysis.ipynb`. These are the closer
  analogue to what a real Quinta Playa run should look like.

- **`quintaplaya/quintaplaya_m3c2_starter.ipynb`** — a notebook written specifically for
  this project: loads two months of exported dense point clouds, does a stable-ground
  registration check, runs M3C2, and plots the result. Paths and parameters (normal
  radius, cylinder radius, core-point spacing) are placeholders — it's a skeleton to
  fill in against real Dec 2024 / Jan 2025 exports, not a finished pipeline.

## About the test data (important)

The official tutorial notebooks (`official_tutorials/`) reference small example point
clouds (`plane_horizontal_t1.xyz`, `ahk_*.laz`, etc.) that py4dgeo fetches
**automatically at first run** via the `pooch` package, from Zenodo
(doi:10.5281/zenodo.18432391). I could not pre-download and bundle that data myself —
my sandbox's network access doesn't reach zenodo.org — but you don't need to: just run
a tutorial notebook with internet access and `find_file(...)` pulls what it needs the
first time, caching it locally after that. No action needed on your end beyond having
`pooch` installed (it's a py4dgeo dependency already).

## Installing py4dgeo

```
git clone --recursive https://github.com/3dgeo-heidelberg/py4dgeo.git
cd py4dgeo
python -m pip install -v --editable .
```

Needs Python ≥3.10 and a C++ compiler toolchain (OpenMP for multi-threading). A Docker
image with JupyterLab preconfigured is also available if you'd rather skip the build.

## Suggested order

1. `official_tutorials/m3c2.ipynb` — learn the core M3C2 API on toy data.
2. `official_tutorials/registration.ipynb` — registration/ICP basics.
3. `demo_workflows/registration_standard_ICP.ipynb` — same idea on real terrain data.
4. `demo_workflows/m3c2-change_analysis.ipynb` — full real-data M3C2 workflow.
5. `quintaplaya/quintaplaya_m3c2_starter.ipynb` — adapt to actual Quinta Playa exports.
6. Once 3+ months are processed: `official_tutorials/4dobc-creation.ipynb` →
   `4dobc-analysis.ipynb` → `demo_workflows/4dobc-change_analysis.ipynb` for full
   time-series change tracking instead of one pairwise comparison.
7. If per-month GCP fit quality keeps varying: `official_tutorials/m3c2ep.ipynb` /
   `demo_workflows/m3c2ep_change_analysis.ipynb` to propagate that uncertainty.

## Adding this to your quintaplaya branch

This folder is meant to be dropped straight into your repo, e.g.:

```
cp -r py4dgeo_analysis /path/to/your/quintaplaya/checkout/
cd /path/to/your/quintaplaya/checkout
git checkout -b py4dgeo-analysis   # or your existing branch
git add py4dgeo_analysis
git commit -m "Add py4dgeo tutorial/demo notebooks and beach-change starter notebook"
git push
```
