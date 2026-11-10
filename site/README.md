# Question website

Open [`../index.html`](../index.html) in a browser. No server, framework or package installation is needed. Internet access is required for the pinned Markdown/KaTeX CDN libraries and math fonts.

The page starts with a random question. The Lucide **previous/next chevrons** move sequentially in either direction; **Random Question** picks a different random question. All respect the selected topic, and sequential navigation wraps at either end. You can also show/hide the answer or jump to a question number. Questions omit reference-data sections and lookup hints; necessary extra parameters appear within the problem statement. Use your aide-mémoire and cheatsheet, then reveal the worked answer. The URL fragment preserves the selected question, for example `index.html#18`. Source and aide-mémoire links open in a new tab.

The two Lucide SVG icons are embedded locally, with their [ISC licence](LUCIDE-LICENSE.txt); they add no runtime dependency.

## Updating the questions

Edit the original Markdown in `question_bank/`, then rebuild the bundled data:

```sh
python3 site/build.py
```

The generated `site/questions.js` lets the page work when opened as a local file, without browser `fetch` restrictions. Do not edit it by hand. No question or answer source files are changed by the build.

## Checks

From the repository root:

```sh
python3 site/build.py --check
node site/test.cjs
```

The render check downloads the same pinned libraries and renders all 44 question/answer pairs. It checks accessible Lucide buttons, forward/back navigation and topic wraparound, the exam-style question format, every math expression, tables, source-link resolution under a hosted subpath and `file://`, and disabled raw HTML/unsafe links.

## Hosting

Publish the repository root with GitHub Pages: in **Settings → Pages**, select **Deploy from a branch**, **main**, and **/ (root)**. Keep `index.html`, `site/`, the aide-mémoire and linked source PDFs at their current relative paths. `.nojekyll` lets Pages serve the files directly; no build workflow is needed.
