# ============================================================
# MINI PROJECT 2 — FINAL REFLECTION
# Religious Text Common Word Analyzer
# ============================================================

# ============================================================
# WHERE IT STARTED: THE PROPOSAL
# ============================================================

# The original idea was personal and clear:
# I wanted to write code that would take 3 major world religion
# texts — the King James Bible (Christianity), the Quran (Islam),
# and the Tipitaka/Pali Canon (Buddhism) — and find the most
# common words shared between all three.

# The motivation was rooted in my own spiritual journey. Having
# grown up in a restrictive Christian household, I've grown
# frustrated watching people cling to the belief that they were
# raised in the ONE true religion. I believe that polarization
# through religion is wrong, and that the real story is in the
# SIMILARITIES — love, peace, community, God, worship — the
# threads that connect us all regardless of the name on the door.

# Core features I planned:
#   - Find the most common shared words across all 3 texts
#   - List them ranked 1-10
#   - Explain WHY those words are shared using facts + my perspective

# What I admitted I didn't know yet:
#   - How to upload and distinguish 3 separate book files in code
#   - How to pull a top-10 shared word list programmatically

# ============================================================
# PIVOT 1: BUDDHISM → HINDUISM
# ============================================================

# The first real change happened before a single line of code
# was written. When I went to source the Buddhist Tipitaka
# (Pali Canon) as a clean, usable English .txt file, I hit a
# wall. The available versions were fragmented, poorly formatted,
# or not efficiently convertible for this kind of word analysis.

# Rather than waste time wrestling with a messy data source,
# I pivoted to Hinduism's The Vedas — the oldest of the major
# world scriptures and equally rich in spiritual language.

# This pivot actually reinforced the project's core message:
# the SPIRIT of the idea matters more than rigid attachment
# to the original plan. The goal was always about finding
# commonality between major world religions — swapping one
# ancient text for another didn't change that mission at all.

# Final 3 source texts chosen (all English plain-text):
#   KJ_Bible.txt  — Christianity  — King James Bible
#   Quran.txt     — Islam         — The Quran
#   Hindu.txt     — Hinduism      — The Vedas

# ============================================================
# MILESTONE 1: THE SKELETON PLAN
# ============================================================

# Before writing real code, Milestone 1 was about planning.
# The skeleton laid out the full pipeline in pseudocode using
# # comments — a blueprint of every step before touching logic:
#
#   Step 1: Load each .txt file
#   Step 2: Clean and tokenize the text (lowercase, strip punctuation)
#   Step 3: Remove stop words (the, and, a, of...)
#   Step 4: Count word frequencies using Counter()
#   Step 5: Find intersection of top words across all 3 books
#   Step 6: Rank by combined frequency
#   Step 7: Display a results table
#   Step 8: Explain why those words are shared

# Open questions carried into Milestone 2:
#   - Use NLTK stopwords or a custom spiritual word list?
#   - How clean are the raw .txt files?
#   - Strict top-N intersection or weighted threshold?
#   - Plain print output or formatted table?

# ============================================================
# PIVOT 2: ANTHROPIC API → OPENAI API → CodeGPT
# ============================================================

# The biggest evolution of the project was HOW the AI insight
# piece was handled. It went through three versions:

# VERSION 1 — Anthropic API (pip install anthropic)
#   The first real code used Anthropic's Claude API to send
#   the shared word results and get back a spiritual insight
#   paragraph. This required an API key from console.anthropic.com
#   and the anthropic Python library.

# VERSION 2 — OpenAI API (pip install openai)
#   Swapped Anthropic out for OpenAI using the cleaner syntax:
#     from openai import OpenAI
#     client = OpenAI()
#     response = client.responses.create(model="gpt-4o", input=prompt)
#     print(response.output_text)
#   Same idea, different provider. Still required an API key
#   from platform.openai.com and a pip install.

# VERSION 3 — CodeGPT (already installed in VS Code, no API needed)
#   The final and cleanest pivot: I already had CodeGPT installed
#   directly in VS Code as an extension. CodeGPT connects to any
#   model (Claude, GPT, Gemini, local models) from inside the editor
#   itself — meaning NO pip installs, NO API keys in the code,
#   and NO external dependencies in the Python script at all.
#
#   The solution: the Python script does all the data work
#   (load, clean, filter, count, rank, display), then auto-generates
#   a ready-to-paste prompt at the bottom of the terminal output.
#   The user copies that prompt, pastes it into the CodeGPT chat
#   panel in VS Code, and gets the AI insight there.
#
#   This made the script lighter, simpler, and more portable.

# ============================================================
# PIVOT 3: FILE PATH FIX (SCRIPT_DIR)
# ============================================================

# After the code was written and the .txt files were confirmed
# to be sitting correctly inside the Mini_Project2 folder,
# the script still threw this error on every file:
#   [ERROR] File not found: KJ_Bible.txt

# The problem: Python was looking for the files relative to
# wherever the TERMINAL was pointed — not where the script lived.
# So if the terminal was open at a parent directory, it couldn't
# see inside Mini_Project2/ even though the files were right there.

# The fix was one clean line added at the top:
#   from pathlib import Path
#   SCRIPT_DIR = Path(__file__).parent.resolve()
#
# And the FILES dictionary was updated to use it:
#   FILES = {
#       "Christianity (KJV Bible)": SCRIPT_DIR / "KJ_Bible.txt",
#       "Islam (Quran)":            SCRIPT_DIR / "Quran.txt",
#       "Hinduism (The Vedas)":     SCRIPT_DIR / "Hindu.txt",
#   }
#
# __file__ is Python's built-in reference to the script itself.
# .parent gives the folder it lives in. .resolve() makes it
# an absolute path so there's zero ambiguity no matter what.
# This is considered best practice for any project where your
# script and its data files live in the same folder.

# After patching this in, the final milestone2.py was rewritten
# cleanly from scratch with SCRIPT_DIR built in from line one —
# no more patching, no more band-aid fixes on top of old code.

# ============================================================
# WHAT STAYED THE SAME THE WHOLE TIME
# ============================================================

# Through every pivot and every version, the CORE mission never
# changed. The pipeline logic — load, clean, filter, count,
# intersect, rank, display — was written in Milestone 1 as a
# skeleton and stayed structurally identical through the final
# version. The spiritual word list, the stop word filter, the
# Counter() frequency approach, the ranked results table —
# all of it held from the very first draft.

# Most importantly, the WHY never changed.
# This project was always about proving — with actual data from
# the texts themselves — that the world's great religions share
# more than they divide. That "love", "peace", "god", "mercy",
# and "truth" showing up at the top of all three books isn't a
# coincidence. It's the point.

# ============================================================
# FINAL THOUGHT
# ============================================================

# The best part of this project is that the code itself lives
# out its own thesis. It started with one plan, hit real walls,
# adapted without losing its purpose, and ended up somewhere
# better than where it began. That's pretty much the definition
# of a spiritual journey too.

# May this project inspire more unity than division.
# ============================================================