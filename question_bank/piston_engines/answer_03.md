# Answer 03 — Fuel-air Otto BSFC and ideal propeller drag

- Question: [question_03.md](question_03.md).
- Source: [2015 examination, Q1](../../past_exams/MAE3405%202015%20S2.PDF#page=2), PDF page 2.

## Assumptions and chemistry ambiguity

The [official 2015 Q1 erratum](../../past_exams/MAE3405%202015%20S2%20Err.PDF#page=1), PDF page 1, corrects all three molecular weights to **kg/kmol**, not kmol/kg. Exam wording, numerical table values and marks are unchanged. Molecular weight alone does not uniquely specify a real Avgas blend. Approximate the 114 kg/kmol fuel as $\mathrm{C_8H_{18}}$ (Topic 3, pp. 23–28), with air $\mathrm{O_2+3.76N_2}$. Then $\phi=1$ implies

$$
\mathrm{C_8H_{18}}+12.5(\mathrm{O_2}+3.76\mathrm{N_2})
\longrightarrow8\mathrm{CO_2}+9\mathrm{H_2O}+47\mathrm{N_2},
$$
$$a=(A/F)_s=\frac{12.5(32)+47(28)}{114}=15.05263.$$

For historical comparison, retain the exam sheet's integer species masses (O₂ 32, N₂ 28 kg/kmol) consistently with the given fuel mass of 114; the historical rounded air molecular weight of 29 would instead give 15.136. The current [aide-mémoire Table 1, p.1](../../MAE3405%20Aide%20Memoire.pdf#page=1) carries more precise species masses; these are not silently mixed with the historical calculation. The lecture's empirical Avgas value, 14.7, is another defensible convention for a real blend, but is not identical to the octane approximation. No unique exact answer is possible without declaring the fuel chemistry convention.

The workings also retain historical atmosphere rounding, $\rho_a=1.006$ kg/m³, rather than 1.0065 in [aide-mémoire Table 5, p.2](../../MAE3405%20Aide%20Memoire.pdf#page=2). This affects power and drag slightly, not the modelling convention. Avgas LHV comes from [Table 2, p.1](../../MAE3405%20Aide%20Memoire.pdf#page=1); reference temperature and $R_u$ come from [reference data, p.6](../../MAE3405%20Aide%20Memoire.pdf#page=6).

Use ambient-air-referenced volumetric efficiency $\dot m_a=\rho_a\eta_v\dot V_s$ as in Topic 4, pp. 20–21. Ignore ram recovery, residual gases and naturally aspirated pumping loss. Include fuel in cycle mass. Assume an ideal, uniform actuator disc with no profile, swirl, hub or gearbox losses; thrust = aircraft drag.

Use states 1–2 for isentropic compression of reactants, 2–3 for constant-volume combustion, 3–4 for isentropic expansion of products, and 4–1 for the model's constant-volume heat rejection. On a $p$–$V$ sketch, 1 and 4 lie at maximum volume and 2 and 3 at minimum volume; the clockwise enclosed area is positive indicated work.

The supplied molecular weights give, in kJ/(kg K),

$$
R_R=\frac{8.314}{28.9}=0.287682,\quad
R_P=\frac{8.314}{28.0}=0.296929,
$$
$$
c_{v,R}=1.055-R_R=0.767318,\qquad
c_{v,P}=1.486-R_P=1.189071,
$$
$$
\gamma_R=\frac{1.055}{0.767318}=1.374918,\qquad
\gamma_P=\frac{1.486}{1.189071}=1.249715.
$$

For $a=A/F$, heat release per kg of total reactants is $q_{\rm rel}=\eta_c\mathrm{LHV}/(a+1)$. The unit's fuel-air model uses

$$
T_2=T_1r^{\gamma_R-1},\qquad
T_3=T_0+\frac{q_{\rm rel}+c_{v,R}(T_2-T_0)}{c_{v,P}},\qquad
T_4=\frac{T_3}{r^{\gamma_P-1}},
$$
$$
w_i=c_{v,P}(T_3-T_4)-c_{v,R}(T_2-T_1).
$$

Here $T_0=298$ K. Do **not** cancel the reference temperature across combustion: $c_{v,P}\ne c_{v,R}$. Do not substitute the air-standard Otto efficiency. This follows Topic 3, pp. 25–28, 37–39 and Topic 4, pp. 24–25: LHV is used as the unit's effective heat-release input, without adding a separate formation-energy or $\Delta nR_uT_0$ correction. A rigorous chemical internal-energy model would require a different, consistently specified reference model. Combustion efficiency is already in $T_3$ and must not be applied again to power. Thermal efficiency relative to fuel LHV is $w_i/[\mathrm{LHV}/(a+1)]$, not $w_i/q_{\rm rel}$ when $\eta_c<1$.

## (a) BSFC

For $T_1=275.15$ K, $r=8$, $a=15.05263$:

| Quantity | Value |
|---|---:|
| $q_{\rm rel}$ | 2450.066 kJ/kg reactants |
| $T_2$ | 600.004 K |
| $T_3$ | 2553.373 K |
| $T_4$ | 1519.146 K |
| Compression work input | 249.267 kJ/kg reactants |
| Expansion work output | 1229.770 kJ/kg reactants |
| $w_i$ | 980.503 kJ/kg reactants |

$$
\dot V_s=4\frac{\pi(0.1)^2}{4}(0.12)\frac{2500}{120}
=0.07853982\ \mathrm{m^3/s},
$$
$$
\dot m_a=1.006(0.80)\dot V_s=0.06320884\ \mathrm{kg/s},\qquad
\dot m_f=\frac{\dot m_a}{15.05263}=0.00419919\ \mathrm{kg/s}.
$$
$$
P_b=0.85(\dot m_a+\dot m_f)w_i=56.1797\ \mathrm{kW}.
$$
$$
\mathrm{BSFC}=\frac{3600\dot m_f}{P_b}
=0.269084\ \mathrm{kg/kWh}.
$$

The brake thermal efficiency is $0.85(0.360175)=0.306149$. Hence $3600/(0.306149\times43700)$ also gives the BSFC.

## (b) Drag and propulsive efficiency

With $V=150/3.6=41.6667$ m/s and $A=\pi(1.2)^2/4=1.130973$ m², momentum theory gives

$$T=2\rho A w(V+w),\qquad P_b=T(V+w).$$

Eliminating $T$:

$$
56179.7=2(1.006)(1.130973)w(41.6667+w)^2.
$$

A calculator trial or bisection between $w=9$ and $10$ m/s gives $w=9.44908$ m/s. Thus

$$
D=T=2(1.006)(1.130973)(9.44908)(51.11575)
=1099.07\ \mathrm{N},
$$
$$
\eta_p=\frac{TV}{P_b}=\frac{V}{V+w}=0.815143.
$$

**Results under the stated octane convention: 0.269 kg/kWh; drag 1.10 kN; ideal propulsive efficiency 81.5%.**

For comparison, recomputing the whole cycle and momentum balance under the other stated conventions gives:

| A/F convention | Volumetric-efficiency reference | $P_b$ (kW) | BSFC (kg/kWh) | Drag (N) | $\eta_p$ |
|---|---|---:|---:|---:|---:|
| Octane, 15.05263 (primary) | Ambient air | 56.1797 | 0.269084 | 1099.07 | 0.81514 |
| Empirical Avgas, 14.7 | Ambient air | 57.5427 | 0.269013 | 1122.08 | 0.81250 |
| Octane, 15.05263 | Total mixture | 52.5905 | 0.269084 | 1037.93 | 0.82233 |

For total-mixture volume, $\rho_R=79.4952/[(8.314/28.9)(275.15)]=1.004290$ kg/m³, $\dot m_R=\rho_R\eta_v\dot V_s$ and $\dot m_f=\dot m_R/(a+1)$. The same work per kg gives the same BSFC at fixed A/F, but lower power changes the actuator-disc solution. These ambiguities are model conventions, not corrections to the official wording.

## Verification

Stoichiometric atom/mass balance, BSFC identity and actuator-disc power balance; official erratum and question table visually checked. Recomputed by [verify.py](verify.py).
