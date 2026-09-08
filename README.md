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

## Daily workflow
 
- **Before you start**: GitHub Desktop → **Fetch origin** → **Pull origin**.
- **Work**: open your notebook in VS Code, make sure the kernel says `quintaplaya`.
- **When you stop**: save in VS Code, then GitHub Desktop → type a short summary (e.g. "added ERA5 seasonal plots") → **Commit to main** → **Push origin**.
## Rules
 
1. **Everyone works in their own notebooks** (`yourname_topic.ipynb`). Never edit someone else's.
2. **Copy functions between notebooks** if you need them. No shared package.
3. **Load data with relative paths**: `pd.read_csv("../data/coastsat/transect_timeseries.csv")`. No `C:/Users/...`.
4. **Data is CSV, GeoJSON or NetCDF** — no `.pkl`. Only the person who processed the data replaces files in `data/`, and they update `data/README.md` when they do.
5. **Pull before you start, push when you stop.** Since nobody touches the same file, there are no conflicts.
6. Need a package? Add it to `environment.yml`, push, and tell the group to run `conda env update -f environment.yml` in Anaconda Prompt / Terminal.
