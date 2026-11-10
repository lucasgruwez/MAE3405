# Answer 13 — Ramjet with an oblique/normal-shock intake

## Assumptions and limit of the answer

Use n-decane LHV = **44602 kJ/kg** from [aide Table 11](../../MAE3405%20Aide%20Memoire.pdf#page=5), fuel at the [reference temperature](../../MAE3405%20Aide%20Memoire.pdf#page=6), and [Table 1 cold-air properties](../../MAE3405%20Aide%20Memoire.pdf#page=1). Keep the lecture hot-product approximation \(c_p=1.148\ \mathrm{kJ/(kg\,K)}\), \(\gamma=1.333\), retain fuel mass, and use 95% efficiency for combustion, post-shock subsonic diffuser and fully expanding exhaust nozzle. A nonisentropic C-D nozzle can still be fully expanded: its exit pressure can equal ambient even though its exit velocity is lower than ideal. No compressor or turbine work is present.

Aide Table 11 supplies n-decane molecular weight and formation enthalpy as well as LHV. The remaining approximation is the constant-product-property combustion/nozzle model, not missing fuel thermochemistry. No exact Cohen chart or species-resolved, temperature-dependent product model is supplied.

1. **Freestream and oblique shock.**
   \[
   V_a=2.5(295.06)=737.65\ \mathrm{m/s},\qquad
   T_{01}=T_{0a}=216.65(1+0.2\cdot2.5^2)=487.4625\ \mathrm K.
   \]
   For \(\beta=30^\circ\),
   \[
   M_{n1}=2.5\sin30^\circ=1.25,
   \]
   \[
   \theta=\tan^{-1}\left[2\cot30^\circ\frac{2.5^2\sin^230^\circ-1}{2.5^2(1.4+\cos60^\circ)+2}\right]
   =7.994141^\circ.
   \]
   Normal-shock relations on the normal component give \(M_{n2}\); then
   \[
   M_2=M_{n2}/\sin(30^\circ-\theta)=2.168756.
   \]
   Use the **downstream** normal component in this relation; the aide mislabels its numerator. The [2014 erratum](../../past_exams/MAE3405%202014%20S2%20Err.PDF) gives the corrected Mach-component relations.

   Oblique-shock total-pressure recovery is 0.987057. The downstream full Mach remains supersonic, so the stated terminating normal shock is possible.

2. **Terminating normal shock.** Apply the normal-shock equations to \(M_2\), not to 1.25 a second time:
   \[
   M_3=\sqrt{\frac{1+0.2M_2^2}{1.4M_2^2-0.2}}=0.55131785.
   \]
   Its total-pressure recovery is 0.642424. Across both shocks, total temperature remains 487.4625 K. The final static and total states are
   \[
   T_3=459.52769\ \mathrm K,\quad p_3=48.24738\ \mathrm{kPa},\quad
   p_{03,\rm shocks}=59.31671\ \mathrm{kPa}.
   \]
   See [aide Table 14](../../MAE3405%20Aide%20Memoire.pdf#page=8) ([continued](../../MAE3405%20Aide%20Memoire.pdf#page=9)) for normal-shock ratios; the checker evaluates the same perfect-gas relations without table rounding.

3. **Subsonic diffuser and combustor pressure.**
   \[
   p_{01}=p_3(1+0.95\cdot0.2M_3^2)^{3.5}=58.72398\ \mathrm{kPa},
   \]
   \[
   p_{04}=0.95p_{01}=55.78778\ \mathrm{kPa}.
   \]
   The 5% burner pressure loss is a loss of recovered **total** pressure. It is not an extra normal-shock efficiency and is not 5% of \(\tfrac12\rho V^2\).

4. **Combustor outlet temperature.** With \(f=0.03\),
   \[
   (1+f)c_{pg}(T_{04}-298)=c_{pa}(T_{01}-298)+f\eta_bLHV,
   \]
   \[
   T_{04}=298+\frac{1.005(487.4625-298)+0.03(0.95)(44602)}{1.03(1.148)}
   =1534.06002\ \mathrm K.
   \]
   This retains the enthalpy-reference offset caused by changing \(c_p\). The LHV comes from the aide's decane row; the constant-product-property temperature remains an approximation, not a Cohen-chart reading.

5. **Fully expanded C-D nozzle.** The ratio \(p_{04}/p_a\approx10.19\) is ample for a choked throat and expanded supersonic exit. Use exit pressure \(p_e=p_a\) but retain nozzle efficiency:
   \[
   T_e'=T_{04}(p_a/p_{04})^{0.333/1.333},\quad
   T_e=T_{04}-0.95(T_{04}-T_e')=892.74766\ \mathrm K,
   \]
   \[
   V_e=\sqrt{2c_{pg}(T_{04}-T_e)}=1213.44682\ \mathrm{m/s}.
   \]
   The nozzle is not a sonic-exit converging nozzle; imposing \(M_e=1\) would be wrong. Exit density is 0.02136801 kg/m³ and exit area per unit air flow is 0.03972396 m²/(kg/s), if required.

6. **Specific thrust.** Pressure thrust vanishes because the exit is fully expanded:
   \[
   F_s=(1+0.03)V_e-V_a=1.03(1213.44682)-737.65
   =512.20023\ \mathrm{N\,s/kg}.
   \]
   **Specific thrust ≈ 512.2 N s/kg using aide decane LHV and the stated constant-property approximation.**

## Important source disagreement

The problem set prints **613.4 N s/kg**, about 19.8% above this computed result (our result is 16.5% below the printed value). That is not a rounding difference. With the same inlet/nozzle states and fuel mass ratio, achieving 613.4 would require a combustor total temperature about **1792.54 K**; the adopted reference-enthalpy balance would then require an effective LHV about **55.33 MJ/kg**, rather than the aide's n-decane LHV 44.602 MJ/kg. These are diagnostic back-calculations, **not alternative supplied fuel properties**.

A variable-property/chemical combustion treatment could alter flame temperature and exhaust properties. The aide supplies fuel thermochemistry, but it does not specify a species-resolved product model, temperature-dependent product enthalpies or an exact Cohen-chart reading. The printed value remains unresolved under the declared lecture-property model; do not change the tabulated fuel properties to force agreement.

Verification: `verify.py`, case `13`, recomputes both shocks, post-shock diffuser loss, reference-enthalpy burner balance using Table 11 decane LHV, nonideal fully expanded nozzle and specific thrust. The disagreement is preserved in the manifest.
