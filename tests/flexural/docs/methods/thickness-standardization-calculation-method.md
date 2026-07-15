# Canonical Thickness-Standardization Calculation Method

## 1. Purpose

This document defines the only thickness-standardization method used by the project: sandwich face-stress standardization. It converts flexural-test specimens with different total and core thicknesses to a common face-stress basis, and optionally to the peak load of a reference geometry. The objective is to reduce geometric bias when material systems are compared.

The method follows four principles:

- Treat the specimen as a sandwich in which the upper and lower faces carry most of the normal bending stress.
- Use ultimate face stress `sigma_f,u` as the primary comparison metric.
- When a common specimen geometry is required, back-calculate the reference peak load `P_max,ref` from `sigma_f,u`.
- When measured face thickness is unavailable, use a material-specific estimate constrained by the actual lay-up and total specimen thickness. The current specimens have four fibre plies per face. Recommended defaults are `1x1 = 0.576 mm per face`, `2x2 = 0.568 mm per face`, and conventional `3K/Roving = 0.780 mm per face`.

## 2. Scope and required inputs

The method applies to symmetric sandwich structures with equal or nearly equal upper and lower face thicknesses. Ultimate face stress is an appropriate primary strength metric when failure is dominated by face tension or compression. When core shear, core crushing, or interface debonding dominates, face stress is only a supporting metric.

Required inputs:

| Parameter | Meaning | Unit |
|---|---|---|
| `b` | Specimen width | mm |
| `d` | Total specimen thickness | mm |
| `t` | Thickness of one face | mm |
| `c` | Core thickness, normally `c = d - 2t` | mm |
| `S` | Support span | mm |
| `L` | Four-point loading span; use `0` for three-point bending | mm |
| `P_max` | Peak load | N |
| `d_ref` | Reference total thickness | mm |
| `t_ref` | Reference thickness of one face | mm |
| `c_ref` | Reference core thickness, normally `d_ref - 2t_ref` | mm |
| `b_ref` | Reference specimen width | mm |
| `S_ref` | Reference support span | mm |
| `L_ref` | Reference four-point loading span; use `0` for three-point bending | mm |

If a dataset contains only `Thickness h [mm]` and an already calculated `Standardkraft [MPa]`, but not the original `P_max`, `b`, `S`, and `t`, the ultimate face stress cannot be calculated rigorously with this method.

## 3. Material properties and face-thickness estimates

The two reports in [`materials/fabric-reports`](../../../../materials/fabric-reports/) provide the material parameters used to estimate face thickness when direct measurements are unavailable.

### 3.1 Physical-value module

The naming convention is:

- `1x1`: Plain / Leinwand fabric.
- `2x2`: Twill / Köper fabric.
- `3K`: conventional 3K carbon-fibre fabric unless stated otherwise.

**Values from the material reports**

| Source | Fabric | Fibre areal weight (FAW) | Total areal weight | Resin/powder weight | Fibre density | Fibre |
|---|---|---:|---:|---:|---:|---|
| [`ECC07230189 Gewebeanalyse Entwicklung Twill.pdf`](<../../../../materials/fabric-reports/ECC07230189 Gewebeanalyse Entwicklung Twill.pdf>) | Twill / Köper | `131.8 g/m²` | `140.1 g/m²` | `8.3 g/m²` | `1.78 g/cm³` | Tenax-E IMS65 24K E23 |
| [`ECC07230190 Gewebeanalyse Entwicklung Playnwoven.pdf`](<../../../../materials/fabric-reports/ECC07230190 Gewebeanalyse Entwicklung Playnwoven.pdf>) | Plain / Leinwand | `134.0 g/m²` | `142.3 g/m²` | `8.3 g/m²` | `1.78 g/cm³` | Tenax-E IMS65 24K E23 |

**Default calculation inputs**

