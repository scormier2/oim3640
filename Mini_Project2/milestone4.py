# ============================================================
# MILESTONE 4: GENERATE INSIGHTFUL CONCLUSIONS
# Books: KJ_Bible.txt | Quran.txt | Hindu.txt
# AI:    CodeGPT (installed in VS Code) handles all AI insight
#
# HOW TO USE:
#   1. Run: python milestone4.py
#   2. Copy the results table printed in the terminal
#   3. Open CodeGPT panel in VS Code sidebar
#   4. Paste the auto-generated prompt into CodeGPT chat
#   5. CodeGPT returns your AI spiritual insight
# ============================================================
 
# --- IMPORTS (built-in only, no pip installs needed) ---
import string
import os
from pathlib import Path
from collections import Counter
 
# SCRIPT_DIR: always points to the folder THIS file lives in.
# This means Python will ALWAYS find KJ_Bible.txt, Quran.txt,
# and Hindu.txt as long as they are in the same Mini_Project2
# folder — no matter where your terminal is pointed when you run it.
SCRIPT_DIR = Path(__file__).parent.resolve()
 
# ============================================================
# CONFIGURATION
# ============================================================
 
# File paths — resolved relative to this script's own folder
FILES = {
    "Christianity (KJV Bible)": SCRIPT_DIR / "KJ_Bible.txt",
    "Islam (Quran)":            SCRIPT_DIR / "Quran.txt",
    "Hinduism (The Vedas)":     SCRIPT_DIR / "Hindu.txt",
}
 
# How many top words to pull per book before finding intersection
# Raise to 500 if you get "0 shared words found"
TOP_N = 300
 
# How many final shared words to display in results
TOP_RESULTS = 10
 
# ============================================================
# SPIRITUAL WORDS — always kept, never filtered out
# These are the meaningful words we WANT to find and count
# ============================================================
SPIRITUAL_KEEP = {
    "god", "lord", "love", "peace", "prayer", "pray", "soul",
    "spirit", "holy", "faith", "truth", "light", "life", "heart",
    "mercy", "grace", "righteous", "righteousness", "worship",
    "blessed", "blessing", "eternal", "divine", "sacred", "good",
    "evil", "sin", "forgive", "forgiveness", "heaven", "earth",
    "man", "men", "people", "world", "day", "time", "water", "fire",
    "king", "fear", "glory", "power", "word", "law", "way", "path",
    "death", "live", "father", "son", "mother", "child", "children",
    "name", "hand", "eye", "face", "voice", "command", "commandment",
    "obey", "servant", "master", "creation", "creator", "knowledge",
    "wisdom", "body", "mind", "duty", "action", "virtue", "reward",
    "punishment", "community", "unity", "devotion", "self",
}
 
# ============================================================
# STOP WORDS — filler words to filter OUT (not spiritually meaningful)
# ============================================================
STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to",
    "for", "of", "with", "by", "from", "is", "was", "are", "were",
    "be", "been", "being", "have", "has", "had", "do", "does", "did",
    "will", "would", "could", "should", "may", "might", "shall",
    "that", "this", "these", "those", "it", "its", "he", "she",
    "they", "we", "you", "i", "his", "her", "their", "our", "your",
    "my", "me", "him", "us", "them", "who", "which", "what", "when",
    "where", "how", "if", "then", "not", "no", "nor", "so", "yet",
    "both", "either", "neither", "each", "all", "any", "some",
    "also", "than", "as", "up", "out", "about", "into", "through",
    "upon", "unto", "thee", "thou", "thy", "ye", "hath", "doth",
    "thereof", "therein", "thine", "saith", "said", "made", "make",
    "come", "came", "go", "went", "gone", "now", "then", "there",
    "here", "one", "two", "three", "after", "before", "against",
    "among", "between", "over", "under", "again", "back", "only",
    "own", "same", "other", "more", "most", "such", "even", "like",
    "much", "many", "every", "whoso", "whosoever", "thus", "therefore",
    "wherefore", "moreover", "verily", "behold", "lo", "chapter",
    "verse", "book", "according", "since", "while", "because",
}
 
 
# ============================================================
# STEP 1: LOAD TEXT FILE
# ============================================================
 
def load_text(filepath):
    """
    Read a .txt file and return its full content as a string.
    filepath is a Path object pointing to the exact file location.
    """
    if not filepath.exists():
        print(f"  [ERROR] File not found: {filepath}")
        print(f"          Make sure {filepath.name} is inside your Mini_Project2 folder.")
        return ""
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()
 
 
# ============================================================
# STEP 2: CLEAN & TOKENIZE
# ============================================================
 
def clean_text(raw_text):
    """
    Lowercase everything, strip punctuation, split into word tokens.
    Returns a list of clean individual words.
    """
    text  = raw_text.lower()
    text  = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    return words
 
 
# ============================================================
# STEP 3: FILTER WORDS
# ============================================================
 
def filter_words(word_list):
    """
    Keep spiritually meaningful words (SPIRITUAL_KEEP).
    Remove filler stop words (STOP_WORDS) and anything under 3 chars.
    """
    filtered = []
    for word in word_list:
        if word in SPIRITUAL_KEEP:
            filtered.append(word)
        elif word not in STOP_WORDS and len(word) > 2:
            filtered.append(word)
    return filtered
 
 
