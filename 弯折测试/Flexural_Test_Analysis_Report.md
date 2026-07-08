# Flexural Test Analysis Report

## 1. Report Objective

This document summarizes the flexural test data analysis, including the raw test data, thickness-standardization method, material-type comparison, statistical results, and final conclusions.

## 2. Data Source

| Item | Content |
|---|---|
| Data file | `测试结果1/数据分析.csv` |
| Analysis tool | `数据分析工具.html` |
| Test type | Three-point flexural test |
| Material types | Roving / `3k`, Plain / `1x1`, Twill / `2x2` |
| Main raw metrics | `Verformung [mm]`, `Standardkraft [MPa]`, `厚度 h [mm]` |

## 3. Thickness-Standardization Method

This report uses the updated thickness-standardization method based on sandwich face stress. For each specimen, the original apparent flexural stress is converted into a simplified D7249 face stress to reduce the influence of total thickness and core-thickness differences on material comparison.

The current specimens are sandwich structures with four fibre plies on each face. The face thickness values used for each material type are:

| Material code | Display name | Face thickness per side `t` |
|---|---|---:|
| `3k` | Roving | `0.780 mm/side` |
| `1x1` | Plain | `0.576 mm/side` |
| `2x2` | Twill | `0.568 mm/side` |

Plain and Twill are estimated from the material-report areal weight, fibre density, and cured fibre volume fraction. Roving does not directly use supplier dry-cloth thickness multiplied by ply count; instead, it is estimated by combining the current Roving total thickness of about `2.2 mm` with the core thickness of about `0.72 mm` inferred from Plain/Twill.

The conversion formulas are:

$$
c = d - 2t
$$

$$
\sigma_f
=
\sigma_{\mathrm{app}}
\frac{d^2}{3t(d+c)}
$$

where `d` is the specimen total thickness, `t` is the face thickness per side, `c` is the core thickness, `\sigma_app` is the original apparent flexural stress, and `\sigma_f` is the standardized face stress.

## 4. Filtering and Analysis Settings

| Setting | Current value |
|---|---|
| Test batches | `01_21`, `01_22`, `01_23_H`, `01_24_H` |
| Specimen ID range | `1-12` for each material, 36 specimens in total |
| Thickness range | `1.77-2.33 mm` |
| Sample-index range | `1-1019`, no sample-index trimming |
| Standardization method | D7249 simplified face stress |
| Yield-detection parameters | Initial elastic fraction: `0.18`; slope-drop threshold: `0.75` |

The statistics in this section use all currently selected data. Peak stress, yield stress, initial slope, and curve area are calculated from the D7249-standardized face-stress curves. The raw peak stress is retained only as a reference column.

## 5. Material-Type Statistical Results

### 5.1 Group Statistics

Values are reported as mean ± sample standard deviation.

| Material type | Sample count `n` | Thickness mm | Core thickness `c` mm | Raw peak MPa | D7249 peak MPa | D7249 yield MPa | Initial slope MPa/mm | Curve area MPa·mm |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Roving / `3k` | 12 | `2.236 ± 0.110` | `0.676 ± 0.110` | `347.3 ± 38.3` | `254.7 ± 24.1` | `237.7 ± 23.0` | `141.5 ± 17.0` | `387.8 ± 91.6` |
| Plain / `1x1` | 12 | `1.869 ± 0.062` | `0.717 ± 0.062` | `317.1 ± 30.6` | `247.7 ± 21.5` | `236.9 ± 24.1` | `137.8 ± 8.2` | `313.8 ± 126.0` |
| Twill / `2x2` | 12 | `1.857 ± 0.040` | `0.721 ± 0.040` | `314.7 ± 22.9` | `247.0 ± 17.6` | `239.4 ± 26.8` | `134.2 ± 10.1` | `455.5 ± 414.6` |

### 5.2 Individual Specimen Results

