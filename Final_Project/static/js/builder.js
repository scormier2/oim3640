// Best Résumé — Builder JavaScript

// ── Step Navigation ──────────────────────────────────────────
function goStep(n) {
  document.querySelectorAll('.form-step').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.nav-step').forEach(el => el.classList.remove('active'));

  const target = document.getElementById(`step-${n}`);
  if (target) target.classList.add('active');

  const navStep = document.querySelector(`.nav-step[data-step="${n}"]`);
  if (navStep) navStep.classList.add('active');

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ── Quick Polish (Sidebar) ───────────────────────────────────
const quickBtn = document.getElementById('quick-polish-btn');
const quickInput = document.getElementById('quick-raw');
const quickResult = document.getElementById('quick-result');
const quickResultText = document.getElementById('quick-result-text');

if (quickBtn) {
  quickBtn.addEventListener('click', async () => {
    const text = quickInput.value.trim();
    if (!text) return;

    quickBtn.innerHTML = '<span class="spinner"></span> Transforming...';
    quickBtn.disabled = true;

    try {
      const res = await fetch('/api/polish-bullet', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });
      const data = await res.json();
      quickResultText.textContent = data.polished || 'Error generating result.';
      quickResult.style.display = 'block';
    } catch (err) {
      quickResultText.textContent = 'Network error. Please try again.';
      quickResult.style.display = 'block';
    }

    quickBtn.innerHTML = 'Transform →';
    quickBtn.disabled = false;
  });
}

// Copy quick result
const quickCopy = document.getElementById('quick-copy');
if (quickCopy) {
  quickCopy.addEventListener('click', () => {
    navigator.clipboard.writeText(quickResultText.textContent);
    quickCopy.textContent = 'Copied!';
    setTimeout(() => quickCopy.textContent = 'Copy', 1500);
  });
}

// ── Score Resume (Sidebar) ───────────────────────────────────
const scoreBtn = document.getElementById('score-btn');
const scoreInput = document.getElementById('score-input');
const scoreResult = document.getElementById('score-result');

if (scoreBtn) {
  scoreBtn.addEventListener('click', async () => {
    const resume = scoreInput.value.trim();
    if (!resume) return;

    scoreBtn.innerHTML = '<span class="spinner"></span> Scoring...';
    scoreBtn.disabled = true;

    try {
      const res = await fetch('/api/score-resume', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ resume }),
      });
      const data = await res.json();
      renderScoreResult(data);
    } catch (err) {
      scoreResult.innerHTML = '<p style="color:#c00;font-size:.85rem">Error scoring resume.</p>';
      scoreResult.style.display = 'block';
    }

    scoreBtn.innerHTML = 'Score It →';
    scoreBtn.disabled = false;
  });
}

function renderScoreResult(data) {
  if (data.raw) {
    scoreResult.innerHTML = `<pre style="font-size:.78rem;white-space:pre-wrap">${data.raw}</pre>`;
    scoreResult.style.display = 'block';
    return;
  }

  const cats = [
    ['action_verbs', 'Action Verbs'],
    ['quantification', 'Quantification'],
    ['format', 'Format'],
    ['relevance', 'Relevance'],
    ['impact', 'Impact'],
  ];

  let html = '';
  cats.forEach(([key, label]) => {
    const item = data.scores?.[key] || {};
    const score = item.score || 0;
    const fix = item.fix || '';
    html += `
      <div class="score-row">
        <span class="score-cat">${label}</span>
        <div class="score-bar-wrap"><div class="score-bar" style="width:${score * 10}%"></div></div>
        <span class="score-num">${score}/10</span>
      </div>
      <div class="score-fix">${fix}</div>
    `;
  });

  html += `
    <div class="score-overall">Overall: ${data.overall || '?'}/10</div>
    <div class="score-topfix">💡 ${data.top_fix || ''}</div>
  `;

  scoreResult.innerHTML = html;
  scoreResult.style.display = 'block';
}

// ── Add Education Entry ──────────────────────────────────────
const addEduBtn = document.getElementById('add-edu');
const eduContainer = document.getElementById('edu-container');

if (addEduBtn) {
  addEduBtn.addEventListener('click', () => {
    const entry = document.createElement('div');
    entry.className = 'edu-entry card-entry';
    entry.innerHTML = `
      <button class="remove-entry" onclick="this.parentElement.remove()">✕</button>
      <div class="form-grid">
        <div class="form-group full"><label>Institution</label><input type="text" class="edu-school" placeholder="University Name" /></div>
        <div class="form-group"><label>Degree & Major</label><input type="text" class="edu-degree" placeholder="B.S. Major" /></div>
        <div class="form-group"><label>GPA</label><input type="text" class="edu-gpa" placeholder="3.5" /></div>
        <div class="form-group"><label>Graduation Date</label><input type="text" class="edu-grad" placeholder="May 2026" /></div>
        <div class="form-group full"><label>Honors / Coursework</label><input type="text" class="edu-honors" placeholder="..." /></div>
      </div>`;
    eduContainer.appendChild(entry);
  });
}

