# Answer 01: Single-stage rocket and propellant comparison

[Question](question_01.md)

This solution uses the ideal-nozzle and trajectory assumptions stated in the question. Reference data come from the [aide-mémoire](../../MAE3405%20Aide%20Memoire.pdf): Tables 3, 5 and 13, including Earth radius 6378 km. The design-altitude thrust is not the sea-level launch thrust.

## (a) Exit velocity

Convert molecular weight to specific gas constant:

\[
R=\frac{R_u}{M},\qquad
T_e=T_c\left(\frac{p_e}{p_c}\right)^{(\gamma-1)/\gamma},
\]

\[
V_e=\sqrt{\frac{2\gamma RT_c}{\gamma-1}
\left[1-\left(\frac{p_e}{p_c}\right)^{(\gamma-1)/\gamma}\right]}.
\]

Use \(p_e/p_c=12044.5709/(3.0\times10^6)=0.004014857\).

| Quantity | Kerosene/O₂ | H₂/O₂ |
|---|---:|---:|
| \(R\), J/(kg K) | 328.747 | 824.802 |
| \(T_e\), K | 1764.02 | 1450.95 |
| **\(V_e\), m/s** | **3061.16** | **4397.48** |

## (b) Propellant flow

The chamber-to-ambient pressure ratio exceeds the choking threshold. For an ideal sonic throat,

\[
\dot m=A_t\frac{p_c}{\sqrt{RT_c}}\sqrt{\gamma}
\left(\frac{2}{\gamma+1}\right)^{(\gamma+1)/[2(\gamma-1)]}.
\]

Thus **\(\dot m=175.554\ \mathrm{kg/s}\)** for kerosene/O₂ and **\(122.206\ \mathrm{kg/s}\)** for H₂/O₂.

## (c) Thrust

\[
F=\dot mV_e+(p_e-p_a)A_e.
\]

At the design altitude \(p_e=p_a\), so **\(F=537.400\ \mathrm{kN}\)** for either propellant. The identical results follow from the shared \(\gamma,p_c,A_t,p_e/p_c\): the product \(\dot mV_e\) is independent of \(RT_c\).

The exit area provides a useful check:

\[
A_e=\frac{\dot mRT_e}{p_eV_e}=2.76120\ \mathrm{m^2}.
\]

Do not use this thrust as the sea-level thrust. The ideal pressure correction at sea level would reduce it to about 290.9 kN; real overexpanded flow may also separate. The question excludes those effects from the trajectory model.

## (d) Specific impulse

\[
I_{sp}=\frac{F}{\dot m g_0}=\frac{V_e}{g_0}.
\]

Results: **312.045 s** for kerosene/O₂; **448.266 s** for H₂/O₂.

## (e) Propellant mass and storage volume

\[
m_p=\dot m t_b,\qquad \mathcal V_p=\frac{m_p}{\rho_{\rm bulk}}.
\]

| Quantity | Kerosene/O₂ | H₂/O₂ |
|---|---:|---:|
| **Propellant mass, kg** | **8777.71** | **6110.31** |
| **Liquid volume, m³** | **8.20347** | **23.1451** |

The liquid volume uses the supplied bulk density. It is not a chamber-gas volume.

## (f) Burnout speed

The final mass contains the structure and satellite:

\[
m_f=1500+50=1550\ \mathrm{kg},\qquad
m_0=m_f+m_p,\qquad r=\frac{m_0}{m_f}.
\]

Integrate the equation along the prescribed flight path,

\[
\frac{dv}{dt}=\frac{V_e\dot m}{m_0-\dot mt}-g_0\sin\theta,
\]

to obtain

\[
v_b=V_e\ln r-g_0t_b\sin\theta.
\]

Here \(g_0t_b\sin80^\circ=483.048\ \mathrm{m/s}\).

| Quantity | Kerosene/O₂ | H₂/O₂ |
|---|---:|---:|
| Initial mass, kg | 10327.71 | 7660.31 |
| Mass ratio \(r\) | 6.66304 | 4.94214 |
| Ideal, no-gravity velocity increment, m/s | 5805.73 | 7026.29 |
| **Burnout speed, m/s** | **5322.68** | **6543.24** |

## (g) Burnout and coast altitude

Integrate the speed once more. For a launch from rest, the distance along the flight path is

\[
s_b=V_et_b\left(1-\frac{\ln r}{r-1}\right)
-\frac12g_0t_b^2\sin\theta.
\]

For example, the logarithmic term follows from integrating \(\ln[m_0/(m_0-\dot mt)]\) between 0 and \(t_b\). Convert to vertical quantities:

\[
z_b=s_b\sin\theta,\qquad v_{z,b}=v_b\sin\theta.
\]

In the stipulated radial coast approximation, conserve mechanical energy:

\[
\frac{v_{z,b}^2}{2}-\frac{\mu}{R_E+z_b}
=-\frac{\mu}{R_E+z_{\max}},
\]

\[
z_{\max}=\left[\frac{1}{R_E+z_b}
-\frac{v_{z,b}^2}{2\mu}\right]^{-1}-R_E.
\]

| Quantity | Kerosene/O₂ | H₂/O₂ |
|---|---:|---:|
| Along-path burnout distance \(s_b\), km | 89.722 | 118.680 |
| **Vertical burnout height \(z_b\), km** | **88.359** | **116.877** |
| Vertical burnout velocity, m/s | 5241.81 | 6443.84 |
| Coast altitude gain, km | 1851.73 | 3314.68 |
| **Maximum altitude above sea level, km** | **1940.09** | **3431.55** |

## Source checks

The set lists hydrogen exit velocity 4423 m/s; the aide-mémoire's Table 13 values give 4397.48 m/s. Its printed volumes of 8240 m³ and \(23\times10^3\) m³ are inconsistent with liquid propellant densities: volumes near 8.2 and 23 m³ have the correct scale. The set's heights also use different near-vertical/property approximations. Use the explicit data and trajectory conventions here rather than forcing agreement with those printed values.

Verification: numerical substitution using Python's standard-library `math`; both fuel cases give the same ideal design thrust, and each mass balance satisfies \(m_0-m_p=1550\ \mathrm{kg}\).
