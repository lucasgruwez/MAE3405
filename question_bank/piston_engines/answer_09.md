# Answer 09 — Infer fuel and air flow from rich exhaust composition

- Question: [question_09.md](question_09.md).
- Source: [Problem set Q7](../../problem_sets/MAE3405%20Problem%20Set%20Questions%20-%20Week%203-4.pdf#page=2), PDF page 2.

## Assumptions and basis

Assume all carbon and hydrogen enter with hydrocarbon fuel, all nitrogen enters with air, and no unlisted products, fuel oxygen, soot or condensation occur. Use air O₂ + 3.76N₂. For the historical hand calculation, round molecular weights from [aide-mémoire Table 1, p.1](../../MAE3405%20Aide%20Memoire.pdf#page=1) to integer kg/kmol and use atomic weights C = 12 and H = 1. Ideal-gas volume fractions equal mole fractions. Use one kmol of wet exhaust as the composition basis; nitrogen fraction is

$$x_{N_2}=1-0.0914-0.051-0.137-0.0231=0.6975.$$

## (i) Species mass flows

$$\overline M_e=0.0914(44)+0.051(28)+0.137(18)+0.0231(2)+0.6975(28)
=27.4918\ \mathrm{kg/kmol}.$$

Hence total molar flow is $\dot n_e=0.1/27.4918=0.00363745$ kmol/s, and $\dot m_i=\dot n_ex_iM_i$:

| Species | Mass flow (kg/s) |
|---|---:|
| CO₂ | 0.01462836 |
| CO | 0.00519428 |
| H₂O | 0.00896995 |
| H₂ | 0.00016805 |
| N₂ | 0.07103936 |
| **Total** | **0.10000000** |

## (ii) Fuel and air

Fuel consists of the carbon and hydrogen recovered in the products:

$$n_C=0.0914+0.051=0.1424\ \mathrm{kmol\ C/kmol\ exhaust},$$
$$n_H=2(0.137+0.0231)=0.3202\ \mathrm{kmol\ H/kmol\ exhaust}.$$
$$\dot m_f=\dot n_e[12(0.1424)+1(0.3202)]=0.00738038\ \mathrm{kg/s}.$$
$$\dot m_a=0.1-\dot m_f=0.09261962\ \mathrm{kg/s},\qquad
A/F=\frac{0.09261962}{0.00738038}=12.54943.$$

As an independent consistency check, the oxygen demand per kmol exhaust is

$$n_{O_2}=\frac{2(0.0914)+0.051+0.137}{2}=0.1854,$$

and $n_{N_2}/n_{O_2}=0.6975/0.1854=3.76214$, close to 3.76; the slight mismatch is consistent with rounded measurements. This is a rich mixture, so CO and H₂ are expected.

## (iii) Fuel molecule

For an alkane, the atomic H/C ratio is $(2n+2)/n=2+2/n$:

$$\frac HC=\frac{0.3202}{0.1424}=2.2485955,\qquad
n=\frac{2}{2.2485955-2}=8.04520.$$

**A plausible integer molecule is C₈H₁₈**, with $n\approx8.05$. The fractional value represents rounded measurements (or a fuel blend), not a literal fractional molecule.

The supplied answer gives A/F = 12.57 and $n=7.9$. The A/F difference is small; the displayed volume fractions give $n=8.045$, not 7.9. Both suggest octane, but the printed 7.9 is not reproduced by the stated atomic balance.

## Verification

Species flows sum to 0.1 kg/s; independent carbon/hydrogen and oxygen/nitrogen balances; inferred alkane H/C checked. Recomputed by [verify.py](verify.py).
