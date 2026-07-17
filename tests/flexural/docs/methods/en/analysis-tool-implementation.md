# How the Flexural-Test Data Analysis Tool Works

[English](analysis-tool-implementation.md) | [Chinese](../zh/analysis-tool-implementation.md)

This document is based on the interface structure and embedded JavaScript logic of [`data-analysis-tool.html`](../../../analysis/data-analysis-tool.html). It explains how the tool reads flexural-test data, applies filters and standardization, identifies yield features, creates statistical figures, and exports results.

## 1. Tool Scope

`data-analysis-tool.html` is a single-file, browser-based analysis tool designed primarily for CSV results from three-point flexural tests. It performs all core calculations in the browser and does not require a back-end server.

Its main functions are:

- Read the default `data-analysis.csv` file or a manually selected CSV file.
- Filter curves by specimen type, specimen ID, test batch, thickness range, and sample-index range.
- Switch among raw apparent stress, thickness standardization, simplified D7249 face stress, and areal-density-specific performance.
- Automatically identify the peak point, yield point, initial slope, and area under the curve for every specimen.
- Generate individual curves, material-type mean curves, linearly cropped mean curves, and publication figures.
- Export publication figures as PNG, SVG, or CSV.

## 2. Data Input and Validation

### 2.1 Data Sources

The tool provides two ways to load data:

1. Click “Load data-analysis.csv” to call `fetch("data-analysis.csv")` and read the default file from the HTML file's directory.
2. Load a CSV file manually through the file picker.

If the browser's security policy blocks local `fetch` requests, the default-loading action may fail. In that case, use the file picker or open the HTML file through a local HTTP server.

### 2.2 Required Columns

The CSV must contain the following columns. A mismatched column name causes an immediate error:

| Column | Purpose |
| --- | --- |
| Test ID | Used to extract the test batch, such as `01_24` or `01_24_H` |
| Specimen type | Material type; the tool currently recognizes mainly `3k`, `1x1`, and `2x2` |
| Unified specimen ID | Unified ID within a type; used on curve labels and the horizontal axis of yield plots |
| Original probe ID | Shown in the series list for traceability to the original specimen |
| Source file | Records the source data file |
| Thickness h [mm] | Input for standardization and thickness filtering |
| Sample index | Used to sort curve points and filter the sample-index range |
| Deformation [mm] | Deformation/displacement used on the curve's horizontal axis |
| Standard force [MPa] | Apparent stress used on the raw curve's vertical axis |

### 2.3 CSV Parsing

The built-in `parseCsv()` function supports:

- Removal of a UTF-8 BOM.
- Comma-separated fields.
- Fields enclosed in double quotation marks.
- Escaped double quotation marks within fields.
- Ignoring empty lines.

After parsing, `loadCsvText()` converts the key numeric columns to `Number` values and removes rows without a valid unified specimen ID, deformation value, or standard-force value.

## 3. Internal Data Model

### 3.1 Row Data

Each CSV row is converted into a sample-point object:

```js
{
  testId,
  type,
  unifiedId,
  originalProbe,
  sourceFile,
  thickness,
  sampleIndex,
  deformation,
  stress
}
```

Here, `deformation` comes from the deformation column and `stress` comes from the standard-force column.

### 3.2 Specimen Grouping

`buildSpecimens()` merges sample points by the following key:

```text
specimen key = specimen type + "|" + unified specimen ID
```

Each specimen object contains:

- `type`: material type.
- `unifiedId`: unified specimen ID.
- `name`: display name, such as `Roving-03`.
- `batch`: test batch extracted from the test ID.
- `thickness`: specimen thickness.
- `points`: curve points sorted in ascending sample-index order.

Material-type display names are fixed as follows:

| Raw type | Display name |
| --- | --- |
| `3k` | Roving |
| `1x1` | Plain |
| `2x2` | Twill |

## 4. Filtering Logic

All charts and statistics are based on the currently visible specimens. `getVisibleSpecimens()` applies these filters in sequence:

1. Material-type checkboxes: `3k`, `1x1`, and `2x2`.
2. Series-selection list: the individual specimens selected by the user.
3. Test batch: recognized from the test ID, for example `01_21` or `01_24_H`.
4. Unified specimen-ID range.
5. Thickness range.

