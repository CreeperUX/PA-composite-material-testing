# Method B: Face-Stress Standardization

[English](method-b-face-stress-standardization.md) | [Chinese](../zh/method-b-face-stress-standardization.md)

## 1. Purpose

This method normalizes three-point flexural test results for specimens of different thicknesses. For the material tested here, the total specimen thickness is approximately `1.8-2.5 mm`, and each face consists of `4 carbon-fiber plies`. Directly comparing apparent flexural strengths calculated with the conventional three-point bending formula would make the results strongly dependent on differences in specimen thickness.

The central idea of Method B is therefore to convert the existing apparent flexural strength into the ultimate stress carried by the carbon-fiber faces. This makes strength comparisons between specimens of different thicknesses more representative of the load-bearing capacity of the face material itself.

## 2. Applicability

This method applies when:

- The specimen has clearly load-bearing carbon-fiber faces.
- The total specimen thickness, width, support span, and apparent flexural strength are known.
- The thickness of one carbon-fiber face is known or can be estimated.
- The primary failure mode is associated with tension, compression, or bending of the faces.

If failure is governed mainly by core shear, core crushing, or interface debonding, this method must be used with caution and the failure mode must be reported separately.

## 3. Input Parameters

| Symbol | Meaning | Unit |
|---|---|---|
| `sigma_app` | Existing apparent flexural strength, such as `sfM` or the maximum `Standardkraft` | MPa |
| `b` | Specimen width | mm |
| `d` | Total specimen thickness | mm |
| `S` | Support span for three-point bending | mm |
| `t` | Thickness of one carbon-fiber face | mm |
| `c` | Core thickness | mm |
| `P_max` | Peak load | N |
| `sigma_f,u` | Ultimate face stress | MPa |

## 4. Calculation Formulas

First, calculate the peak load from the existing apparent flexural strength:

$$
P_{\max}
=
\frac{2\sigma_{\mathrm{app}}bd^2}{3S}
$$

Here, `sigma_app` is expressed in `MPa`, or `N/mm²`, so the resulting `P_max` is expressed in `N`.

Then calculate the core thickness:

$$
c=d-2t
$$

Finally, calculate the ultimate face stress:

$$
\sigma_{f,u}
=
\frac{P_{\max}S}{2(d+c)bt}
$$

If `P_max` does not need to be reported explicitly, the formulas above can be combined as:

$$
\sigma_{f,u}
=
\frac{\sigma_{\mathrm{app}}d^2}
{3(d+c)t}
$$

where:

$$
c=d-2t
$$

## 5. Calculation Procedure

1. Read `sigma_app`, `b`, and `d` for each specimen from the existing data table.
2. Confirm the three-point-bending support span `S`.
3. Enter the thickness `t` of one carbon-fiber face.
4. Calculate the core thickness as `c = d - 2t`.
5. Calculate the ultimate face stress `sigma_f,u`.
6. Use `sigma_f,u` as the standardized strength metric for specimens of different thicknesses.

## 6. Recommended Output

The final results table should contain at least the following fields:

| Specimen ID | Type | d mm | b mm | sigma_app MPa | t mm | c mm | sigma_f,u MPa |
|---|---|---:|---:|---:|---:|---:|---:|
| Example | 3k | 2.26 | 17.71 | 356.73 | - | - | - |

## 7. Short Conclusion

For the current flexural specimens, which are `1.8-2.5 mm` thick and have `4 carbon-fiber plies` per face, Method B is more appropriate than a direct comparison of apparent flexural strength. It converts the geometric influence of thickness differences into face load-bearing stress and is therefore better suited to strength comparisons across specimen types or final formed thicknesses.
