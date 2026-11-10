# Answer 11 — Converging-nozzle ramjet

Assume one inlet normal shock, followed by the stated nonideal subsonic diffuser; ideal combustion efficiency (unspecified in the original), 1% loss of recovered inlet **total** pressure, retained fuel mass, and a 95%-efficient converging exhaust nozzle. There is no compressor or turbine. Use the lecture's constant-property, 298 K-reference enthalpies, not an inferred Cohen-chart value.

1. **Freestream total state.**
   \[
   V_a=1.75(295.06)=516.355\ \mathrm{m/s},\qquad
   T_{01}=T_{0a}=216.65(1+0.2\cdot1.75^2)=349.348125\ \mathrm K.
   \]
   \(p_{0a}=p_a(1+0.2M_a^2)^{3.5}\). Total temperature is conserved through the shock and adiabatic diffuser, but total pressure is not.

2. **Normal shock at Mach 1.75.**
   [Aide Table 14](../../MAE3405%20Aide%20Memoire.pdf#page=8) gives the normal-shock ratios. Evaluating the same perfect-gas relations without table rounding gives \(M_d=0.6280887\) and
   \[
   p_d/p_a=3.40625,\quad \rho_d/\rho_a=2.2790698,\quad T_d/T_a=1.4945791.
   \]
   Hence \(p_d=18.64881\ \mathrm{kPa}\), \(T_d=323.80056\ \mathrm K\). Total pressure after the shock is 24.32675 kPa, a recovery ratio of 0.834565 of the freestream total pressure.

3. **Subsonic diffuser and combustor pressure.** Only the remaining subsonic dynamic head is subject to the 95% diffuser efficiency:
   \[
   p_{01}=p_d(1+0.95\cdot0.2M_d^2)^{3.5}=24.01684\ \mathrm{kPa},
   \]
   \[
   T_{03}=2200\ \mathrm K,\qquad p_{03}=0.99p_{01}=23.77667\ \mathrm{kPa}.
   \]
   Applying a subsonic ram formula directly to flight Mach 1.75 would miss the shock loss.

4. **Fuel flow from a reference-enthalpy balance.**
   \[
   (1+f)c_{pg}(2200-298)-c_{pa}(349.348125-298)=fLHV,
   \]
   \[
   f=\frac{1.148(2200-298)-1.005(349.348125-298)}{43100-1.148(2200-298)}
   =0.05210345.
   \]
   This is fuel/kg of original air. It is a constant-property approximation; no chart reading has been invented. A 98% burner efficiency would require more fuel, but is not specified for this ramjet.

5. **Converging nozzle choking.** The [aide critical-pressure relation](../../MAE3405%20Aide%20Memoire.pdf#page=7) gives \(r_*=1.918852\).
   The available ratio \(p_{03}/p_a=4.34287\) exceeds this; the exit is sonic, not fully expanded:
   \[
   T_e=\frac{2(2200)}{2.333}=1885.98371\ \mathrm K,\quad
   p_e=\frac{23.77667}{1.918852}=12.39109\ \mathrm{kPa},
   \]
   \[
   V_e=\sqrt{1.333(287)T_e}=849.42491\ \mathrm{m/s},\quad
   \rho_e=0.02289231\ \mathrm{kg/m^3}.
   \]
   Taking 1 kg/s of original air as the calculation basis,
   \[
   \frac{A_e}{\dot m_a}=\frac{(1+f)}{\rho_eV_e}=0.05410579\ \frac{\mathrm{m^2}}{\mathrm{kg/s}}.
   \]

6. **Specific thrust and TSFC.**
   \[
   F_s=(1+f)V_e-V_a+\frac{A_e}{\dot m_a}(p_e-p_a)
   =377.32788+374.20704=751.53492\ \mathrm{N\,s/kg}.
   \]
   \[
   TSFC=\frac{3600f}{F_s}=0.2495858\ \mathrm{kg/(N\,h)}
   =249.586\ \mathrm{kg/(kN\,h)}.
   \]

7. **Physical comment.** The model gives positive thrust at this operating point, but high fuel use. Nearly half of the thrust is pressure thrust from underexpanded exhaust. Omitting that term would not describe the stated converging nozzle. Shock losses limit ram-pressure recovery; a fully expanding nozzle can use more of the available pressure. These calculations do not establish flame stability or self-starting capability, and a pure ramjet cannot provide static take-off thrust.

**Source comparison:** 752 N s/kg and 0.25 kg/(N h) agree within 0.1% and 0.2%. `verify.py`, case `11`, checks the shock, post-shock diffuser, first-law fuel ratio, choking and pressure thrust independently of the printed answer.
