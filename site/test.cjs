// No package install: node site/test.cjs [optional directory of cached CDN scripts]
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

async function main() {
  const root = path.resolve(__dirname, '..');
  const context = vm.createContext({ URL, console });
  vm.runInContext('window = globalThis', context);
  const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
  const navigation = html.match(/<div class="question-navigation">([\s\S]*?)<\/div>/)[1];
  for (const id of ['topic-filter', 'previous-question', 'next-question', 'random-question', 'jump-form', 'question-input']) {
    assert(navigation.includes(`id="${id}"`), `${id} must be in the top navigation`);
  }
  assert(html.indexOf(navigation) < html.indexOf('id="question-content"'));
  for (const [id, label, icon] of [
    ['previous-question', 'Previous Question', 'm15 18-6-6 6-6'],
    ['next-question', 'Next Question', 'm9 18 6-6-6-6'],
  ]) {
    const button = html.match(new RegExp(`<button id="${id}"[^>]*>[\\s\\S]*?<\\/button>`))[0];
    assert(button.includes(`aria-label="${label}"`) && button.includes(`title="${label}"`));
    assert(button.includes(`d="${icon}"`) && button.includes('aria-hidden="true"'));
  }
  const controls = html.match(/<div class="controls">([\s\S]*?)<\/div>/)[1];
  assert(controls.includes('id="answer-toggle"') && !controls.includes('id="next-question"'));
  assert(html.indexOf(controls) > html.indexOf('id="question-content"'));
  const urls = [...html.matchAll(/<script defer src="(https:[^"]+)"/g)].map(match => match[1]);
  for (const url of urls) {
    let source;
    if (process.argv[2]) source = fs.readFileSync(path.join(process.argv[2], path.basename(new URL(url).pathname)), 'utf8');
    else {
      const response = await fetch(url);
      assert(response.ok, `${url}: ${response.status}`);
      source = await response.text();
    }
    vm.runInContext(source, context, { filename: url });
  }
  for (const file of ['site/questions.js', 'site/app.js']) {
    vm.runInContext(fs.readFileSync(path.join(root, file), 'utf8'), context, { filename: file });
  }
  const bank = context.QUESTION_BANK;
  assert.equal(bank.length, 44);
  assert.deepEqual(Array.from(bank, q => q.id), Array.from({ length: 44 }, (_, i) => i + 1));
  assert.equal(context.questionInSequence(bank, 1, 'all').id, 2);
  assert.equal(context.questionInSequence(bank, 15, 'all').id, 16);
  assert.equal(context.questionInSequence(bank, 44, 'all').id, 1);
  assert.equal(context.questionInSequence(bank, 1, 'all', -1).id, 44);
  assert.equal(context.questionInSequence(bank, 16, 'all', -1).id, 15);
  for (const topic of new Set(bank.map(q => q.topic))) {
    const pool = bank.filter(q => q.topic === topic);
    for (let i = 0; i < pool.length; i++) {
      assert.equal(context.questionInSequence(bank, pool[i].id, topic).id, pool[(i + 1) % pool.length].id);
      assert.equal(context.questionInSequence(bank, pool[i].id, topic, -1).id, pool[(i - 1 + pool.length) % pool.length].id);
    }
  }
  let mathCount = 0;
  const renderToString = context.katex.renderToString;
  context.katex.renderToString = (tex, options) => {
    mathCount++;
    return renderToString(tex, { ...options, throwOnError: true });
  };
  const render = context.createRenderer('https://example.test/MAE3405/');
  let expectedMath = 0;
  let tables = 0;
  for (const question of bank) {
    assert(!/^#{1,6}\s+Provided\b/im.test(question.question), `${question.id}: no provided-data section`);
    assert(!question.question.includes('MAE3405%20Aide%20Memoire.pdf'), `${question.id}: no reference-location hints`);
    assert(!/^[-*]?\s*Adaptation\s*[:/]/im.test(question.question), `${question.id}: adaptation notes belong in the answer`);
    for (const kind of ['question', 'answer']) {
      const source = question[kind];
      const output = render(source, question[`${kind}Path`]);
      assert(!output.includes('katex-error') && !output.includes('ParseError'), `${question.id} ${kind}: math error`);
      expectedMath += (source.match(/\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\$\$[\s\S]*?\$\$|\$[^\n$]+\$/g) || []).length;
      tables += (output.match(/<table>/g) || []).length;
      if (source.includes('MAE3405%20Aide%20Memoire.pdf')) {
        assert(output.includes('href="https://example.test/MAE3405/MAE3405%20Aide%20Memoire.pdf'), `${question.id}: aide link`);
      }
    }
  }
  assert.equal(mathCount, expectedMath, 'Every math expression must reach KaTeX');
  assert(tables > 20, 'Markdown tables must render');
  const unsafe = render('<script>alert(1)</script>\n\n[bad](javascript:alert(1))', bank[0].questionPath);
  assert(!unsafe.includes('<script>') && !unsafe.includes('href="javascript:'), 'Raw HTML and unsafe links must not execute');
  const localRender = context.createRenderer('file:///unit/index.html');
  assert(localRender('[Aide](../../MAE3405%20Aide%20Memoire.pdf#page=2)', bank[0].questionPath)
    .includes('href="file:///unit/MAE3405%20Aide%20Memoire.pdf#page=2"'));
  console.log(`PASS: 44 pairs, ${mathCount} KaTeX expressions, ${tables} tables, Lucide buttons, forward/back navigation/topic wraparound, subpath/file links and safe Markdown rendering.`);
}

main().catch(error => { console.error(error); process.exitCode = 1; });
