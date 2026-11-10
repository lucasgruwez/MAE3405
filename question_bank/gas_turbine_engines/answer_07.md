# Answer 07 — Afterburning and nozzle resizing

Keep the gas-generator operating point fixed at the stated air flow, use 98% afterburner efficiency (not separately given in the source), retain both fuel additions, and retain hot-side \(c_p\) across reheat. Each nozzle is converging. The main combustor fuel estimate is the disclosed first-law approximation, not a Cohen-chart reading.

1. **Find the dry-engine reference condition.** Use the [aide intake relations](../../MAE3405%20Aide%20Memoire.pdf#page=7) at the stated flight speed and intake efficiency.
   \[
   T_{02}=T_{01}\left[1+\frac{9^{2/7}-1}{0.87}\right],\quad p_{02}=9p_{01}.
   \]
   These give \(T_{01}=276.28184\ \mathrm K\), \(p_{01}=63.30654\ \mathrm{kPa}\), \(T_{02}=553.65738\ \mathrm K\), \(p_{02}=569.75883\ \mathrm{kPa}\).

   Using the main burner reference-enthalpy balance gives \(f_b=0.02031737\). Then
   \[
   T_{04}=1250-\frac{c_{pa}(T_{02}-T_{01})}{0.99(1+f_b)c_{pg}}=1009.60698\ \mathrm K,
   \]
   \[
   p_{04}=0.94p_{02}\left[1-\frac{1250-T_{04}}{0.87(1250)}\right]^{1.333/0.333}
   =197.02852\ \mathrm{kPa}.
   \]

2. **Dry nozzle and baseline fuel consumption.** The [aide critical-pressure relation](../../MAE3405%20Aide%20Memoire.pdf#page=7) gives \(r_*=1.918852\) at the stated efficiency and hot-gas properties.
   Dry nozzle ratio = 4.798, so
   \[
   T_{e,d}=\frac{2T_{04}}{2.333}=865.50105\ \mathrm K,\quad
   p_{e,d}=102.68040\ \mathrm{kPa},\quad V_{e,d}=575.42645\ \mathrm{m/s}.
   \]
   With \(A=\dot m RT_e/(p_eV_e)\),
   \[
   A_d=0.06434261\ \mathrm{m^2},\quad
   F_d=15[(1+f_b)V_{e,d}-260]+A_d(p_{e,d}-p_a)=8.871536\ \mathrm{kN}.
   \]
   Baseline fuel flow = 0.304761 kg/s and TSFC = 123.6695 kg/(kN h).

3. **Afterburner fuel addition.** Let \(r=\dot m_{f,AB}/\dot m_{g,\rm in}\), not fuel/initial air. Since both sides of the afterburner contain hot products,
   \[
   (1+r)c_{pg}(2000-298)-c_{pg}(T_{04}-298)=r\eta_{AB}LHV,
   \]
   \[
   r=\frac{1.148(2000-T_{04})}{0.98(43100)-1.148(2000-298)}=0.02822382.
   \]
   Fuel relative to original air and exhaust mass are therefore
   \[
   f_{tot}=f_b+(1+f_b)r=0.04911462,\quad
   \dot m_{f,tot}=15f_{tot}=0.736719\ \mathrm{kg/s},
   \quad \dot m_{e,w}=15(1+f_{tot})=15.73672\ \mathrm{kg/s}.
   \]
   Simply adding \(r\) to \(f_b\) uses inconsistent denominators.

4. **Wet nozzle.**
   \[
   p_{06}=0.97p_{04}=191.11767\ \mathrm{kPa},\quad T_{06}=2000\ \mathrm K.
   \]
   The ratio \(p_{06}/p_a=4.654>1.918852\), so it remains choked:
   \[
   T_{e,w}=1714.53065\ \mathrm K,\quad
   p_{e,w}=99.59998\ \mathrm{kPa},\quad V_{e,w}=809.89487\ \mathrm{m/s},
   \]
   \[
   A_w=\frac{15(1+f_{tot})RT_{e,w}}{p_{e,w}V_{e,w}}=0.09599607\ \mathrm{m^2}.
   \]
   \[
   F_w=15[(1+f_{tot})V_{e,w}-260]+A_w(p_{e,w}-p_a)
   =14.46463\ \mathrm{kN}.
   \]
   Wet pressure thrust = 5.61954 kN; it has not been cancelled against ram drag. Wet TSFC = 183.3569 kg/(kN h).

5. **Requested percentage increases.** Use \(100(X_w/X_d-1)\):

   | Part | Result |
   |---|---|
   | (i) Nozzle area | **49.195% increase** |
   | (ii) Net thrust | **63.045% increase** |
   | (iii) Fuel flow | **141.737% increase** |
   | (iii) TSFC | **48.264% increase** |

   Check: \(TSFC_w/TSFC_d=(\dot m_{f,w}/\dot m_{f,d})/(F_w/F_d)=2.41737/1.63045\).

**Source comparison:** 49% area and 63% thrust agree closely. The set gives 144% fuel and 50% TSFC, versus 141.7% and 48.3% here. Main-burner chart approximation, unspecified afterburner efficiency and whether added fuel mass is retained affect those figures. The source does not give enough detail to claim exact agreement; the adopted assumptions are explicit.

Verification: `verify.py`, case `07`, recomputes both nozzles and all four percentage changes, with the same dry-engine baseline rather than mixing printed and computed results.
