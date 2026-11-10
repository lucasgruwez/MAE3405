# Answer 14 — Supercharger power and intercooled density boost

- Question: [question_14.md](question_14.md).
- Source: [Problem set Q12](../../problem_sets/MAE3405%20Problem%20Set%20Questions%20Week%205-6.pdf#page=1), PDF page 1.

## Assumptions and adaptation

Boost is explicitly a **pressure ratio of 1.3**, not 1.3 bar gauge. Use ambient static air at the inlet and no intercooler pressure loss or ram recovery. Air and atmosphere properties come from [aide-mémoire Table 1, p.1](../../MAE3405%20Aide%20Memoire.pdf#page=1) and [Table 5, p.2](../../MAE3405%20Aide%20Memoire.pdf#page=2); no subparts change.

## (i) Supercharger drive power

For ideal isentropic compression to the delivery pressure,

$$T_{c,s}=T_a(1.3)^{(\gamma-1)/\gamma}.$$

Actual temperature rise follows compressor isentropic efficiency:

$$\Delta T_c=\frac{T_a[1.3^{(1.4-1)/1.4}-1]}{0.80}
=26.77290\ \mathrm{K},\qquad T_c=301.92290\ \mathrm{K}.$$

The shaft input includes mechanical-drive losses:

$$P_{sc}=\frac{\dot m_ac_p\Delta T_c}{\eta_{m,sc}}
=\frac{0.1(1.005)(26.77290)}{0.90}=2.98964\ \mathrm{kW}.$$

## (ii) Intercooled density increase

Reducing the rise by 50% gives

$$T_i=T_a+0.5\Delta T_c=288.53645\ \mathrm{K}.$$

Using $\rho=p/(RT)$ at both stations (same gas),

$$\frac{\rho_i}{\rho_a}=\frac{p_i}{p_a}\frac{T_a}{T_i}
=1.3\frac{275.15}{288.53645}=1.239687.$$

Thus the charge density is about $1.2471$ kg/m³ using the historical ambient density rounded to 1.006 kg/m³ rather than Table 5's 1.0065, and the increase is

$$100\left(\frac{\rho_i}{\rho_a}-1\right)=23.9687\%.$$

**Results: 2.99 kW drive input; 24.0% density increase.** This matches the source. Intercooling does not reduce the already-incurred compressor work for a fixed inlet condition, pressure ratio and mass flow; it changes downstream density.

## Verification

Isentropic/actual temperature rise, mechanical shaft loss and ideal-gas density ratio independently evaluated; agrees with printed 3.0 kW / 24%. Recomputed by [verify.py](verify.py).