| Parameter | Default | Basis |
|---|---:|---|
| `FAW` | `132.9 g/m²` | Mean fibre areal weight of Twill and Plain |
| `rho_f` | `1.78 g/cm³` | Carbon-fibre density reported by the supplier |
| `V_f` | `0.55` | Engineering estimate for the cured fibre volume fraction; use sensitivity analysis |
| `W_r` | `8.3 g/m²` | Reported resin-powder/coating weight |
| `rho_r` | `1.15 g/cm³` | Engineering estimate for epoxy density |
| Plies per face | `4` | Current sandwich lay-up |

**Derived thicknesses**

| Derived quantity | Value | Use |
|---|---:|---|
| Fibre-equivalent ply thickness `t_ply,fiber` | `0.136 mm` | Fibre-volume contribution only |
| Resin/powder-equivalent ply thickness `t_ply,resin` | `0.007 mm` | Converts the reported powder weight to thickness |
| Cured equivalent ply thickness `t_ply` | `0.143 mm` | Fibre and powder contributions combined |
| Four-ply face thickness `t` | `0.572 mm per face` | Mean default for `1x1` and `2x2` |
| Four-ply face thickness without powder | `0.544 mm per face` | Conservative sensitivity input |

Recommended values when direct measurements are unavailable are `1x1 = 0.576 mm per face` and `2x2 = 0.568 mm per face`. A common Plain/Twill input may use their mean, `0.572 mm per face`. A conservative calculation that excludes the powder/coating contribution may use `0.544 mm per face`. The conventional 3K default is defined separately below.

### 3.2 Material-specific records

The areal weights, powder weights, and fibre densities for `1x1` and `2x2` come directly from the material reports. No batch-specific supplier report is currently available for `3K/Roving`; consequently, conventional 3K 200 gsm references are combined with the measured total-thickness constraint. Replace this estimate when batch-specific supplier data, lay-up measurements, or micrographs become available.

**External 3K references**

