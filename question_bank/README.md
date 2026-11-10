# MAE3405 question bank

44 question/answer pairs: 9 past-exam questions and 35 problem-set exercises, organised into the four topics below.

Open the [practice website](../index.html) for random questions and revealable answers. See [website instructions](../site/README.md) for rebuilding or hosting it.

Use the [exam aide-mémoire](../MAE3405%20Aide%20Memoire.pdf) and your own cheatsheet alongside the questions. Questions contain no “Provided data” sections, reference lookup locations or worked-method hints. Necessary exercise-specific values form part of the question itself; reference guidance and modelling notes appear in the answers.

Each `question_NN.md` contains one source question with its subparts. Its matching `answer_NN.md` gives a worked solution framework, intermediate calculations and final answers. Numbering restarts in each topic.

## Topics

| Topic | Source index |
|---|---|
| [Piston engines](piston_engines/manifest.md) | [Questions and answers](piston_engines/manifest.md) |
| [Gas turbine engines](gas_turbine_engines/manifest.md) | [Questions and answers](gas_turbine_engines/manifest.md) |
| [Propellers, helicopters and Froude theory](propellers_helicopters_froude/manifest.md) | [Questions and answers](propellers_helicopters_froude/manifest.md) |
| [Rocketry](rocketry/manifest.md) | [Questions and answers](rocketry/manifest.md) |

General thermodynamics and fuel-composition exercises sit under piston engines. The electric-motor exercise sits under propellers/helicopters. Mixed piston-engine/propeller questions stay together under propellers/helicopters; turboprops sit under gas turbines.

## How to use the bank

1. Open a topic's source index and choose a question without opening its answer.
2. Work with pen, paper, a calculator, the aide-mémoire and your cheatsheet. State assumptions, show working and retain units.
3. Compare your method and intermediate values with the answer, not just the final number.

The answers are independently derived study solutions, **not official marking guides**. Where the source omits data or its printed answer conflicts with the calculation, the question states the supplied data and the answer explains the discrepancy.

## Source handling

- **Exams:** preserve the wording, numerical givens, subparts and marks, with Markdown formatting and mathematical transcription. Apply the supplied official errata. Keep interpretation notes in the answer; retain a question-specific override only where necessary to distinguish a historical input from current reference values.
- **Problem sets:** retain each numbered exercise and replace computational sweeps/plots with specified operating points. Embed genuinely necessary additional values in the problem statement or its tables, rather than in a separate data section. Students must find standard reference data and relations themselves. Record adaptations in answers and topic manifests. Printed problem-set answers appear only in answer files, where relevant.
- **Duplicates:** retain near-duplicates, including the two Mil Mi-6 exercises; omit only exact duplicates. Source numbering gaps are gaps in the supplied documents, not missing bank questions.
- **Previously missing tables:** Mars composition now comes from aide-mémoire Table 8, and formation enthalpies from Table 12. The [O-360](piston_engines/question_10.md) engine-specification table remains unavailable, so that exercise retains its labelled replacement dataset.
- **Combustion-chart approximations:** gas-turbine Q21/Q22 use a disclosed first-law substitute rather than an exact Cohen-chart reading. [Ramjet Q28B](gas_turbine_engines/question_13.md) uses the aide-mémoire's decane fuel data but still needs an explicit constant-product-property approximation; its answer flags a substantial unresolved disagreement with the printed result.
- **Historical exam values:** preserve original question givens. Where an old paper's data differ from the current aide-mémoire, identify the override or rounding convention rather than silently changing the old question.
- **Solutions:** use the question's stated property values and conventions. Rounding, fuel properties, nozzle-loss models and trajectory approximations can change the source's quoted answer.
- **Originals:** every question links to its source PDF and identifies its source question number. No source documents have been changed.

The 2014 erratum corrects the oblique-shock relations on the equation sheet. The 2015 erratum corrects Question 1 molecular-weight units to kg/kmol. Other source typos receive an explicit note rather than an undocumented correction.

## Exam reconstruction

Each supplied exam contains three numbered questions. To practise a complete paper, use:

| Paper | Piston engines | Propellers/helicopters | Gas turbines |
|---|---|---|---|
| 2013 | [Q1](piston_engines/question_01.md) | [Q2](propellers_helicopters_froude/question_01.md) | [Q3](gas_turbine_engines/question_01.md) |
| 2014 | [Q1](piston_engines/question_02.md) | [Q2](propellers_helicopters_froude/question_02.md) | [Q3](gas_turbine_engines/question_02.md) |
| 2015 | [Q1](piston_engines/question_03.md) | [Q2](propellers_helicopters_froude/question_03.md) | [Q3](gas_turbine_engines/question_03.md) |

The papers allow 3 hours of writing plus 10 minutes of reading. They require all three questions, assumptions, diagrams where needed, working, and derivations for equations not on the supplied equation sheet. Refer to the source PDF for its original equation sheet.

No rocket question appears in these three past papers; the rocketry section draws from the problem set.

Original question-page facsimiles for transcription checks: [2013](assets/exam_2013_questions.png), [2014](assets/exam_2014_questions.png), [2015](assets/exam_2015_questions.png). These contain multiple questions; use the Markdown files for individual practice.

## Verification

All four topic checkers passed. They recompute the declared numerical models using Python's standard library; the completed bank also passed sequential numbering, question/answer pairing, local-link and math-delimiter checks. Source disagreements remain flagged rather than treated as verified official answers.

To repeat the numerical checks from the unit folder:

```sh
python3 question_bank/piston_engines/verify.py
python3 question_bank/gas_turbine_engines/verify.py
python3 question_bank/propellers_helicopters_froude/verify.py
python3 question_bank/rocketry/verify.py
```
