# Answer 05 — Ideal turbojet point calculations

Assume air-standard properties on both sides, no combustor pressure loss, ideal intake/compressor/turbine/nozzle and no shaft loss. Fuel supplies energy but adds negligible flowing mass, as instructed. The primary answer uses a converging propelling nozzle; the fully expanded interpretation is evaluated separately because source Q20 does not specify geometry.

1. **Intake totals.** Use the [aide intake relations](../../MAE3405%20Aide%20Memoire.pdf#page=7) with ideal efficiency and \(V_a=M_aa_a\).
   The compressor ratio 20 excludes ram compression.

2. **Compressor and turbine balances.**
   \[
   T_{02}=T_{01}(20)^{2/7},\quad p_{02}=20p_{01},\quad T_{03}=1400\ \mathrm K,
   \]
   \[
   c_p(T_{03}-T_{04})=c_p(T_{02}-T_{01}),\qquad
   p_{04}=p_{02}(T_{04}/1400)^{3.5}.
   \]

   | State/quantity | (i) Mach 0.8, 10,000 m | (ii) Mach 0.4, 5000 m |
   |---|---|---|
   | Flight speed | 239.568 m/s | 128.208 m/s |
   | \(T_{01}\) | 251.7036 K | 263.8278 K |
   | \(p_{01}\) | 40.2924 kPa | 60.3136 kPa |
   | \(T_{02}\) | 592.3963 K | 620.9310 K |
   | \(p_{02}\) | 805.8481 kPa | 1206.2718 kPa |
   | \(T_{04}\) | 1059.3073 K | 1042.8968 K |
   | \(p_{04}\) | 303.6561 kPa | 430.3697 kPa |

3. **Fuel requirement.** Equal specific heats on both sides make the common 298 K enthalpy reference cancel. Neglecting fuel mass in the flowing gas,
   \[
   fLHV=c_p(T_{03}-T_{02}),\qquad
   f=\frac{1.005(1400-T_{02})}{43100}.
   \]
   Thus \(f_i=0.01883159\), \(f_{ii}=0.01816623\) kg fuel/kg air. Including fuel energy in TSFC is consistent with neglecting its small mass in momentum and turbine balances.

4. **Converging-nozzle choking and specific thrust.**
   The [aide critical-pressure and sonic-state relations](../../MAE3405%20Aide%20Memoire.pdf#page=7), with ideal nozzle efficiency, give \(r_*=1.892929\). Actual nozzle ratios are 11.486 and 7.967: both choke. Use sonic exit states and continuity for area per unit air flow.
   \[
   F_s=V_e-V_a+\frac{A_e}{\dot m_a}(p_e-p_a),\qquad
   TSFC=\frac{3600f}{F_s}.
   \]

   | Quantity | (i) | (ii) |
   |---|---|---|
   | Exit temperature | 882.7561 K | 869.0806 K |
   | Exit pressure | 160.4160 kPa | 227.3565 kPa |
   | Exit speed | 595.5597 m/s | 590.9286 m/s |
   | Pressure contribution to \(F_s\) | 355.2949 N s/kg | 321.8028 N s/kg |
   | **Specific thrust** | **711.2866 N s/kg** | **784.5234 N s/kg** |
   | **TSFC** | **0.0953114 kg/(N h)** | **0.0833607 kg/(N h)** |

   A converging nozzle cannot isentropically expand to ambient through a sonic exit when \(p_0/p_a\) exceeds the critical ratio; retaining pressure thrust is mandatory.

5. **Alternative: ideal fully expanded C-D nozzle.** If “ideal nozzles” was intended to mean complete expansion,
   \[
   V_e=\sqrt{2c_pT_{04}[1-(p_a/p_{04})^{2/7}]},\quad
   F_s=V_e-V_a,
   \]
   with no pressure thrust. The results are:

   | Quantity | (i) | (ii) |
   |---|---|---|
   | Exit speed | 1034.0217 m/s | 968.3187 m/s |
   | **Specific thrust** | **794.4537 N s/kg** | **840.1107 N s/kg** |
   | **TSFC** | **0.0853338 kg/(N h)** | **0.0778450 kg/(N h)** |

The geometry ambiguity changes the answer materially, so neither interpretation should be passed off as the unique source answer. The set supplies no completed numerical answer for these points. `verify.py`, case `05`, checks both interpretations and both operating points; the tiny sonic energy/property rounding follows the supplied \(c_p,\gamma,R\).
