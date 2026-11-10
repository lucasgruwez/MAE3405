# Answer 02 — 2014 examination Q2

Assume ideal disks, negligible rotor profile power and losses, no ground effect and a perpendicular 6m tail-thrust moment arm. The main rotor supports $mg$; the secondary correction for lateral tail thrust is neglected.

Atmosphere comes from [Aide Memoire, Table 5, p. 2](../../MAE3405%20Aide%20Memoire.pdf#page=2); the arithmetic below retains the original examination data-sheet rounding, $\rho=1.111\ \mathrm{kg/m^3}$ and $a=336.43\ \mathrm{m/s}$. Using the aide's extra digits gives a slightly different rounded result. Gravity is in [Table 3, p. 1](../../MAE3405%20Aide%20Memoire.pdf#page=1), and static Froude power is on [p. 6](../../MAE3405%20Aide%20Memoire.pdf#page=6).

## Main-rotor thrust and power

\[
T_m=2000(9.81)=19620\ \mathrm N,
\quad A_m=\pi(5)^2=78.5398\ \mathrm{m^2}.
\]
Hover momentum theory gives $T_m=2\rho A_m v_{im}^2$ and $P_m=T_m v_{im}$, so
\[
v_{im}=\sqrt{\frac{19620}{2(1.111)(78.5398)}}=10.6031\ \mathrm{m/s},
\]
\[
P_m=208032.7\ \mathrm W=208.033\ \mathrm{kW}.
\]

## Main-rotor reaction torque

Tip Mach number specifies rotational tip speed in this approximation:
\[
U_{\rm tip}=0.5(336.43)=168.215\ \mathrm{m/s},
\quad\Omega_m=\frac{168.215}{5}=33.643\ \mathrm{rad/s}
\quad(n_m=321.267\ \mathrm{RPM}).
\]
Shaft power is torque times angular speed:
\[
Q_m=\frac{P_m}{\Omega_m}=6183.53\ \mathrm{N\,m}.
\]

## Tail-rotor thrust and power

Yaw moment balance gives
\[
T_t(6)=Q_m,\quad T_t=1030.59\ \mathrm N.
\]
The tail-disk radius is 0.75m, not 1.5m:
\[
A_t=\pi(0.75)^2=1.76715\ \mathrm{m^2},
\]
\[
v_{it}=\sqrt{\frac{T_t}{2\rho A_t}}=16.2007\ \mathrm{m/s},
\quad P_t=T_t v_{it}=16696.3\ \mathrm W=16.70\ \mathrm{kW}.
\]
Main-rotor and tail-rotor torques need not be equal; it is the **tail thrust moment** that balances the main-rotor torque. The result is a lower-bound induced-power estimate, not total installed tail-shaft power.

Verification: `python3 verify.py` reproduces the main torque, $T_t(6)=6183.53$N m and $P_t=16.6963$kW.
