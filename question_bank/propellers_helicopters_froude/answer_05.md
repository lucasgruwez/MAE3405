# Answer 05 — Problem-set Q14

Use $c_v$ and $R$ in kJ/(kg K), LHV in kJ/kg, and power in kW until converting to watts for Froude theory. Reactants and products have the **same total mass**, including fuel.

Use [Aide Memoire, Table 2, p. 1](../../MAE3405%20Aide%20Memoire.pdf#page=1) for avgas LHV and [p. 6](../../MAE3405%20Aide%20Memoire.pdf#page=6) for reference temperature, gas relations, four-stroke flow and static Froude power. Atmosphere is in [Table 5, p. 2](../../MAE3405%20Aide%20Memoire.pdf#page=2); the arithmetic retains the original problem-set rounding ($p_1=79495.2\ \mathrm{Pa}$, $\rho_\infty=1.006\ \mathrm{kg/m^3}$). Using the aide's extra density digits changes thrust slightly. The reactant/product heat capacities remain original question givens, not standard-air properties.

## 1. Reference-energy fuel–air Otto cycle

From the supplied properties,
\[
\gamma_R=1+\frac{0.287}{0.768}=1.373698,
\qquad\gamma_P=1+\frac{0.287}{1.199}=1.239366.
\]
The isentropic compression gives
\[
T_2=T_1r_c^{\gamma_R-1}
=275.15(7.5)^{0.287/0.768}=584.222\ \mathrm K.
\]
Combustion heat per kg of **reactant mixture** is
\[
q_H=\frac{\eta_c\,\mathrm{LHV}}{AF+1}
=\frac{0.99(43700)}{15.5}=2791.161\ \mathrm{kJ/kg_R}.
\]
The lecture reference-energy balance is
\[
q_H=c_{vP}(T_3-T_r)-c_{vR}(T_2-T_r),
\]
not $q_H=c_{vP}T_3-c_{vR}T_2$. Consequently
\[
T_3=298+\frac{2791.161+0.768(584.222-298)}{1.199}
=2809.243\ \mathrm K,
\]
\[
T_4=\frac{T_3}{r_c^{\gamma_P-1}}=1734.320\ \mathrm K.
\]
Expansion work minus compression work gives
\[
w_i=c_{vP}(T_3-T_4)-c_{vR}(T_2-T_1)
\]
\[
=1.199(2809.243-1734.320)-0.768(584.222-275.15)
=1051.465\ \mathrm{kJ/kg_R}.
\]
This retains the 298K reference offset when composition/specific heat changes. The air-standard formula $1-r_c^{1-\gamma}$ is not appropriate.

## 2. Inducted flow and brake power

The four-stroke swept-volume flow is
\[
\dot V_s=4\frac\pi4(0.1)^2(0.125)\frac{2700}{120}
=0.0883573\ \mathrm{m^3/s}.
\]
The provided air-induction convention gives
\[
\dot m_a=0.8\frac{79495.2}{287(275.15)}\dot V_s
=0.0711577\ \mathrm{kg/s},
\]
\[
\dot m_f=\frac{\dot m_a}{14.5}=0.00490743\ \mathrm{kg/s},
\quad \dot m_R=0.0760651\ \mathrm{kg/s}.
\]
Use $\dot m_R$, not just $\dot m_a$, with work per kg of mixture:
\[
P_b=\eta_m\dot m_Rw_i
=0.85(0.0760651)(1051.465)=67.9828\ \mathrm{kW}.
\]
Combustion efficiency has already entered $q_H$; do not multiply by it again.

## 3. Static thrust

For one ideal disk $A=\pi(1)^2=3.14159\ \mathrm{m^2}$. Invert the static Froude power relation on p. 6:
\[
T=[67982.8\sqrt{2(1.006)(3.14159)}]^{2/3}
=3079.82\ \mathrm N=3.080\ \mathrm{kN}.
\]
The induced disk speed is $v_i=P_b/T=22.0736\ \mathrm{m/s}$; useful translational thrust power is zero in a static test, although shaft power is not zero.

Source comparison: the printed 3.07kN differs by approximately 0.3%, consistent with slightly different/rounded atmosphere or unspecified fuel data. With the aide's avgas LHV, the documented atmosphere rounding and induction conventions, 3.080kN is the reproducible answer. The air-based volumetric-efficiency interpretation is a disclosed modelling adaptation, not a recovered original given.

Verification: `python3 verify.py` checks the 298K heat balance and evaluates both cycle power and static thrust numerically.