The sample-index range does not remove a specimen. Instead, `getDisplayPoints()` filters the points within each curve.

## 5. Chart Modes

The tool has four main views:

| Mode | Calculation |
| --- | --- |
| Raw | Displays standard force directly against deformation |
| Standardized | Calls `normalizeStress()` for every point before plotting |
| Type mean | Resamples curves by material type and calculates a mean curve |
| Type mean: cropped | Automatically crops every curve to its linear segment before calculating the type mean |

In the raw and standardized views, the curve chart marks the yield point and peak point of each specimen. Mean views show only mean curves.

## 6. Standardization Calculations

Standardization affects only the standardized view and the related mean views. The raw view always uses the original standard-force values.

### 6.1 No Standardization

When the mode is `none`:

$$
\sigma_{\mathrm{display}} = \sigma_{\mathrm{app}}
$$

The material-type correction factors have no effect in this mode.

### 6.2 Reference Second Moment of Area I0/I

This mode converts each curve to a reference thickness `h0`. The code assumes that all specimens have the same width and uses the second-moment ratio for a solid rectangular section:

$$
I \propto h^3
$$

The actual calculation is:

$$
\sigma_{\mathrm{norm}}
=
\sigma_{\mathrm{app}}
\frac{h_0^3}{h^3}
=
\sigma_{\mathrm{app}}
\left(\frac{h_0}{h}\right)^3
$$

where:

- `h` is the current specimen thickness from the CSV thickness column.
- `h0` is the reference thickness entered in the interface; its default is `2.00 mm`.

If the thickness is invalid or the reference thickness is less than or equal to zero, the tool retains the original value.

### 6.3 Simplified D7249 Face Stress

This mode approximately converts solid-beam apparent stress into sandwich-structure face stress. The tool assumes:

- Three-point bending.
- Symmetric upper and lower faces.
- Failure governed primarily by the faces.
- No explicit use of width when the CSV has no width column.

Let the total thickness be `d` and the thickness of one face be `t`. The core thickness is:

$$
c = \max(d - 2t, 0)
$$

The code also imposes the following limit:

$$
t \le 0.98 \times \frac{d}{2}
$$

The apparent-to-face-stress conversion is:

$$
\sigma_f
=
\sigma_{\mathrm{app}}
\frac{d^2}{3t(d+c)}
$$

The thickness `t` of one face is selected by material type. The current specimens are sandwich structures with four fiber plies on each side. The Plain and Twill defaults are estimated from the areal density and cured fiber-volume fraction in the material reports; the Roving default is further constrained by the currently measured total thickness:

| Material type | Tool display | Default one-side face thickness `t` |
| --- | --- | ---: |
| `3k` | Roving | `0.780 mm/side` |
| `1x1` | Plain | `0.576 mm/side` |
| `2x2` | Twill | `0.568 mm/side` |

The interface allows direct editing of `t` for all three materials, either for sensitivity analysis or to replace the estimates with later microscopic cross-section or layup measurements. The D7249 standardization passes the current specimen's `type` to `getFaceThickness(type)`. Consequently, individual curves, type means, linearly cropped means, yield/peak statistics, and areal-density-specific performance with “simplified D7249 face stress” selected as the pre-standardization method all use the face thickness assigned to that material.

### 6.4 Areal-Density-Specific Performance

This mode first performs a pre-standardization step and then divides by the areal density assigned to the material type:

$$
y_{\mathrm{specific}}
=
\frac{y_{\mathrm{base}} \cdot k_{\mathrm{type}}}{A_{\mathrm{type}}}
$$

where:

- `y_base` comes from the pre-standardization selection: no pre-standardization, reference second moment of area I0/I, or simplified D7249 face stress.
- `k_type` is the material-type correction factor.
- `A_type` is the areal density for the corresponding material type; all three default to `132.9 g/m²`.

The interface displays the unit as:

```text
MPa·m²/g
```

If the areal density is invalid or less than or equal to zero, the tool returns only `y_base * k_type`.

### 6.5 Material-Type Correction Factors

When the standardization mode is not `none`, the tool reads a manually entered correction factor for each material type:

