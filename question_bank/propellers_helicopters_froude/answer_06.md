# Answer 06 — Problem-set Q15

Reference data: [Aide Memoire, Tables 1–3, p. 1](../../MAE3405%20Aide%20Memoire.pdf#page=1) (air, avgas and gravity), [Table 5, p. 2](../../MAE3405%20Aide%20Memoire.pdf#page=2) (1000m atmosphere), and [p. 6](../../MAE3405%20Aide%20Memoire.pdf#page=6) (static Froude power, induction and BSFC). The arithmetic retains the original problem-set atmosphere rounding, $p=89874.5\ \mathrm{Pa}$ and $\rho=1.111\ \mathrm{kg/m^3}$; using the aide's extra digits changes the final figures slightly. Stoichiometry retains the declared integer atomic masses and rounds the Table 1 nitrogen/oxygen ratio to 3.76.

## Hover power

The two 4m blades form one disk of radius 4m:
\[
A_m=\pi(4)^2=50.2655\ \mathrm{m^2},\quad T_m=mg=7357.5\ \mathrm N.
\]
Ideal hover gives
\[
v_i=\sqrt{\frac{7357.5}{2(1.111)(50.2655)}}=8.11630\ \mathrm{m/s},
\]
\[
P_m=T_m v_i=59.7157\ \mathrm{kW}.
\]
The tail-rotor power is **specified**, so its blade dimensions are redundant:
\[
P_t=0.10P_m=5.97157\ \mathrm{kW},\qquad
P_b=P_m+P_t=65.6873\ \mathrm{kW}.
\]

## Stoichiometry and fuel flow

For one kmol of the pseudo-fuel CH₂.₂,
\[
\mathrm{CH}_{2.2}+1.55(\mathrm{O_2}+3.76\mathrm{N_2})
\longrightarrow\mathrm{CO_2}+1.1\mathrm{H_2O}+5.828\mathrm{N_2}.
\]
Fuel molecular mass is 14.2kg/kmol; the required air mass is $1.55[32+3.76(28)]=212.784$kg per kmol of fuel. Thus
\[
(AF)_s=\frac{212.784}{14.2}=14.9848.
\]
Four-stroke engine induction gives
\[
\dot V_s=6\frac\pi4(0.1)^2(0.12)\frac{2500}{120}
=0.1178097\ \mathrm{m^3/s},
\]
\[
\dot m_a=0.85\frac{89874.5}{287(281.65)}\dot V_s
=0.1113384\ \mathrm{kg/s},
\quad \dot m_f=\frac{\dot m_a}{14.9848}=0.00743009\ \mathrm{kg/s}.
\]
Here $p/(RT)=1.11188\ \mathrm{kg/m^3}$; the disk calculation uses the separately rounded tabular density 1.111. This small rounding difference is intentional and documented.

### (i) Volumetric fuel consumption

\[
\dot V_f=\frac{0.00743009(3600)}{0.7082}
=37.7695\ \mathrm{L/h}\approx37.8\ \mathrm{L/h}.
\]

### (ii) Brake specific fuel consumption

\[
\mathrm{BSFC}=\frac{0.00743009(3600)}{65.6873}
=0.407207\ \mathrm{kg/(kW\,h)}\approx0.41\ \mathrm{kg/(kW\,h)}.
\]

### (iii) Thermal efficiencies

Fuel energy rate before combustion losses is
\[
\dot Q_f=\dot m_f\,\mathrm{LHV}
=0.00743009(43700)=324.695\ \mathrm{kW}.
\]
Therefore the **brake thermal efficiency** is
\[
\eta_{bth}=\frac{P_b}{\dot Q_f}
=0.202304=20.23\%.
\]
Mechanical efficiency gives $P_i=P_b/0.90=72.9858\ \mathrm{kW}$ and **indicated thermal efficiency**
\[
\eta_{ith}=\frac{P_i}{\dot Q_f}=0.224783=22.48\%.
\]
If one instead wants cycle efficiency relative only to heat actually released, divide indicated power by $\eta_c\dot Q_f$:
\[
\eta_{\rm cycle,released}=\frac{P_i}{0.98\dot Q_f}=22.94\%.
\]
This last convention reproduces the source's **22.9%**. It is not brake thermal efficiency based on supplied fuel LHV, nor the indicated efficiency based on total fuel input. The adaptation reports these conventions explicitly rather than treating the printed figure as interchangeable with them.

No compression ratio is supplied: do not attempt to reconstruct an Otto temperature cycle. Required shaft power and induction data are sufficient. The listed specific heats are unused; combustion efficiency is relevant only if converting to the released-heat convention.

Verification: `python3 verify.py` reproduces 37.7695L/h, 0.407207kg/(kW h), 20.2304% and 22.4783%; division by 0.98 gives the printed 22.9% convention.
