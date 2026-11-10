# Answer 07 — Problem-set Q16D

The statement does not name the drag reference area or define “maximum torque”. The adaptation adopts the Topic 6 **total swept-disk area** convention and the Topic 2 **linear torque–speed / stall-torque** model. These are stated assumptions, not newly discovered dimensions or a measured motor map.

Use gravity from [Aide Memoire, Table 3, p. 1](../../MAE3405%20Aide%20Memoire.pdf#page=1) and drag from [p. 6](../../MAE3405%20Aide%20Memoire.pdf#page=6). Interpolate density between the sea-level and 500m rows of [Table 5, p. 2](../../MAE3405%20Aide%20Memoire.pdf#page=2):
\[
h=200(0.3048)=60.96\ \mathrm m,\qquad
\rho=1.225+(1.1673-1.225)\frac{60.96}{500}
=1.217965216\ \mathrm{kg/m^3}.
\]

## Area, wind and thrust

\[
u=36/3.6=10\ \mathrm{m/s},\quad d_r=4(0.0254)=0.1016\ \mathrm m,
\]
\[
A=4\pi(d_r/2)^2=0.0324293\ \mathrm{m^2},\qquad W=1.5(9.81)=14.715\ \mathrm N.
\]
The drag force and total inclined thrust are
\[
D=\tfrac12(1.217965216)(0.0324293)(0.75)(10)^2=1.48117\ \mathrm N,
\]
\[
T=\sqrt{W^2+D^2}=14.78936\ \mathrm N.
\]
The disk thrust direction tilts by $\tan^{-1}(D/W)\approx5.75^\circ$.

## Relative disk velocity and shaft power

For completeness, the supplied resultant speed comes from momentum theory. The induced velocity vector is parallel to thrust; its magnitude is $v_i=T/(2\rho A u_r)$. Vector addition with the horizontal relative wind gives
\[
u_r^2=u^2+2u v_i\frac DT+v_i^2.
\]
Eliminating $v_i$, and writing $b=W/(2\rho A)$, yields
\[
u_r^4-u^2u_r^2-\tfrac12C_Du^3u_r-\tfrac1{16}C_D^2u^4-b^2=0.
\]
The physical root is $u_r=16.08617\ \mathrm{m/s}$, consistent with the supplied 16.086m/s. Hence
\[
v_i=\frac{14.78936}{2(1.217965216)(0.0324293)(16.08617)}
=11.63843\ \mathrm{m/s}.
\]
The ideal shaft power is
\[
P_s=Tv_i+Du
=14.78936(11.63843)+1.48117(10)
=186.937\ \mathrm W.
\]
Although the drone is stationary relative to the ground, it acts on a moving air stream: the $Du$ term represents energy transfer to that stream, not ground-relative mechanical work on the drone.

### (i) Endurance

\[
P_{\rm battery}=P_s/0.8=233.671\ \mathrm W,
\quad E=22.2(1.3)=28.86\ \mathrm{Wh}.
\]
\[
t=\frac{28.86}{233.671}=0.1235072\ \mathrm h
=7.41043\ \mathrm{min}.
\]
The 1.3Ah is the **whole battery's** capacity, not the capacity for each motor. Four equal motors are already accounted for through total disk area and shaft power.

### (ii) RPM

No-load speed is $n_0=KV\,V=1200(22.2)=26640$RPM. With $\tau/\tau_{\rm stall}=1/6$,
\[
n=n_0\left(1-\frac16\right)=26640\frac56=22200\ \mathrm{RPM}.
\]
The factor $5/6$ comes from the torque–speed assumption, **not** the 80% efficiency. A maximum continuous torque rating would not justify it; without the explicit model, KV and a fraction of unspecified “maximum torque” are insufficient to infer loaded RPM.

The source prints 7.4min and 22,200RPM, agreeing under these assumptions. Real endurance needs profile power, controller losses, voltage sag, capacity reserve and the actual motor/propeller operating map.

Verification: `python3 verify.py` interpolates Table 5 density at 60.96m, solves the quartic, checks its residual, and reproduces 7.41043min and 22200RPM. Using the supplied rounded disk speed rather than the unrounded root has negligible effect at the quoted answer precision.
