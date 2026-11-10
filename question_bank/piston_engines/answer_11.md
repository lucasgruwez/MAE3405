# Answer 11 — IMEP, brake power and fuel efficiency

- Question: [question_11.md](question_11.md).
- Source: [Problem set Q9](../../problem_sets/MAE3405%20Problem%20Set%20Questions%20-%20Week%203-4.pdf#page=2), PDF page 2.

## Assumptions and adaptation

The original table and two requested outputs remain. Use 3000 m density from [aide-mémoire Table 5, p.2](../../MAE3405%20Aide%20Memoire.pdf#page=2). The liquid-isooctane LHV used here, 44.425 MJ/kg, is a reference lookup from Topic 3, PDF p.36; the n-octane entry in [Table 11, p.5](../../MAE3405%20Aide%20Memoire.pdf#page=5) is a different fuel dataset. Define volumetric efficiency relative to ambient air and neglect ram-pressure recovery, intake heating and additional pumping corrections. IMEP is already net indicated cycle work per swept volume; do not run an additional Otto-cycle calculation or apply a separate combustion efficiency. Airspeed is not used when ram recovery is neglected (the usual intake assumption in Topic 4 p.18).

The total swept volume and four-stroke swept-volume rate are

$$V_s=4\frac{\pi(0.1)^2}{4}(0.12)=0.003769911\ \mathrm{m^3},$$
$$\dot V_s=0.003769911\frac{2500}{120}=0.07853982\ \mathrm{m^3/s}.$$

Indicated and brake power:

$$P_i=\mathrm{IMEP}\dot V_s=1000(0.07853982)=78.5398\ \mathrm{kW},$$
$$P_b=\eta_mP_i=0.85(78.5398)=66.7588\ \mathrm{kW}.$$

Fuel rate is obtained from inducted air and specified A/F:

$$\dot m_a=0.9091(0.78)(0.07853982)=0.05569243\ \mathrm{kg/s},$$
$$\dot m_f=\frac{0.05569243}{14.8}=0.003763002\ \mathrm{kg/s}.$$

Thus

$$\eta_{b,th}=\frac{P_b}{\dot m_f\mathrm{LHV}}
=\frac{66.7588}{0.003763002(44425)}=0.399344=39.93\%.$$

**Results: 66.8 kW brake output; 39.9% brake thermal efficiency.** These reproduce the source's 66.8 kW / 40%. The liquid-fuel LHV matches the specified fuel phase; substituting Avgas or gaseous octane properties would be a different calculation.

## Verification

IMEP-to-power conversion, four-stroke cycle frequency, air/fuel mass flow and liquid-fuel energy balance agree with the supplied result. Recomputed by [verify.py](verify.py).
