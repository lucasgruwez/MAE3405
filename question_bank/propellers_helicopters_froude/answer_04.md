# Answer 04 — Problem-set Q3D

Balanced three-phase **real** input power is
\[
P_{\rm in}=\sqrt3 V_L I_L\cos\phi.
\]
The source hint without $\cos\phi$ is apparent power, in VA, and must not be used as real input watts.

## No load

\[
P_{\rm in,NL}=\sqrt3(440)(1.2)(0.30)=274.357\ \mathrm W.
\]
There is no useful external shaft load, so $P_{\rm out,NL}=0$:
\[
P_{\rm loss,NL}=274.357\ \mathrm W,\qquad \eta_{\rm NL}=0\%.
\]
The motor can still turn while having zero **useful-load** efficiency: all input is dissipated in internal mechanical, magnetic and electrical losses.

## Full load

The added rating interpretation gives
\[
P_{\rm out,FL}=5(746)=3730\ \mathrm W,
\]
\[
P_{\rm in,FL}=\sqrt3(440)(6.8)(0.78)=4042.191\ \mathrm W.
\]
Therefore
\[
P_{\rm loss,FL}=4042.191-3730=312.191\ \mathrm W,
\]
\[
\eta_{\rm FL}=\frac{3730}{4042.191}=0.922767=92.28\%.
\]
These are motor efficiencies; inverter/battery losses are not included.

## Speed regulation

Using the Topic 2 convention,
\[
\mathrm{SR}=100\frac{1195-1150}{1150}=3.913\%.
\]
Using no-load speed as denominator would give 3.766%, but that is not the supplied lecture convention.

The source's compact answer “4042 W, 312 W/274.4 W, 92.28%, 3.91%” agrees after separating full-load and no-load quantities. Its printed hint, not its numerical answer, is the issue. Without interpreting 5hp as actual full-load shaft output, the full-load loss and efficiency would be undetermined by the electrical data alone.

Verification: `python3 verify.py` independently evaluates both three-phase inputs, their loss balance and regulation.
