# Answer 09 — Problem-set Q17

Use [Aide Memoire, Tables 1–2, p. 1](../../MAE3405%20Aide%20Memoire.pdf#page=1) for air properties and avgas LHV, [Table 5, p. 2](../../MAE3405%20Aide%20Memoire.pdf#page=2) for SSL conditions, [p. 6](../../MAE3405%20Aide%20Memoire.pdf#page=6) for reference temperature, gas/flow and static Froude relations, and [p. 7](../../MAE3405%20Aide%20Memoire.pdf#page=7) for isentropic state and compressor-efficiency relations. The mixture heat capacities are original question givens, not Table 1 standard-air values.

## 1. Turbocharger and intercooler

Only air passes through the compressor. With $\gamma_a=1.4$,
\[
T_{cs}=288.15(1.3)^{(1.4-1)/1.4}=310.580\ \mathrm K.
\]
Compressor isentropic efficiency gives
\[
T_c=288.15+\frac{T_{cs}-288.15}{0.85}
=314.5386\ \mathrm K.
\]
The cooler removes **75% of the temperature rise**, leaving 25%:
\[
T_1=288.15+0.25(314.5386-288.15)=294.7471\ \mathrm K,
\]
\[
p_1=1.3(101325)=131722.5\ \mathrm{Pa}.
\]
This is not cooling the absolute temperature by 75%. The compressor is exhaust driven; no shaft-drive subtraction is made under the stated no-back-pressure-penalty assumption.

## 2. Reference-energy fuel–air cycle

Use $R_R=R_P=c_p-c_v=0.287\ \mathrm{kJ/(kg\,K)}$. Then
\[
\gamma_R=1.373698,\quad\gamma_P=1.239366,
\]
\[
T_2=T_1(7)^{0.287/0.768}=609.9033\ \mathrm K,
\]
\[
q_H=\frac{0.95(43700)}{14.5+1}=2678.387\ \mathrm{kJ/kg_R}.
\]
At combustion, different heat capacities require the 298K reference offset:
\[
q_H=1.199(T_3-298)-0.768(T_2-298),
\]
\[
T_3=298+\frac{2678.387+0.768(609.9033-298)}{1.199}
=2731.6354\ \mathrm K.
\]
Isentropic expansion and net work are
\[
T_4=T_3/(7)^{0.287/1.199}=1714.4897\ \mathrm K,
\]
\[
w_i=1.199(T_3-T_4)-0.768(T_2-T_1)
=977.5178\ \mathrm{kJ/kg_R}.
\]
Do not cancel the reference temperature across a change in gas composition, and do not apply combustion efficiency twice.

## 3. Induction and brake power

\[
\dot V_s=4\frac\pi4(0.1)^2(0.12)\frac{2500}{120}
=0.0785398\ \mathrm{m^3/s}.
\]
With volumetric efficiency 100% at intercooler outlet conditions,
\[
\dot m_a=\frac{131722.5}{287(294.7471)}(0.0785398)
=0.1222977\ \mathrm{kg/s},
\]
\[
\dot m_f=\dot m_a/14.5=0.00843433\ \mathrm{kg/s},
\quad\dot m_R=\dot m_a+\dot m_f=0.1307320\ \mathrm{kg/s}.
\]
Thus
\[
P_i=\dot m_Rw_i=127.793\ \mathrm{kW},
\quad P_b=0.90P_i=115.0136\ \mathrm{kW}.
\]
Volumetric efficiency here is defined on air induction, while specific cycle work is per kg of **fuel plus air**. Omitting fuel from the work-rate mass is inconsistent.

## 4. Static propeller thrust

The external propeller disk sees ambient SSL density, not boosted manifold density:
\[
A=\pi(0.9)^2=2.54469\ \mathrm{m^2}.
\]
Invert the static Froude relation on p. 6:
\[
T=[115013.6\sqrt{2(1.225)(2.54469)}]^{2/3}
=4352.78\ \mathrm N=4.353\ \mathrm{kN}.
\]
The disk-induced speed is $v_i=P_b/T=26.4230\ \mathrm{m/s}$. Two blades do not mean two actuator disks.

The source's 4.4kN agrees when rounded to one decimal kN. LHV and reference temperature now come from the aide; the induction convention and negligible turbocharger pumping penalty remain explicit modelling adaptations.

Verification: `python3 verify.py` evaluates compressor/cooler states, verifies combustion energy, calculates cycle work and recovers the thrust from the power balance.
