# Answer 05 — Steady-flow energy balance and thermal efficiency

- Question: [question_05.md](question_05.md).
- Source: [Problem set Q2](../../problem_sets/MAE3405%20Problem%20Set%20Questions%20Week%201-2.pdf#page=1), PDF page 1.

## Interpretation and assumptions

“Combined” is taken literally: $\dot m_e=\dot m_a+\dot m_f=0.2$ kg/s and $\dot m_f=\dot m_a/15$. Thus

$$\dot m_a=0.1875\ \mathrm{kg/s},\qquad \dot m_f=0.0125\ \mathrm{kg/s}.$$

The question adaptation specifies atmospheric exhaust pressure (needed to obtain exit velocity), fuel at the reference temperature with negligible kinetic energy, and negligible potential energy. Retain the pipe-flow kinetic-energy terms. LHV represents the available chemical energy; do not add formation enthalpies again.

Use constant air, N₂, CO₂ and water-vapour properties from [aide-mémoire Table 1, p.1](../../MAE3405%20Aide%20Memoire.pdf#page=1) and SSL conditions from [Table 5, p.2](../../MAE3405%20Aide%20Memoire.pdf#page=2). The question's reference is 25°C (298.15 K), not the rounded general 298 K reference. Topic 1, PDF pp.9–11 and 49–52 covers flow energy and mixture properties.

## (i) Steady-flow first law

Mass-weight exhaust properties:

$$
c_{p,e}=0.65(1.0416)+0.15(0.8418)+0.20(1.8723)
=1.17777\ \mathrm{kJ/(kg\ K)},
$$
$$
R_e=0.65(0.29680)+0.15(0.18892)+0.20(0.46152)
=0.313562\ \mathrm{kJ/(kg\ K)}.
$$

Pipe velocities follow continuity, not the flight speed:

$$
\rho_e=\frac{101325}{313.562(1173.15)}=0.275448\ \mathrm{kg/m^3},
$$
$$
C_i=\frac{0.1875}{1.225[\pi(0.125)^2/4]}=12.4726\ \mathrm{m/s},
$$
$$
C_e=\frac{0.2}{0.275448[\pi(0.15)^2/4]}=41.0883\ \mathrm{m/s}.
$$

With shaft output positive and heat loss positive out,

$$
P_{\rm out}=\dot m_f\mathrm{LHV}-\dot Q_{\rm loss}
+\dot m_ah_i-\dot m_eh_e
+\frac{\dot m_aC_i^2-\dot m_eC_e^2}{2000},
$$

where the factor 2000 converts the kinetic terms from W to kW. With $h=c_p(T-T_0)$:

$$
\dot m_ah_i=0.1875(1.005)(288.15-298.15)=-1.884375\ \mathrm{kW},
$$
$$
\dot m_eh_e=0.2(1.17777)(1173.15-298.15)=206.10975\ \mathrm{kW}.
$$

The net kinetic-energy increase is 0.1542405 kW. Therefore

$$
P_{\rm out}=562.5-15-1.884375-206.10975-0.1542405
=339.3516\ \mathrm{kW}.
$$

## (ii) Thermal efficiency

$$\eta_{th}=\frac{339.3516}{0.0125(45000)}=0.603292=60.33\%.$$

**Results: 339.4 kW; 60.3%.**

The printed 376.7 kW / 62.8% is not consistent with the stated combined flow and these species properties. Taking 0.2 kg/s as *air only* would give a 600 kW fuel input, explaining the denominator behind the published percentage, but changes the mass specification and still does not yield the quoted power with a consistent exhaust balance. The supplied answer is therefore not adopted.

## Verification

Independent mixture properties, inlet/outlet continuity, separate air/fuel mass balance and complete first-law power balance. Recomputed by [verify.py](verify.py).
