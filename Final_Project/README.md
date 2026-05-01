# Best Résumé 🎓

> AI-powered resume builder inspired by MLT Fellowship, CareerSpring, and Harvard OCS formats.

## What It Does

Best Résumé transforms raw, conversational experience descriptions into polished, recruiter-ready resume bullets using the Claude AI API. It follows the most trusted resume standards used by elite career development programs.

**Example transformation:**
- You say: *"I was a teaching assistant in a program for 30 admitted students and my assistance directly generated 27 of them passing"*
- AI writes: **Directly created a 90% success rate as a Teaching Assistant in a 30-student selective cohort**

### Features
- ✦ **Quick Polish** — paste any raw experience, get ATS-optimized bullets instantly
- ✦ **Full Resume Builder** — guided 3-step form generates a complete, formatted resume
- ✦ **Resume Scorer** — get a 1–10 score across 5 dimensions with specific fix suggestions
- ✦ **Job Tailor** — paste a job description to get keyword gaps and bullet improvements
- ✦ **Three format standards**: Harvard OCS, MLT Fellow, CareerSpring

---

## How to Install & Run

### Prerequisites
- Python 3.9+
- An [Anthropic API key](https://console.anthropic.com/)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/best-resume.git
cd best-resume

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Open .env and add your ANTHROPIC_API_KEY

# 5. Run the app
python app.py
```

Then open your browser to: **http://localhost:5000**

---

## Required API Keys

| Key | Where to Get It |
|-----|----------------|
| `ANTHROPIC_API_KEY` | [console.anthropic.com](https://console.anthropic.com/) |
| `FLASK_SECRET_KEY` | Any random string (e.g. run `python -c "import secrets; print(secrets.token_hex(32))"`) |

---

## Project Structure

```
best-resume/
├── app.py                  # Flask application & API routes
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
├── .gitignore
├── README.md
├── AI_USAGE.md
├── templates/
│   ├── index.html          # Landing page
│   └── builder.html        # Resume builder UI
└── static/
    ├── css/
    │   ├── main.css        # Global styles
    │   └── builder.css     # Builder-specific styles
    └── js/
        ├── main.js         # Landing page interactions
        └── builder.js      # Builder logic & API calls
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python + Flask |
| AI | Anthropic Claude API (`claude-opus-4-5`) |
| Frontend | HTML, CSS, Vanilla JavaScript |
| Config | python-dotenv |

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/polish-bullet` | POST | Transform raw text into resume bullets |
| `/api/generate-resume` | POST | Generate complete resume from form data |
| `/api/score-resume` | POST | Score resume on 5 dimensions |
| `/api/tailor-resume` | POST | Tailor resume to a job description |

---

## Inspiration

This project is informed by resume standards from programs I've personally participated in:
- **MLT (Management Leadership for Tomorrow)** — emphasizes measurable leadership impact
- **CareerSpring** — focuses on first-generation student voice and transferable skills
- **Harvard OCS** — the gold-standard one-page, action-verb-driven format

---

*Final Project — Python Course · 2025*
