# Answer 06 — Air-standard Otto cycle from temperature limits

- Question: [question_06.md](question_06.md).
- Source: [Problem set Q4](../../problem_sets/MAE3405%20Problem%20Set%20Questions%20-%20Week%203-4.pdf#page=1), PDF page 1.

## Assumptions and state numbering

Use air properties from [aide-mémoire Table 1, p.1](../../MAE3405%20Aide%20Memoire.pdf#page=1) and SSL pressure from [Table 5, p.2](../../MAE3405%20Aide%20Memoire.pdf#page=2); no change to the three tasks. Assume constant specific heats and an ideal air-standard Otto cycle, with 1–2 and 3–4 isentropic and 2–3 and 4–1 constant volume. Let 1 be the cold BDC state and 3 the hot TDC state.

## (i) Compression ratio and efficiency

$$T_1=15+273.15=288.15\ \mathrm{K},\quad T_3=1400+273.15=1673.15\ \mathrm{K}.$$

Since $q_H=c_v(T_3-T_2)$,

$$T_2=1673.15-\frac{800}{0.718}=558.9439\ \mathrm{K}.$$

From isentropic compression, $T_2/T_1=r^{\gamma-1}$:

$$r=\left(\frac{558.9439}{288.15}\right)^{1/0.4}=5.24051.$$

Because both isentropic legs have the same air properties and volume ratio, $T_4/T_3=T_1/T_2$ and

$$\eta_{Otto}=1-\frac{c_v(T_4-T_1)}{c_v(T_3-T_2)}
=1-\frac{T_1}{T_2}=0.484474=48.45\%.$$

## (ii) Extreme pressure ratio

Maximum pressure is at state 3 and minimum at 1. The ideal-gas law and $v_1/v_3=r$ give

$$\frac{p_3}{p_1}=\frac{T_3}{T_1}\frac{v_1}{v_3}
=\frac{1673.15}{288.15}(5.24051)=30.4292.$$

Thus $p_3=30.4292(101.325)=3083.24$ kPa = 3.083 MPa. The pressure ratio itself does not depend on the assumed SSL pressure.

## (iii) Maximum theoretical efficiency

For any heat engine bounded by these extreme reservoir temperatures, the Carnot upper bound is

$$\eta_{\max}=1-\frac{T_{\min}}{T_{\max}}
=1-\frac{288.15}{1673.15}=0.827780=82.78\%.$$

This is a bound, not the efficiency of the original Otto processes. **Results: $r=5.24$; Otto efficiency 48.45%; pressure ratio 30.43; Carnot bound 82.78%.**

## Verification

Reconstructed all requested ratios from the ideal-gas law and constant-volume heat input; agrees with rounded published answers. Recomputed by [verify.py](verify.py).
