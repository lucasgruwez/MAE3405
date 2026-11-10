# Answer 01 — Fuel-air Otto engine: drag and fuel flow

- Question: [question_01.md](question_01.md).
- Source: [2013 examination, Q1](../../past_exams/MAE3405%202013%20S2.PDF#page=2), PDF page 2.

## Assumptions and source typo

The printed `kmol/kg` units for the two molecular weights are reversed; interpret the numerical values as **28.9 and 28.0 kg/kmol**. The question deliberately preserves the original typo. The 2013 examination data sheet (PDF p.3) supplies the LHV, **45.0 MJ/kg**, not the current [aide-mémoire Table 2, p.1](../../MAE3405%20Aide%20Memoire.pdf#page=1) value of 43.7 MJ/kg. The workings retain the historical atmosphere density rounded to 1.006 kg/m³ at 2000 m; [Table 5, p.2](../../MAE3405%20Aide%20Memoire.pdf#page=2) gives 1.0065 kg/m³. This small rounding difference is not a separate atmosphere model. Use Avgas density from Table 2 and the knot conversion, reference temperature and $R_u$ from [aide-mémoire reference data, p.6](../../MAE3405%20Aide%20Memoire.pdf#page=6).

Neglect ram recovery, residual gases and pumping losses. Use the Topic 4, pp. 20–21 convention $\dot m_a=\rho_a\eta_v\dot V_s$ (volumetric efficiency referred to ambient air). Include fuel in the mass receiving cycle work. Treat the propeller as an ideal actuator disc, with downwash measured **at the disc**, not in the far wake; all brake power reaches it. Steady level flight gives thrust = drag.

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

## (a) Brake power and drag

For $T_1=275.15$ K, $r=7$, $a=14.7$:

| Quantity | Value |
|---|---:|
| $q_{\rm rel}$ | 2579.618 kJ/kg reactants |
| $T_2$ | 570.706 K |
| $T_3$ | 2643.418 K |
| $T_4$ | 1626.045 K |
| Compression work input | 226.785 kJ/kg reactants |
| Expansion work output | 1209.730 kJ/kg reactants |
| Net indicated work $w_i$ | 982.944 kJ/kg reactants |

For a four-stroke engine, each cylinder admits one charge per two revolutions:

$$
\dot V_s=6\frac{\pi(0.1)^2}{4}(0.12)\frac{2700}{120}
=0.1272345\ \mathrm{m^3/s}.
$$
$$
\dot m_a=1.006(0.80)(0.1272345)=0.1023983\ \mathrm{kg/s},
$$
$$
\dot m_f=\frac{0.1023983}{14.7}=0.00696587\ \mathrm{kg/s},\qquad
\dot m_R=0.1093642\ \mathrm{kg/s}.
$$
$$
P_b=0.85\dot m_Rw_i=91.3741\ \mathrm{kW}.
$$

From equal dynamic pressure, $V_E=V\sqrt{\rho/\rho_0}$:

$$
V=\frac{150(1.85)}{3.6}\sqrt{\frac{1.225}{1.006}}
=85.0608\ \mathrm{m/s},\qquad w=0.175V=14.8856\ \mathrm{m/s}.
$$

The disc adds power $P_b=T(V+w)$; thus

$$
D=T=\frac{91374.1}{1.175(85.0608)}=914.23\ \mathrm{N}.
$$

The corresponding ideal propulsive efficiency is $1/1.175=0.85106$.

## (b) Fuel volume flow

$$
\dot V_f=\frac{\dot m_f}{\rho_f}(3600)(1000)
=\frac{0.00696587}{708.2}(3.6\times10^6)
=35.4097\ \mathrm{L/h}.
$$

**Results: drag 0.914 kN; fuel consumption 35.4 L/h.**

Density and mass flow, not a separately tabulated volumetric heating value, are used for L/h. If instead $\eta_v$ is defined for total fuel-air mixture volume, the required density is $p/(R_RT)$ and all flow-dependent outputs are smaller by about 6.5%; that is a different convention, not a reason to drop fuel mass from cycle work.

## Verification

Cycle first-law identity and four-stroke flow calculation; year-specific LHV checked; question/table visually compared with the original page PNG. Recomputed by [verify.py](verify.py).
