# Answer 02 — Aft-fan ramjet

## Framework and assumptions

Flow: oblique shock → normal shock → subsonic diffuser → split. Core: burner → turbine → hot nozzle. Bypass: fan → cold nozzle. The turbine powers only bypass air through the aft-fan, **not** all inlet air as in a front-fan turbofan. Use the instructed negligible fuel-mass approximation; no shaft loss is specified. Combustor temperature means total temperature.

1. **Freestream and oblique shock.**

   \[
   V_a=1.7(295.06)=501.602\ \mathrm{m/s},\quad
   T_{0a}=216.65(1+0.2\cdot1.7^2)=341.8737\ \mathrm K.
   \]

   The oblique-shock deflection relation is
   \[
   \tan\theta=2\cot\beta\frac{M_1^2\sin^2\beta-1}{M_1^2(\gamma_a+\cos2\beta)+2}.
   \]
   The [2014 erratum](../../past_exams/MAE3405%202014%20S2%20Err.PDF) corrects the Mach-component relations: use the **downstream** normal component in \(M_2=M_{n2}/\sin(\beta-\theta)\), despite the aide's printed numerator label.

   With \(\beta=50^\circ\), the corrected shock equations give
   \[
   M_{n1}=1.7\sin50^\circ=1.302276,\quad
   \theta=11.89563^\circ,\quad
   M_2=\frac{M_{n2}}{\sin(50^\circ-\theta)}=1.271770.
   \]

   Normal-shock relations applied to \(M_{n1}\) give oblique-shock total-pressure recovery 0.978977. Use the **full** Mach 1.271770 at the terminating normal shock, whose recovery is 0.983952. Neither shock changes total temperature. See [aide Table 14](../../MAE3405%20Aide%20Memoire.pdf#page=8) ([continued](../../MAE3405%20Aide%20Memoire.pdf#page=9)) for normal-shock ratios; the checker evaluates the same perfect-gas relations without table rounding.

2. **Post-shock subsonic intake.** After both shocks:

   \[
   M_d=0.800693,\quad T_d=303.0199\ \mathrm K,\quad p_d=17.06535\ \mathrm{kPa},
   \quad p_{0d}=26.03130\ \mathrm{kPa}.
   \]

   Apply diffuser efficiency only to this state's remaining dynamic head:
   \[
   p_{01}=p_d[1+0.95(0.2M_d^2)]^{3.5}=25.51724\ \mathrm{kPa},\quad
   T_{01}=341.8737\ \mathrm K.
   \]
   Multiplying the freestream ideal ram ratio by 0.95 is not this efficiency definition.

3. **Aft-fan and cold nozzle.**

   \[
   T_{0c}=T_{01}\left[1+\frac{1.8^{2/7}-1}{0.85}\right]=415.4226\ \mathrm K,\qquad
   p_{0c}=1.8p_{01}=45.93103\ \mathrm{kPa}.
   \]

   Use the [aide nonideal critical-pressure ratio](../../MAE3405%20Aide%20Memoire.pdf#page=7).
   Here \(p_{0c}/p_a=8.389>r_{*,a}=1.96435\), so the cold nozzle is choked:
   \[
   T_c=\frac{2T_{0c}}{2.4}=346.1855\ \mathrm K,\quad
   p_c=23.38227\ \mathrm{kPa},\quad V_c=372.9576\ \mathrm{m/s}.
   \]
   \[
   \rho_c=\frac{p_c}{RT_c}=0.235340\ \mathrm{kg/m^3},\quad
   \dot m_c=\rho_cV_c(0.5)=43.88593\ \mathrm{kg/s}.
   \]
   Thus \(\dot m_h=\dot m_c/3=14.62864\ \mathrm{kg/s}\); total air flow = 58.51457 kg/s. Do not estimate flow from an unspecified intake area.

4. **Burner and turbine/fan balance.** Fuel mass is neglected as requested, so combustion efficiency is not needed to find thrust when \(T_{03}\) is specified:
   \[
   T_{03}=1900\ \mathrm K,\quad p_{03}=0.96p_{01}=24.49655\ \mathrm{kPa}.
   \]
   \[
   \dot m_hc_{pg}(T_{03}-T_{04})=\dot m_cc_{pa}(T_{0c}-T_{01}),
   \]
   \[
   T_{04}=1900-\frac{3(1.005)(415.4226-341.8737)}{1.148}=1706.8380\ \mathrm K.
   \]
   \[
   p_{04}=p_{03}\left[1-\frac{1900-1706.8380}{0.90(1900)}\right]^{1.333/0.333}
   =15.16076\ \mathrm{kPa}.
   \]

5. **Hot nozzle.** \(p_{04}/p_a=2.769>r_{*,g}=1.91885\): also choked.
   \[
   T_h=1463.2131\ \mathrm K,\quad p_h=7.90095\ \mathrm{kPa},\quad
   V_h=748.1864\ \mathrm{m/s}.
   \]
   From \(\dot m_h=\rho_hV_hA_h\), \(A_h=1.03921\ \mathrm{m^2}\).

6. **Thrust, including both pressure terms.**
   \[
   F_c=\dot m_c(V_c-V_a)+0.5(p_c-p_a)
   =-5.64568+8.95369=3.30801\ \mathrm{kN},
   \]
   \[
   F_h=\dot m_h(V_h-V_a)+A_h(p_h-p_a)
   =3.60720+2.52120=6.12840\ \mathrm{kN}.
   \]
   **Net cruise thrust = 9.43641 kN.** The cold exit is slower than flight speed, but its positive pressure thrust more than offsets its negative momentum contribution.

Verification: `verify.py`, case `02`; exact shock relations rather than rounded tables. The 50° reading was checked against the original page; both supplemental Mach relations match the official erratum. No official numerical exam solution supplied. Using a 500° shock angle or accelerating both core and bypass flow through this aft-fan would describe a different engine.
