# Propellers, helicopters and Froude theory

11 question/answer pairs: three examination questions followed by eight problem-set questions. Each original numbered question keeps its subparts together. No exact duplicates were found. This index contains no numerical answers.

| ID | Source | Question | Answer | Adaptation / interpretation |
|---|---|---|---|---|
| 01 | 2013 exam Q2 | [Blade lift and rotor power](question_01.md) | [Solution](answer_01.md) | Original wording and marks; supported blade mass and ideal-rotor assumptions are discussed in the answer. |
| 02 | 2014 exam Q2 | [Main torque and tail power](question_02.md) | [Solution](answer_02.md) | Original wording and marks; ideal disks and perpendicular tail-thrust arm are answer assumptions. |
| 03 | 2015 exam Q2 | [Mi-6 payload and hover ceiling](question_03.md) | [Solution](answer_03.md) | Original wording and marks; the answer adopts a density-power lapse for its ceiling estimate. The question specifies a fixed SSL-rated accessory deduction. |
| 04 | Topics 1–2 Q3D | [Three-phase propeller-drive motor](question_04.md) | [Solution](answer_04.md) | Retain balanced line voltage/current, rated shaft output and hp conversion in the body. Regulation and the source's missing power-factor multiplier are discussed in the answer. |
| 05 | Topics 5–6 Q14 | [Otto engine and static propeller](question_05.md) | [Solution](answer_05.md) | Retain the engine table, four-stroke operation and ambient air-induction convention. Keep engine/Froude parts together. |
| 06 | Topics 5–6 Q15 | [Hover fuel use and efficiencies](question_06.md) | [Solution](answer_06.md) | Retain the engine table, radius and air-induction conventions and integer atomic masses. Discuss thermal-efficiency conventions in the answer. |
| 07 | Topics 5–6 Q16D | [Drone endurance and RPM](question_07.md) | [Solution](answer_07.md) | State swept-area drag reference and stall-torque interpretation; supply disk relative speed to avoid a numerical quartic solution. |
| 08 | Topics 7–8 Q16 | [Static thrust and induced velocity](question_08.md) | [Solution](answer_08.md) | Retain blade distributions, hub radius and zero-lift angle; no integration instructions or inflow-method hints. |
| 09 | Topics 7–8 Q17 | [Turbocharged engine and Froude thrust](question_09.md) | [Solution](answer_09.md) | Retain the engine table, intercooler-outlet air induction, zero cooler pressure drop and exhaust-driven turbocharger with negligible pumping penalty. |
| 10 | Topics 7–8 Q17C | [Mi-6 problem-set variant](question_10.md) | [Solution](answer_10.md) | Same numerical givens as exam Q2, with different wording/subpart labels. Retain density-power lapse and fixed accessory allowance in the body; duplicate context stays outside the question. |
| 11 | Topics 7–8 Q19 | [Helicopter forward-flight power](question_11.md) | [Solution](answer_11.md) | Retain swept-area drag convention; quartic, formulas and trial-root interval appear only in the answer. |

Each question links to its original PDF and gives actual PDF page numbers. The problem sets' printed page numbers continue across the separate files. Question 16D precedes Question 16 because that is their source-document order.

## Reference data and answer assumptions

Students must find reference data and formulas unaided in the aide or personal cheatsheet. Questions contain no Provided-data sections, reference lookup directions, worked formulas, calculation routes or adaptation/near-duplicate notes. Essential exercise-specific conditions appear in ordinary prose before the problem-set tasks; standard ideal-rotor and no-loss assumptions remain for students to choose and report.

Reference locations below support answer checking, not question prompts. The root [MAE3405 Aide Memoire.pdf](../../MAE3405%20Aide%20Memoire.pdf) contains:

- [Tables 1–3, p. 1](../../MAE3405%20Aide%20Memoire.pdf#page=1): standard-air properties/composition, avgas properties and Earth gravity.
- [Table 5, p. 2](../../MAE3405%20Aide%20Memoire.pdf#page=2): all required atmosphere entries; interpolate adjacent rows for off-grid altitudes/densities.
- [p. 6](../../MAE3405%20Aide%20Memoire.pdf#page=6): reference temperature, knot conversion, lift/drag, gas/flow/BSFC and axial/static Froude relations; [p. 7](../../MAE3405%20Aide%20Memoire.pdf#page=7): isentropic state and compressor-efficiency relations.

Original exam wording, givens and marks and all original problem-set tables remain, including reactant/product heat capacities. Those mixture properties must not be replaced with Table 1 standard-air values. Some worked answers retain the source papers' rounded atmosphere values, explicitly noted; aide precision may change final digits. Integer-mass stoichiometry is a declared approximation, not silently updated to precise molecular weights.

The problem-set bodies retain conditions that reference material cannot determine: motor rating/line-voltage and stall-torque interpretations, air-induction conventions, turbocharger pressure-loss/pumping conditions, swept-area drag references, usable battery energy, efficiency/load boundaries and turboshaft density-power lapse with a fixed accessory allowance. Horsepower, feet and inches conversions remain where essential. The quadcopter's resultant disk speed is supplied as one ordinary given, avoiding a numerical quartic without providing the worked momentum or power relations.

All three examination questions preserve their original wording and marks without appended assumptions. Examination Q2 from 2015 gives no engine altitude characteristic, so its ceiling is underdetermined without a chosen lapse model. Answer 03 adopts power proportional to density and keeps the original fixed SSL-rated accessory deduction; the paired problem-set Question 10 states that lapse condition in its body. Both worked estimates keep the existing numerical results.

Fuel–air reference-energy conventions, ideal-disk/blade-element simplifications, oblique-flow relations/quartics, interpolation methods and calculator trial intervals appear in answers or these notes, not in questions. No additional continuous-atmosphere model is needed for the ceilings or drone density.

## Model and source checks

- Topic 3, pp. 26–27 and 37–38: the fuel–air cycle uses the reference-energy balance with different reactant and product heat capacities. The answers do not substitute the air-standard Otto shortcut.
- Topic 4, pp. 6–7: four-stroke induction uses air flow; cycle work uses the combined air/fuel mass.
- Topic 2, p. 12: altitude power requires a declared lapse model. An SSL rating alone does not determine a hover ceiling.
- Topic 2, pp. 23 and 30–31: speed-regulation and ideal DC torque–speed conventions. A brushless motor's continuous rated torque does not automatically equal stall torque.
- Topic 6, pp. 13–17: hover and oblique-flow momentum theory. Page 16 defines the exercise's drag coefficient using swept rotor area; no fuselage frontal area is inferred.
- Topic 7, pp. 12 and 24: simple static blade-element assumptions. No-inflow lift estimates and momentum-induced power estimates remain distinct approximations.

Source-answer discrepancies and unused/redundant givens are explained in the answer files, not in this index. The solutions are independently derived study aids, not official marking guides.

## Verification

From the unit folder, run:

```sh
python3 question_bank/propellers_helicopters_froude/verify.py
```

The dependency-free checker recomputes all numerical answers, checks energy/momentum residuals, solves the oblique-flow quartics and hover-ceiling balance, applies Table 5 interpolation where needed, and checks the 11-pair sequence and local links. It rejects Provided headings, question reference lookups and calculation/adaptation hints; questions have no required aide links. No external packages or plots are required.