| Source | Published value | Use in this project |
|---|---|---|
| [Easy Composites 200g 2x2 Twill 3K](https://www.easycomposites.us/200g-black-stuff-22-twill-3k-carbon-fiber-cloth) | Approximately `0.25 mm` per ply under 1 bar vacuum compaction | Dry-fabric/compaction reference only |
| [CA Composites 3K 200GSM Carbon Fiber Cloth](https://cacomposites.com/product/3k-carbon-fiber-cloth/) | `203 g/m²`, thickness `0.26 mm`, reference `0.25 ± 0.02 mm`, fibre density `1.78 g/cm³` | Reference for the 3K areal-weight class |
| [Fibre Glast 3K 2x2 Twill Product Data Sheet](https://s3.amazonaws.com/cdn.fibreglast.com/downloads/00310-B.pdf) | `5.7 oz/yd²` (about `200 gsm`) and `.012 in` (about `0.305 mm`) | Upper reference for dry-fabric thickness |

| Code | Material | Fabric/tow description | Source | FAW | Total areal weight | Resin/powder | Fibre density | Fibre/grade | Status |
|---|---|---|---|---:|---:|---:|---:|---|---|
| `1x1` | Plain / Leinwand | Plain fabric | [`ECC07230190...Playnwoven.pdf`](<../../../../materials/fabric-reports/ECC07230190 Gewebeanalyse Entwicklung Playnwoven.pdf>) | `134.0 g/m²` | `142.3 g/m²` | `8.3 g/m²` | `1.78 g/cm³` | Tenax-E IMS65 24K E23 | Reported |
| `2x2` | Twill / Köper | Twill fabric | [`ECC07230189...Twill.pdf`](<../../../../materials/fabric-reports/ECC07230189 Gewebeanalyse Entwicklung Twill.pdf>) | `131.8 g/m²` | `140.1 g/m²` | `8.3 g/m²` | `1.78 g/cm³` | Tenax-E IMS65 24K E23 | Reported |
| `3K` | Conventional carbon fabric / Roving | Non-tape 3K fabric | Public supplier data | `200-210 g/m²` | About `200-210 g/m²` dry | No powder included | `1.78 g/cm³` | Supplier-dependent 3K fibre | Typical published value |

The current thickness parameters for four plies per face are:

| Code | Thickness basis | Ply thickness `t_ply` | Recommended `t` | Sensitivity range |
|---|---|---:|---:|---:|
| `1x1` | Reported FAW, `V_f = 0.55`, and powder contribution | `0.144 mm` | `0.576 mm per face` | `0.548-0.576 mm per face` |
| `2x2` | Reported FAW, `V_f = 0.55`, and powder contribution | `0.142 mm` | `0.568 mm per face` | `0.538-0.568 mm per face` |
| `3K` | Conventional 3K 200 gsm reference constrained by measured total thickness | `0.195 mm` | `0.780 mm per face` | `0.72-0.82 mm per face` |

The conventional 3K value must not be calculated as the supplier dry-fabric thickness `0.26 mm × 4 = 1.04 mm per face`, because both faces would then approach or exceed the measured total specimen thickness.

The physical interpretation is:

- Cured thickness is driven primarily by `FAW`, `rho_f`, and `V_f`. Similar areal weights and volume fractions naturally produce similar thicknesses.
- Plain and Twill FAW values differ by only about `1.7%`, so their estimated four-ply face thicknesses differ by only about `0.008 mm`.
- Conventional non-tape 3K 200 gsm fabric has a higher areal weight than the approximately 130 gsm spread-tow Plain and Twill materials, so its cured face should be thicker, but not as thick as four unconstrained dry plies.
- Plain/Twill face estimates and measured total thickness imply a core thickness of about `0.72 mm`. Constraining the Roving median total thickness to about `2.28 mm` gives `t_3K ≈ (2.28 - 0.72) / 2 = 0.78 mm per face`.
- Plain is not necessarily thinner than Twill. The reported Plain FAW is slightly higher, so it is slightly thicker at equal `V_f`; the difference remains smaller than the present estimation uncertainty.

| 3K basis | Ply thickness or method | Four-ply face thickness |
|---|---:|---:|
| Areal-weight method with `FAW ≈ 190-200 g/m²` and compacted `V_f ≈ 0.58-0.60` | `0.18-0.20 mm` | `0.72-0.80 mm per face` |
| Current total-thickness constraint with Plain/Twill-derived core `c ≈ 0.72 mm` | `(d_3K-c)/2` | `0.78 mm per face` |
| Supplier dry-fabric/1 bar compacted thickness | `0.25-0.305 mm` | `1.00-1.22 mm per face`; upper reference only |

### 3.3 Face-thickness calculation

The mean ply fibre areal weight is:

$$
FAW_{\mathrm{avg}}=\frac{131.8+134.0}{2}=132.9\ \mathrm{g/m^2}
$$

For a known or assumed cured fibre volume fraction `V_f`, the cured equivalent ply thickness is estimated as:

$$
t_{\mathrm{ply}}
=
\frac{FAW}{\rho_f \times 1000 \times V_f}
+
\frac{W_r}{\rho_r \times 1000}
$$

Here `FAW` and `W_r` are in `g/m²`, `rho_f` and `rho_r` are in `g/cm³`, and the result is in `mm`.

With the default values:

$$
t_{\mathrm{ply,fiber}}
=
\frac{132.9}{1.78\times1000\times0.55}
=0.136\ \mathrm{mm}
$$

$$
t_{\mathrm{ply,resin}}
=
\frac{8.3}{1.15\times1000}
=0.007\ \mathrm{mm}
$$

$$
t_{\mathrm{ply}}\approx0.143\ \mathrm{mm}
$$

For four plies per face:

$$
t=4t_{\mathrm{ply}}\approx0.572\ \mathrm{mm}
$$

This is an equivalent cured thickness derived from areal weight, density, and volume fraction; it is not the free thickness of dry fabric. Formal reporting should include sensitivity checks over `V_f = 0.50-0.60` and `t ± 5-10%`.

## 4. Sandwich face-stress standardization

### 4.1 Core thickness

For known total thickness `d` and face thickness `t`:

$$
c=d-2t
$$

Use measured `t` whenever possible. Otherwise use the material-specific estimates above and replace them when micrograph or lay-up measurements become available.

### 4.2 Ultimate face stress

For a symmetric sandwich under four-point bending:

$$
\sigma_{f,u}
=
\frac{P_{\max}(S-L)}{2(d+c)bt}
$$

For three-point bending, `L = 0`:

$$
\sigma_{f,u}
=
\frac{P_{\max}S}{2(d+c)bt}
$$

The result is in `MPa`, because `N/mm² = MPa`.

### 4.3 Reference-geometry peak load

After calculating face stress, the peak load for a reference geometry is:

$$
P_{\max,\mathrm{ref}}
=
\frac{2\sigma_{f,u}(d_{\mathrm{ref}}+c_{\mathrm{ref}})b_{\mathrm{ref}}t_{\mathrm{ref}}}{S_{\mathrm{ref}}-L_{\mathrm{ref}}}
$$

For three-point bending:

$$
P_{\max,\mathrm{ref}}
=
\frac{2\sigma_{f,u}(d_{\mathrm{ref}}+c_{\mathrm{ref}})b_{\mathrm{ref}}t_{\mathrm{ref}}}{S_{\mathrm{ref}}}
$$

### 4.4 Reference-geometry apparent strength

For compatibility with existing apparent-strength plots:

$$
\sigma_{\mathrm{app,ref}}
=
\frac{3P_{\max,\mathrm{ref}}S_{\mathrm{ref}}}{2b_{\mathrm{ref}}d_{\mathrm{ref}}^2}
$$

This is a presentation quantity derived from the reference load. It must not replace ultimate face stress as the primary material metric.

## 5. Recommended workflow

1. Record `b`, `d`, `S`, `L`, `P_max`, and material type for every specimen.
2. Use measured `t` when available; otherwise use `1x1 = 0.576`, `2x2 = 0.568`, or `3K/Roving = 0.780 mm per face`.
3. Calculate `c = d - 2t` and verify `c > 0`.
4. Calculate `sigma_f,u` with the equation in Section 4.2.
5. Define `d_ref`, `t_ref`, `c_ref`, `b_ref`, `S_ref`, and `L_ref`.
6. Calculate `P_max,ref` with the equation in Section 4.3.
7. Calculate `sigma_app,ref` only when a common plotting metric is required; always retain `sigma_f,u` in the report.
8. Calculate the mean, standard deviation, standard error, or 95% confidence interval by material type and plot comparisons before and after standardization.

## 6. Output templates

Recommended specimen-level output:

| Specimen ID | Type | `b` mm | `d` mm | `t` mm | `c` mm | `S` mm | `L` mm | `P_max` N | `sigma_f,u` MPa | `P_max,ref` N | `sigma_app,ref` MPa | Notes |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Example | 3K | 25.0 | 12.0 | 1.0 | 10.0 | 240.0 | 0.0 | 1925 | 420 | 1950 | - | Face-dominated failure |

Recommended group output:

| Type | Sample count | Mean thickness mm | Mean face thickness mm | Mean `sigma_f,u` MPa | SD MPa | SEM MPa | 95% CI MPa |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1x1 | - | - | - | - | - | - | - |
| 2x2 | - | - | - | - | - | - | - |
| 3K | - | - | - | - | - | - | - |

## 7. Worked example

Given:

| Parameter | Value |
|---|---:|
| `b` | 25 mm |
| `d` | 12 mm |
| `t` | 1 mm |
| `c` | 10 mm |
| `S` | 240 mm |
| `L` | 0 mm |
| `P_max` | 1925 N |

The ultimate face stress is:

$$
\sigma_{f,u}
=
\frac{1925\times240}{2(12+10)\times25\times1}
=420\ \mathrm{MPa}
$$

For `d_ref = 14 mm`, `c_ref = 12 mm`, `t_ref = 1 mm`, `b_ref = 25 mm`, and `S_ref = 280 mm`:

$$
P_{\max,\mathrm{ref}}
=
\frac{2\times420\times(14+12)\times25\times1}{280}
=1950\ \mathrm{N}
$$

Under the assumption of unchanged ultimate face stress, the specimen therefore corresponds to a reference-geometry peak load of approximately `1950 N`.
