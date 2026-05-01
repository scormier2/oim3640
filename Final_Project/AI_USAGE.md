# AI Usage — Best Résumé

## How I Used AI in This Project

This document describes my use of AI tools throughout the development of Best Résumé, in accordance with course requirements for transparency.

---

## AI Tools Used

### Claude (Anthropic) — Core Product Feature
Claude is the engine of the application itself, not just a development aid. The Anthropic API (`claude-opus-4-5`) is called at runtime to power four distinct features:

1. **Bullet Polish** — The user provides raw, conversational descriptions of their experience (e.g., *"I did 286 cold calls"*). Claude transforms these into concise, action-verb-driven resume bullets with quantified impact.

2. **Full Resume Generation** — Claude assembles a complete resume from structured user input, applying MLT, CareerSpring, and Harvard OCS formatting conventions without the user needing to know those rules.

3. **Resume Scoring** — Claude evaluates a submitted resume across five dimensions (action verbs, quantification, format, relevance, and impact), returns a numeric score for each, and provides one actionable fix per category.

4. **Job Tailoring** — Claude compares a resume against a job description, identifies keyword gaps, suggests bullet rewrites, and produces a match score.

### Claude (Anthropic) — Development Assistant
I also used Claude as a coding assistant during development for:
- Debugging Flask route logic
- Structuring the JSON request/response schemas
- CSS layout troubleshooting
- Writing the initial prompt templates, which I then iterated on manually

### GitHub Copilot / VS Code AI Features
Used for autocomplete suggestions while writing repetitive HTML form structures and JavaScript event listener patterns. All suggestions were reviewed, modified, and accepted manually.

---

## What I Did Not Use AI For

- The overall product concept and resume format strategy — these came from my personal experience in MLT, CareerSpring, and Harvard OCS programs
- The decision about which scoring dimensions to use
- The aesthetic and design direction of the site (typography, color, layout)
- The actual prompt engineering — writing, testing, and refining the system prompts sent to Claude required significant manual iteration to produce high-quality resume output
- The project proposal and requirements analysis

---

## Prompt Engineering Decisions

The core skill of this project is in how Claude is instructed to behave. Each API call uses a carefully crafted prompt that:

- **Constrains the output format** (e.g., "Return ONLY the bullet points. No explanation, no preamble.")
- **References real-world standards** (MLT, Harvard OCS) to anchor Claude's style
- **Enforces specific rules** (action verb first, no "I", under 20 words, quantify everything)
- **Requests structured JSON** for scoring and tailoring endpoints, with explicit field names

Writing effective prompts required multiple iterations. Early versions produced bullets that were too long, included explanations, or didn't quantify enough. The final prompts were developed through testing with real experience descriptions.

---

## Why This Use of AI Is Appropriate

Resume writing is a domain where most people know their experience but struggle to translate it into the specific, quantified, verb-first language that hiring managers expect. This gap disproportionately affects first-generation students, career switchers, and people from underrepresented backgrounds — exactly the populations served by MLT and CareerSpring.

AI is used here not to replace human judgment but to lower the barrier to professional presentation. The user still provides all the content; Claude helps them say it in the most effective way.

---

## Honest Uncertainties

- Claude's output quality varies across prompts. Rare edge cases produce generic or overly long bullets that the user should review and edit.
- The resume scoring is Claude's assessment, not a hiring manager's — it is directionally useful but not a guarantee of real-world outcomes.
- Prompt templates were tuned on a limited set of test cases. Unusual industries or roles may produce less polished output.

---

*This document was written by the project author and reviewed for accuracy.*
