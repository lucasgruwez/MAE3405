# Answer 10 — Problem-set Q17C

This is retained separately because it is not an exact textual duplicate of examination Q2 from 2015, although all numerical givens and the physical problem coincide. The solution is repeated here so this pair is usable independently.

## (i) Maximum payload at SSL

\[
P_0=2(4050)=8100\ \mathrm{kW},\quad
P_{m0}=P_0-0.2P_0=6480\ \mathrm{kW},
\quad A=\pi(17.5)^2=962.113\ \mathrm{m^2}.
\]
Invert the static Froude power relation on [Aide Memoire, p. 6](../../MAE3405%20Aide%20Memoire.pdf#page=6), with SSL density from [Table 5, p. 2](../../MAE3405%20Aide%20Memoire.pdf#page=2) and gravity from [Table 3, p. 1](../../MAE3405%20Aide%20Memoire.pdf#page=1):
\[
T_{\max}=[6480000\sqrt{2(1.225)(962.113)}]^{2/3}
=462573.4\ \mathrm N,
\]
\[
m_{\max}=T_{\max}/9.81=47153.3\ \mathrm{kg},
\quad m_{\rm payload}=47153.3-28000=19153.3\ \mathrm{kg}.
\]
Thus the ideal maximum payload is **19,153kg**, in agreement with the source.

## (ii) Hover ceiling without payload

For $m=28000$kg, the SSL required main-rotor power is
\[
P_{\rm req,0}=\frac{(28000\cdot9.81)^{3/2}}
{\sqrt{2(1.225)(962.113)}}=2965.135\ \mathrm{kW}.
\]
As density falls, required induced power increases as $1/\sqrt\sigma$. The added density-lapse assumption gives available main power $8100\sigma-1620$kW. Therefore
\[
8100\sigma-1620=2965.135\sigma^{-1/2}.
\]
Writing $x=\sqrt\sigma$ gives a hand-solvable cubic,
\[
f(x)=8100x^3-1620x-2965.135=0.
\]
For example $f(0.80)=-113.935$kW and $f(0.82)=172.545$kW. Trial/interpolation narrows the physical root to
\[
x=0.8080864,\qquad\sigma=0.6530037,
\qquad\rho=0.799929\ \mathrm{kg/m^3}.
\]
At the root both available and required main-rotor powers are approximately 3669.33kW. Interpolate the adjacent 4000m and 4500m density rows in [Table 5, p. 2](../../MAE3405%20Aide%20Memoire.pdf#page=2):
\[
h=4000+500\frac{0.8191-0.799929}{0.8191-0.7768}
=4226.6\ \mathrm m.
\]
The model's ceiling is **4.23km**, not exactly the printed **4100m**. The source gives no explicit altitude-power characteristic, so a precise ceiling is underdetermined before adaptation. Its 4100m should be treated as approximate/model dependent, not used to back-fit unspecified engine data. No piston-engine empirical $1.132\sigma-0.132$ lapse has been imposed on the turboshafts.

The 20% allowance remains a fixed fraction of **SSL rated power** at altitude. Making it 20% of altitude power changes the model and its answer. No ground-effect correction is applied despite “just lifted from the ground”; this is an ideal out-of-ground-effect estimate.

Verification: `python3 verify.py` recalculates this and Question 03 from the same physical data and checks the cubic power balance.