| Type | ID | Thickness mm | Core `c` mm | Raw peak MPa | D7249 peak MPa | D7249 yield MPa | Peak deflection mm | Yield deflection mm |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `3k` | 1 | 2.26 | 0.700 | 356.7 | 263.1 | 248.5 | 1.879 | 1.667 |
| `3k` | 2 | 2.33 | 0.770 | 327.4 | 245.0 | 236.3 | 1.729 | 1.608 |
| `3k` | 3 | 2.33 | 0.770 | 353.3 | 264.4 | 247.6 | 1.922 | 1.710 |
| `3k` | 4 | 2.27 | 0.710 | 337.7 | 249.6 | 227.9 | 1.849 | 1.617 |
| `3k` | 5 | 2.28 | 0.720 | 371.1 | 274.8 | 236.4 | 1.999 | 1.616 |
| `3k` | 6 | 2.28 | 0.720 | 363.8 | 269.4 | 251.8 | 1.959 | 1.736 |
| `3k` | 7 | 2.29 | 0.730 | 323.4 | 240.0 | 214.9 | 1.846 | 1.593 |
| `3k` | 8 | 1.94 | 0.380 | 448.6 | 311.0 | 297.2 | 1.585 | 1.484 |
| `3k` | 9 | 2.31 | 0.750 | 295.6 | 220.3 | 212.3 | 1.702 | 1.621 |
| `3k` | 10 | 2.16 | 0.600 | 319.4 | 230.7 | 218.5 | 1.802 | 1.641 |
| `3k` | 11 | 2.15 | 0.590 | 328.3 | 236.7 | 223.1 | 1.724 | 1.562 |
| `3k` | 12 | 2.23 | 0.670 | 342.4 | 250.9 | 238.3 | 1.944 | 1.773 |
| `1x1` | 1 | 1.86 | 0.708 | 304.2 | 237.1 | 228.0 | 1.691 | 1.569 |
| `1x1` | 2 | 1.86 | 0.708 | 292.4 | 228.0 | 225.9 | 1.570 | 1.549 |
| `1x1` | 3 | 1.85 | 0.698 | 356.7 | 277.2 | 257.2 | 1.885 | 1.693 |
| `1x1` | 4 | 1.84 | 0.688 | 370.6 | 287.2 | 280.2 | 2.078 | 1.917 |
| `1x1` | 5 | 1.90 | 0.748 | 290.5 | 229.2 | 225.8 | 1.603 | 1.573 |
| `1x1` | 6 | 1.86 | 0.708 | 290.2 | 226.3 | 223.1 | 1.610 | 1.519 |
| `1x1` | 7 | 1.77 | 0.618 | 320.9 | 243.6 | 239.6 | 1.720 | 1.690 |
| `1x1` | 8 | 1.79 | 0.638 | 368.0 | 281.0 | 277.3 | 1.918 | 1.887 |
| `1x1` | 9 | 1.84 | 0.688 | 318.0 | 246.5 | 216.7 | 1.997 | 1.594 |
| `1x1` | 10 | 1.98 | 0.828 | 297.6 | 240.5 | 197.8 | 1.678 | 1.294 |
| `1x1` | 11 | 1.94 | 0.788 | 297.3 | 237.3 | 234.5 | 1.596 | 1.556 |
| `1x1` | 12 | 1.94 | 0.788 | 299.3 | 239.0 | 236.1 | 1.565 | 1.545 |
| `2x2` | 1 | 1.84 | 0.704 | 307.2 | 239.9 | 237.4 | 1.755 | 1.735 |
| `2x2` | 2 | 1.87 | 0.734 | 326.7 | 257.5 | 255.8 | 1.790 | 1.780 |
| `2x2` | 3 | 1.86 | 0.724 | 308.4 | 242.3 | 237.5 | 1.943 | 1.701 |
| `2x2` | 4 | 1.84 | 0.704 | 297.3 | 232.2 | 229.4 | 1.605 | 1.585 |
| `2x2` | 5 | 1.92 | 0.784 | 324.7 | 259.8 | 255.2 | 1.640 | 1.610 |
| `2x2` | 6 | 1.85 | 0.714 | 289.8 | 227.0 | 216.8 | 1.723 | 1.471 |
| `2x2` | 7 | 1.82 | 0.684 | 349.6 | 271.4 | 271.4 | 1.982 | 1.982 |
| `2x2` | 8 | 1.80 | 0.664 | 314.5 | 242.7 | 232.5 | 1.754 | 1.532 |
| `2x2` | 9 | 1.81 | 0.674 | 310.2 | 240.1 | 232.8 | 1.702 | 1.600 |
| `2x2` | 10 | 1.93 | 0.794 | 270.5 | 217.1 | 173.8 | 1.517 | 1.819 |
| `2x2` | 11 | 1.87 | 0.734 | 347.4 | 273.8 | 269.7 | 1.841 | 1.811 |
| `2x2` | 12 | 1.87 | 0.734 | 330.6 | 260.6 | 260.6 | 1.800 | 1.800 |

