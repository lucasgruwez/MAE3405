# Answer 11 — Problem-set Q19

Use [Aide Memoire, Table 5, p. 2](../../MAE3405%20Aide%20Memoire.pdf#page=2) for atmosphere, [Table 3, p. 1](../../MAE3405%20Aide%20Memoire.pdf#page=1) for gravity, and [p. 6](../../MAE3405%20Aide%20Memoire.pdf#page=6) for knot conversion and drag. The arithmetic retains the original problem-set density rounding, $\rho=1.111\ \mathrm{kg/m^3}$; using Table 5's extra digit changes power slightly. The oblique-flow quartic and power model below are additional lecture relations, not the aide's axial-flow Froude equations.

## 1. Drag-area convention and force balance

Topic 6 §6.5 explicitly defines drag using **swept rotor area**. Adopting that convention closes the source statement without inventing a fuselage frontal area:
\[
A=\pi(5)^2=78.5398\ \mathrm{m^2},
\quad u=25\frac{1.85}{3.6}=12.84722\ \mathrm{m/s},
\quad W=600(9.81)=5886\ \mathrm N.
\]
Thus
\[
D=\frac12\rho A C_Du^2
=\frac12(1.111)(78.5398)(0.35)(12.84722)^2
=2520.35\ \mathrm N,
\]
\[
T=\sqrt{W^2+D^2}=6402.90\ \mathrm N.
\]
The rotor thrust is inclined by $\tan^{-1}(D/W)\approx23.2^\circ$ from vertical. Taking $T=W$ despite this drag would be inconsistent.

## 2. Resultant airspeed at the disk

Let $u_r$ be the magnitude of ambient relative flow plus induced velocity at the disk. The induced velocity is along thrust, with magnitude
\[
v_i=\frac{T}{2\rho A u_r}.
\]
Its component in the freestream direction is $v_i D/T$, so vector addition gives
\[
u_r^2=u^2+2uv_i\frac DT+v_i^2.
\]
Substitute $v_i$ and $D=\tfrac12\rho A C_Du^2$:
\[
u_r^4-u^2u_r^2-\frac12 C_Du^3u_r
-\frac1{16}C_D^2u^4-\left(\frac{W}{2\rho A}\right)^2=0.
\]
This is the Topic 6 forward-flight equation. Here
\[
b=\frac{W}{2\rho A}=33.72767\ \mathrm{m^2/s^2}.
\]
The numerical polynomial is approximately
\[
f(u_r)=u_r^4-165.0511u_r^2-371.0785u_r-1346.1262.
\]
The physical root has $u_r>u$ and is
\[
u_r=14.07838\ \mathrm{m/s}.
\]
For calculator interpolation, $f(14.0)<0$ and $f(14.2)>0$; refining near 14.078 gives the quoted root. The velocity is not a blade-tip rotational velocity; no rotor RPM or blade-element integration is necessary.

## 3. Induced and parasite power

\[
v_i=\frac{6402.90}{2(1.111)(78.5398)(14.07838)}
=2.606094\ \mathrm{m/s}.
\]
Shaft power supplies both induced power and power against drag:
\[
P=Tv_i+Du=\frac{T^2}{2\rho A u_r}+Du.
\]
Numerically,
\[
P_{\rm induced}=16.6866\ \mathrm{kW},\qquad
P_{\rm parasite}=32.3795\ \mathrm{kW},
\]
\[
P=49.0660\ \mathrm{kW}\approx49.1\ \mathrm{kW}.
\]
This includes no tail-rotor, accessory, profile or transmission power.

Source comparison: 49.16kW is printed. The explicitly specified rounded atmosphere and $1\ \mathrm{knot}=1.85$km/h give 49.066kW, a difference of about 0.2%; no parameter was altered to force agreement. If $C_D$ were instead based on an unspecified fuselage area, the problem would be underdetermined. The adopted swept-area convention is the lecture model, not a physical claim that helicopter frontal area equals rotor area.

Verification: `python3 verify.py` solves the unrounded quartic, checks its residual and independently computes $Tv_i+Du$.
