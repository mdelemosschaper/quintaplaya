# Coastal Assessment of Quinta Playa

## Contents 

- CoastSat Post Processing
- ERA 5 Wave Analysis
- Waves, Shorelines, ENSO comparision Analysis
- Stockdon Wave Run Up Analysis 
- Go Pro Wave Run Up Analysis
- Groundwater Well Analysis
- Groundwater and Wave Run Up (Field Data and Stockdon) comparison Analysis 

## Downloading the environment 
Open **Anaconda Prompt** (Windows) or **Terminal** (Mac) and build the environment:
```bash
   cd Documents/quintaplaya
   conda env create -f environment.yml
```

## Daily workflow (with branches)
 
Everyone works on their own branch, never directly on `main`. `main` only receives finished work through a pull request.
 
**1. Start of a task - make a branch**
- GitHub Desktop → **Current Branch** (top bar) → **New Branch**.
- Name it `yourname/topic`, e.g. `marcus/enso-decomposition`.
- Make sure it says "based on **main**" → **Create Branch** → **Publish branch**.
  
**2. Work**
- Open your notebook in VS Code (kernel `quintaplaya`), make your changes, save.
- GitHub Desktop → type a short summary → **Commit to yourname/topic** → **Push origin**.
- Repeat as often as you like — commits on your branch don't affect anyone else.

**3. Finished - merge into main**
- GitHub Desktop → **Branch → Create Pull Request** (opens GitHub in your browser).
- Add a one-line description → **Create pull request** → **Merge pull request** → **Confirm merge**.
- Back in GitHub Desktop → **Current Branch → main** → **Fetch origin** → **Pull origin**.
- Optional: **Branch → Delete** the old branch.

**4. Next task** — start again from step 1, always branching from an up-to-date `main`.
 
**Keeping up with others**: any time you want the latest work from the group while on your branch, switch to `main`, **Pull origin**, then switch back and **Branch → Update from main**.
 
## Rules
 
1. **Everyone works in their own notebooks** (`yourname_topic.ipynb`). Never edit someone else's.
2. **Copy functions between notebooks** if you need them. No shared package.
3. **Load data with relative paths**: `pd.read_csv("../data/coastsat/transect_timeseries.csv")`. No `C:/Users/...`.
4. **Data is CSV, GeoJSON or NetCDF** — no `.pkl`. Only the person who processed the data replaces files in `data/`, and they update `data/README.md` when they do.
5. **Branch per task, pull request to merge.** Never commit directly to `main`. Since nobody touches the same notebook, pull requests will merge cleanly.
6. Need a package? Add it to `environment.yml`, push, and tell the group to run `conda env update -f environment.yml` in Anaconda Prompt / Terminal.

