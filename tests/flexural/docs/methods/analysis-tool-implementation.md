# How the flexural-test data analysis tool works

This document describes the interface and embedded JavaScript logic in [`data-analysis-tool.html`](../../analysis/data-analysis-tool.html). The tool reads flexural-test data, filters and standardizes curves, identifies characteristic points, generates statistical charts, and exports results.

## 1. Scope

The analysis tool is a standalone browser application for processed three-point flexural-test CSV data. All calculations run locally in the browser; no backend service is required.

Its main functions are:

- load the default [`data-analysis.csv`](../../analysis/data-analysis.csv) or a manually selected CSV;
- filter curves by material type, specimen ID, test batch, thickness, and sample index;
- switch between raw apparent stress, thickness-normalized stress, simplified D7249 face stress, and areal-density-specific performance;
- detect the peak point, yield point, initial slope, and curve area for every specimen;
- generate individual curves, material-type mean curves, cropped linear mean curves, and publication charts;
- export publication charts as PNG, SVG, or CSV.

## 2. Input and validation

The tool first attempts to load `data-analysis.csv` from the same directory. If browser security rules block local `fetch` requests, select the CSV manually or serve the directory through a local HTTP server.

The CSV must include these columns:

| Column | Purpose |
|---|---|
| `Test ID` | Test batch, such as `01_24` or `01_24_H` |
| `Specimen Type` | Material code, normally `3k`, `1x1`, or `2x2` |
| `Unified Specimen ID` | Stable specimen number within one material type |
| `Original Probe ID` | Traceability to the original machine export |
| `Source File` | Source-data filename |
| `Thickness h [mm]` | Thickness filter and normalization input |
| `Sample Index` | Point order and sample-range filter |
| `Deflection [mm]` | Curve x-coordinate |
| `Standard Stress [MPa]` | Raw apparent-stress y-coordinate |

The parser handles UTF-8 CSV text, quoted fields, escaped quotes, commas inside quoted fields, and CRLF or LF line endings. Missing required columns stop the import and produce a visible error.

## 3. Internal data model

Each CSV row is converted to a typed record. Records are then grouped by material type and unified specimen ID. Within each specimen group, points are ordered by sample index and converted into a curve object containing metadata, raw points, and calculated metrics.

The application keeps the following state in memory:

- complete parsed rows and specimen curves;
- active filters and view mode;
- normalization parameters;
- chart zoom and pan state;
- user-defined material colors, face thicknesses, areal densities, and correction factors.

Changing a control recalculates the affected derived data and redraws the interface.

## 4. Filtering

Filters are applied before statistics and mean curves are calculated. Available filters include material type, text search, specimen-ID range, thickness range, sample-index range, and test batch. The active filter summary is shown above the plots and is included in exported chart metadata.

## 5. Curve views

The tool provides four main views:

1. **Raw curves** show individual specimen curves.
2. **Normalized curves** show individual curves after the selected normalization.
3. **Type mean** resamples curves to a common deflection grid and calculates a mean curve for every material type.
4. **Type mean: cropped** limits each specimen to its automatically detected initial linear region before calculating the mean.

Reference lines can show material-type means, the overall selected mean, or both. The number of resampling points and reference-line width are configurable.

## 6. Normalization methods

### 6.1 No normalization

The tool displays `Standard Stress [MPa]` without geometric correction.

### 6.2 Section-inertia reference

For a rectangular section,

$$
I = \frac{b h^3}{12}
$$

When specimen width is assumed constant, a curve is converted to reference thickness `h0` with

$$
\sigma_0 = \sigma \frac{I_0}{I}
= \sigma \left(\frac{h_0}{h}\right)^3
$$

This is a geometric comparison mode and not a replacement for a material-specific failure model.

### 6.3 Simplified D7249 face stress

For a symmetric sandwich specimen with one face thickness `t`, total thickness `d`, and core thickness `c = d - 2t`, the tool uses

$$
\sigma_f = \sigma_{app}\frac{d^2}{3t(d+c)}
$$

The method assumes three-point bending, symmetric faces, and face-dominated failure. Face thickness is configured separately for `3k`, `1x1`, and `2x2`.

### 6.4 Areal-density-specific performance

The selected base metric is divided by the user-defined areal density:

$$
P_{specific}=\frac{P}{\rho_A}
$$

The resulting stress unit is `MPa·m²/g`. The base metric can be raw stress, section-inertia normalized stress, or D7249 face stress.

### 6.5 Material-type factor

Optional type-specific factors can be applied for sensitivity studies. Their physical basis and chosen values must be documented in any report that uses them.

## 7. Characteristic metrics

For each displayed specimen, the tool calculates:

- peak stress and the corresponding deflection;
- an initial slope from the configured elastic fraction;
- a yield point when the smoothed local slope drops below the configured fraction of the initial slope;
- curve area by trapezoidal integration.

If no clear slope reduction is detected, the peak point is used as the fallback characteristic point. Yield results therefore depend on the smoothing and threshold settings and should be verified against the curve shape.

## 8. Mean curves and statistics

Mean curves are calculated only from currently selected specimens. Each curve is interpolated onto a common deflection grid before point-by-point averaging. Group tables report specimen count, average thickness, initial slope, yield stress and deflection, peak stress and deflection, and curve area.

Publication charts summarize selected metrics by material type and can include standard-deviation error bars. Statistical outputs inherit the current filters and normalization settings.

## 9. Exports

The tool exports the publication chart as:

- PNG for reports and presentations;
- SVG for editable vector workflows;
- CSV for downstream plotting and statistical processing.

Exported results should be saved together with the source CSV, active filter range, normalization method, and parameter values so the analysis remains reproducible.

## 10. Operating assumptions

- The CSV schema and units match the required column list.
- Specimen IDs uniquely identify curves within a material type.
- Width is constant when the section-inertia method is used without a width column.
- D7249 face-stress results are interpreted only for approximately symmetric, face-dominated sandwich behavior.
- Material face thicknesses and areal densities are verified before final reporting.
- Curve-area comparisons use a consistent terminal-deflection rule.

For final reporting, first archive the processed CSV, then record filters and normalization parameters, inspect outliers, export the required charts, and calculate formal inferential statistics in a dedicated statistical workflow when needed.
