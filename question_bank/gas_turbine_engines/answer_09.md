# Answer 09 — Reheated twin-spool turboprop

Assume capture-area flow, no bleed or extra duct losses, fuel at 298 K and retained fuel mass in both burners. The generator shaft has 99% efficiency; the free power turbine has no specified extra shaft loss beyond the gearbox. Interpret reheat ratio 0.005 relative to incoming **hot gas**, following Topic 10; the alternative initial-air denominator is quantified below.

1. **Take-off speed, air flow and intake totals.** Using the [aide knot conversion](../../MAE3405%20Aide%20Memoire.pdf#page=6),
   \[
   V_a=75(1.85)/3.6=38.54167\ \mathrm{m/s},\quad
   \dot m_a=1.225V_a(0.2)=9.442708\ \mathrm{kg/s}.
   \]
   \[
   T_{01}=288.15+V_a^2/(2c_{pa})=288.88903\ \mathrm K,
   \]
   \[
   p_{01}=101325\left[1+0.95\frac{V_a^2}{2c_{pa}(288.15)}\right]^{3.5}=102.19172\ \mathrm{kPa}.
   \]

2. **Compressor and main burner.**
   \[
   T_{02}=T_{01}\left[1+\frac{10^{2/7}-1}{0.85}\right]=605.20476\ \mathrm K,\quad p_{02}=1021.91716\ \mathrm{kPa}.
   \]
   \[
   (1+0.015)c_{pg}(T_{03}-298)=c_{pa}(T_{02}-298)+0.015(0.98)(43100),
   \]
   \[
   T_{03}=1106.69775\ \mathrm K,\qquad p_{03}=0.97p_{02}=991.25965\ \mathrm{kPa}.
   \]

3. **Generator turbine.**
   \[
   T_{04}=T_{03}-\frac{c_{pa}(T_{02}-T_{01})}{0.99(1.015)c_{pg}}=831.12027\ \mathrm K,
   \]
   \[
   p_{04}=p_{03}\left[1-\frac{T_{03}-T_{04}}{0.90T_{03}}\right]^{1.333/0.333}
   =271.07872\ \mathrm{kPa}.
   \]

4. **Reheat burner: both streams already use hot-side properties.** Let \(r=0.005\) relative to incoming hot gas:
   \[
   (1+r)c_{pg}(T_{05}-298)=c_{pg}(T_{04}-298)+r(0.98)(43100).
   \]
   \[
   T_{05}=1011.51610\ \mathrm K,\qquad p_{05}=0.98p_{04}=265.65715\ \mathrm{kPa}.
   \]
   Total fuel/original-air ratio and mass flow after reheat are
   \[
   f_{tot}=0.015+1.015(0.005)=0.020075,
   \quad \dot m_{g,2}=\dot m_a(1+f_{tot}).
   \]
   The added-fuel enthalpy is zero at the chosen reference, but its outgoing sensible enthalpy must be retained.

5. **Free power turbine and gearbox.**
   \[
   p_{06}=1.2p_a=121.590\ \mathrm{kPa},
   \]
   \[
   T_{06}=T_{05}\left[1-0.90\left(1-(p_{06}/p_{05})^{0.333/1.333}\right)\right]
   =850.05027\ \mathrm K.
   \]
   \[
   \dot W_s=0.85\dot m_a(1+f_{tot})c_{pg}(T_{05}-T_{06})=1.517645\ \mathrm{MW}.
   \]

6. **Residual jet.** The [aide critical-pressure relation](../../MAE3405%20Aide%20Memoire.pdf#page=7) gives 1.918852 for this hot nozzle. PNPR 1.2 is below it, hence the nozzle is unchoked:
   \[
   T_e=T_{06}\{1-0.95[1-(1/1.2)^{0.333/1.333}]\}=814.09458\ \mathrm K,
   \]
   \[
   V_e=\sqrt{2c_{pg}(T_{06}-T_e)}=287.32258\ \mathrm{m/s},
   \]
   \[
   F_j=\dot m_a[(1+f_{tot})V_e-V_a]=2403.631\ \mathrm N.
   \]
   Exit pressure equals ambient; no pressure thrust.

7. **Thrust power.**
   \[
   TP=0.85\dot W_s+V_aF_j=1.289998+0.092640=1.382638\ \mathrm{MW}.
   \]
   **Thrust power ≈ 1383 kW.** The source answer 1381 kW agrees within 0.12%.

**Fuel-ratio ambiguity:** if 0.005 is instead relative to original air, use \(r=0.005/1.015\) in the reheat balance, giving \(f_{tot}=0.020000\) and \(TP=1379.01\ \mathrm{kW}\). The printed 1381 kW lies between these nearby conventions. Neither interpretation warrants silently using inconsistent burner denominators.

Verification: `verify.py`, case `09`, checks reference enthalpy, two fuel mass additions, both turbine pressure/temperature relations, the free-shaft/gearbox path and unchoked exhaust. The alternate denominator is also reproducible with the supplied helper.
