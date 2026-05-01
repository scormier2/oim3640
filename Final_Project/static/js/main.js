// Best Résumé — Main JavaScript

// Animate demo card text cycling
const beforeTexts = [
  '"I was a teaching assistant in a program for 30 admitted students and my assistance directly generated 27 of them passing"',
  '"In my role I did 286 cold calls"',
  '"I managed our social media and we got a lot more followers"',
  '"I helped onboard new employees at my company"',
];

const afterTexts = [
  'Directly created a <strong>90% success rate</strong> as a Teaching Assistant in a 30-student selective cohort',
  '<strong>286+</strong> cold calls and client engagements driving measurable pipeline growth',
  'Grew social media following <strong>40%</strong> through targeted content strategy and consistent posting cadence',
  'Streamlined onboarding for <strong>12+ new hires</strong>, reducing ramp-up time across departments',
];

let demoIndex = 0;
const beforeEl = document.getElementById('demo-before-text');
const afterEl = document.getElementById('demo-after-text');

if (beforeEl && afterEl) {
  setInterval(() => {
    demoIndex = (demoIndex + 1) % beforeTexts.length;
    beforeEl.style.opacity = '0';
    afterEl.style.opacity = '0';
    setTimeout(() => {
      beforeEl.textContent = beforeTexts[demoIndex];
      afterEl.innerHTML = afterTexts[demoIndex];
      beforeEl.style.opacity = '1';
      afterEl.style.opacity = '1';
    }, 400);
  }, 4500);

  beforeEl.style.transition = 'opacity 0.4s';
  afterEl.style.transition = 'opacity 0.4s';
}

// Smooth scroll polyfill for older browsers
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});
