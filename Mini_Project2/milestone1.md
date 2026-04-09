# ============================================================
# MILESTONE 1: PIVOT & PLANNING
# ============================================================

# --- WHAT CHANGED FROM MY PROPOSAL (AND WHY) ---
# When I went to execute on my original proposal, I hit my first
# real-world engineering decision: Buddhism's Pali Canon (Tipitaka)
# didn't have a clean, efficiently convertible English text version
# that I could reliably pull into my project. Rather than waste time
# wrestling with a messy data source, I pivoted to Hinduism's The Vedas
# — a decision grounded in practicality, not preference. This actually
# reinforced my project's core message: the spirit of the idea matters
# more than rigid attachment to the original plan.

# --- MY THREE SOURCE TEXTS (ALL ENGLISH) ---
# File             | Religion      | Book
# -----------------|---------------|------------------
# KJ_Bible.txt     | Christianity  | King James Bible
# Quran.txt        | Islam         | The Quran
# Hindu.txt        | Hinduism      | The Vedas
#
# I standardized all three to English plain-text .txt files for
# simplicity and consistency — no format conversion headaches,
# no encoding issues, just raw text I can read and process uniformly.

# ============================================================
# SKELETON CODE PLAN
# Blueprint before real code is written. Goal: map out the most
# efficient and simple path to finding shared words across all 3 texts.
# ============================================================

# --- STEP 1: IMPORTS ---
# We need:
#   - string or re       → to strip punctuation
#   - collections        → Counter for word frequency counting
#   - os/pathlib         → to load the .txt files cleanly

# --- STEP 2: LOAD THE BOOKS ---
# Function: load_text(filepath)
#     Open the .txt file
#     Read all content as a single string
#     Return the raw text

# --- STEP 3: CLEAN & TOKENIZE ---
# Function: clean_text(raw_text)
#     Lowercase everything              → "Love" == "love"
#     Strip punctuation                 → "love." == "love"
#     Split into individual words       → ["love", "peace", "god", ...]
#     Return list of clean word tokens

# --- STEP 4: REMOVE STOP WORDS ---
# Stop words = filler words that aren't meaningful
#     Examples: "the", "a", "and", "of", "in", "is", "it"
# Use a predefined stopwords list (NLTK library or a custom set)
# Filter them OUT so we only count spiritually meaningful words
#     Return filtered list

# --- STEP 5: COUNT WORD FREQUENCIES ---
# Function: count_words(word_list)
#     Use Counter() to count how many times each word appears
#     Return a dictionary: { "love": 342, "god": 891, ... }

# --- STEP 6: FIND COMMON WORDS ACROSS ALL 3 BOOKS ---
# Get the top N words from each book (e.g., top 200)
# Find the INTERSECTION — words that appear in ALL THREE top lists
#     This is the heart of the project:
#     Words every religion emphasizes = universal spiritual values

# --- STEP 7: RANK & DISPLAY TOP 10 SHARED WORDS ---
# Sort the shared words by combined frequency across all 3 books
# Display a ranked list:
#     Rank | Word   | Bible Count | Quran Count | Vedas Count
#     1    | love   | 310         | 97          | 44
#     2    | god    | 4000+       | 2000+       | 800+
#     ...

# --- STEP 8: EXPLAIN WHY THESE WORDS ARE SHARED ---
# For each top shared word, provide a short explanation grounded in
# personal philosophy + factual religious context:
#     "love"  → Central command in Christianity (Mark 12:30-31),
#                core principle in Islam (Hadith on mercy),
#                and Ahimsa/Metta concepts in Vedic/Hindu tradition
#     "peace" → "Shalom" in Hebrew tradition, "Salaam" in Arabic,
#                "Shanti" in Sanskrit — literally the same concept
# This section bridges the data with MEANING

# --- MAIN FLOW ---
# bible_text  = load_text("KJ_Bible.txt")
# quran_text  = load_text("Quran.txt")
# hindu_text  = load_text("Hindu.txt")

# bible_words  = clean_text(bible_text)  → remove_stopwords() → count_words()
# quran_words  = clean_text(quran_text)  → remove_stopwords() → count_words()
# hindu_words  = clean_text(hindu_text)  → remove_stopwords() → count_words()

# shared_words = find_common_words(bible_words, quran_words, hindu_words)
# top_10       = rank_top_10(shared_words)
# display_results(top_10)
# explain_results(top_10)

# --- WHAT I STILL NEED TO FIGURE OUT (CARRIED INTO MILESTONE 2) ---
# - Decide whether to use NLTK's stopword list or build a custom one
#   tuned for religious language (e.g., keeping "god", "lord", "prayer"
#   which NLTK might strip out as too common)
# - Test whether the .txt files are clean enough or need pre-processing
#   (encoding fixes, header/footer removal from downloaded versions)
# - Decide on intersection method — strict top-N overlap vs. a weighted
#   frequency threshold
# - Format the final output — plain print, a formatted table, or visual