| Type | Input field |
| --- | --- |
| Roving / `3k` | `factor3k` |
| Plain / `1x1` | `factor1x1` |
| Twill / `2x2` | `factor2x2` |

In ordinary standardization modes:

$$
y_{\mathrm{display}}
=
y_{\mathrm{mode}} \cdot k_{\mathrm{type}}
$$

In the areal-density-specific mode, the factor is applied before division by the areal density.

## 7. Yield Point, Peak, and Curve Area

`computeFeatures()` extracts features from every visible specimen. Feature extraction uses the current display mode, so the raw and standardized views can produce different numerical values.

### 7.1 Peak Point

The peak is the point with the greatest vertical-axis value on the current displayed curve:

$$
P_{\mathrm{peak}}
=
\arg\max(y)
$$

Here, `y` may represent raw apparent stress, standardized stress, face stress, or areal-density-specific performance.

### 7.2 Initial Slope

The tool treats an initial portion of the curve as the elastic segment. Its default fraction is `0.18`, and it can be changed in the interface. The value is constrained to `0.05-0.45`.

The end index of the elastic segment is:

$$
n_{\mathrm{elastic}}
=
\max(5,\ \lfloor n \cdot f_{\mathrm{elastic}} \rfloor)
$$

The initial slope is obtained by least-squares linear fitting:

$$
m
=
\frac{n\sum xy-\sum x\sum y}
{n\sum x^2-(\sum x)^2}
$$

### 7.3 Yield-Point Identification

The tool first applies a moving average with a window size of 5 to the vertical-axis values. Starting near the elastic segment, it then calculates the local slope of the smoothed curve:

$$
m_i
=
\frac{y_{i+2}-y_{i-2}}{x_{i+2}-x_{i-2}}
$$

The first point that satisfies both of the following conditions is identified as the yield point:

$$
y_i > 0.18 \cdot y_{\mathrm{peak}}
$$

$$
m_i < m_{\mathrm{initial}} \cdot r_{\mathrm{drop}}
$$

Here, `r_drop` is the slope-drop threshold. Its default is `0.75`, with an allowed range of `0.20-0.95`.

If no clear slope-drop point is found, the peak point is used as the yield feature point.

### 7.4 Curve Area

The area under the curve is calculated by trapezoidal integration:

$$
A
=
\sum_{i=1}^{n-1}
\frac{(x_i-x_{i-1})(y_i+y_{i-1})}{2}
$$

On a stress-deformation curve, this value can be used as a relative energy-absorption or overall curve-response metric. It is not a rigorous energy value unless the vertical- and horizontal-axis units have been converted accordingly.

## 8. Mean Curves and Reference Lines

### 8.1 Type Mean Curves

`makeAveragedSeries()` groups curves by material type and resamples each group by linear interpolation. The default is `180` resampling points; the user can select a value constrained to `50-500`.

For each material type:

1. Find the greatest final deformation among all curves of that type.
2. Create equally spaced horizontal-axis coordinates from `0` to that greatest final deformation.
3. Interpolate every curve at those coordinates.
4. Average the valid interpolation results.

### 8.2 Type Mean: Cropped

`makeLinearAveragedSeries()` first crops each curve with `cropToLinearSegment()`. The cropping logic is similar to yield identification:

- Use the initial elastic-segment slope as the reference.
- Calculate the local slope from the moving-average curve.
- Stop when the local slope falls below `initial slope × slope-drop threshold`.

The cropped mean curve is calculated only over the deformation range shared by all cropped curves. Its horizontal-axis endpoint is therefore the smallest endpoint among those curves.

### 8.3 Reference Lines

Reference lines show overall trends on the individual-curve chart. The available options are:

| Option | Meaning |
| --- | --- |
| Hidden | Do not draw a reference line |
| Mean line for each type | Draw one dashed mean curve for every material type |
| Mean line for all selected specimens | Draw one overall mean line for all selected specimens |
| Type means + overall mean | Draw both types of reference line |

Reference lines are hidden in the linearly cropped mean mode.

## 9. Statistical Output

### 9.1 Top-Level KPIs

The top-level indicators are recalculated from the current filter results:

- Number of specimens.
- Total number of currently selected sample points.
- Number of specimens per material type.
- Mean peak value.
- Mean yield point.

