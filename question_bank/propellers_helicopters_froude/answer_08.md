# Answer 08 — Problem-set Q16

Use SSL density from [Aide Memoire, Table 5, p. 2](../../MAE3405%20Aide%20Memoire.pdf#page=2) and apply the lift/linear-lift relations on [p. 6](../../MAE3405%20Aide%20Memoire.pdf#page=6) locally to each blade strip.

## (i) Integrate the blade-element thrust

The angular speed is
\[
\Omega=2\pi\frac{2700}{60}=282.7433\ \mathrm{rad/s}.
\]
Let $x=r/R$, so $dr=R\,dx$, $x_h=0.05$ and $x_t=1$. Because the slope is given **per degree**, use the numerical angle in degrees directly:
\[
C_L=0.15(12-4x)=1.8-0.6x,
\quad c=0.1R(1.1-x).
\]
For three blades,
\[
T=\frac B2\rho\Omega^2\int_{r_h}^R r^2C_L(r)c(r)\,dr
=\frac B2\rho\Omega^2(0.1R^4)
\int_{0.05}^1x^2(1.8-0.6x)(1.1-x)\,dx.
\]
**Polynomial algebra:**
\[
(1.8-0.6x)(1.1-x)=1.98-2.46x+0.6x^2,
\]
\[
x^2(1.8-0.6x)(1.1-x)=1.98x^2-2.46x^3+0.6x^4.
\]
Therefore
\[
I=\left[0.66x^3-0.615x^4+0.12x^5\right]_{0.05}^{1}.
\]
At the tip the antiderivative is $0.66-0.615+0.12=0.165$; at the root it is
\[
0.66(0.05)^3-0.615(0.05)^4+0.12(0.05)^5
=0.00007869375.
\]
Thus $I=0.16492130625$ and
\[
T=\frac32(1.225)(282.7433)^2(0.1)(1)^4(0.16492130625)
=2422.64\ \mathrm N=2.423\ \mathrm{kN}.
\]
No numerical quadrature is needed. The hub is a **radius** cutoff, not the integration length. Retaining only one blade would underpredict thrust by a factor of three.

## (ii) Induced velocity

Use the total thrust on one ideal swept disk of area $A=\pi R^2$:
\[
v_i=\sqrt{\frac{T}{2\rho A}}
=\sqrt{\frac{2422.64}{2(1.225)\pi(1)^2}}
=17.7413\ \mathrm{m/s}\approx18\ \mathrm{m/s}.
\]
This is the **disk-induced speed**; the far wake is $2v_i=35.4827\ \mathrm{m/s}$.

The source gives 2.4kN and 18m/s, agreeing at its stated precision. Part (i) ignores the inflow subsequently estimated in (ii), as required by simple blade-element theory; the result is not a self-consistent coupled BET/momentum solution. The imposed linear lift law also reaches $C_L$ near 1.8 at the root, so ignoring stall is a significant idealisation.

Verification: `python3 verify.py` evaluates the analytic antiderivative, the 2422.640N thrust and 17.74134m/s induced speed.
