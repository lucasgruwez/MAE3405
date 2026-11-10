# Answer 02 — Supercharged and intercooled fuel-air Otto engine

- Question: [question_02.md](question_02.md).
- Source: [2014 examination, Q1](../../past_exams/MAE3405%202014%20S2.PDF#page=2), PDF page 2.

## Assumptions

Use ambient static conditions at the compressor inlet, no intercooler pressure loss, no temperature change on fuel addition, and exhaust pumping pressure equal to ambient. The question explicitly says **mixture** fills the swept volume: use mixture density, not air density, and split the resulting mass flow by A/F. Supercharger compresses air only. Use the Topic 5, pp. 6–10 pumping-loop model. The 2014 erratum concerns shock relations on page 7 and does not change Q1. Air and fuel properties match the [aide-mémoire Tables 1–2, p.1](../../MAE3405%20Aide%20Memoire.pdf#page=1). The workings retain historical pressure rounding to 54.0199 kPa from [Table 5, p.2](../../MAE3405%20Aide%20Memoire.pdf#page=2); the extra table digits do not materially change the answer. The reference temperature and $R_u$ come from [aide-mémoire reference data, p.6](../../MAE3405%20Aide%20Memoire.pdf#page=6). The question omits the original table's “Air: see gas properties table below” lookup direction; engine data and marks are unchanged.

## Supercharger and charge conditions

With ambient $T_a=255.65$ K, $p_a=54.0199$ kPa,

$$
T_c=T_a+\frac{T_a(1.5^{(1.4-1)/1.4}-1)}{0.80}
=294.9000\ \mathrm{K}.
$$
$$
T_1=T_a+0.5(T_c-T_a)=275.2750\ \mathrm{K},\qquad
p_1=1.5p_a=81.02985\ \mathrm{kPa}.
$$

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

## (a) Cycle power, pumping power and drive load

At $T_1=275.2750$ K, $r=7.5$, $a=14.7$ and LHV = 43700 kJ/kg:

| Quantity | Value |
|---|---:|
| $q_{\rm rel}$ | 2644.268 kJ/kg reactants |
| $T_2$ | 585.927 K |
| $T_3$ | 2707.610 K |
| $T_4$ | 1637.082 K |
| Compression work input | 238.369 kJ/kg reactants |
| Expansion work output | 1272.934 kJ/kg reactants |
| $w_i$ | 1034.566 kJ/kg reactants |

$$
\dot V_s=6\frac{\pi(0.1)^2}{4}(0.12)\frac{2500}{120}
=0.1178097\ \mathrm{m^3/s}.
$$
$$
\rho_R=\frac{81.02985}{(8.314/28.9)(275.2750)}=1.023213\ \mathrm{kg/m^3},
$$
$$
\dot m_R=\rho_R\dot V_s=0.1205444\ \mathrm{kg/s},\quad
\dot m_f=\frac{\dot m_R}{15.7}=0.00767799\ \mathrm{kg/s},\quad
\dot m_a=0.1128665\ \mathrm{kg/s}.
$$

Power-loop brake contribution:

$$P_{b,\mathrm{power}}=0.88\dot m_Rw_i=109.7458\ \mathrm{kW}.$$

During intake the charge acts at $p_1$, whereas exhaust is expelled at $p_a$. The rectangular pumping-loop indicated work is $(p_1-p_a)V_s$, positive here:

$$P_{b,\mathrm{pump}}=0.88(p_1-p_a)\dot V_s=2.80019\ \mathrm{kW}.$$

The compressor consumes $\dot m_ac_{p,a}(T_c-T_a)$, and its drive has mechanical efficiency 0.85:

$$P_{sc}=\frac{0.1128665(1.005)(294.9000-255.65)}{0.85}=5.23784\ \mathrm{kW}.$$

Therefore the **net shaft output** is

$$P_b=109.7458+2.80019-5.23784=107.3081\ \mathrm{kW}.$$

Subtract the drive load **after** engine mechanical efficiency, rather than applying the engine loss to it again. Omitting the positive pumping loop gives 104.508 kW, but does not follow the Topic 5 model.

## (b) Fuel consumption

$$
\dot V_f=\frac{0.00767799}{708.2}(3.6\times10^6)=39.0296\ \mathrm{L/h}.
$$

**Results: 107.3 kW net brake output; 39.0 L/h.**

## Verification

Mixture mass split, cycle work, compressor load and positive pumping loop independently evaluated; table and marks visually checked against the page PNG. Recomputed by [verify.py](verify.py).
