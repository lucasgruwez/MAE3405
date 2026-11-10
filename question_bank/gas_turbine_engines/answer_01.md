# Answer 01 — Twin-spool aft-fan engine

## Framework and assumptions

Steady, adiabatic components apart from combustion; negligible component inlet/outlet kinetic energies when using total states; no bleed, cooling, installation drag or duct pressure losses. Capture areas are the two stated inlet areas. Retain fuel mass. Generator shaft efficiency is 99%; the otherwise unspecified direct power-turbine/fan coupling is lossless. Cold and hot streams have separate nozzles.

Flow paths: core intake → compressor → burner → generator turbine → power turbine → hot nozzle; independent fan intake → fan → cold nozzle. The generator turbine powers the compressor; the power turbine powers only the fan.

1. **Freestream and captured flows.**

   \[
   V_a=0.8(299.46)=239.568\ \mathrm{m/s},\quad
   \dot m_h=\rho_aV_aA_h=49.4349\ \mathrm{kg/s},
   \quad \dot m_c=247.1743\ \mathrm{kg/s}.
   \]

   Thus the cold/core air-flow ratio is 5, not an independently prescribed FPR.

2. **Intakes and core compression.** Adiabatic intake losses reduce total pressure, not total temperature:

   Use the [aide intake relations](../../MAE3405%20Aide%20Memoire.pdf#page=7).

   \[
   T_{02}=T_{01}\left[1+\frac{15^{(\gamma_a-1)/\gamma_a}-1}{0.85}\right].
   \]

   Both intakes deliver \(T_{01}=251.704\ \mathrm K\), \(p_{01}=39.4982\ \mathrm{kPa}\). Core compressor delivery: \(T_{02}=597.525\ \mathrm K\), \(p_{02}=592.472\ \mathrm{kPa}\). Compressor specific work is \(c_{pa}(T_{02}-T_{01})=347.550\ \mathrm{kJ/kg\ of\ core\ air}\).

3. **Combustion with a common enthalpy reference.** The Topic 8 convention is essential when \(c_p\) changes:

   \[
   (1+f)c_{pg}(T_{03}-298)=c_{pa}(T_{02}-298)+f\eta_bLHV.
   \]

   With \(f=0.02\), \(\eta_b=0.98\), \(LHV=43100\ \mathrm{kJ/kg}\),
   \[
   T_{03}=1276.499\ \mathrm K,\qquad p_{03}=0.97p_{02}=574.698\ \mathrm{kPa}.
   \]
   Do not replace this balance with \((1+f)c_{pg}T_{03}-c_{pa}T_{02}=f\eta_bLHV\): that drops the reference-enthalpy offset.

4. **Generator turbine.** Its shaft work supplies only the core compressor:

   \[
   (1+f)c_{pg}(T_{03}-T_{04})=\frac{c_{pa}(T_{02}-T_{01})}{0.99}.
   \]
   \[
   T_{04}=976.692\ \mathrm K,\quad
   p_{04}=p_{03}\left[1-\frac{T_{03}-T_{04}}{0.90T_{03}}\right]^{\gamma_g/(\gamma_g-1)}
   =171.282\ \mathrm{kPa}.
   \]

5. **Power turbine and fan work.** PNPR fixes \(p_{05}=1.2p_a=31.7234\ \mathrm{kPa}\), so

   \[
   T_{05}=T_{04}\left[1-0.90\left(1-(p_{05}/p_{04})^{(\gamma_g-1)/\gamma_g}\right)\right]
   =674.508\ \mathrm K.
   \]
   \[
   \dot W_{PT}=\dot m_h(1+f)c_{pg}(T_{04}-T_{05})=17.4923\ \mathrm{MW}.
   \]

   This fixes the fan temperature rise and then its pressure ratio:
   \[
   T_{0c}=T_{01}+\frac{\dot W_{PT}}{\dot m_cc_{pa}}=322.121\ \mathrm K,
   \quad
   FPR=\left[1+0.85\left(\frac{T_{0c}}{T_{01}}-1\right)\right]^{\gamma_a/(\gamma_a-1)}=2.10996.
   \]
   Hence fan delivery \(p_{0c}=83.3394\ \mathrm{kPa}\).

6. **Check each nozzle separately.** Use the [aide nozzle efficiency, critical-pressure and sonic-temperature relations](../../MAE3405%20Aide%20Memoire.pdf#page=7), then continuity for exit area. A choked converging exit is sonic; otherwise expand to ambient pressure.

   | Stream | Nozzle ratio / critical ratio | Exit T | Exit p | Exit speed | Exit area |
   |---|---|---|---|---|---|
   | Hot | 1.200 / 1.91885: unchoked | 645.978 K | 26.4362 kPa | 255.942 m/s | 1.38163 m² |
   | Cold | 3.152 / 1.96435: choked | 268.434 K | 42.4259 kPa | 328.415 m/s | 1.36668 m² |

7. **Momentum and pressure thrust.**

   \[
   F_h=\dot m_h[(1+f)V_h-V_a]+A_h(p_h-p_a)=1.06248\ \mathrm{kN},
   \]
   \[
   F_c=\dot m_c(V_c-V_a)+A_c(p_c-p_a)=43.8136\ \mathrm{kN}.
   \]

   The cold pressure-thrust term is about 21.853 kN; it cannot be omitted. **Cruise thrust = 44.8761 kN per engine.**

Rounding: this answer retains the historical rounded exam ISA values; the aide's more precise row changes only the last reported digits.

Verification: `verify.py`, case `01`, recomputes all total states, shaft balances, nozzle states and thrust. Small thermodynamic rounding arises because the supplied \(c_p,\gamma,R\) are not exactly mutually consistent; listed nozzle sonic velocities follow the lecture convention. No official numerical exam solution was supplied. The free-spool efficiency assumption is explicit, not an extra 99% factor.
