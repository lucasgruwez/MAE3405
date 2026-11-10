# Answer 08 — Single-spool turboprop

Use capture-area flow, steady adiabatic turbomachinery, retained fuel mass, no bleed or unlisted losses, and the Topic 10 single-spool power convention \(\dot W_s=\eta_{gb}(\dot W_t-\dot W_c/\eta_m)\). The single turbine supplies both compressor work and net shaft work; do not solve it as two independent turbine spools.

1. **Air flow and intake.**
   \[
   \dot m_a=0.7361(125)(0.1)=9.20125\ \mathrm{kg/s},
   \]
   \[
   T_{01}=255.65+\frac{125^2}{2(1005)}=263.42363\ \mathrm K,
   \]
   \[
   p_{01}=54019.9\left[1+0.93\frac{125^2}{2(1005)(255.65)}\right]^{3.5}
   =59.55824\ \mathrm{kPa}.
   \]

2. **Compressor and combustor.**
   \[
   T_{02}=T_{01}\left[1+\frac{8^{2/7}-1}{0.87}\right]=509.11835\ \mathrm K,\quad
   p_{02}=8p_{01}=476.46594\ \mathrm{kPa}.
   \]
   Common-reference combustion balance:
   \[
   f=\frac{1.148(1200-298)-1.005(T_{02}-298)}{0.98(43100)-1.148(1200-298)}=0.01998233.
   \]
   This is a first-law fuel estimate, not a graph reading. \(p_{03}=0.96p_{02}=457.40731\ \mathrm{kPa}\), \(T_{03}=1200\ \mathrm K\).

3. **Turbine exit fixed by PNPR.**
   \[
   p_{04}=1.3p_a=70.22587\ \mathrm{kPa},
   \]
   \[
   T_{04}=1200\left[1-0.90\left(1-(p_{04}/p_{03})^{0.333/1.333}\right)\right]=796.27742\ \mathrm K.
   \]

4. **Gross turbine work minus compressor work.**
   \[
   \dot W_t=\dot m_a(1+f)c_{pg}(1200-T_{04}),\quad
   \dot W_c=\dot m_ac_{pa}(T_{02}-T_{01}).
   \]
   Numerically these are approximately 4.350 MW and 2.272 MW. With the specified shaft and gearbox convention,
   \[
   \dot W_s=0.90(\dot W_t-\dot W_c/0.99)=1.849320\ \mathrm{MW}.
   \]
   This is propeller-input shaft power, not thrust power. Multiplying the gross turbine power by 0.99 instead would be a different mechanical-loss convention.

5. **Unchoked propelling nozzle.** The [aide critical-pressure relation](../../MAE3405%20Aide%20Memoire.pdf#page=7) gives \(r_*=1.918852\) at the stated efficiency and hot-gas properties.
   Since 1.3 is below this, \(p_e=p_a\), and
   \[
   T_e=T_{04}\{1-0.95[1-(1/1.3)^{0.333/1.333}]\}=748.28726\ \mathrm K,
   \]
   \[
   V_e=\sqrt{2c_{pg}(T_{04}-T_e)}=331.94190\ \mathrm{m/s},
   \quad F_j=\dot m_a[(1+f)V_e-125]=1965.156\ \mathrm N.
   \]
   There is no exit pressure thrust; ram drag is included.

6. **Total thrust power.**
   \[
   TP=0.85\dot W_s+125F_j
   =1.571922+0.245644=1.817566\ \mathrm{MW}.
   \]
   **Thrust power ≈ 1.818 MW.** This must not be confused with shaft power 1.849 MW or total thrust \(TP/125\).

**Source disagreement:** the printed answer is 1.86 MW, about 2.3% above this result. The stated first-law fuel/property model and the Topic 10 shaft-loss convention reproduce 1.818 MW; the printed figure is not an exact check. No undocumented fuel-chart reading is substituted to force agreement.

Verification: `verify.py`, case `08`. It evaluates the turbine's full pressure drop in one stage; its auxiliary `T04` field is the hypothetical generator-only state and is **not** used for this single-spool turbine. The actual final turbine state is its `T05=796.27742 K`, `p05=70.22587 kPa`.
