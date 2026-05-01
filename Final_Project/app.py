"""
Best Résumé - AI-Powered Resume Builder
Flask application entry point
"""

import os
from flask import Flask, render_template, request, jsonify, session
from dotenv import load_dotenv
import anthropic
import json

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-key-change-in-prod")

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# ── Routes ──────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/builder")
def builder():
    return render_template("builder.html")


@app.route("/preview")
def preview():
    return render_template("preview.html")


# ── API Endpoints ────────────────────────────────────────────────────────────

@app.route("/api/polish-bullet", methods=["POST"])
def polish_bullet():
    """
    Takes raw experience dialogue and converts it into a polished resume bullet.
    Example: "I did 286 cold calls" → "286+ cold calls driving measurable client engagement"
    """
    data = request.get_json()
    raw_text = data.get("text", "").strip()

    if not raw_text:
        return jsonify({"error": "No text provided"}), 400

    prompt = f"""You are an expert resume writer trained on MLT Fellowship, CareerSpring, and Harvard OCS resume standards.

Your ONLY job: convert raw experience dialogue into 1–3 powerful, ATS-optimized resume bullet points.

Rules:
- Start every bullet with a STRONG action verb (past tense)
- Quantify achievements whenever numbers are present (exact or approximate)
- Keep each bullet under 20 words
- Use industry-standard phrasing that hiring managers love
- Never use "I", "my", "we"
- Surface impact, not just tasks
- If multiple angles exist, provide 2–3 variants labeled Option A, Option B, Option C

Raw input: "{raw_text}"

Return ONLY the bullet point(s). No explanation, no preamble."""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}],
    )

    result = message.content[0].text.strip()
    return jsonify({"polished": result})


@app.route("/api/generate-resume", methods=["POST"])
def generate_resume():
    """
    Generates a complete, formatted resume from structured user input.
    Follows MLT / CareerSpring / Harvard format standards.
    """
    data = request.get_json()

    # Build the full resume prompt
    resume_data = json.dumps(data, indent=2)

    prompt = f"""You are an elite resume consultant with expertise in MLT Fellowship, CareerSpring, and Harvard Office of Career Services resume standards. These programs have placed thousands of candidates at top companies and graduate schools.

Generate a complete, polished resume from the following user data. Follow this EXACT format:

FORMAT RULES:
1. Header: Full Name (largest) | Phone | Email | LinkedIn | City, State
2. Education: Institution, Degree, Major, GPA (if ≥ 3.0), Graduation Date — list relevant coursework or honors
3. Experience: Role | Organization | Location | Dates → 3 bullet points per role, action verb + metric + impact
4. Leadership & Activities: Role | Organization | Dates → 1–2 bullets
5. Skills: Technical Skills | Languages | Certifications (comma-separated, no bullet points)
6. NEVER include an objective statement
7. Bullets: Start with strong action verbs, quantify everything possible, max 20 words per bullet
8. Tense: Past tense for past roles, present tense for current roles

USER DATA:
{resume_data}

Return the resume as clean, formatted plain text using pipes (|) for separators and dashes for bullets. Make it immediately copy-paste ready. Elevate every bullet to its strongest possible version."""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )

    result = message.content[0].text.strip()
    return jsonify({"resume": result})


@app.route("/api/score-resume", methods=["POST"])
def score_resume():
    """
    Scores an existing resume and gives actionable feedback.
    """
    data = request.get_json()
    resume_text = data.get("resume", "").strip()

    if not resume_text:
        return jsonify({"error": "No resume provided"}), 400

    prompt = f"""You are a senior recruiter at a Fortune 500 company who has reviewed 10,000+ resumes. Score this resume using MLT, CareerSpring, and Harvard OCS criteria.

Score each category 1–10 and give ONE specific, actionable fix per category:

1. Action Verbs (are they strong and varied?)
2. Quantification (are achievements measured?)
3. Format & Scannability (clean, consistent, ATS-friendly?)
4. Relevance (tailored language?)
5. Impact Clarity (does each bullet show WHY it mattered?)

Then give an Overall Score (average) and ONE top-priority fix.

RESUME:
{resume_text}

Return as JSON with this structure:
{{
  "scores": {{
    "action_verbs": {{"score": X, "fix": "..."}},
    "quantification": {{"score": X, "fix": "..."}},
    "format": {{"score": X, "fix": "..."}},
    "relevance": {{"score": X, "fix": "..."}},
    "impact": {{"score": X, "fix": "..."}}
  }},
  "overall": X,
  "top_fix": "..."
}}"""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=800,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = message.content[0].text.strip()
    # Strip markdown fences if present
    clean = raw.replace("```json", "").replace("```", "").strip()
    try:
        result = json.loads(clean)
    except json.JSONDecodeError:
        result = {"raw": raw}

    return jsonify(result)


@app.route("/api/tailor-resume", methods=["POST"])
def tailor_resume():
    """
    Tailors a resume to a specific job description.
    """
    data = request.get_json()
    resume_text = data.get("resume", "").strip()
    job_description = data.get("job_description", "").strip()

    if not resume_text or not job_description:
        return jsonify({"error": "Resume and job description required"}), 400

    prompt = f"""You are an expert resume tailoring specialist. A candidate needs their resume optimized for a specific job.

Tasks:
1. Identify the top 5 keywords/skills from the job description that should appear in the resume
2. Suggest which existing bullets to strengthen and how
3. Recommend any missing experiences or skills to highlight
4. Flag any irrelevant content to remove or de-emphasize

JOB DESCRIPTION:
{job_description}

CURRENT RESUME:
{resume_text}

Return as JSON:
{{
  "keywords": ["keyword1", "keyword2", ...],
  "bullet_improvements": [
    {{"original": "...", "improved": "...", "reason": "..."}}
  ],
  "missing_highlights": ["..."],
  "remove_or_reduce": ["..."],
  "match_score": X
}}"""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1200,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = message.content[0].text.strip()
    clean = raw.replace("```json", "").replace("```", "").strip()
    try:
        result = json.loads(clean)
    except json.JSONDecodeError:
        result = {"raw": raw}

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