# ============================================================
# STEP 4: COUNT FREQUENCIES
# ============================================================
 
def count_words(word_list):
    """Return a Counter dictionary of { word: how_many_times_it_appears }."""
    return Counter(word_list)
 
 
# ============================================================
# STEP 5: FIND SHARED WORDS ACROSS ALL 3 BOOKS
# ============================================================
 
def find_shared_words(counters_dict, top_n=TOP_N):
    """
    Get the top N words from each book.
    Find words that appear in ALL THREE top lists (set intersection).
    Return those shared words with their per-book counts.
    """
    top_sets = {}
    for religion, counter in counters_dict.items():
        top_sets[religion] = {word for word, _ in counter.most_common(top_n)}
 
    religions = list(top_sets.keys())
    shared    = top_sets[religions[0]] & top_sets[religions[1]] & top_sets[religions[2]]
 
    return {
        word: {religion: counters_dict[religion][word] for religion in religions}
        for word in shared
    }
 
 
# ============================================================
# STEP 6: RANK BY COMBINED FREQUENCY
# ============================================================
 
def rank_shared_words(shared_words, top=TOP_RESULTS):
    """Sort shared words by their total count across all 3 books."""
    ranked = sorted(
        shared_words.items(),
        key=lambda x: sum(x[1].values()),
        reverse=True
    )
    return ranked[:top]
 
 
# ============================================================
# STEP 7: DISPLAY RESULTS + AUTO-GENERATE CodeGPT PROMPT
# ============================================================
 
def display_results(ranked_words):
    """
    Print a clean formatted results table.
    Then print a ready-to-paste CodeGPT prompt at the bottom.
    """
    religions = list(ranked_words[0][1].keys())
 
    # --- Results Table ---
    print("\n" + "=" * 72)
    print("  TOP SHARED WORDS ACROSS ALL 3 RELIGIOUS TEXTS")
    print("=" * 72)
    header = f"{'Rank':<6} {'Word':<16} " + "  ".join(f"{r:<22}" for r in religions) + " Total"
    print(header)
    print("-" * 72)
 
    for rank, (word, counts) in enumerate(ranked_words, 1):
        total      = sum(counts.values())
        counts_str = "  ".join(f"{counts[r]:<22}" for r in religions)
        print(f"{rank:<6} {word:<16} {counts_str} {total}")
 
    print("=" * 72)
 
    # --- Auto-generated CodeGPT Prompt ---
    word_list_str = ", ".join(f'"{word}"' for word, _ in ranked_words)
 
    print("\n" + "=" * 72)
    print("  CODEGPT PROMPT — copy everything below and paste into CodeGPT:")
    print("=" * 72)
    print(f"""
The following words were found in the TOP {TOP_N} most frequent words
of ALL THREE of these religious texts:
  - Christianity: The King James Bible
  - Islam: The Quran
  - Hinduism: The Vedas
 
Shared words ranked by combined frequency: {word_list_str}
 
Please provide a warm, insightful 300-400 word analysis:
  1. What does it mean that these words are shared across all 3 religions?
  2. What universal human spiritual values do they represent?
  3. What positive conclusion can we draw about the oneness of these faiths?
  4. How should this encourage appreciation of similarities over differences?
  Speak to someone on a personal spiritual journey who values open-mindedness.
""")
    print("=" * 72)
 
 
# ============================================================
# MAIN — RUNS THE FULL PIPELINE
# ============================================================
 
def main():
    print("\n" + "=" * 72)
    print("  RELIGIOUS TEXT COMMON WORD ANALYZER — MILESTONE 2")
    print("  Finding the Oneness Between Christianity, Islam & Hinduism")
    print("  AI Analysis powered by CodeGPT (inside VS Code)")
    print("=" * 72)
 
    counters_dict = {}
 
    # --- Load, clean, and count each book ---
    for religion, filepath in FILES.items():
        print(f"\n  Loading: {religion} ({filepath.name})...")
        raw = load_text(filepath)
        if not raw:
            continue
        words    = clean_text(raw)
        filtered = filter_words(words)
        counter  = count_words(filtered)
        counters_dict[religion] = counter
        print(f"  → {len(raw):,} characters | {len(words):,} raw words | {len(filtered):,} after filtering")
 
    if len(counters_dict) < 3:
        print("\n  [STOPPED] Could not load all 3 files. Check file names and location.")
        return
 
    # --- Find shared words ---
    print(f"\n  Finding words in the top {TOP_N} of ALL THREE texts...")
    shared_words = find_shared_words(counters_dict, top_n=TOP_N)
    print(f"  → {len(shared_words)} shared words found across all 3 books.")
 
    if not shared_words:
        print("  [TIP] Try increasing TOP_N from 300 to 500 in the CONFIGURATION section.")
        return
 
    # --- Rank and display ---
    ranked = rank_shared_words(shared_words, top=TOP_RESULTS)
    display_results(ranked)
 
    print("  NEXT STEP: Open CodeGPT in the VS Code sidebar,")
    print("  paste the prompt above, and get your AI insight.\n")
    print("  May this project inspire more unity than division.\n")
 
 
if __name__ == "__main__":
    main()