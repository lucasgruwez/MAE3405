# Answer 03 — Twin-spool turboprop

## Framework and assumptions

Per engine: intake → compressor → combustor → generator turbine → power turbine → nozzle. The generator drives only the compressor; the power turbine drives the propeller through the gearbox. Retain fuel mass, assume no bleed or unlisted duct losses, and use the specified intake area as capture area. The 80% efficiency is the propeller efficiency; apply it only to gearbox-output shaft power, not to residual jet thrust. No additional power-spool mechanical loss is given.

1. **Airspeed, air flow and intake totals.**
   \[
   V_a=0.6(312.27)=187.362\ \mathrm{m/s},\qquad
   \dot m_a=0.5895(187.362)(0.2)=22.08998\ \mathrm{kg/s}.
   \]
   \[
   T_{01}=T_a+\frac{V_a^2}{2c_{pa}}=260.1149\ \mathrm K,
   \quad p_{01}=p_a\left[1+0.95\frac{V_a^2}{2c_{pa}T_a}\right]^{3.5}
   =51.75619\ \mathrm{kPa}.
   \]

2. **Compressor and combustor.**
   \[
   T_{02}=T_{01}\left[1+\frac{12^{2/7}-1}{0.85}\right]=576.5178\ \mathrm K,\quad
   p_{02}=621.0742\ \mathrm{kPa}.
   \]
   Compressor specific work = 317.9849 kJ/kg air. With \(f=0.02\), the common-reference enthalpy balance is
   \[
   (1+f)c_{pg}(T_{03}-298)=c_{pa}(T_{02}-298)+f(0.98)(43100).
   \]
   It gives \(T_{03}=1258.4687\ \mathrm K\), \(p_{03}=0.97p_{02}=602.4420\ \mathrm{kPa}\). The exhaust flow is \(1.02\dot m_a\), not \(\dot m_a\).

3. **Generator turbine.**
   \[
   T_{04}=T_{03}-\frac{c_{pa}(T_{02}-T_{01})}{0.99(1+f)c_{pg}}
   =984.1665\ \mathrm K,
   \]
   \[
   p_{04}=p_{03}\left[1-\frac{T_{03}-T_{04}}{0.90T_{03}}\right]^{\gamma_g/(\gamma_g-1)}
   =198.5227\ \mathrm{kPa}.
   \]

4. **Power turbine and propeller shaft.** The nozzle pressure ratio fixes
   \[
   p_{05}=1.3p_a=53.37891\ \mathrm{kPa},
   \]
   \[
   T_{05}=T_{04}\left[1-0.90\left(1-(p_{05}/p_{04})^{(\gamma_g-1)/\gamma_g}\right)\right]
   =736.3980\ \mathrm K.
   \]
   \[
   \dot W_s=0.85\dot m_a(1.02)c_{pg}(T_{04}-T_{05})=5.447565\ \mathrm{MW}.
   \]
   The 99% generator-spool loss was already included in step 3; do not apply it to this free turbine again.

5. **Residual nozzle thrust.** The [aide critical-pressure relation](../../MAE3405%20Aide%20Memoire.pdf#page=7) gives \(r_*=1.91885\) for the stated hot-gas properties and nozzle efficiency.
   Since PNPR = 1.3, the nozzle is unchoked and fully expanded to \(p_a\):
   \[
   T_e=T_{05}\{1-0.95[1-(1/1.3)^{0.333/1.333}]\}=692.0167\ \mathrm K,
   \]
   \[
   V_e=\sqrt{2c_{pg}(T_{05}-T_e)}=319.2171\ \mathrm{m/s},
   \]
   \[
   F_j=\dot m_a[(1.02)V_e-V_a]=3053.707\ \mathrm N.
   \]
   Pressure thrust is zero; ram drag is already subtracted. Jet thrust power \(V_aF_j=0.572149\ \mathrm{MW}\).

6. **(a) Thrust power of each engine.**
   \[
   TP=0.80(5.447565)+0.572149=4.930201\ \mathrm{MW\ per\ engine}.
   \]

7. **(b) Aircraft fuel consumption: two engines.**
   \[
   \dot m_{f,\rm aircraft}=2(0.02)(22.08998)=0.883599\ \mathrm{kg/s},
   \]
   \[
   \dot V_f=\frac{0.883599}{793}\frac{\mathrm{m^3}}{\mathrm s}
   (3600)(1000)=4011.30\ \mathrm{litres/hour}.
   \]
   Per-engine fuel consumption would be 2005.65 litres/hour, but the question asks for the aircraft total.

Verification: `verify.py`, case `03`. Both spool balances, gearbox and propeller factors, unchoked nozzle, two-engine count and m³-to-litre conversion were checked. No official numerical exam solution supplied.
