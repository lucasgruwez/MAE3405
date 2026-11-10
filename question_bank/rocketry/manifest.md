# Rocketry source manifest

No rocket questions occur in the supplied 2013–2015 exam papers. All five numbered questions in the Weeks 11–12 problem set appear below. No exact duplicates were found in this topic.

Use the [exam aide-mémoire](../../MAE3405%20Aide%20Memoire.pdf) and your own cheatsheet alongside these questions. Question files contain the problem statement and necessary exercise-specific givens, with no provided-data sections, lookup locations or method hints. Reference guidance and numerical conventions remain in the answers.

| ID | Source | Question | Answer | Adaptation / source issue |
|---|---|---|---|---|
| 01 | Weeks 11–12 Q29 | [Propellant comparison](question_01.md) | [Solution](answer_01.md) | Embeds bulk mixture-density estimates and trajectory conventions in the question because the available reference data do not determine them. Planetary, atmosphere and propellant lookups are left to the student. Distinguishes vertical height from along-path distance. Source volume units have a factor-of-1000 scale error. |
| 02 | Weeks 11–12 Q30 | [Sea-level thrust and burnout](question_02.md) | [Solution](answer_02.md) | Specifies constant-effective-velocity approximation and vertical-height convention. |
| 03 | Weeks 11–12 Q31 | [Staging and payload](question_03.md) | [Solution](answer_03.md) | Identifies the omitted target as Earth escape speed without supplying its value or lookup location; defines the stage structure fraction in the question. |
| 04 | Weeks 11–12 Q33 | [Hydrogen nozzle comparison](question_04.md) | [Solution](answer_04.md) | Retains the source's formation enthalpy and states the negligible-bleed model in the question. Species properties and nozzle relations must be found by the student. Constant-cp model excludes dissociation. |
| 05 | Weeks 11–12 Q33B | [Open gas-generator motor](question_05.md) | [Solution](answer_05.md) | Embeds original fuel properties, nominal fuel molecular weight and negligible preburner-exhaust thrust in the question; standard species and nozzle data are not supplied. |

## Verification

- Recomputed the five solutions with Python's standard-library `math` functions. Run `python3 question_bank/rocketry/verify.py` from the unit folder to repeat the numerical checks.
- Checked stoichiometric, stage and propellant mass balances.
- Checked choked-nozzle continuity, energy conservation, and the actual sonic condition for Questions 04–05.
- Compared the results with the source's printed answers and documented discrepancies in the individual answers.
- Updated Questions 01, 04 and 05 to the aide-mémoire's Earth radius, gas molecular weights/heat capacities and formation data; recomputed the affected answers and checker targets.
- Read aide-mémoire PDF page 5 as an image to verify rasterised formation data. Worked answers document the reference sources; question files do not identify their locations.
- These are independently derived study solutions, not official marking guides.
