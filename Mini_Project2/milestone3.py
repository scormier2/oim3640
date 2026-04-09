# ============================================================
# MILESTONE 3: GENERATE INSIGHTFUL CONCLUSIONS
# Books: KJ_Bible.txt | Quran.txt | Hindu.txt
# Goal:  Find top shared words across all 3 texts, then usesetx OPENAI_API_KEY "your_api_key_here"
#        the OpenAI API to generate insightful, positive
#        conclusions about what those shared words reveal about
#        the oneness of human spiritual belief.
# ============================================================
 
# --- IMPORTS ---
import string
import os
from collections import Counter
from openai import OpenAI  # pip install openai
 
# ============================================================
# CONFIGURATION
# ============================================================
 
# Path to your 3 book .txt files (place them in same folder as this script)
FILES = {
    "Christianity (KJV Bible)": "KJ_Bible.txt",
    "Islam (Quran)":            "Quran.txt",
    "Hinduism (The Vedas)":     "Hindu.txt",
}
 
# How many top words to pull from each book before finding intersection
TOP_N = 300
 
# How many shared words to show in final results
TOP_RESULTS = 10
 
# Words to keep even if they look "common" — spiritually meaningful terms
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
 
# Standard English stop words to filter OUT (non-meaningful filler)
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
# STEP 1: LOAD TEXT
# ============================================================
 
def load_text(filepath):
    """Read a .txt file and return raw string content."""
    if not os.path.exists(filepath):
        print(f"  [ERROR] File not found: {filepath}")
        print(f"          Make sure {filepath} is in the same folder as this script.")
        return ""
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()
 
 
# ============================================================
# STEP 2: CLEAN & TOKENIZE
# ============================================================
 
def clean_text(raw_text):
    """
    Lowercase, strip punctuation, split into word tokens.
    Returns a list of clean individual words.
    """
    text  = raw_text.lower()
    text  = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    return words
 
 
# ============================================================
# STEP 3: FILTER STOP WORDS (KEEP SPIRITUAL WORDS)
# ============================================================
 
def filter_words(word_list):
    """
    Remove meaningless filler stop words.
    Always keep words in SPIRITUAL_KEEP even if short/common.
    """
    filtered = []
    for word in word_list:
        if word in SPIRITUAL_KEEP:
            filtered.append(word)
        elif word not in STOP_WORDS and len(word) > 2:
            filtered.append(word)
    return filtered
 
 
# ============================================================
# STEP 4: COUNT WORD FREQUENCIES
# ============================================================
 
def count_words(word_list):
    """Return a Counter dict of {word: frequency}."""
    return Counter(word_list)
 
 
# ============================================================
# STEP 5: FIND SHARED WORDS ACROSS ALL 3 BOOKS
# ============================================================
 
def find_shared_words(counters_dict, top_n=TOP_N):
    """
    Pull top N words from each book, find the intersection —
    words that appear in ALL THREE top lists.
    Returns a dict of shared words with their counts per book.
    """
    top_sets = {}
    for religion, counter in counters_dict.items():
        top_words = {word for word, _ in counter.most_common(top_n)}
        top_sets[religion] = top_words
 
    religions = list(top_sets.keys())
    shared    = top_sets[religions[0]] & top_sets[religions[1]] & top_sets[religions[2]]
 
    result = {}
    for word in shared:
        result[word] = {religion: counters_dict[religion][word] for religion in religions}
 
    return result
 
 
# ============================================================
# STEP 6: RANK TOP RESULTS BY COMBINED FREQUENCY
# ============================================================
 
def rank_shared_words(shared_words, top=TOP_RESULTS):
    """Sort shared words by total combined frequency across all 3 books."""
    ranked = sorted(
        shared_words.items(),
        key=lambda x: sum(x[1].values()),
        reverse=True
    )
    return ranked[:top]
 
 
# ============================================================
# STEP 7: DISPLAY RESULTS TABLE
# ============================================================
 
