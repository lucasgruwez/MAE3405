# Answer 03: One-stage versus two-stage payload

[Question](question_03.md)

## 1. Relate the velocity increment to stage masses

Write the carried fraction at each stage ignition as

\[
L=\frac{m_{L,n}}{m_{0,n}}.
\]

The mass at burnout, before discarding structure, is \(m_{f,n}=(S+L)m_{0,n}\). The propellant fraction is \(1-S-L\). For \(N\) equal-ratio stages,

\[
\Delta v=NV_e\ln\left(\frac{1}{S+L}\right),
\qquad L=\exp\left(-\frac{\Delta v}{NV_e}\right)-S.
\]

The final probe mass is \(m_{\rm probe}=m_0L^N\). This follows because each stage carries a fraction \(L\) of its own initial mass to the next stage.

## (i) One stage

\[
L=e^{-11200/4500}-0.075=0.00800214.
\]

Therefore

\[
m_{\rm probe}=1000L=8.00214\ \mathrm{kg},
\]

\[
m_s=0.075(1000)=75.000\ \mathrm{kg},
\]

\[
m_p=1000-m_s-m_{\rm probe}=916.99786\ \mathrm{kg}.
\]

**One-stage payload: 8.00 kg; propellant: 917.00 kg.**

## (ii) Two stages

\[
L=e^{-11200/(2\times4500)}-0.075=0.21310092.
\]

The first stage carries an upper-stage assembly of mass

\[
m_{0,2}=1000L=213.10092\ \mathrm{kg}.
\]

The upper stage carries the probe:

\[
m_{\rm probe}=m_{0,2}L=1000L^2=45.41200\ \mathrm{kg}.
\]

Calculate each stage's own structure and propellant:

| Quantity, kg | Lower stage | Upper stage |
|---|---:|---:|
| Initial mass including carried mass | 1000.00000 | 213.10092 |
| Carried mass | 213.10092 | 45.41200 |
| Own structure \(Sm_{0,n}\) | 75.00000 | 15.98257 |
| Own propellant \((1-S-L)m_{0,n}\) | 711.89908 | 151.70635 |

\[
m_{p,\rm total}=711.89908+151.70635=863.60543\ \mathrm{kg}.
\]

**Two-stage payload: 45.41 kg; total propellant: 863.61 kg.**

Total discarded structure is 90.98257 kg. The launch mass balance is

\[
45.41200+863.60543+90.98257=1000.00000\ \mathrm{kg}.
\]

Each stage supplies 5600 m/s. Discarding the first stage's structure avoids accelerating it through the second burn and permits the higher payload.

## Source convention

The source omits the required velocity increment. The lecture context and its quoted answers correspond to the ideal Earth escape requirement: 11.2 km/s in [aide-mémoire Table 3, p. 1](../../MAE3405%20Aide%20Memoire.pdf#page=1). The adapted question identifies that target without repeating the tabulated value. Here \(S=m_s/m_0\), **not** \(m_s/(m_s+m_p)\). Substituting the latter definition would solve a different problem.

Verification: each stage's rocket equation gives 5600 m/s, and the one-stage and two-stage mass balances both close to 1000 kg.