### 5.3 Cross-Sectional-Density-Normalized Specific Performance

For panel applications, the mechanical performance delivered per unit cross-sectional density is a more direct indicator of material efficiency. The cross-sectional densities used in this section are:

| Material type | Cross-sectional density |
|---|---:|
| Roving / `3k` | `160` |
| Plain / `1x1` | `130` |
| Twill / `2x2` | `130` |

The specific performance is calculated as:

$$
P_{\mathrm{specific}}=\frac{P_{\mathrm{D7249}}}{\rho_A}
$$

where `P_D7249` is the D7249-standardized mechanical metric and `\rho_A` is the corresponding material cross-sectional density. Values are reported as mean ± sample standard deviation.

| Material type | Cross-sectional density | Peak/density | Yield/density | Initial slope/density | Curve area/density |
|---|---:|---:|---:|---:|---:|
| Roving / `3k` | 160 | `1.592 ± 0.151` | `1.486 ± 0.144` | `0.884 ± 0.106` | `2.424 ± 0.573` |
| Plain / `1x1` | 130 | `1.906 ± 0.166` | `1.822 ± 0.185` | `1.060 ± 0.063` | `2.414 ± 0.969` |
| Twill / `2x2` | 130 | `1.900 ± 0.136` | `1.841 ± 0.206` | `1.032 ± 0.078` | `3.504 ± 3.189` |

Using Roving as the baseline, the peak specific performance is about `119.7%` for Plain and `119.4%` for Twill. For yield specific performance, Plain reaches about `122.6%` of Roving and Twill reaches about `123.9%`. Therefore, when mass or cross-sectional density is a key constraint in panel applications, Plain and Twill provide better material efficiency than Roving.

### 5.4 QC Consistency Evaluation

For practical panel applications, the consistency of the 12 specimens within each material group should also be considered, in addition to average performance. This report uses the coefficient of variation as the QC metric:

$$
CV=\frac{SD}{\bar{x}}\times100\%
$$

where `SD` is the sample standard deviation and `\bar{x}` is the sample mean. A lower `CV` indicates better within-group consistency. The QC evaluation prioritizes D7249 peak stress, D7249 yield stress, and initial slope. Curve area is used only as an auxiliary reference because it is strongly affected by the terminal deflection of each test.

| Material type | Sample count `n` | Peak CV | Yield CV | Initial slope CV | Curve area CV | Key QC average CV |
|---|---:|---:|---:|---:|---:|---:|
| Roving / `3k` | 12 | `9.5%` | `9.7%` | `12.0%` | `23.6%` | `10.4%` |
| Plain / `1x1` | 12 | `8.7%` | `10.2%` | `5.9%` | `40.1%` | `8.3%` |
| Twill / `2x2` | 12 | `7.1%` | `11.2%` | `7.6%` | `91.0%` | `8.6%` |

