# Answer 13 — Altitude power and an equivalent-airspeed ceiling

- Question: [question_13.md](question_13.md).
- Source: [Problem set Q11](../../problem_sets/MAE3405%20Problem%20Set%20Questions%20-%20Week%203-4.pdf#page=3), PDF page 3.

## Adaptation and assumptions

The original plot is replaced by one power evaluation at 2000 m. The original zero-excess-power ceiling is retained. We explicitly adopt its approximate use of measured 2700 RPM power as $P_{b0}$, rather than introduce a test-weather correction. Use the supplied empirical power law and the aide-mémoire atmosphere table; no separate ISA law or supplied density bracket is needed. Do not use density-only scaling $P_b/P_{b0}=\sigma$ when the stated linear law includes friction offset.

## (i) Power at 2000 m

$$\tau=506(0.381)=192.786\ \mathrm{N\,m},$$
$$P_{b0}=192.786\frac{2\pi(2700)}{60}\frac1{1000}=54.50896\ \mathrm{kW}.$$

From [aide-mémoire Table 5, p.2](../../MAE3405%20Aide%20Memoire.pdf#page=2), $\sigma_{2000}=1.0065/1.225=0.82163265$:

$$P_b(2000)=54.50896[1.132(0.82163265)-0.132]
=43.5030\ \mathrm{kW}.$$

## (ii) Ceiling condition

Equivalent airspeed is $V_E=V\sqrt{\sigma}$, so

$$V_E=150\frac{1.85}{3.6}=77.08333\ \mathrm{m/s},\qquad V=\frac{77.08333}{\sqrt\sigma}.$$

Power available to overcome drag is $\eta_pP_b$. At a level-flight ceiling,

$$\eta_pP_b=DV.$$

Therefore the scalar equation in $\sigma$ is

$$
0.85(54.50896)(1.132\sigma-0.132)
=\frac{350(77.08333)}{1000\sqrt\sigma}.
$$

The left side increases with density while the right side decreases, so the physically relevant positive root is unique. A hand-calculation bracket in brake-power units is:

| Altitude (m) | Engine brake power available (kW) | Brake power required $DV/0.85$ (kW) |
|---|---:|---:|
| 3000 | 38.5968 | 36.8444 |
| 3500 | 36.2848 | 37.8113 |

The sign changes between these rows; bisection/interpolation gives the density ratio and altitude below. The root must use **true** airspeed on the right-hand side, not equivalent airspeed.

$$\sigma_c=0.72199005,\qquad P_b(h_c)=37.3546\ \mathrm{kW}.$$

The required density is $\rho_c=1.225\sigma_c=0.8844378$ kg/m³. Table 5 gives 0.9091 kg/m³ at 3000 m and 0.8632 kg/m³ at 3500 m. Linear interpolation gives

$$h_c=3000+500\frac{0.9091-0.8844378}{0.9091-0.8632}=3268.7\ \mathrm m.$$

Thus **ceiling $\approx$ 3.269 km**. At this point true airspeed is approximately 90.718 m/s and available thrust power equals required drag power (about 31.751 kW).

The original answer (43.5 kW at 2000 m and approximately 3250 m ceiling) is consistent with this approximation. Correcting the 21.1°C test-cell reading to standard conditions would change the SSL reference power and ceiling; that correction is deliberately excluded by the adapted question so the original intent remains clear.

## Verification

2700 RPM power, density-lapse law, scalar power-balance root and aide-mémoire density interpolation recomputed. Recomputed by [verify.py](verify.py).
