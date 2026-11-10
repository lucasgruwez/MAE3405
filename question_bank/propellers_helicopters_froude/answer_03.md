# Answer 03 — 2015 examination Q2

## (a) Maximum SSL payload

Total rated power is $P_0=2(4050)=8100\ \mathrm{kW}$. The tail/accessory deduction is $0.2P_0=1620\ \mathrm{kW}$, leaving
\[
P_{m0}=6480\ \mathrm{kW},\quad A=\pi(17.5)^2=962.113\ \mathrm{m^2}.
\]
Invert the ideal static Froude power relation on [Aide Memoire, p. 6](../../MAE3405%20Aide%20Memoire.pdf#page=6), using SSL density from [Table 5, p. 2](../../MAE3405%20Aide%20Memoire.pdf#page=2) and gravity from [Table 3, p. 1](../../MAE3405%20Aide%20Memoire.pdf#page=1):
\[
T_{\max}=[P_{m0}\sqrt{2\rho_0 A}]^{2/3}
=462573.4\ \mathrm N.
\]
\[
m_{\max}=\frac{T_{\max}}{g}=47153.3\ \mathrm{kg},
\quad m_{\rm payload}=47153.3-28000=19153.3\ \mathrm{kg}.
\]
Thus maximum ideal SSL payload is **19.15 tonnes**. Five blades sweep one disk; blade count is not a multiplier on disk area.

## (b) Hover ceiling without payload

The original question gives no power-lapse characteristic. Under the explicit added model, $P_{\rm eng}=P_0\sigma$ and
\[
P_{m,\rm available}=8100\sigma-1620\quad\mathrm{kW}.
\]
The 1620kW is constant, as required by “20% of the SSL rated engine power”. Do not use $6480\sigma$.

At zero payload $T=28000g=274680\ \mathrm N$. Required SSL main power is
\[
P_{\rm req,0}=\frac{(274680)^{3/2}}{\sqrt{2(1.225)(962.113)}}
=2965.135\ \mathrm{kW}.
\]
At altitude it becomes $P_{\rm req}=2965.135/\sqrt\sigma$. Equating power,
\[
8100\sigma-1620=\frac{2965.135}{\sqrt\sigma}.
\]
Put $x=\sqrt\sigma$:
\[
8100x^3-1620x-2965.135=0.
\]
Trial/interpolation gives $x=0.8080864$, hence
\[
\sigma=0.6530037,\quad \rho=0.799929\ \mathrm{kg/m^3}.
\]
At this density both available and required main power are about **3669.33kW**. Interpolate between the adjacent 4000m and 4500m entries in [Table 5, p. 2](../../MAE3405%20Aide%20Memoire.pdf#page=2):
\[
h=4000+500\frac{0.8191-0.799929}{0.8191-0.7768}
=4226.6\ \mathrm m.
\]
The ideal hover ceiling is **4.23km** under the specified density-lapse assumption. Table interpolation is sufficient; no additional continuous-atmosphere formula is needed.

No unique ceiling follows from SSL power alone: a real turboshaft power-lapse/temperature-limit map or an explicit approximation is necessary. Ground effect and profile losses have been excluded; real payload and ceiling will differ.

The problem-set near-duplicate prints 19,153kg and 4100m. The payload agrees. Its 4100m is only an approximate ceiling and does not satisfy the stated density-lapse power balance with Table 5; no unexplained adjustment has been made to force that number.

Verification: `python3 verify.py` checks the payload and solves the ceiling balance by bisection; $P_{\rm available}-P_{\rm required}$ vanishes at the quoted unrounded density ratio.