Based on the average CV of the key QC metrics, Plain has the best overall consistency, Twill is close to Plain, and Roving is slightly less consistent. If only peak-strength consistency is considered, Twill is the most stable. If initial-stiffness consistency is considered, Plain is clearly the best. Curve-area scatter is large, especially for Twill at `91.0%`, indicating that this metric is highly sensitive to terminal deflection or individual long-deformation curves and should not be used as the main QC criterion.

## 6. Figure Records

### 6.1 Raw Curves

The raw `Standardkraft [MPa] - Verformung [mm]` curves show that Roving has the highest apparent peak stress, with an average raw peak of `347.3 MPa`; Plain and Twill reach `317.1 MPa` and `314.7 MPa`, respectively. This difference includes both material load-carrying capability and specimen thickness/core-geometry effects, so it should not be used directly as the final material-strength ranking.

### 6.2 Standardized Curves

After D7249 face-stress standardization, the peak values of the three material types become much closer: `254.7 MPa` for Roving, `247.7 MPa` for Plain, and `247.0 MPa` for Twill. This indicates that a substantial part of the raw apparent peak difference comes from thickness and geometric effects.

### 6.3 Material-Type Mean Curves

Material-type mean curves should be exported from `数据分析工具.html` using either the "Type mean" or "Type mean: cropped" view. For ultimate-strength comparison, the D7249-standardized peak should be prioritized. For initial-response comparison, the cropped linear mean curve and initial slope should be prioritized.

### 6.4 Publication Figures

At minimum, the following publication figures are recommended:

1. D7249 peak face stress, with SD error bars.
2. D7249 yield face stress, with SD error bars.
3. Initial slope, with SD error bars.
4. QC consistency plot using peak CV, yield CV, and initial-slope CV.

Curve area can be included as an auxiliary figure, but it is strongly affected by terminal deflection. The Twill group shows especially large scatter in this metric, so curve area is not recommended as a primary conclusion metric.

## 7. Discussion

### 7.1 Thickness Effect

In the raw apparent peak stress, Roving is clearly higher than Plain and Twill, with average values of `347.3 MPa`, `317.1 MPa`, and `314.7 MPa`, respectively. After D7249 face-stress standardization, the peak values become `254.7 MPa`, `247.7 MPa`, and `247.0 MPa`, reducing the group difference from about `30 MPa` in the raw apparent values to about `8 MPa`.

This shows that specimen total thickness and core geometry have a clear influence on the original apparent flexural strength. For this test batch, direct comparison of `Standardkraft [MPa]` would overestimate the advantage of Roving over Plain/Twill. D7249 face stress is more suitable as a cross-thickness comparison metric.

### 7.2 Material-Type Differences

Based on D7249-standardized peak stress, Roving has the highest average value at `254.7 MPa`, which is about `2.8%` higher than Plain at `247.7 MPa` and about `3.1%` higher than Twill at `247.0 MPa`. Plain and Twill are nearly identical in standardized peak stress.

For yield stress, all three materials are also very close: Roving reaches `237.7 MPa`, Plain reaches `236.9 MPa`, and Twill reaches `239.4 MPa`. Under the current yield-detection parameters, the initial instability or yield behavior of the three weave types does not differ strongly.

For initial slope, Roving is highest at `141.5 MPa/mm`, followed by Plain at `137.8 MPa/mm` and Twill at `134.2 MPa/mm`. Roving is slightly stiffer and Twill is slightly lower, but the group differences are small.

When normalized by cross-sectional density, the ranking changes. Roving has a cross-sectional density of `160`, while Plain and Twill are both `130`. The peak/density values are `1.592` for Roving, `1.906` for Plain, and `1.900` for Twill. The yield/density values are `1.486` for Roving, `1.822` for Plain, and `1.841` for Twill. Therefore, although Roving has a slightly higher absolute standardized peak value, Plain and Twill provide better load-carrying efficiency per unit cross-sectional density, with an advantage of about `19-24%` over Roving.

For curve area, Twill has the highest average value, but also a very large standard deviation. This indicates that the metric is strongly affected by individual long-deformation curves or test termination deflection. In this report, curve area should be treated as an auxiliary toughness/extended-response indicator rather than a primary strength criterion.

