# Answer 02: Sea-level launch thrust and burnout height

[Question](question_02.md)

Use the [aide-mémoire](../../MAE3405%20Aide%20Memoire.pdf), Tables 3 and 5 and the conversion/reference data on p. 6, for the constants substituted below.

## (i) Launch thrust

Convert temperature and gas constant:

\[
T_c=2750+273.15=3023.15\ \mathrm K,
\qquad R=\frac{8314}{22}=377.909\ \mathrm{J/(kg\,K)}.
\]

The pressure ratio \(p_c/p_e=29.61\) exceeds the ideal choking threshold. The nozzle exit velocity and choked throat mass flow are

\[
V_e=\sqrt{\frac{2\gamma RT_c}{\gamma-1}
\left[1-\left(\frac{p_e}{p_c}\right)^{(\gamma-1)/\gamma}\right]}
=2501.47\ \mathrm{m/s},
\]

\[
\dot m=A_t\frac{p_c}{\sqrt{RT_c}}\sqrt\gamma
\left(\frac{2}{\gamma+1}\right)^{(\gamma+1)/[2(\gamma-1)]}
=179.247\ \mathrm{kg/s}.
\]

At launch \(p_e=p_a\), so the pressure-thrust term vanishes:

\[
F_0=\dot mV_e=448382\ \mathrm N.
\]

**Launch thrust: 448.38 kN.**

## (ii) Burnout height

First determine the masses:

\[
m_f=3000+100=3100\ \mathrm{kg},\qquad
m_p=\dot mt_b=13443.55\ \mathrm{kg},
\]

\[
m_0=16543.55\ \mathrm{kg},\qquad
r=\frac{m_0}{m_f}=5.33663.
\]

The along-path equation of motion under the stated approximation is

\[
\frac{dv}{dt}=\frac{V_e\dot m}{m_0-\dot mt}-g\sin\theta.
\]

Integrating from rest gives

\[
v(t)=V_e\ln\left(\frac{m_0}{m_0-\dot mt}\right)-gt\sin\theta.
\]

Integrating again gives along-path burnout distance:

\[
s_b=V_et_b\left[1-\frac{\ln r}{r-1}\right]
-\frac12gt_b^2\sin\theta.
\]

Substitute \(t_b=75\ \mathrm s\), \(\theta=85^\circ\):

\[
s_b=87678.87\ \mathrm m.
\]

The vertical height is

\[
z_b=s_b\sin85^\circ=87345.22\ \mathrm m.
\]

**Vertical burnout height: 87.35 km.**

Check: the burnout speed is \(V_e\ln r-gt_b\sin85^\circ=3456.00\ \mathrm{m/s}\). The source's rounded 88 km agrees with the along-path distance of 87.68 km. Here the question asks for its vertical component. The constant-effective-velocity trajectory model does not include the increase in pressure thrust as ambient pressure falls.

Verification: standard-library numerical substitution; \(\dot m t_b+m_f=m_0\), and \(z_b<s_b\) as required for a nonvertical flight path.
