# Answer 12 — Fully expanding ramjet nozzle

Use the Q26 inlet and combustor assumptions restated in the question: normal-shock intake above Mach 1, 95% subsonic diffuser, 1% loss of recovered total pressure, ideal burner efficiency and retained fuel mass. Above Mach 1 the new C-D propelling nozzle is **isentropic**, so do not carry the previous 95% exhaust efficiency into that part of this calculation.

1. **Mach 1.75 inlet.**
   \[
   V_a=516.355\ \mathrm{m/s},\quad T_{01}=216.65(1+0.2\cdot1.75^2)=349.348125\ \mathrm K.
   \]
   Normal-shock relations give
   \[
   M_d=0.6280887,\quad p_d=18.64881\ \mathrm{kPa},\quad T_d=323.80056\ \mathrm K.
   \]
   Then
   \[
   p_{01}=p_d(1+0.95\cdot0.2M_d^2)^{3.5}=24.01684\ \mathrm{kPa},
   \quad p_{03}=0.99p_{01}=23.77667\ \mathrm{kPa}.
   \]

2. **Combustor fuel ratio at 2200 K.** Reference enthalpy gives
   \[
   f=\frac{c_{pg}(2200-298)-c_{pa}(T_{01}-298)}{LHV-c_{pg}(2200-298)}=0.05210345.
   \]
   This is the disclosed first-law approximation, not an exact Cohen-chart estimate.

3. **Fully expanded isentropic exit.** Here \(p_e=p_a\) and \(\eta_j=1\):
   \[
   T_e=2200(p_a/p_{03})^{(\gamma_g-1)/\gamma_g}=1524.39731\ \mathrm K,
   \]
   \[
   V_e=\sqrt{2c_{pg}(2200-T_e)}=1245.46528\ \mathrm{m/s}.
   \]
   The nozzle inlet/ambient ratio 4.34287 exceeds the ideal critical ratio 1.85242, so a sonic throat and supersonic exit are physically available. If required, density is 0.01251395 kg/m³ and exit area per unit air flow is 0.06750443 m²/(kg/s).

4. **Specific thrust and TSFC.** No pressure-thrust term remains at a fully expanded exit:
   \[
   F_s=(1+f)V_e-V_a=794.00332\ \mathrm{N\,s/kg},
   \qquad TSFC=\frac{3600f}{F_s}=0.2362363\ \mathrm{kg/(N\,h)}.
   \]
   Thus **specific thrust ≈ 794.0 N s/kg**, **TSFC ≈ 0.2362 kg/(N h)** (236.24 kg/(kN h)). Source values are 791 N s/kg and 0.23 kg/(N h): thrust differs by 0.38%, TSFC by 2.71%. The source provides no chart/fuel convention to remove that discrepancy; it is not silently forced to agree.

5. **Mach 1 endpoint: first check choking.** From the supplied intermediate state,
   \[
   p_{03}/p_a=9.96378/5.47488=1.81991.
   \]
   This is below both the original 95%-efficient converging-nozzle critical ratio 1.91885 and the ideal hot-gas critical ratio 1.85242. The Mach 1 boundary therefore has **no physical sonic throat** under the stated losses.

   The original converging nozzle has \(p_e=p_a\), \(T_e=1909.6277\ \mathrm K\), \(V_e=816.5138\ \mathrm{m/s}\), and exit Mach ≈ 0.9553. Its minimum area is its exit, so its physical exit/minimum-area ratio is 1; that minimum area must not be labelled \(A^*\).

   For an ideal-nozzle limiting check, the supplied pressure ratio gives
   \[
   M_e=\sqrt{\frac{2}{0.333}\{(p_{03}/p_a)^{0.333/1.333}-1\}}=0.984417,
   \]
   \[
   A_e/A^*=1.000210.
   \]
   This last number uses a **virtual** sonic reference area on the subsonic branch, not a physically choked throat. Selecting a supersonic area-Mach root would contradict the prescribed pressure ratio.

6. **Mach 5 endpoint: C-D nozzle.** Use the [aide pressure/Mach and area-ratio relations](../../MAE3405%20Aide%20Memoire.pdf#page=7). From \(p_{03}=175.95584\ \mathrm{kPa}\), \(p_a=5.47488\ \mathrm{kPa}\),
   \[
   M_e=\sqrt{\frac{2}{\gamma_g-1}\left[(p_{03}/p_a)^{(\gamma_g-1)/\gamma_g}-1\right]}=2.878354.
   \]
   \[
   \frac{A_e}{A_t}=\frac{1}{M_e}\left[\frac{2}{\gamma_g+1}\left(1+\frac{\gamma_g-1}{2}M_e^2\right)\right]^{(\gamma_g+1)/(2(\gamma_g-1))}
   =4.22037,
   \]
   now with \(A_t=A^*\), a real sonic throat.

7. **Practicality.** The required system changes from essentially converging/unchoked at Mach 1 to a C-D nozzle with expansion ratio about 4.22 at Mach 5. A single **fixed-geometry** nozzle cannot remain fully expanded throughout this range; shocks, separation or under/overexpansion and performance penalties would occur off design. A variable-area throat/exit system can in principle serve the range, but needs substantial geometry and inlet/combustor matching. Area ratio alone does not prove that the engine supplies sufficient excess thrust to accelerate the aircraft through the entire range.

Verification: `verify.py`, case `12` and `12_endpoints`, recomputes the Mach 1.75 point, endpoint inlet losses, ideal area-Mach relations and the Mach 1 choking exception. Rounded \(c_p,\gamma,R\) account for sub-0.1% differences between sonic/energy formulations.