### 7.3 QC Consistency

Including within-group consistency as a QC metric prevents the material evaluation from relying only on mean values. Using the average CV of three key metrics, namely D7249 peak stress, D7249 yield stress, and initial slope, Plain has the best consistency at `8.3%`, Twill is close at `8.6%`, and Roving is slightly worse at `10.4%`.

By individual metric, Twill has the lowest peak CV at only `7.1%`, indicating the best repeatability in ultimate strength. Plain has the lowest initial-slope CV at `5.9%`, indicating the best repeatability in initial stiffness. Roving remains below about `10%` CV for peak and yield, but its initial-slope CV reaches `12.0%`, making its overall consistency slightly weaker.

Curve area is not suitable as a primary QC metric. Twill reaches a curve-area CV of `91.0%`, and Plain reaches `40.1%`, showing that this metric is strongly influenced by terminal deflection or individual extended-deformation specimens. Formal quality control should prioritize the CV of peak stress, yield stress, and initial slope.

### 7.4 Failure Mode and Applicability

The simplified D7249 face-stress standardization assumes that flexural failure is primarily controlled by the upper and lower faces and that the faces are approximately symmetric. The current data file does not directly record fracture appearance, core shear, core crushing, or face-core debonding, so this report treats the D7249-standardized results as the main geometric correction metric.

If some specimens mainly failed by core shear, core crushing, or interface debonding, the face stress should not be interpreted as a pure fibre-face ultimate strength. This assumption should be verified later using specimen photos, fracture observations, or microscopic cross-sections.

In addition, specimen `3k-08` has a thickness of `1.94 mm`, which is clearly lower than the other Roving specimens. With the current `t = 0.780 mm/side`, its calculated core thickness is only `0.380 mm`, and its D7249 peak reaches `311.0 MPa`, much higher than most other specimens in the group. This point should be checked separately in the final statistics, especially for thickness measurement and specimen structure.

## 8. Conclusions

1. The raw apparent flexural strength shows Roving higher than Plain and Twill, but the difference decreases substantially after D7249 standardization. This indicates that thickness and core geometry are important influencing factors in this dataset.
2. With the current face-thickness estimates, the absolute standardized peak values are close: Roving `254.7 MPa`, Plain `247.7 MPa`, and Twill `247.0 MPa`. Roving is slightly higher, but its advantage is only about `3%`.
3. For practical panel applications, specific performance per unit cross-sectional density is recommended as the main comparison metric. After normalization using Roving `160` and Plain/Twill `130`, the peak specific performance of Plain and Twill is about `120%` of Roving, and the yield specific performance is about `123-124%` of Roving.
4. In terms of cross-sectional-density efficiency, Plain and Twill are clearly better than Roving. Plain has the highest initial-slope specific performance, while Twill has a slightly higher yield specific performance. If lightweight panel efficiency is prioritized, Plain/Twill are the better choices.
5. From the QC consistency perspective, Plain has the lowest average CV of the key metrics at `8.3%`; Twill is close at `8.6%`; Roving is weaker at `10.4%`. If batch stability is required, Plain/Twill remain preferable to Roving.
6. Considering both specific performance and QC consistency, Plain is the most balanced option. Twill performs well in yield specific performance and peak consistency, but its curve-area scatter is large. Roving has a slightly higher absolute peak value, but it does not lead in density-specific efficiency or consistency.
7. Specimen `3k-08` and the large scatter in Twill curve area should be flagged for review in the final report to avoid over-interpreting single-specimen anomalies or test-termination effects.

## 9. Follow-Up Work

- Add microscopic cross-section or layup-measured face thickness to replace the current estimated values.
- Perform sensitivity analysis for `3k` face thickness over `0.72-0.82 mm/side`.
- Perform conservative sensitivity analysis for `1x1` and `2x2` by excluding powder/coating thickness.
- Export final figures with consistent numbering for publication or presentation materials.
