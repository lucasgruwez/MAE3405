# Answer 06 — Nonideal turbojet

Assume steady operation, no bleed/cooling or extra duct losses, 15 kg/s **air** flow, retained fuel mass, a converging nozzle and fuel supplied at 298 K. The question replaces the source's Cohen-chart request with a constant-property combustion model; derive its fuel ratio from the first law.

1. **Intake.** Adiabatic intake losses preserve total temperature:
   \[
   T_{01}=242.65+\frac{260^2}{2(1005)}=276.28184\ \mathrm K,
   \]
   \[
   p_{01}=41060.7\left[1+0.95\frac{260^2}{2(1005)(242.65)}\right]^{3.5}
   =63.30654\ \mathrm{kPa}.
   \]

2. **Compressor.**
   \[
   T_{02}=T_{01}\left[1+\frac{9^{2/7}-1}{0.87}\right]=553.65738\ \mathrm K,\qquad
   p_{02}=9p_{01}=569.75883\ \mathrm{kPa}.
   \]
   Compressor specific work = \(1.005(T_{02}-T_{01})=278.7624\ \mathrm{kJ/kg\ air}\).

3. **Fuel ratio and combustor pressure.** For a common 298 K reference,
   \[
   (1+f)c_{pg}(1250-298)-c_{pa}(T_{02}-298)=f\eta_bLHV,
   \]
   \[
   f=\frac{1.148(1250-298)-1.005(553.65738-298)}{0.98(43100)-1.148(1250-298)}
   =0.02031737.
   \]
   This calculated approximate actual ratio includes the 98% combustion efficiency. It is **not** claimed to be a reading from the Cohen graph. \(\dot m_f=0.304761\ \mathrm{kg/s}\), \(p_{03}=0.94p_{02}=535.57330\ \mathrm{kPa}\).

4. **Turbine work and delivery pressure.**
   \[
   (1+f)c_{pg}(1250-T_{04})=\frac{c_{pa}(T_{02}-T_{01})}{0.99},
   \]
   \[
   T_{04}=1009.60698\ \mathrm K,\quad
   p_{04}=p_{03}\left[1-\frac{1250-T_{04}}{0.87(1250)}\right]^{1.333/0.333}
   =197.02852\ \mathrm{kPa}.
   \]
   Use the ideal turbine temperature drop in the pressure relation, not the actual temperature drop alone.

5. **Choking, exit state and area.** The [aide critical-pressure relation](../../MAE3405%20Aide%20Memoire.pdf#page=7) gives \(r_*=1.918852\).
   Since \(p_{04}/p_a=4.798>r_*\), the nozzle chokes:
   \[
   T_e=\frac{2T_{04}}{2.333}=865.50105\ \mathrm K,\quad
   p_e=\frac{p_{04}}{r_*}=102.68040\ \mathrm{kPa},
   \]
   \[
   V_e=\sqrt{1.333(287)T_e}=575.42645\ \mathrm{m/s},\quad
   \rho_e=\frac{p_e}{RT_e}=0.413369\ \mathrm{kg/m^3}.
   \]
   \[
   A_e=\frac{15(1+f)}{\rho_eV_e}=0.0643426\ \mathrm{m^2}.
   \]

6. **Net thrust and TSFC.**
   \[
   F_N=15[(1+f)V_e-260]+A_e(p_e-p_a)
   =4.90676+3.96477=8.87154\ \mathrm{kN}.
   \]
   \[
   TSFC=\frac{3600(0.304761)}{8.87154}=123.669\ \mathrm{kg/(kN\,h)}
   =0.123669\ \mathrm{kg/(N\,h)}.
   \]

**Source comparison:** printed area 0.0644 m² and thrust 8.86 kN agree to about 0.2%. Its printed TSFC 0.120 kg/(N h) is **120 kg/(kN h)**, not 0.120 kg/(kN h). Our approximate fuel model gives 123.67 kg/(kN h), about 3.1% higher. A different graphical fuel estimate can explain that sensitivity; no unverified Cohen reading has been invented to force the fuel consumption to match.

Verification: `verify.py`, case `06`, includes the hot mass increase, 99% shaft loss, 87% turbine efficiency, nonideal critical ratio, pressure thrust and factor-of-1000 TSFC unit conversion.
