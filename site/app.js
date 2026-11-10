/* Markdown-it parses the document; texmath protects all four math delimiters for KaTeX. */
function createRenderer(baseURL) {
  const md = markdownit({ html: false, linkify: false }).use(texmath, {
    engine: katex,
    delimiters: ['dollars', 'brackets'],
    katexOptions: { throwOnError: false, strict: 'ignore', trust: false },
  });

  md.renderer.rules.link_open = (tokens, index, options, env, renderer) => {
    const token = tokens[index];
    token.attrSet('href', new URL(token.attrGet('href'), env.source).href);
    token.attrSet('target', '_blank');
    token.attrSet('rel', 'noopener noreferrer');
    return renderer.renderToken(tokens, index, options);
  };
  const image = md.renderer.rules.image;
  md.renderer.rules.image = (tokens, index, options, env, renderer) => {
    const token = tokens[index];
    token.attrSet('src', new URL(token.attrGet('src'), env.source).href);
    return image(tokens, index, options, env, renderer);
  };

  // Dollar display math also works inside list paragraphs without a preceding blank line.
  return (text, sourcePath) => md.render(
    text.replace(/\\\[([\s\S]*?)\\\]/g, (_, tex) => '$$' + tex + '$$'),
    { source: new URL(sourcePath, baseURL) },
  );
}

function questionInSequence(bank, currentId, topic, step = 1) {
  const pool = bank.filter(q => topic === 'all' || q.topic === topic);
  const index = pool.findIndex(q => q.id === currentId);
  return pool[(index + step + pool.length) % pool.length];
}

function start() {
  const get = id => document.getElementById(id);
  try {
    const bank = window.QUESTION_BANK;
    if (!Array.isArray(bank) || !bank.length) throw new Error('Question data is missing. Run python3 site/build.py.');
    if (typeof markdownit !== 'function' || typeof texmath !== 'function' || typeof katex !== 'object') {
      throw new Error('The Markdown or math renderer could not load. Check your internet connection and reload.');
    }
    const render = createRenderer(document.baseURI);
    const filter = get('topic-filter');
    const input = get('question-input');
    const answer = get('answer');
    const toggle = get('answer-toggle');
    let current;

    for (const [topic, label] of new Map(bank.map(q => [q.topic, q.topicLabel]))) {
      filter.add(new Option(label, topic));
    }
    input.max = Math.max(...bank.map(q => q.id));

    function show(question, focus = false) {
      current = question;
      if (filter.value !== 'all' && filter.value !== question.topic) filter.value = 'all';
      get('question-number').textContent = `Question ${question.id}`;
      get('question-topic').textContent = question.topicLabel;
      get('question-title').textContent = question.title;
      get('question-content').innerHTML = render(question.question, question.questionPath);
      get('answer-content').replaceChildren();
      answer.hidden = true;
      toggle.textContent = 'Show Answer';
      toggle.setAttribute('aria-expanded', 'false');
      input.value = question.id;
      input.setCustomValidity('');
      history.replaceState(null, '', `#${question.id}`);
      if (focus) {
        get('question-number').focus({ preventScroll: true });
        window.scrollTo(0, 0);
      }
    }

    function randomQuestion() {
      const pool = bank.filter(q => (filter.value === 'all' || q.topic === filter.value) && q.id !== current?.id);
      show(pool[Math.floor(Math.random() * pool.length)], Boolean(current));
    }

    toggle.addEventListener('click', () => {
      if (answer.hidden) {
        get('answer-content').innerHTML = render(current.answer, current.answerPath);
      }
      answer.hidden = !answer.hidden;
      toggle.textContent = answer.hidden ? 'Show Answer' : 'Hide Answer';
      toggle.setAttribute('aria-expanded', String(!answer.hidden));
    });
    get('previous-question').addEventListener('click', () => {
      show(questionInSequence(bank, current.id, filter.value, -1), true);
    });
    get('next-question').addEventListener('click', () => {
      show(questionInSequence(bank, current.id, filter.value), true);
    });
    get('random-question').addEventListener('click', randomQuestion);
    filter.addEventListener('change', randomQuestion);
    input.addEventListener('input', () => input.setCustomValidity(''));
    get('jump-form').addEventListener('submit', event => {
      event.preventDefault();
      const question = bank.find(q => q.id === Number(input.value));
      if (input.checkValidity() && question) show(question, true);
      else {
        input.setCustomValidity(`Enter a whole question number from 1 to ${input.max}.`);
        input.reportValidity();
      }
    });
    window.addEventListener('hashchange', () => {
      const question = bank.find(q => String(q.id) === location.hash.slice(1));
      if (question && question.id !== current.id) show(question, true);
    });

    const requested = bank.find(q => String(q.id) === location.hash.slice(1));
    if (requested) show(requested);
    else randomQuestion();
    get('status').hidden = true;
    get('practice').hidden = false;
  } catch (error) {
    get('status').textContent = error.message;
  }
}

if (typeof document !== 'undefined') start();
