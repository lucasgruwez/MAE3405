# Answer 07 — Methanol stoichiometry and phase-dependent LHV

- Question: [question_07.md](question_07.md).
- Source: [Problem set Q5](../../problem_sets/MAE3405%20Problem%20Set%20Questions%20-%20Week%203-4.pdf#page=1), PDF page 1.

## Assumptions and adaptation

Formation data are available in [aide-mémoire Table 12, p.5](../../MAE3405%20Aide%20Memoire.pdf#page=5), matching the Topic 3 p.32 image table. For the historical hand calculation, use air O₂ + 3.76N₂, round the O₂/N₂ molecular weights in [Table 1, p.1](../../MAE3405%20Aide%20Memoire.pdf#page=1) to 32/28 kg/kmol, and take CH₃OH as 32 kg/kmol. Neither a supplemental formation table nor numerical integration is needed. Use one kmol fuel, complete stoichiometric combustion, inert nitrogen, and water vapour in the products.

## (i) Stoichiometric A/F

Balancing carbon, hydrogen and oxygen:

$$
\mathrm{CH_3OH}+1.5(\mathrm{O_2}+3.76\mathrm{N_2})
\longrightarrow\mathrm{CO_2}+2\mathrm{H_2O}+5.64\mathrm{N_2}.
$$

One oxygen atom is already present in methanol; ignoring it would overestimate the required air.

$$\frac AF=\frac{1.5(32)+5.64(28)}{32}
=\frac{205.92}{32}=6.435\ \mathrm{kg\ air/kg\ fuel}.$$

## (ii) Gaseous-fuel LHV

The product formation enthalpy per kmol fuel is

$$H_P^0=-393.52-2(241.83)=-877.18\ \mathrm{MJ/kmol\ fuel}.$$

Heat of combustion is $H_R^0-H_P^0$, positive for released heat:

$$\mathrm{LHV}_g=\frac{-201.17-(-877.18)}{32}
=21.1253125\ \mathrm{MJ/kg}=21125.3\ \mathrm{kJ/kg}.$$

## (iii) Liquid-fuel reduction

$$\mathrm{LHV}_l=\frac{-238.58-(-877.18)}{32}
=19.95625\ \mathrm{MJ/kg}=19956.3\ \mathrm{kJ/kg}.$$

The phase change costs $(238.58-201.17)/32=1.1690625$ MJ/kg. Hence

$$\text{reduction}=100\frac{21.1253125-19.95625}{21.1253125}=5.53394\%.$$

**Results: A/F = 6.435; gaseous LHV = 21125 kJ/kg; reduction = 5.53%.** These agree with the source to its precision (6.43, 21.12 MJ/kg, 5.54%). The sign is important: liquid fuel has *lower* LHV because energy is consumed in vaporisation.

## Verification

Atom balance, mass A/F and independent phase-specific formation-enthalpy sums; aide-mémoire p.5 image table visually checked against the lecture values. Recomputed by [verify.py](verify.py).
