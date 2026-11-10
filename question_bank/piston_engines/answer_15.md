# Answer 15 — Net brake-power gain from mechanical supercharging

- Question: [question_15.md](question_15.md).
- Source: [Problem set Q13](../../problem_sets/MAE3405%20Problem%20Set%20Questions%20Week%205-6.pdf#page=1), PDF page 1.

## Adaptation and model ambiguity

All original engine data and the requested net gain remain. Air and SSL reference data are left for the student to find rather than duplicated in the question. The original invariant “indicated power per unit ambient induced volume” does not state whether the separately modelled positive pumping loop is included. The question declares the primary interpretation as **net indicated power**; the alternative power-loop interpretation is documented only in this answer. Fuel mass is ignored as directed.

## Swept-volume rate and original power

$$V_s=6\frac{\pi(0.075)^2}{4}(0.100)=0.002650719\ \mathrm{m^3},$$
$$\dot V_s=V_s\frac{2800}{120}=0.06185011\ \mathrm{m^3/s}.$$

Original ambient induced volume and mass flow:

$$\dot V_{a,0}=0.80\dot V_s=0.04948008\ \mathrm{m^3/s},\qquad
\dot m_{a,0}=1.225\dot V_{a,0}=0.06061310\ \mathrm{kg/s}.$$
$$P_{i,0}=\frac{110}{0.80}=137.5\ \mathrm{kW}.$$

## Delivery density and increased indicated power

$$\Delta T_c=\frac{288.15(1.6^{0.4/1.4}-1)}{0.70}=59.16161\ \mathrm{K},$$
$$T_c=347.31161\ \mathrm{K},\qquad
\frac{\rho_c}{\rho_a}=1.6\frac{288.15}{347.31161}=1.32745345.$$

The supercharged engine fills its swept volume at delivery conditions, hence

$$\dot m_{a,sc}=\rho_c\dot V_s=0.10057634\ \mathrm{kg/s}.$$

The ambient-equivalent volume-flow ratio is the mass-flow ratio:

$$k=\frac{\dot m_{a,sc}}{\dot m_{a,0}}
=\frac{1.00}{0.80}\frac{\rho_c}{\rho_a}=1.65931681.$$

The given invariant then yields

$$P_{i,sc}=kP_{i,0}=228.15606\ \mathrm{kW},$$
$$P_{b,sc,\mathrm{before\ drive}}=0.80P_{i,sc}=182.52485\ \mathrm{kW}.$$

## Compressor-drive deduction and net gain

$$P_{sc}=\frac{\dot m_{a,sc}c_p\Delta T_c}{0.95}
=\frac{0.10057634(1.005)(59.16161)}{0.95}=6.29475\ \mathrm{kW}.$$

Therefore

$$P_{b,sc}=182.52485-6.29475=176.23010\ \mathrm{kW},$$
$$\Delta P_b=176.23010-110=66.23010\ \mathrm{kW}.$$

**Primary result: net increase 66.23 kW (net shaft output 176.23 kW).** Do not subtract supercharger drive power from indicated power and then apply engine mechanical efficiency: drive power is a brake-shaft load.

## Alternative separate pumping-loop convention

If the invariant refers to the high-pressure power loop only, Topic 5 p.9 adds the positive pumping-loop brake power

$$\Delta P_{b,pump}=\eta_m(p_c-p_a)\dot V_s
=0.80(0.6)(101.325)(0.06185011)=3.00814\ \mathrm{kW}.$$

The corresponding gain becomes $66.23010+3.00814=69.23824$ kW, and net output 179.238 kW. This alternative must be labelled; adding it to an already-net indicated power double counts the pumping contribution.

The printed 70.4 kW gain is not obtained exactly from either consistent interpretation with the supplied efficiencies and air properties. The separate-loop result is closer but still differs by 1.16 kW. The source does not supply enough detail to justify forcing its number; the model-dependent discrepancy is retained.

## Verification

Ambient-equivalent flow scaling, compressor work and both net-power conventions recomputed independently; published gain discrepancy documented. Recomputed by [verify.py](verify.py).
