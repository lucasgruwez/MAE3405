# Answer 12 — Dynamometer performance at 2000 RPM

- Question: [question_12.md](question_12.md).
- Source: [Problem set Q10](../../problem_sets/MAE3405%20Problem%20Set%20Questions%20-%20Week%203-4.pdf#page=3), PDF page 3.

## Adaptation and assumptions

The original speed sweep/plots have been replaced by the 2000 RPM row, with **all eight requested quantities** retained. Test-cell air volume is actual volume, not standard litres. Use Avgas properties from [aide-mémoire Table 2, p.1](../../MAE3405%20Aide%20Memoire.pdf#page=1) and assume no dynamometer transmission loss or separate tare load.

## (i) Torque

$$\tau=Fr=525(0.381)=200.025\ \mathrm{N\,m}.$$

## (ii) Brake power

$$P_b=\tau\omega=200.025\frac{2\pi(2000)}{60}
=41893.14\ \mathrm{W}=41.8931\ \mathrm{kW}.$$

## Mass and swept-volume rates

$$\rho_a=\frac{101300}{287(21.1+273.15)}=1.199530\ \mathrm{kg/m^3}.$$
$$\dot V_a=\frac{1905\times10^{-3}}{60}=0.0317500\ \mathrm{m^3/s},\quad
\dot m_a=1.199530(0.0317500)=0.03808507\ \mathrm{kg/s}.$$
$$\dot m_f=\frac{0.210\times10^{-3}}{60}(708.2)=0.002478700\ \mathrm{kg/s}.$$
$$V_s=4\frac{\pi(0.0826)^2}{4}(0.102)=0.002186302\ \mathrm{m^3},$$
$$\dot V_s=V_s\frac{2000}{120}=0.03643837\ \mathrm{m^3/s}.$$

## (iii) Specific fuel consumption

$$\mathrm{BSFC}=\frac{3600(0.002478700)}{41.8931}
=0.213002\ \mathrm{kg/kWh}.$$

## (iv) BMEP

$$\mathrm{BMEP}=\frac{41.8931}{0.03643837}=1149.70\ \mathrm{kPa}.$$

## (v) Volumetric efficiency

$$\eta_v=\frac{\dot V_a}{\dot V_s}
=\frac{0.0317500}{0.03643837}=0.871334=87.13\%.$$

## (vi) Brake thermal efficiency

$$\eta_{b,th}=\frac{41.8931}{0.002478700(43700)}=0.386756=38.68\%.$$

## (vii) Air/fuel ratio

$$A/F=\frac{0.03808507}{0.002478700}=15.36494.$$

## (viii) Equivalence ratio

$$\phi=\frac{(F/A)}{(F/A)_s}=\frac{(A/F)_s}{A/F}
=\frac{14.7}{15.36494}=0.956724.$$

The mixture is slightly lean. **Results:** 200.0 N m; 41.89 kW; 0.2130 kg/kWh; 1150 kPa; 87.13%; 38.68%; A/F = 15.365; $\phi=0.9567$. These agree with the rounded published values; its 15.38 / 0.956 are minor density/rounding differences.

## Verification

Torque/power and BSFC/efficiency identities, dimensional conversions and all eight requested values recomputed. Recomputed by [verify.py](verify.py).
