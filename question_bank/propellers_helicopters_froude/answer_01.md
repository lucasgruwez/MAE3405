# Answer 01 — 2013 examination Q2

Use [Aide Memoire, Table 5, p. 2](../../MAE3405%20Aide%20Memoire.pdf#page=2) for SSL density, [Table 3, p. 1](../../MAE3405%20Aide%20Memoire.pdf#page=1) for gravity, and the lift/static Froude relations on [p. 6](../../MAE3405%20Aide%20Memoire.pdf#page=6).

## (a) Shaft unloading speed

Only the blade weight must be supported: no helicopter mass is supplied. At radius $r$, the tangential speed is $U=\Omega r$ and blade area is $c\,dr$. Thus
\[
dL=\frac12\rho(\Omega r)^2 C_Lc\,dr,
\quad L=\frac{\rho\Omega^2C_Lc}{6}(R^3-r_h^3).
\]
Zero vertical reaction at the shaft requires $L=m_bg=20(9.81)=196.2\ \mathrm N$. With $R=3.5\ \mathrm m$, $r_h=0.4\ \mathrm m$, $c=0.250\ \mathrm m$,
\[
R^3-r_h^3=42.811\ \mathrm{m^3},
\]
\[
\Omega=\sqrt{\frac{6(196.2)}{1.225(1)(0.250)(42.811)}}
=9.47566\ \mathrm{rad/s},
\quad n=\frac{60\Omega}{2\pi}=90.49\ \mathrm{RPM}.
\]
Four identical blades multiply both lift and weight by four, so do not change this RPM.

## (b) Rotor power

For four blades $T=4m_bg=784.8\ \mathrm N$. There is one swept disk, not four disks:
\[
A=\pi R^2=38.4845\ \mathrm{m^2}.
\]
In ideal hover, mass flow is $\dot m=\rho A v_i$ and far-wake speed is $2v_i$. Momentum gives $T=2\rho A v_i^2$; energy gives $P=\tfrac12\dot m(2v_i)^2=Tv_i$. Hence
\[
v_i=\sqrt{\frac{784.8}{2(1.225)(38.4845)}}=2.88505\ \mathrm{m/s},
\]
\[
P=784.8(2.88505)=2264.19\ \mathrm W=2.264\ \mathrm{kW}.
\]
This is a minimum **induced-power estimate**, not a profile-drag calculation. The original gives no section drag coefficient, so actual shaft power cannot be determined. The specified approximation deliberately uses no-inflow blade-element lift to determine RPM and momentum theory to estimate power; a coupled inflow solution would require further blade geometry/pitch information. The blade root cutoff is included in lift; the ideal disk uses the full swept area.

Verification: `python3 verify.py` gives $n=90.4859$RPM and $P=2264.19$W and recovers $T=2\rho A v_i^2$.
