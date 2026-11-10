# Answer 08 — Fuel-air Otto efficiency and mean effective pressure

- Question: [question_08.md](question_08.md).
- Source: [Problem set Q6A](../../problem_sets/MAE3405%20Problem%20Set%20Questions%20-%20Week%203-4.pdf#page=1), PDF page 1.

## Adaptation and assumptions

Formation data are available in [aide-mémoire Table 12, p.5](../../MAE3405%20Aide%20Memoire.pdf#page=5), matching Topic 3 p.32. The question retains the effective cycle properties from Topic 3 p.39 as cycle givens. Use SSL conditions from [Table 5, p.2](../../MAE3405%20Aide%20Memoire.pdf#page=2), and $R_u$/cycle reference temperature from [reference data, p.6](../../MAE3405%20Aide%20Memoire.pdf#page=6). Retain historical integer molecular weights from [Table 1, p.1](../../MAE3405%20Aide%20Memoire.pdf#page=1) and the C₈H₁₈ entry in [Table 11, p.5](../../MAE3405%20Aide%20Memoire.pdf#page=5), with air O₂ + 3.76N₂ and complete combustion to gaseous water. Approximate gaseous isooctane with Table 12's gaseous C₈H₁₈ formation enthalpy. Use the course's **effective cycle** $c_v$ and $\gamma$, rather than forming high-temperature product properties from 298 K species data. Their rounded effective values need not exactly reproduce the independently computed initial gas constant. The six-cylinder total swept volume is already 3 L; do not multiply it by six again. No engine speed is required for a work-per-cycle MEP. Neglect residual gases and all mechanical, combustion and volumetric losses; fresh reactants fill the full BDC volume. Obtain initial charge density from the ideal-gas mixture molecular weight.

## (i) LHV and mixture ratio

$$
\mathrm{C_8H_{18}}+12.5(\mathrm{O_2}+3.76\mathrm{N_2})
\longrightarrow8\mathrm{CO_2}+9\mathrm{H_2O}+47\mathrm{N_2}.
$$
$$
a=\frac{12.5(32)+47(28)}{114}=15.0526316.
$$
$$
\mathrm{LHV}=\frac{-208.45-[8(-393.52)+9(-241.83)]}{114}
=44.8787719\ \mathrm{MJ/kg}=44878.8\ \mathrm{kJ/kg}.
$$

Topic 3 p.36 also quotes a slightly different gaseous octane heating value, using other molecular-weight/phase approximations. Table 12 and the retained historical integer molecular weights reproduce the problem's 44.88 MJ/kg. Table 11 on the same aide page is a different hydrocarbon-property dataset (n-octane); it must not silently replace the declared gas-phase fuel approximation.

## (ii) Fuel-air efficiency

With unit combustion efficiency,

$$q_H=\frac{44878.8}{15.0526316+1}=2795.7268\ \mathrm{kJ/kg\ reactants}.$$

Keep separate reactant/product heat capacities and retain the reference-energy terms:

$$T_2=T_1r^{\gamma_R-1}=288.15(9.33)^{0.327}=598.0947\ \mathrm{K},$$
$$T_3=298+\frac{2795.7268+0.8392(598.0947-298)}{1.143}
=2964.2871\ \mathrm{K},$$
$$T_4=\frac{2964.2871}{9.33^{0.259}}=1662.3441\ \mathrm{K}.$$

The compression work is 260.1056 kJ/kg and expansion work is 1488.1209 kJ/kg:

$$w_i=1.143(T_3-T_4)-0.8392(T_2-T_1)=1228.0154\ \mathrm{kJ/kg}.$$
$$\eta_{th}=\frac{1228.0154}{2795.7268}=0.439247=43.9247\%.$$

This follows the unit's reference-temperature/LHV model (Topic 3 pp. 26–27, 37–39), not a single-$c_v$ air-standard cycle or a separate exact chemical internal-energy calculation.

## (iii) Cycle MEP

At the start of compression the gas occupies the **total BDC volume**:

$$V_1=\frac{r}{r-1}V_s=\frac{9.33}{8.33}(0.003)=0.003360144\ \mathrm{m^3}.$$

The reactant mean molecular weight is

$$\overline M_R=\frac{114+12.5(32)+47(28)}{1+12.5+47}=30.247934\ \mathrm{kg/kmol},$$
$$R_R=\frac{8.314}{30.247934}=0.27486175\ \mathrm{kJ/(kg\ K)}.$$
$$m_R=\frac{p_1V_1}{R_RT_1}=0.004298744\ \mathrm{kg}.$$
$$W_i=m_Rw_i=5.278924\ \mathrm{kJ},\qquad
\mathrm{MEP}=\frac{W_i}{V_s}=1759.64\ \mathrm{kPa}=1.75964\ \mathrm{MPa}.$$

**Results: LHV 44879 kJ/kg; efficiency 43.9%; MEP 1.76 MPa.** Using swept volume instead of BDC volume to compute initial charge mass would incorrectly lower the ideal-cycle MEP. Real-engine intake-flow problems using volumetric efficiency have a different charge convention.

## Verification

Stoichiometric mass conservation, formation-enthalpy sum, reference-energy cycle work and BDC-volume MEP; reproduces all three published results. Recomputed by [verify.py](verify.py).
