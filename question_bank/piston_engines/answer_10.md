# Answer 10 — Lycoming O-360 air-standard and brake performance

- Question: [question_10.md](question_10.md).
- Source: [Problem set Q8](../../problem_sets/MAE3405%20Problem%20Set%20Questions%20-%20Week%203-4.pdf#page=2), PDF page 2.

## Adaptation and assumptions

The original engine specification table remains unavailable, including in the aide-mémoire, so the question's engine table uses a **representative replacement variant**, not a recovered transcription. All four source subparts remain; numerical results depend on this variant. Fuel properties are now available in [aide-mémoire Table 2, p.1](../../MAE3405%20Aide%20Memoire.pdf#page=1); a missing fuel appendix is no longer a blocker. It does not invent a claim that its engine data were found in the lecture notes. Assume four-stroke operation, constant air $\gamma=1.4$, and volumetric efficiency defined against ambient air. Mechanical efficiency is unnecessary because measured brake powers are given. Use air properties from [Table 1, p.1](../../MAE3405%20Aide%20Memoire.pdf#page=1) and SSL air density from [Table 5, p.2](../../MAE3405%20Aide%20Memoire.pdf#page=2). Topic 3, PDF pp.7–13 and Topic 4, PDF pp.7–21 cover efficiency, displacement and flow definitions.

## (i) Air-standard efficiency

$$\eta_{AS}=1-r^{1-\gamma}=1-8.5^{-0.4}=0.575153=57.52\%.$$

This is an ideal air-standard value, not the real engine's fuel-air or brake efficiency.

## (ii) Clearance per cylinder

Since $r=(V_c+V_{s,cyl})/V_c$,

$$V_c=\frac{V_s/4}{r-1}=\frac{5.90/4}{8.5-1}
=0.196667\ \mathrm{L/cylinder}.$$

## (iii) BMEP

For a four-stroke engine, $\dot V_s=V_sN/120$ when $N$ is in RPM. Thus

$$\dot V_{s,TO}=0.00590\frac{2700}{120}=0.132750\ \mathrm{m^3/s},$$
$$\mathrm{BMEP}_{TO}=\frac{134}{0.132750}=1009.42\ \mathrm{kPa}.$$

At cruise,

$$\dot V_{s,cr}=0.00590\frac{2400}{120}=0.118000\ \mathrm{m^3/s},$$
$$\mathrm{BMEP}_{cr}=\frac{87.1}{0.118000}=738.136\ \mathrm{kPa}.$$

A 65% power setting does not imply 65% BMEP when the RPM is different.

## (iv) Take-off brake thermal efficiency

$$\dot m_a=\rho_a\eta_v\dot V_{s,TO}
=1.225(0.85)(0.132750)=0.13822594\ \mathrm{kg/s},$$
$$\dot m_f=\frac{0.13822594}{14.7}=0.009403125\ \mathrm{kg/s},$$
$$\eta_{b,th}=\frac{134}{0.009403125(43700)}=0.326100=32.61\%.$$

**Results for the replacement variant: 57.52%; 0.1967 L/cylinder; BMEP 1009 kPa and 738 kPa; brake efficiency 32.61%.**

The printed answers are 57.2%, 0.197 L, 944/758 kPa and 30.6%. Clearance agrees, but the remaining values require other compression ratio, speed/power or fuel data. The absent original table prevents verifying which variant was intended; the original numerical answers must not be presented as verified for the replacement data.

## Verification

Clearance derived from geometric ratio; take-off/cruise BMEP recomputed at their separate speeds; fuel-energy balance checked. Missing original engine table explicitly flagged. Recomputed by [verify.py](verify.py).
