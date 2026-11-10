# Answer 05: Kerosene–oxygen rocket with an open gas generator

[Question](question_05.md)

Use [aide-mémoire Tables 1, 5 and 12](../../MAE3405%20Aide%20Memoire.pdf) for the tabulated gas properties, ambient pressure and formation enthalpies. The fuel formation enthalpy and heat capacity remain original question givens; its nominal molecular weight remains an explicit approximation.

## 1. Balance the reaction

On a basis of 1 kmol of fuel,

\[
\mathrm{C_{12}H_{26}+18.5O_2\rightarrow12CO_2+13H_2O}.
\]

Using the aide-mémoire's gas molecular weights, the reactant mass is \(170+18.5(32.01)=762.185\ \mathrm{kg}\). The product masses are \(12(44.01)=528.12\ \mathrm{kg}\) of CO₂ and \(13(18.015)=234.195\ \mathrm{kg}\) of water vapour. The 0.130 kg basis mismatch (0.017%) comes from the nominal fuel molecular weight and rounded gas data; use the product masses for product properties.

## 2. Mixture properties

There are 25 kmol of product per 762.315 kg:

\[
M=\frac{762.315}{25}=30.4926\ \mathrm{kg/kmol},\qquad
R=\frac{8314}{30.4926}=272.656\ \mathrm{J/(kg\,K)}.
\]

\[
c_p=\frac{528.12(841.8)+234.195(1872.3)}{762.315}
=1158.386\ \mathrm{J/(kg\,K)},
\]

\[
c_v=c_p-R=885.729\ \mathrm{J/(kg\,K)},\qquad
\gamma=1.307833.
\]

Do not mole-average the mass-specific heat capacities.

## 3. Chamber temperature

The positive chemical heat release per kmol of fuel is

\[
Q_{\rm chem}=(-291000)-[12(-393520)+13(-241830)]
=7575030\ \mathrm{kJ}.
\]

The product heat-capacity sum is

\[
C_{p,P}=528.12(841.8)+234.195(1872.3)=883054.7145\ \mathrm{J/K}
\]

for the chosen reaction basis. The reactant heat-capacity sum is

\[
C_{p,R}=170(2000)+592.185(921.6)=885757.696\ \mathrm{J/K}.
\]

With \(T_{\rm in}-T_{\rm ref}=250.15-298.15=-48\ \mathrm K\),

\[
T_c=T_{\rm ref}+
\frac{\eta_cQ_{\rm chem}+C_{p,R}(T_{\rm in}-T_{\rm ref})}{C_{p,P}}
=7970.39\ \mathrm K,
\]

where \(Q_{\rm chem}\) must enter in joules. The constant-property, no-dissociation approximation causes this high temperature; a real equilibrium calculation would give different properties and temperature.

## (a) Main-nozzle thrust

Energy conservation and the actual sonic condition give

\[
T_* =\frac{2T_c}{\gamma+1}=6907.25\ \mathrm K.
\]

From the nozzle efficiency,

\[
p_*=p_c\left[1-\frac{\gamma-1}{\eta_n(\gamma+1)}\right]^{\gamma/(\gamma-1)}
=3.68079\ \mathrm{MPa}.
\]

Because \(p_a<p_*\), the converging nozzle chokes. With \(A_*=\pi(0.500)^2/4=0.196350\ \mathrm{m^2}\),

\[
V_*=\sqrt{\gamma RT_*}=1569.41\ \mathrm{m/s},
\]

\[
\dot m_{\rm main}=\frac{p_*A_*V_*}{RT_*}=602.264\ \mathrm{kg/s}.
\]

Include the pressure thrust:

\[
F=\dot m_{\rm main}V_*+(p_*-p_a)A_*
=1.66685\ \mathrm{MN}.
\]

**Thrust: 1.667 MN**, excluding any preburner-exhaust contribution.

## (b) Total propellant flow

The main flow is 95% of the total, so

\[
\dot m_{\rm total}=\frac{\dot m_{\rm main}}{0.95}
=633.962\ \mathrm{kg/s}.
\]

The diverted preburner flow is

\[
\dot m_{\rm pre}=0.05\dot m_{\rm total}=31.698\ \mathrm{kg/s}.
\]

**Total propellant flow: 634.0 kg/s.** Adding 5% of the main flow would be incorrect: the 5% is a fraction of the total.

The preburner efficiency does not enter these outputs under the stated assumptions. A calculation of preburner power, turbine work or its exhaust thrust would need further data.

## Source check

The set quotes 1.66 MN and 630.3 kg/s. These differ by less than 0.6% from this calculation, which uses the stated property table and an actual sonic exit with nozzle efficiency included in critical pressure. Do not adjust the mass flow just to match the printed result.

Verification: standard-library numerical substitution; stoichiometric atom counts, nozzle continuity and \(0.95\dot m_{\rm total}=\dot m_{\rm main}\) checked. The nominal-molecular-weight mass-rounding discrepancy is stated above rather than hidden.
