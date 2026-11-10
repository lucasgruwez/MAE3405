# Answer 04 — Continuity, thrust and fuel consumption

Assume steady uniform axial flow, capture area equal to intake area, negligible fuel injection momentum and exhaust pressure equal to atmospheric pressure. There is therefore no pressure-thrust term. Fuel density is not needed unless a volumetric fuel flow is requested.

1. **Read atmosphere and convert units.** Use the direct 6.5 km row in [aide Table 5](../../MAE3405%20Aide%20Memoire.pdf#page=2), without interpolation:
   \[
   T_a=245.90\ \mathrm K,\quad p_a=44034.8461\ \mathrm{Pa},\quad
   \rho_a=0.6238\ \mathrm{kg/m^3},\quad a_a=314.3579\ \mathrm{m/s}.
   \]
   \[
   V_a=0.398a_a=125.114444\ \mathrm{m/s},\quad
   V_e=950/3.6=263.88889\ \mathrm{m/s},\quad T_e=523.15\ \mathrm K.
   \]
   The source's 250⁰C typography means **250°C**, not 2500°C.

2. **Air and exhaust mass flows.** From \(\dot m=\rho VA\),
   \[
   A_i=\frac\pi4(0.300)^2=0.0706858\ \mathrm{m^2},\quad
   A_e=\frac\pi4(0.285)^2=0.0637940\ \mathrm{m^2},
   \]
   \[
   \dot m_a=0.6238(125.114444)A_i=5.516774\ \mathrm{kg/s}.
   \]
   Exhaust density must use the specified exhaust gas constant:
   \[
   \rho_e=\frac{p_a}{R_eT_e}=\frac{44034.8461}{250(523.15)}=0.336690\ \mathrm{kg/m^3},
   \quad \dot m_e=\rho_eV_eA_e=5.668014\ \mathrm{kg/s}.
   \]

3. **(a) Fuel/air ratio from mass conservation.**
   \[
   \dot m_f=\dot m_e-\dot m_a=0.151240\ \mathrm{kg/s},\qquad
   f=\frac{\dot m_f}{\dot m_a}=0.0274146\ \mathrm{kg\ fuel/kg\ air}.
   \]

4. **(b) Net thrust and TSFC.** Gross thrust is exhaust momentum plus any exit pressure force; here the latter vanishes:
   \[
   F_G=\dot m_eV_e=1495.726\ \mathrm N,\quad
   D_{ram}=\dot m_aV_a=690.228\ \mathrm N,
   \]
   \[
   F_N=F_G-D_{ram}=805.498\ \mathrm N.
   \]
   \[
   TSFC=\frac{3600\dot m_f}{F_N}=0.675936\ \mathrm{kg/(N\,h)}.
   \]
   Do not report \(\dot m_f/F_N\) in kg/(N h) without converting seconds to hours.

5. **(c) Gross thrust expended on ram drag.**
   \[
   \frac{D_{ram}}{F_G}(100)=46.1467\%.
   \]
   It is the fraction of **gross**, not net, thrust.

**Comparison with the source:** the set gives \(f=0.0279\), \(F_N=806.2\ \mathrm N\), TSFC = 0.688 kg/(N h), and 46.1%. The direct aide row gives 0.02741, 805.5 N and 0.6759. Thrust differs by 0.09%, fuel ratio by 1.74% and TSFC by 1.75%; subtracting nearly equal mass flows makes the fuel results sensitive to atmospheric rounding. The ram-drag fraction agrees to the source's precision. The source does not document its atmospheric inputs. These are not silently replaced by the printed answers.

Verification: `verify.py`, case `04`, directly checks continuity, force balance, hour conversion and ram/gross ratio using the direct aide 6500 m row.
