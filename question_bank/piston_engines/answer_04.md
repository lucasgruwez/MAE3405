# Answer 04 — Mars atmospheric mixture

- Question: [question_04.md](question_04.md).
- Source: [Problem set Q1](../../problem_sets/MAE3405%20Problem%20Set%20Questions%20Week%201-2.pdf#page=1), PDF page 1.

## Adaptation and assumptions

Use the Mars composition in [aide-mémoire Table 8, p.4](../../MAE3405%20Aide%20Memoire.pdf#page=4), with volume fractions interpreted as mole fractions as directed by the source question. Select CO₂, N₂, Ar, O₂, CO and H₂O; water's 210 ppm is 0.000210. Neglect NO, Ne, HDO, Kr and Xe and normalise the selected fractions. This is an explicit species truncation, not a replacement composition. Use constant $c_p$ and molecular weights from [Table 1, p.1](../../MAE3405%20Aide%20Memoire.pdf#page=1), including CO $c_p=1.0357$ kJ/(kg K); retain source-given Ar $c_p=0.523$ kJ/(kg K) and molecular weight 39.95 kg/kmol because Table 1 omits Ar. Treat the mixture as ideal gases. Use $R_u$ from [aide-mémoire reference data, p.6](../../MAE3405%20Aide%20Memoire.pdf#page=6); Topic 1, PDF pp.49–52 covers mixture weighting.

The listed fractions sum to $S=0.99851$. Set $x_i=x_{i,\rm listed}/S$. On a one-kmol mixture basis,

$$\overline M=\sum_i x_iM_i=43.47846\ \mathrm{kg/kmol}.$$

Mass fractions are $Y_i=x_iM_i/\overline M$:

| Species | $Y_i$ |
|---|---:|
| CO₂ | 0.96629295 |
| N₂ | 0.01742195 |
| Ar | 0.01472347 |
| O₂ | 0.00095852 |
| CO | 0.00051597 |
| H₂O | 0.00008714 |

$$
R=\frac{R_u}{\overline M}=\frac{8.314}{43.47846}
=0.1912211\ \mathrm{kJ/(kg\ K)}.
$$
$$
c_p=\sum_iY_ic_{p,i}=0.8408534\ \mathrm{kJ/(kg\ K)},\qquad
c_v=c_p-R=0.6496323\ \mathrm{kJ/(kg\ K)},
$$
$$\gamma=\frac{c_p}{c_v}=1.294353.$$

**Results: 43.48 kg/kmol; 0.1912 kJ/(kg K); 1.294.** Do not mole-weight mass-specific $c_p$, or average species $\gamma$ directly; the mixture ratio is formed from the mixture heat capacities.

The source gives 43.41 kg/kmol, 0.1915 kJ/(kg K) and 1.29. The latter agrees to two decimals; the small differences in the first two remain with the explicit Table 8 selection, normalisation and current Table 1 molecular weights. Do not force agreement by treating an incomplete list as summing to one or replacing the computed mixture properties with Table 7's planetary averages.

## Verification

Table 8 species selection and ppm conversion, Table 1 molecular weights/CO heat capacity, mole-fraction normalisation, mass fractions summing to one, and $c_p-c_v=R$ evaluated. Recomputed by [verify.py](verify.py).