def display_results(ranked_words):
    """Print a clean formatted table of results."""
    religions = list(ranked_words[0][1].keys()) if ranked_words else []
 
    print("\n" + "=" * 70)
    print("  TOP SHARED WORDS ACROSS ALL 3 RELIGIOUS TEXTS")
    print("=" * 70)
    header = f"{'Rank':<6} {'Word':<16} " + "  ".join(f"{r[:18]:<20}" for r in religions) + "  Total"
    print(header)
    print("-" * 70)
 
    for rank, (word, counts) in enumerate(ranked_words, 1):
        total      = sum(counts.values())
        counts_str = "  ".join(f"{counts[r]:<20}" for r in religions)
        print(f"{rank:<6} {word:<16} {counts_str}  {total}")
 
    print("=" * 70)
 
 
# ============================================================
# STEP 8: AI-POWERED INSIGHT (OPENAI API)
# ============================================================
 
def get_ai_insight(ranked_words):
    """
    Send the top shared words to GPT via the OpenAI API.
    GPT will generate warm, insightful, positive conclusions
    about what these shared words reveal about human spirituality.
    """
 
    # Build the word summary to send to the AI
    word_summary = ""
    for rank, (word, counts) in enumerate(ranked_words, 1):
        total      = sum(counts.values())
        religions  = list(counts.keys())
        counts_str = ", ".join(f"{r}: {counts[r]}" for r in religions)
        word_summary += f"  {rank}. '{word}' — Total: {total} ({counts_str})\n"
 
    prompt = f"""You are analyzing the most common shared words found across three major world religious texts:
- Christianity: The King James Bible
- Islam: The Quran
- Hinduism: The Vedas
 
The following words appeared in the TOP {TOP_N} most frequent words in ALL THREE texts:
 
{word_summary}
 
Please provide a warm, insightful, and uplifting analysis (around 300-400 words) that:
1. Explains what it means that these specific words are shared across all three religions
2. Highlights the universal human spiritual values they represent
3. Draws a positive conclusion about the oneness and commonality of these faiths
4. Encourages appreciation of similarities rather than focus on differences
5. Speaks to someone who is on a personal spiritual journey and values open-mindedness
 
Be thoughtful, grounded in factual religious context, and inspiring in tone.
"""
 
    print("\n" + "=" * 70)
    print("  AI-POWERED INSIGHT (GPT via OpenAI API)")
    print("=" * 70)
    print("  Sending results to GPT for analysis...\n")
 
    try:
        client   = OpenAI()  # Reads OPENAI_API_KEY from your environment
 
        response = client.responses.create(
            model="gpt-4o",
            input=prompt
        )
 
        insight_text = response.output_text
        print(insight_text)
        print("=" * 70)
        return insight_text
 
    except Exception as e:
        print(f"  [ERROR] OpenAI API error: {e}")
        print("          Make sure OPENAI_API_KEY is set in your environment.")
 
    return None
 
 
# ============================================================
# MAIN — FULL PIPELINE
# ============================================================
 
def main():
    print("\n" + "=" * 70)
    print("  RELIGIOUS TEXT COMMON WORD ANALYZER — MILESTONE 2")
    print("  Finding the Oneness Between Christianity, Islam & Hinduism")
    print("=" * 70)
 
    counters_dict = {}
 
    # --- Load, clean, count each book ---
    for religion, filepath in FILES.items():
        print(f"\n  Loading: {religion} ({filepath})...")
        raw      = load_text(filepath)
        if not raw:
            continue
        words    = clean_text(raw)
        filtered = filter_words(words)
        counter  = count_words(filtered)
        counters_dict[religion] = counter
        print(f"  → {len(raw):,} characters | {len(words):,} raw words | {len(filtered):,} after filtering")
 
    if len(counters_dict) < 3:
        print("\n  [STOPPED] Could not load all 3 files. Please check file paths.")
        return
 
    # --- Find shared words ---
    print(f"\n  Finding words in the top {TOP_N} of ALL THREE texts...")
    shared_words = find_shared_words(counters_dict, top_n=TOP_N)
    print(f"  → {len(shared_words)} shared words found across all 3 books.")
 
    # --- Rank and display ---
    ranked = rank_shared_words(shared_words, top=TOP_RESULTS)
    display_results(ranked)
 
    # --- AI Insight ---
    get_ai_insight(ranked)
 
    print("\n  Done. May this project inspire more unity than division.\n")
 
 
if __name__ == "__main__":
    main()