// ── Add Experience Entry ─────────────────────────────────────
const addExpBtn = document.getElementById('add-exp');
const expContainer = document.getElementById('exp-container');

if (addExpBtn) {
  addExpBtn.addEventListener('click', () => {
    const entry = document.createElement('div');
    entry.className = 'exp-entry card-entry';
    entry.innerHTML = `
      <button class="remove-entry" onclick="this.parentElement.remove()">✕</button>
      <div class="entry-type-tabs">
        <button class="entry-tab active" data-type="work">Work / Internship</button>
        <button class="entry-tab" data-type="leadership">Leadership / Activity</button>
      </div>
      <div class="form-grid">
        <div class="form-group"><label>Title / Role</label><input type="text" class="exp-title" placeholder="Role" /></div>
        <div class="form-group"><label>Organization</label><input type="text" class="exp-org" placeholder="Company / Org" /></div>
        <div class="form-group"><label>Location</label><input type="text" class="exp-loc" placeholder="City, State" /></div>
        <div class="form-group"><label>Dates</label><input type="text" class="exp-dates" placeholder="Jun 2024 – Aug 2024" /></div>
        <div class="form-group full"><label>What did you do? (raw — AI will transform)</label><textarea class="exp-raw" rows="3" placeholder="Describe in your own words..."></textarea></div>
        <div class="form-group full ai-zone">
          <button class="btn-ai-polish">✦ Polish with AI</button>
          <div class="polished-preview" style="display:none">
            <div class="polished-label">AI Bullets (click to use)</div>
            <div class="polished-text"></div>
            <input type="hidden" class="exp-polished" />
          </div>
        </div>
      </div>`;
    expContainer.appendChild(entry);
    attachPolishListeners(entry);
    attachTabListeners(entry);
  });
}

// ── Entry Type Tab Listeners ─────────────────────────────────
function attachTabListeners(container) {
  container.querySelectorAll('.entry-tab').forEach(tab => {
    tab.addEventListener('click', () => {
      container.querySelectorAll('.entry-tab').forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
    });
  });
}

document.querySelectorAll('.exp-entry').forEach(entry => {
  attachTabListeners(entry);
});

// ── AI Polish per Experience Entry ───────────────────────────
function attachPolishListeners(entry) {
  const btn = entry.querySelector('.btn-ai-polish');
  const rawTA = entry.querySelector('.exp-raw');
  const preview = entry.querySelector('.polished-preview');
  const polishedText = entry.querySelector('.polished-text');
  const hiddenInput = entry.querySelector('.exp-polished');

  if (!btn) return;

  btn.addEventListener('click', async () => {
    const raw = rawTA.value.trim();
    if (!raw) return;

    btn.innerHTML = '<span class="spinner"></span> Polishing...';
    btn.disabled = true;

    try {
      const res = await fetch('/api/polish-bullet', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: raw }),
      });
      const data = await res.json();
      polishedText.textContent = data.polished;
      hiddenInput.value = data.polished;
      preview.style.display = 'block';
    } catch (err) {
      polishedText.textContent = 'Error. Please try again.';
      preview.style.display = 'block';
    }

    btn.innerHTML = '✦ Polish with AI';
    btn.disabled = false;
  });

  // Click polished text to accept and copy to raw field label
  if (polishedText) {
    polishedText.addEventListener('click', () => {
      rawTA.value = polishedText.textContent;
      polishedText.style.color = '#2a7a2a';
      setTimeout(() => polishedText.style.color = '', 1000);
    });
  }
}

// Attach to initial entry
document.querySelectorAll('.exp-entry').forEach(entry => {
  attachPolishListeners(entry);
});

// ── Remove entry button style ─────────────────────────────────
const style = document.createElement('style');
style.textContent = `.remove-entry { position: absolute; top: .75rem; right: .75rem; background: none; border: none; color: #ccc; cursor: pointer; font-size: 1rem; } .remove-entry:hover { color: #c00; }`;
document.head.appendChild(style);

// ── Collect All Form Data ─────────────────────────────────────
function collectFormData() {
  const education = [];
  document.querySelectorAll('.edu-entry').forEach(e => {
    education.push({
      school: e.querySelector('.edu-school')?.value || '',
      degree: e.querySelector('.edu-degree')?.value || '',
      gpa: e.querySelector('.edu-gpa')?.value || '',
      graduation: e.querySelector('.edu-grad')?.value || '',
      honors: e.querySelector('.edu-honors')?.value || '',
    });
  });

  const experience = [];
  document.querySelectorAll('.exp-entry').forEach(e => {
    const activeTab = e.querySelector('.entry-tab.active');
    const type = activeTab ? activeTab.dataset.type : 'work';
    const polished = e.querySelector('.exp-polished')?.value;
    const raw = e.querySelector('.exp-raw')?.value || '';
    experience.push({
      type,
      title: e.querySelector('.exp-title')?.value || '',
      org: e.querySelector('.exp-org')?.value || '',
      location: e.querySelector('.exp-loc')?.value || '',
      dates: e.querySelector('.exp-dates')?.value || '',
      description: polished || raw,
    });
  });

  return {
    name: document.getElementById('full-name')?.value || '',
    email: document.getElementById('email')?.value || '',
    phone: document.getElementById('phone')?.value || '',
    linkedin: document.getElementById('linkedin')?.value || '',
    location: document.getElementById('location')?.value || '',
    education,
    experience,
    skills: {
      technical: document.getElementById('tech-skills')?.value || '',
      languages: document.getElementById('languages')?.value || '',
      certifications: document.getElementById('certs')?.value || '',
    },
  };
}

