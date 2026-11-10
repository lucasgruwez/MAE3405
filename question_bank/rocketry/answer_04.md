# Answer 04: Hydrogen–oxygen rocket nozzle comparison

[Question](question_04.md)

Species properties below come from [aide-mémoire Table 1, p. 1](../../MAE3405%20Aide%20Memoire.pdf#page=1), and ambient pressure from Table 5, p. 2. Keep the source question's formation enthalpy; Table 12 gives the reference temperature.

## 1. Combustion balance

On a basis of 1 kmol of water produced,

\[
\mathrm{H_2+\tfrac12O_2\rightarrow H_2O}.
\]

The tabulated molecular weights give 2.016 kg H₂ and 16.005 kg O₂ per 18.015 kg of water produced. The 0.006 kg basis mismatch reflects tabulated molecular-weight rounding. With efficiency applied to the chemical heat release,

\[
18.015c_{p,w}(T_c-T_{\rm ref})
=\eta_c(241.827\times10^6)
+(2.016c_{p,H_2}+16.005c_{p,O_2})(T_{\rm in}-T_{\rm ref}).
\]

Use \(T_{\rm in}=250.15\ \mathrm K\):

\[
T_c=298.15+
\frac{0.90(241.827\times10^6)
+[2.016(14209.1)+16.005(921.6)](-48)}{18.015(1872.3)}
=6689.04\ \mathrm K.
\]

The high temperature follows from the stipulated constant heat capacities and omission of dissociation. It is not a realistic equilibrium flame temperature.

Exhaust properties:

\[
R=461.52\ \mathrm{J/(kg\,K)}\quad\text{(Table 1)}.
\]

\[
c_v=c_p-R=1410.78\ \mathrm{J/(kg\,K)},\qquad
\gamma=\frac{c_p}{c_v}=1.327138.
\]

## (i) Converging nozzle

### Sonic exit state

Energy conservation and the sonic condition give

\[
c_p(T_c-T_*)=\frac{V_*^2}{2}=\frac{\gamma RT_*}{2},
\qquad T_*=\frac{2T_c}{\gamma+1}=5748.72\ \mathrm K.
\]

Use the nozzle efficiency to find the actual critical pressure:

\[
\frac{T_{*,s}}{T_c}
=1-\frac{\gamma-1}{\eta_n(\gamma+1)},
\]

\[
p_*=p_c\left[1-\frac{\gamma-1}{\eta_n(\gamma+1)}\right]^{\gamma/(\gamma-1)}
=3.65560\ \mathrm{MPa}.
\]

Because \(p_a=5474.8887\ \mathrm{Pa}<p_*\), the nozzle chokes. Its geometric exit is the throat.

\[
A_* =\frac{\pi(0.500)^2}{4}=0.196350\ \mathrm{m^2},
\qquad V_*=\sqrt{\gamma RT_*}=1876.46\ \mathrm{m/s},
\]

\[
\dot m=\frac{p_*A_*V_*}{RT_*}=507.651\ \mathrm{kg/s}.
\]

### Momentum and pressure thrust

\[
F_{\rm conv}=\dot mV_*+(p_*-p_a)A_*.
\]

The momentum term is about 0.95259 MN; the pressure term is 0.71670 MN.

**Converging-nozzle thrust: 1.66929 MN.**

The pressure thrust is substantial. A sonic exit at a pressure far above ambient is not a fully expanded exhaust.

## (ii) Fully expanded converging-diverging nozzle

Set \(p_e=p_a\). With the stipulated overall efficiency,

\[
V_e=\sqrt{2\eta_n c_pT_c
\left[1-\left(\frac{p_a}{p_c}\right)^{(\gamma-1)/\gamma}\right]}
=4440.17\ \mathrm{m/s}.
\]

The question fixes the same throat flow, \(\dot m=507.651\ \mathrm{kg/s}\). The exit pressure-thrust term is now zero:

\[
F_{\rm CD}=\dot mV_e=2.25406\ \mathrm{MN}.
\]

\[
\%\,\text{increase}
=100\left(\frac{F_{\rm CD}}{F_{\rm conv}}-1\right)=35.031\%.
\]

**Yes: the CD nozzle gives about 2.254 MN, a 35.0% increase.**

A geometry check gives

\[
T_e=T_c-\frac{V_e^2}{2c_p}=1424.09\ \mathrm K,
\qquad A_e=\frac{\dot mRT_e}{p_aV_e}=13.7252\ \mathrm{m^2}.
\]

Thus \(A_e/A_*=69.90\): full expansion at this altitude requires a large exit area.

## Source check

The set quotes 1.673 MN and 2.25 MN. The results above agree within about 0.3%. Applying the ideal critical-pressure formula and then reducing exit speed by \(\sqrt{\eta_n}\) gives a slightly different, nonsonic exit state; the question instead specifies an actual sonic throat throughout. No tap-off flow fraction appears in the source, so no separate bleed penalty can be inferred.

Verification: standard-library numerical substitution; the exit states satisfy energy conservation, continuity and the sonic condition in part (i), and \(p_e=p_a\) eliminates pressure thrust in part (ii).
