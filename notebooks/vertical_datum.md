# Vertical datum convention — Quinta Playa

Decision, 2026-10-09.

## Convention

All **land elevations** (RTK beach profiles, drone DEM) are kept on **EGM2008**, in
their native datum, unmodified.

All **water levels** are shifted onto that datum by a single constant:

    water level above EGM2008 (t) = +0.276 + tide(t) + SLA(t)
    TWL above EGM2008 (t)        = +0.276 + tide(t) + SLA(t) + R2%(t)

Zero on the DEM is the **EGM2008 geoid surface, not mean sea level**. Local MSL at
Quinta Playa sits at **+0.276 m** on this datum. Do not label the DEM zero "MSL".

## Derivation of the +0.276 m offset

| term | value | source |
|---|---|---|
| MDT (sea surface above GOCO06s) | +0.546 m | `adt − sla`, DUACS 0.125° L4, v202411 |
| geoid term `N_GOCO06s − N_EGM2008` | −0.270 m | ICGEM calculation service, site coordinates |
| **local MSL above EGM2008** | **+0.276 m** | sum |

Chain, with `h` ellipsoidal height, `N_E` = EGM2008 geoid, `N_G` = GOCO06s geoid:

    DEM elevation           H_E    = h − N_E
    MDT definition          MDT    = MSS − N_G
    sea surface (ellips.)   SSH(t) = MSS + SLA(t) + tide(t)
    sea surface on EGM2008         = MDT + SLA(t) + tide(t) + (N_G − N_E)

Derived quantities on this datum:
- MHW (from tide+SLA peaks, 1995–2024): 0.584 m on the MSS datum → **+0.860 m on EGM2008**

## Provenance of the MDT

- DUACS version `202411` = DT2024, which uses **MDT_CNES_CLS22** (switch date 2024/11/06;
  CNES-CLS18 before). Source: CMEMS-SL-QUID-008-032-068, Table 15 and §II.4.5.
- MDT CNES-CLS22 geodetic first guess = CNES-CLS22 MSS − **GOCO06s**, reference period
  **1993–2012**, refined with drifter/Argo/HF-radar data. Source: Jousset et al. (2026), ESSD 18, 2285.
- `MDT = adt − sla` taken from the same product file, so MDT and SLA share the 1993–2012
  reference period by construction. Verified constant in time (see `marcus_sla.ipynb`).
- The C3S PQAD for vDT2024 does **not** state the MDT version or geoid; its reference list
  still cites CNES-CLS18. Do not source the geoid from that document.

## Uncertainty

The +0.276 m is a difference of two comparable terms, so its relative uncertainty is worse
than either input. Carry **±0.1–0.2 m**, dominated by:

1. **EGM2008's own error at Isabela** — remote volcanic island, limited terrestrial gravity.
   This is the regime Seeger & Minderhoud (2026) identify as worst-performing for geoid models.
2. **MDT coastal accuracy** — CNES-CLS22's geodetic first guess has ~100–125 km effective
   resolution with additional Lagrangian filtering in the 0–80 km coastal band. The MDT around
   Isabela carries no local information; it is a smooth regional value. ~4 cm per Birol et al. (2025).
3. **RTK base station absolute height** — if the drone DEM was georeferenced from a base with an
   averaged single-point position, this can exceed every other term combined. Establish how the
   base position was fixed.
4. **Which geoid the drone software actually applied** — confirm EGM2008, not EGM96.

Context: Seeger & Minderhoud (2026) report a global coastal mean of 0.24 m (median 0.16,
s.d. 0.52) for MSL above EGM2008, computed by this same route. +0.276 m at Quinta Playa sits
essentially at the global mean — not anomalous, and not in the >1 m regime they flag for parts
of the Pacific and Latin America. Note the raw MDT (+0.546 m) is not the quantity comparable
to their statistic; +0.276 m is.

**To be validated in the field:** one RTK shot of the still-water line at a logged UTC time
gives the total offset empirically, base-position error included. Agreement within ~0.1 m
validates the chain.

## What this does NOT change

The CoastSat shoreline correction stays on the **MSS datum**. It uses
`corrected = raw + (wl − REF_LEVEL)/tanβ` with `REF_LEVEL = 0.0` meaning the MSL contour, and
both terms are on the MSS datum. Feeding EGM2008-shifted water levels in without also shifting
`REF_LEVEL` would move every shoreline to the EGM2008 geoid contour instead — a systematic
0.276/tanβ ≈ 7 m horizontal shift at tanβ = 0.04, and it would invalidate the existing
CoSMoS-COAST calibrations.

Keep two clearly named series:
- `water_level` — MSS datum, used for the shoreline correction and CoSMoS-COAST
- `water_level_egm2008` — EGM2008 datum, used against profiles, the drone DEM and nest elevations

To compare satellite shorelines against the drone DEM, extract the **+0.276 m EGM2008 contour**
from the DEM rather than its 0 m contour. That matches the existing MSL-referenced satellite
shorelines and leaves the whole CoSMoS-COAST chain untouched.

## References

- Seeger, K. & Minderhoud, P. S. J. (2026). Sea level much higher than assumed in most coastal
  hazard assessments. *Nature* 652, 667–674. doi:10.1038/s41586-026-10196-1
- Jousset, S. et al. (2026). New global mean dynamic topography CNES-CLS-22. *ESSD* 18, 2285.
- CMEMS Sea Level TAC DUACS products QUID, CMEMS-SL-QUID-008-032-068.
- Lyard, F. H. et al. (2021). FES2014 global ocean tide atlas. *Ocean Science* 17, 615–649.
- Birol, F. et al. (2025). Understanding uncertainties in the satellite altimeter measurement of
  coastal sea level. *Ocean Science* 21, 133–150.
- Ince, E. S. et al. (2019). ICGEM. *ESSD* 11, 647–674.
- Pronk, M. et al. (2024). DeltaDTM: a global coastal digital terrain model. *Sci. Data* 11, 273.
  (EGM2008, assumed ≈ MSL — carries the same +0.276 m offset if ever used quantitatively.)