// ── Generate Resume ───────────────────────────────────────────
const generateBtn = document.getElementById('generate-btn');
const resumeOutput = document.getElementById('resume-output');
const resumeText = document.getElementById('resume-text');

if (generateBtn) {
  generateBtn.addEventListener('click', async () => {
    const data = collectFormData();

    generateBtn.innerHTML = '<span class="spinner"></span> Generating your résumé...';
    generateBtn.disabled = true;
    resumeOutput.style.display = 'none';

    try {
      const res = await fetch('/api/generate-resume', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });
      const result = await res.json();
      resumeText.textContent = result.resume || 'Error generating resume.';
      resumeOutput.style.display = 'block';
      resumeOutput.scrollIntoView({ behavior: 'smooth' });
    } catch (err) {
      resumeText.textContent = 'Network error. Please try again.';
      resumeOutput.style.display = 'block';
    }

    generateBtn.innerHTML = '✦ Generate My Résumé';
    generateBtn.disabled = false;
  });
}

// ── Copy Resume ───────────────────────────────────────────────
const copyResume = document.getElementById('copy-resume');
if (copyResume) {
  copyResume.addEventListener('click', () => {
    navigator.clipboard.writeText(resumeText.textContent);
    copyResume.textContent = 'Copied!';
    setTimeout(() => copyResume.textContent = 'Copy Text', 1800);
  });
}

// ── Tailor to Job ─────────────────────────────────────────────
const tailorBtn = document.getElementById('tailor-btn');
const tailorResult = document.getElementById('tailor-result');
const tailorContent = document.getElementById('tailor-content');

if (tailorBtn) {
  tailorBtn.addEventListener('click', async () => {
    const resume = resumeText.textContent;
    const jd = document.getElementById('job-description')?.value || '';

    if (!jd.trim()) {
      alert('Please paste a job description in Step 3 first.');
      return;
    }

    tailorBtn.innerHTML = '<span class="spinner"></span> Tailoring...';
    tailorBtn.disabled = true;

    try {
      const res = await fetch('/api/tailor-resume', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ resume, job_description: jd }),
      });
      const data = await res.json();
      renderTailorResult(data);
    } catch (err) {
      tailorContent.innerHTML = '<p>Error tailoring. Please try again.</p>';
      tailorResult.style.display = 'block';
    }

    tailorBtn.innerHTML = 'Tailor to Job →';
    tailorBtn.disabled = false;
  });
}

function renderTailorResult(data) {
  if (data.raw) {
    tailorContent.innerHTML = `<pre style="white-space:pre-wrap;font-size:.82rem">${data.raw}</pre>`;
    tailorResult.style.display = 'block';
    return;
  }

  let html = '';

  if (data.match_score) {
    html += `<div class="match-score-badge">Match Score: ${data.match_score}/10</div>`;
  }

  if (data.keywords?.length) {
    html += `<div style="margin-bottom:1rem"><strong style="font-size:.85rem">Keywords to include:</strong><div class="keyword-list" style="margin-top:.5rem">`;
    data.keywords.forEach(k => { html += `<span class="keyword-badge">${k}</span>`; });
    html += `</div></div>`;
  }

  if (data.bullet_improvements?.length) {
    html += `<div style="margin-bottom:1rem"><strong style="font-size:.85rem">Bullet Improvements:</strong>`;
    data.bullet_improvements.forEach(b => {
      html += `
        <div class="improvement-card">
          <div class="improvement-original">${b.original}</div>
          <div class="improvement-new">→ ${b.improved}</div>
          <div class="improvement-reason">${b.reason}</div>
        </div>`;
    });
    html += `</div>`;
  }

  if (data.missing_highlights?.length) {
    html += `<div style="margin-bottom:1rem"><strong style="font-size:.85rem">Missing highlights to add:</strong><ul style="margin-top:.4rem;padding-left:1.25rem;font-size:.87rem">`;
    data.missing_highlights.forEach(m => { html += `<li style="margin-bottom:.25rem">${m}</li>`; });
    html += `</ul></div>`;
  }

  tailorContent.innerHTML = html;
  tailorResult.style.display = 'block';
  tailorResult.scrollIntoView({ behavior: 'smooth' });
}

// ── Format Tabs ───────────────────────────────────────────────
document.querySelectorAll('.option-tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.option-tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
  });
});
