# Four-point flexural-test pre-test record

## 1. Basis and scope

This form was reconstructed from the 12 three-point flexural-test PDF reports in [`test-results/`](../test-results/). It is intended for laboratory setup before testing newly manufactured specimens with the same nominal dimensions, materials, and layups.

Values shared by all historical reports are prefilled as defaults. The required four-point fixture geometry has four contact points with a `20 mm` centre-to-centre distance between each adjacent pair. Actual fixture dimensions, calibration status, and machine settings take precedence and must be recorded when they differ from the defaults.

Historical specimen dimensions and mechanical results are not reused here. Every new specimen must be measured before testing.

## 2. Four-point fixture geometry

```text
Left support       Left loading       Right loading       Right support
     o------------------o------------------o------------------o
             20 mm              20 mm              20 mm

Outer span S = 60 mm; inner span L = 20 mm; L/S = 1/3
```

| Parameter | Symbol | Prefilled value | Unit | Laboratory check or measured value |
|---|---|---:|---:|---|
| Left support to left loading roller | - | 20.00 | mm |  |
| Loading-roller spacing, inner span | `L` | 20.00 | mm |  |
| Right loading roller to right support | - | 20.00 | mm |  |
| Support-roller spacing, outer span | `S` | 60.00 | mm |  |
| Span ratio | `L/S` | 1/3 | - |  |
| Loading-roller radius | - | 2.25* | mm |  |
| Support-roller radius | - | 2.25* | mm |  |
| Four-point fixture model or ID | - |  | - |  |
| Crosshead speed | - | 2.50 | mm/min |  |

`*` The radius comes from the historical three-point fixture. Enter the actual value if the four-point fixture differs.

### 2.1 Crosshead-speed conversion

All 12 historical reports record a three-point support span `S3 = 40 mm` and crosshead speed `v3 = 1.00 mm/min`. To retain the same nominal outer-fibre strain rate with the specified symmetric four-point geometry:

$$
\dot{\varepsilon}_3 = \frac{6 h v_3}{S_3^2}
$$

$$
\dot{\varepsilon}_4 = \frac{6 h v_4}{(S_4-L_4)(S_4+2L_4)}
$$

For equal strain rates and equal nominal specimen thickness,

$$
v_4 = v_3\frac{(S_4-L_4)(S_4+2L_4)}{S_3^2}
= 1.00\frac{(60-20)(60+40)}{40^2}
= 2.50\ \text{mm/min}
$$

Recalculate the speed if displacement control, fixture geometry, or the target strain rate differs from these assumptions.

## 3. Method preset from the historical reports

| Item | Historical setting | Entry or confirmation before four-point testing |
|---|---|---|
| Test standard | Based on DIN EN ISO 14125 | Record the actual standard, edition, and deviations |
| Material | CF | Enter `3k`, `1x1`, or `2x2` |
| Climate | Standard atmosphere, DIN EN ISO 139 | Record temperature, relative humidity, and conditioning duration |
| Specimen state | Conditioned | Confirm conditioning of the new batch |
| Test machine | 1455 | Record actual machine model and asset ID |
| Load cell | 20 kN, S/N 794031 | Record range, serial number, and calibration validity |
| Accuracy class | See current calibration certificate | Record certificate number and expiry date |
| Historical fixture | ITA 9, large bending fixture | Replace with the actual four-point fixture ID |
| Fixture padding | None | Confirm actual configuration |
| Initial tool distance | 3.00 mm | Enter the actual four-point starting position |
| Crosshead speed | 1 mm/min for historical three-point tests | Use `2.50 mm/min` or document a recalculated value |
| Pre-travel | None | Record actual setting |
| Preload | 10 N | Confirm value and post-preload zeroing procedure |
| Test program | Method A | Record the machine method name |
| Force stop threshold | 30% of `Fmax` | Confirm applicability or record an alternative |
| Modulus method | Secant | Confirm if modulus will be reported |
| Modulus start | 0.05% | Record actual setting if applicable |
| Modulus end | 0.25% | Record actual setting if applicable |
| Compression face | Marked face upward | Mark and confirm every specimen |
| Test direction | Unknown in historical reports | Record direction relative to the main fibre or weave direction |

The historical three-point support span of `40 mm` is not used for the new four-point setup. Use `S = 60 mm` and `L = 20 mm` unless the actual measured geometry is documented otherwise.

### 3.1 Relevant observations from the reports

| Historical observation | Required handling for the new test |
|---|---|
| Parameters and support span were agreed with the client | Record the specified four-point geometry and any deviations from ISO 14125 |
| The historical fixture was client-made and results were not fully standardized | Record fixture ID, roller radii, alignment, and deviations before testing |
| All 36 historical specimens were reported as failing under compression stress | Inspect the marked upper face and the constant-moment region between the loading rollers |

## 4. Specimen plan

The historical reports cover `3k`, `1x1`, and `2x2`. Each report contains three specimens across four batches, giving 12 historical specimens per material.

| Material code | Historical batches | Suggested specimens per batch | Planned total | Prepared total | Notes |
|---|---|---:|---:|---:|---|
| `3k` | `01_21`, `01_22`, `01_23_H`, `01_24_H` | 3 | 12 |  |  |
| `1x1` | `01_21`, `01_22`, `01_23_H`, `01_24_H` | 3 | 12 |  |  |
| `2x2` | `01_21`, `01_22`, `01_23_H`, `01_24_H` | 3 | 12 |  |  |

## 5. New-specimen measurements

Complete this table before loading. Measure width and total thickness at three positions and calculate the average. Do not substitute historical dimensions.

| Specimen ID | Material | Batch | Length mm | Width 1 mm | Width 2 mm | Width 3 mm | Mean width `b` mm | Thickness 1 mm | Thickness 2 mm | Thickness 3 mm | Mean thickness `h` mm | Mass g | Marked face up | Fibre or weave direction | Visual inspection and testability |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

If sandwich or face-stress analysis is required, add the following measurements:

| Specimen ID | Upper face `t1` mm | Lower face `t2` mm | Core `c` mm | Measurement method or cross-section image ID |
|---|---:|---:|---:|---|
|  |  |  |  |  |

## 6. Final pre-test checklist

- [ ] The centre-to-centre spacing between each adjacent pair of contact points is `20 mm`, or the measured deviation is recorded.
- [ ] The outer span is recorded as `S = 60 mm` and the inner span as `L = 20 mm`.
- [ ] Roller radii, fixture ID, and alignment have been verified.
- [ ] Conditioning and actual laboratory climate have been recorded.
- [ ] Load-cell range, serial number, and calibration validity have been recorded.
- [ ] Crosshead speed is `2.50 mm/min`, or a revised calculation is documented.
- [ ] Preload is `10 N`, and the force and displacement zeroing procedure has been confirmed.
- [ ] The stop threshold is `30% Fmax`, or an approved alternative has been recorded.
- [ ] Width, thickness, orientation, and visual condition are recorded for every specimen.
- [ ] Data-acquisition channels, sample rate, filename convention, and storage path have been confirmed.
- [ ] Deviations from the standard or historical method are listed below.

## 7. Approval and deviations

| Item | Entry |
|---|---|
| Test date |  |
| Operator |  |
| Reviewer |  |
| Machine asset ID |  |
| Fixture ID |  |
| Method file or version |  |
| Data-storage location |  |
| Deviations and approvals |  |
