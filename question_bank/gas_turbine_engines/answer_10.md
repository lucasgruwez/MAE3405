# Answer 10 — Twin-spool turbofan

Flow: intake → fan → split. Core air then passes through the HP compressor, burner, HP turbine, LP turbine and hot nozzle. Bypass air passes directly from fan to cold nozzle. The fan handles **all** air, whereas the HP compressor handles only core air. Retain fuel mass and 99% efficiency on each spool; assume no bleed or unlisted losses.

1. **Intake and fan.**
   \[
   V_a=0.8(299.46)=239.568\ \mathrm{m/s},\quad
   T_{01}=T_a+\frac{V_a^2}{2c_{pa}}=251.70365\ \mathrm K,
   \]
   \[
   p_{01}=p_a\left[1+0.95\frac{V_a^2}{2c_{pa}T_a}\right]^{3.5}=39.49816\ \mathrm{kPa}.
   \]
   \[
   T_{0f}=T_{01}\left[1+\frac{1.7^{2/7}-1}{0.90}\right]=297.48688\ \mathrm K,
   \quad p_{0f}=1.7p_{01}=67.14688\ \mathrm{kPa}.
   \]

2. **HP compressor and combustion.** OPR includes the fan, so HP compressor ratio is \(20/1.7=11.764706\):
   \[
   T_{02}=T_{0f}\left[1+\frac{(20/1.7)^{2/7}-1}{0.90}\right]=635.45236\ \mathrm K,
   \quad p_{02}=20p_{01}=789.96327\ \mathrm{kPa}.
   \]
   Using \(h=c_p(T-298)\),
   \[
   f=\frac{1.148(1300-298)-1.005(T_{02}-298)}{0.98(43100)-1.148(1300-298)}=0.01974207.
   \]
   \(p_{03}=0.96p_{02}=758.36474\ \mathrm{kPa}\). This is the lecture first-law fuel estimate, not a fabricated graph reading.

3. **HP turbine supplies only the HP compressor.**
   \[
   (1+f)c_{pg}(1300-T_{04})=\frac{c_{pa}(T_{02}-T_{0f})}{0.99}.
   \]
   \[
   T_{04}=1006.93025\ \mathrm K,\quad
   p_{04}=p_{03}\left[1-\frac{1300-T_{04}}{0.90(1300)}\right]^{1.333/0.333}
   =239.12162\ \mathrm{kPa}.
   \]

4. **LP turbine supplies the fan on total air flow.** Per unit core air, the fan handles \(1+B=5\) units of air:
   \[
   (1+f)c_{pg}(T_{04}-T_{05})=\frac{5c_{pa}(T_{0f}-T_{01})}{0.99}.
   \]
   \[
   T_{05}=808.42359\ \mathrm K,\qquad
   p_{05}=p_{04}\left[1-\frac{T_{04}-T_{05}}{0.90T_{04}}\right]^{1.333/0.333}=88.87930\ \mathrm{kPa}.
   \]
   Using only bypass fan work would understate LP turbine extraction in this front-fan architecture.

5. **Cold nozzle fixes the absolute mass flow.** Use the [aide critical-pressure and sonic-state relations](../../MAE3405%20Aide%20Memoire.pdf#page=7) for each stream. Cold \(p_{0f}/p_a=2.540>1.96435\); hot \(p_{05}/p_a=3.362>1.91885\): both choke. The sonic exit states are:

   | Quantity | Cold | Hot |
   |---|---|---|
   | Exit temperature | 247.90573 K | 693.03351 K |
   | Exit pressure | 34.18270 kPa | 46.31899 kPa |
   | Exit velocity | 315.60818 m/s | 514.91215 m/s |
   | Exit density | 0.4804386 kg/m³ | 0.2328750 kg/m³ |

   \[
   \dot m_c=\rho_cV_c(0.8)=121.30427\ \mathrm{kg/s},\quad
   \dot m_h=\dot m_c/4=30.32607\ \mathrm{kg/s}.
   \]
   Core exhaust = \((1+f)\dot m_h\). Hot nozzle area from continuity is 0.257899 m². The cold nozzle area is **not** an intake capture area.

6. **Both momentum and pressure thrusts.**
   \[
   F_c=\dot m_c(V_c-V_a)+0.8(p_c-p_a)=15.42120\ \mathrm{kN},
   \]
   \[
   F_h=\dot m_h[(1+f)V_h-V_a]+A_h(p_h-p_a)=13.78614\ \mathrm{kN}.
   \]
   Cold and hot pressure contributions are 6.19720 and 5.12776 kN respectively. Hence
   \[
   F_N=29.20734\ \mathrm{kN}.
   \]

7. **TSFC uses core fuel but total net thrust.**
   \[
   \dot m_f=f\dot m_h=0.598699\ \mathrm{kg/s},\qquad
   TSFC=\frac{3600\dot m_f}{F_N[\mathrm{kN}]}=73.7937\ \mathrm{kg/(kN\,h)}.
   \]

**Results:** net thrust ≈ **29.21 kN**, TSFC ≈ **73.79 kg/(kN h)**. The source's 29 kN and 74.1 kg/(kN h) agree within 0.8% and 0.5%, respectively; the disclosed fuel/property approximation is consistent with that tolerance.

Verification: `verify.py`, case `10`, checks OPR/FPR, separate spool loads, cold-area mass-flow inference, both choked nozzles, fuel addition and both pressure-thrust terms.