### 9.2 Material-Type Comparison Table

`renderSummaryTable()` summarizes the following values by material type:

| Metric | Calculation |
| --- | --- |
| `n` | Number of specimens of that type under the current filters |
| Mean thickness | Mean specimen thickness |
| Initial slope | Mean of the initial slopes of the specimens |
| Yield stress | Mean vertical-axis value at the specimen yield points |
| Yield deformation | Mean horizontal-axis value at the specimen yield points |
| Peak stress | Mean vertical-axis value at the specimen peak points |
| Peak deformation | Mean horizontal-axis value at the specimen peak points |
| Curve area | Mean trapezoidally integrated area of the specimens |

### 9.3 Publication Figures

Publication figures show bars grouped by material type and overlay the individual specimen values. Available metrics are:

- Peak stress.
- Yield stress.
- Initial slope.
- Curve area.
- Thickness.

Available error bars are:

| Option | Calculation |
| --- | --- |
| SD | Sample standard deviation with `n - 1` in the variance denominator |
| SEM | `SD / sqrt(n)` |
| 95% CI | `1.96 × SEM` |
| No error bars | Error is 0 |

`makePaperStats()` generates the statistics and retains only material types with valid values.

## 10. Export Logic

Publication figures can be exported in three formats:

| Format | Filename pattern | Content |
| --- | --- | --- |
| PNG | `flexural_figure_<metric>_600dpi.png` | 780 × 540 logical dimensions, rendered at 5× scale |
| SVG | `flexural_figure_<metric>.svg` | Vector bar chart |
| CSV | `flexural_statistics_<metric>.csv` | Grouped statistics table |

The exported CSV columns are:

```text
type,n,mean,sd,sem,ci95,error_mode,metric
```

Numeric values retain no more than six decimal places.

## 11. Interaction and Refresh Behavior

The tool uses event-driven updates:

- Changing the language reapplies all interface text and redraws the charts.
- Changing a filter resets the curve zoom and recalculates the results.
- Changing standardization parameters, material correction factors, or yield-detection parameters recalculates every feature.
- The curve chart supports mouse-wheel zoom, drag-to-pan, and view reset.
- Resizing the browser window redraws the Canvas.

All charts are drawn directly with HTML Canvas; no external charting library is used.

## 12. Important Assumptions and Limitations

1. `Specimen type + unified specimen ID` must identify one specimen uniquely. If the same combination is repeated in different test batches, the tool merges the data into one specimen.
2. Curve points are sorted by sample index. Mean-curve interpolation assumes that deformation generally increases monotonically with the sample index.
3. The reference-second-moment mode assumes the same width for every specimen because the CSV has no width column.
4. The simplified D7249 face-stress mode is an approximation converted from apparent stress. It applies to symmetric sandwich specimens under three-point bending with face-dominated failure.
5. The yield point is algorithmically identified rather than manually interpreted. It changes with the sample range, smoothing window, initial elastic-segment fraction, and slope-drop threshold.
6. Areal-density-specific performance depends on the user-entered areal densities and material-type correction factors. Equal defaults do not mean that all three materials have exactly the same true areal density.
7. PNG export uses a high-resolution Canvas. The filename includes `600dpi`, but the code does not write separate DPI metadata.

## 13. Recommended Workflow

1. Confirm that `data-analysis.csv` is in the same directory as the HTML file, or manually select the correct CSV.
2. Check that specimen types, batches, IDs, and thicknesses were recognized correctly.
3. Select the view appropriate to the comparison:
   - To inspect only the original test results, use “Raw.”
   - To compare thickness-corrected results, use “Standardized” and select an appropriate standardization method.
   - To inspect the overall material-type trend, use “Type mean.”
   - To compare only the initial linear response, use “Type mean: cropped.”
4. Select the standardization method appropriate to the material structure:
   - For an approximately solid rectangular section, prefer the reference second moment of area.
   - For a sandwich or face-dominated structure, use simplified D7249 face stress and verify the face-thickness settings for all three materials.
   - To compare efficiency per unit areal density, use areal-density-specific performance.
5. Adjust the yield-detection parameters and confirm that the yield-point markers agree with the curve shapes.
6. Verify the mean values in the material-type comparison table, then export the publication figure or CSV.
