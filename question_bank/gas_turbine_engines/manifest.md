# Gas turbine engines

13 question/answer pairs: three examination questions followed by ten problem-set questions. Each source question keeps its subparts together. No exact duplicates were found. This index contains no numerical answers.

| ID | Source | Question | Answer | Adaptation / interpretation |
|---|---|---|---|---|
| 01 | 2013 exam Q3 | [Twin-spool aft-fan](question_01.md) | [Solution](answer_01.md) | Original wording, table and marks. Capture-area and free-spool coupling assumptions appear only in the answer. |
| 02 | 2014 exam Q3 | [Aft-fan ramjet](question_02.md) | [Solution](answer_02.md) | Original wording, table and marks. Read the printed angle as 50° and apply the official shock-equation erratum. |
| 03 | 2015 exam Q3 | [Twin-spool turboprop](question_03.md) | [Solution](answer_03.md) | Original wording, table and marks. Distinguish per-engine output from whole-aircraft fuel flow. |
| 04 | Topics 1–2 Q3 | [Continuity, thrust and fuel use](question_04.md) | [Solution](answer_04.md) | Use the aide's direct atmosphere row and clarify the exhaust-temperature typography. |
| 05 | Topics 9–10 Q20 | [Ideal turbojet operating points](question_05.md) | [Solution](answer_05.md) | Replace sweeps by two specified points; define the primary nozzle geometry and compare the fully expanded alternative. |
| 06 | Topics 9–10 Q21 | [Nonideal turbojet](question_06.md) | [Solution](answer_06.md) | Replace the requested Cohen-chart estimate with a disclosed constant-property first-law approximation. |
| 07 | Topics 9–10 Q22 | [Afterburner](question_07.md) | [Solution](answer_07.md) | Restate Q21 engine data before the subparts; specify constant-property combustion, fixed gas-generator operation and afterburner efficiency. The answer defines its fuel-ratio notation. |
| 08 | Topics 9–10 Q23 | [Single-spool turboprop](question_08.md) | [Solution](answer_08.md) | Retain the source task and table. The answer states the single-spool loss and combustion conventions and records a source discrepancy. |
| 09 | Topics 9–10 Q24A | [Reheated turboprop](question_09.md) | [Solution](answer_09.md) | Retain the task; define the reheat fuel-ratio denominator and quantify the alternative in the answer. |
| 10 | Topics 9–10 Q25 | [Twin-spool turbofan](question_10.md) | [Solution](answer_10.md) | Retain the task; specify Jet A1, OPR including the fan and separate converging nozzles. |
| 11 | Topics 9–10 Q26 | [Converging-nozzle ramjet](question_11.md) | [Solution](answer_11.md) | Replace the sweep by Mach 1.75 at 20 km; state burner, hot-product and recovered-pressure conditions. |
| 12 | Topics 9–10 Q27 | [Fully expanding ramjet](question_12.md) | [Solution](answer_12.md) | Use one thrust/TSFC point; retain the Mach 1–5 geometry comparison with numerical endpoint states and hot-product conditions. The answer checks boundary choking. |
| 13 | Topics 9–10 Q28B | [Two-shock fuelled ramjet](question_13.md) | [Solution](answer_13.md) | Use aide Table 11 n-decane fuel data; retain the disclosed constant-product-property approximation. A substantial disagreement with the printed answer remains unresolved; see the solution's diagnostic calculation. |

Every question links to its source PDF and identifies the actual PDF page. The Topics 9–10 PDF has four physical pages, printed 11–14 in the combined problem set.

## Source and model checks

- Reference data: [aide Tables 1–2, cold gases and liquid fuels](../../MAE3405%20Aide%20Memoire.pdf#page=1); [Table 5, ISA](../../MAE3405%20Aide%20Memoire.pdf#page=2) ([continued](../../MAE3405%20Aide%20Memoire.pdf#page=3)); [Table 11, n-decane](../../MAE3405%20Aide%20Memoire.pdf#page=5); [conversion/reference data](../../MAE3405%20Aide%20Memoire.pdf#page=6); [component/nozzle equations](../../MAE3405%20Aide%20Memoire.pdf#page=7); [Table 14, normal shocks](../../MAE3405%20Aide%20Memoire.pdf#page=8) ([continued](../../MAE3405%20Aide%20Memoire.pdf#page=9)). Reference links and solution guidance belong in the answers and this manifest. Questions contain no reference lookups, copied equations or separate data supplements; original source tables remain intact.
- Numerical answers retain historical rounded exam ISA inputs except continuity Q3 (pair 04), which now uses the aide's direct altitude row. Small last-digit differences from using the aide's full precision elsewhere do not justify recomputing those answers.
- The aide does not supply the lumped hot-product heat capacity/ratio, an exact Cohen chart or the shock deflection-angle relation. Q26, Q27 and Q28B state the needed hot-product approximation in ordinary prose before their tasks. Shock equations and corrections appear only in the answers. In the aide's downstream shock-component relation, use the downstream normal Mach despite the printed numerator label; this agrees with the 2014 erratum.
- Exam transcriptions were checked against the original-page images. The question files preserve original bodies, tables and marks without appended assumptions; those assumptions appear in the answers. The 2014 erratum supplies the corrected oblique-shock Mach-component relations; the 2015 erratum concerns piston-engine Q1 only.
- Retain fuel mass unless the question explicitly neglects it. Shaft efficiencies affect transferred work; turbine isentropic efficiencies determine temperature/pressure relations.
- Topic 8, pp. 35–36: combustion uses a common enthalpy reference, with separate cold/hot heat capacities. The ideal Q20 exercise retains its stated equal-property approximation.
- **No exact Cohen-chart readings are claimed.** Q21 and Q22 use disclosed first-law substitutes. Q28B uses the aide's n-decane LHV without inventing a chart reading to force agreement with its printed result.
- Topic 9, pp. 25–30: use the nonideal critical-pressure ratio for converging nozzles and retain pressure thrust at choked exits. Full expansion does not imply a lossless nozzle; Q27 explicitly specifies an isentropic replacement above Mach 1.
- Topic 10, p. 6: PNPR means final turbine total pressure divided by ambient static pressure. Capture-area and otherwise missing mechanical-loss conventions appear in the answers.
- Source comparisons, numerical results and uncertainty explanations appear in answer files, not in this index. The solutions are independently derived study aids, not official marking guides.

## Verification

From the unit folder, run:

```sh
python3 question_bank/gas_turbine_engines/verify.py
```

The dependency-free script recomputes all 13 cases and checks mass/energy/shaft balances, nozzle regimes, afterburner percentages, alternative nozzle/fuel conventions, file pairing and local links. It also checks question numeric conditions, exam marks, source subparts and tables, standalone Q22 engine data, and the absence of data supplements, reference lookups and worked-equation hints. It does not require aide links in question files. Passing these checks verifies the declared models; it does not resolve the undocumented source-answer disagreement in Q28B.
