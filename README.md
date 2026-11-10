# MAE3405 question bank

44 practice questions with worked answers across piston engines, gas turbines, propellers/helicopters and rocketry.

Open [index.html](index.html) locally, or use the [published site](https://lucasgruwez.github.io/MAE3405/) once GitHub Pages is enabled. Internet access is needed for the Markdown and maths renderers.

## GitHub Pages

In **Settings → Pages**, select **Deploy from a branch**, choose **main** and **/ (root)**, then save. No build workflow or package installation is needed.

## Contents

- `index.html` and `site/`: practice website, generated question data, build script and tests.
- `question_bank/`: editable Markdown questions, answers and numerical checks.
- Aide-mémoire, `past_exams/` and `problem_sets/`: references linked by the bank.

Lecture slides, assignments, cheatsheets and other coursework are intentionally excluded. Worked answers are study solutions, not official marking guides; known source discrepancies are documented in the answers.

## Updating and checking

Edit Markdown in `question_bank/`, then run:

```sh
python3 site/build.py
python3 site/build.py --check
node site/test.cjs
for check in question_bank/*/verify.py; do python3 "$check"; done
```

See [the bank overview](question_bank/README.md) and [site instructions](site/README.md).
