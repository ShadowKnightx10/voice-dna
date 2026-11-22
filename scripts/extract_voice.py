#!/usr/bin/env python3
"""
voice-dna: Anti-Slop Personal Voice Extractor
Analyzes unvarnished human writing, chat logs, transcripts, or commit messages
to extract linguistic cadence, vocabulary, and directness, outputting a calibrated VOICE.md profile.

Zero external dependencies - standard library only.
"""

import sys
import os
import re
import json
import math
import argparse
from pathlib import Path
from collections import Counter, defaultdict

# Built-in corporate slop words to detect during profiling
SLOP_KEYWORDS = {
    "spearhead", "spearheaded", "spearheading",
    "leverage", "leveraged", "leveraging",
    "orchestrate", "orchestrated", "orchestrating",
    "synergize", "synergized", "synergy", "synergies",
    "navigate", "navigated", "navigating",
    "champion", "championed", "championing",
    "empower", "empowered", "empowering",
    "foster", "fostered", "fostering",
    "ideate", "ideated", "ideating",
    "operationalize", "operationalized", "operationalizing",
    "mission-critical", "cutting-edge", "robust",
    "seamless", "seamlessly", "unparalleled",
    "holistic", "holistically", "best-in-class",
    "transformative", "bespoke", "dynamic",
    "pivotal", "catalyst", "tapestry", "beacon"
}

CONTRACTION_EXPANSION_PAIRS = [
    (r"\b(don't|doesn't|didn't)\b", r"\b(do not|does not|did not)\b"),
    (r"\b(can't|cannot)\b", r"\b(can not|cannot)\b"),
    (r"\b(won't|wouldn't)\b", r"\b(will not|would not)\b"),
    (r"\b(it's|that's|there's|here's|what's)\b", r"\b(it is|that is|there is|here is|what is)\b"),
    (r"\b(i'm|you're|we're|they're)\b", r"\b(i am|you are|we are|they are)\b"),
    (r"\b(i've|we've|they've|you've)\b", r"\b(i have|we have|they have|you have)\b"),
    (r"\b(i'd|we'd|they'd|you'd|he'd|she'd)\b", r"\b(i would|we would|they would|you would|he would|she would)\b"),
    (r"\b(isn't|aren't|wasn't|weren't)\b", r"\b(is not|are not|was not|were not)\b"),
    (r"\b(haven't|hasn't|hadn't)\b", r"\b(have not|has not|had not)\b"),
]

STOPWORDS_NGRAM = {
    "a", "an", "the", "and", "or", "but", "if", "then", "else", "when",
    "at", "by", "for", "with", "about", "against", "between", "into", "through",
    "during", "before", "after", "above", "below", "to", "from", "up", "down",
    "in", "out", "on", "off", "over", "under", "again", "further", "then", "once",
    "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
    "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only",
    "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just",
    "don", "should", "now"
}

def clean_text(raw_text: str) -> str:
    """Normalize whitespace and strip formatting artifacts."""
    text = re.sub(r"\r\n", "\n", raw_text)
    text = re.sub(r"```[\s\S]*?```", " ", text) # strip code blocks
    text = re.sub(r"`[^`]+`", " ", text)        # strip inline code
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text) # markdown links to text
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()

def extract_user_messages_from_json(content: str) -> str:
    """Parse JSON or JSONL chat logs, filtering OUT assistant/system messages."""
    user_texts = []
    
    # Try parsing line-by-line JSONL first
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    is_jsonl = True
    for line in lines:
        try:
            data = json.loads(line)
            role = data.get("role") or data.get("speaker") or data.get("author") or ""
            role_str = str(role).lower()
            if role_str in {"user", "human", "client", "customer"} or ("assistant" not in role_str and "system" not in role_str and "model" not in role_str):
                msg = data.get("content") or data.get("text") or data.get("message") or ""
                if isinstance(msg, list):
                    msg = " ".join([item.get("text", "") if isinstance(item, dict) else str(item) for item in msg])
                if msg:
                    user_texts.append(str(msg))
        except json.JSONDecodeError:
            is_jsonl = False
            break
            
    if is_jsonl and user_texts:
        return "\n\n".join(user_texts)

    # Try full JSON parse
    try:
        data = json.loads(content)
        extracted = []
        def walk(node):
            if isinstance(node, dict):
                role = str(node.get("role", "")).lower()
                sender = str(node.get("author", "")).lower()
                msg = node.get("content") or node.get("text") or node.get("message") or ""
                if role in {"user", "human"} or sender in {"user", "human"}:
                    if isinstance(msg, str) and msg.strip():
                        extracted.append(msg.strip())
                    elif isinstance(msg, list):
                        for sub in msg:
                            if isinstance(sub, dict) and "text" in sub:
                                extracted.append(sub["text"])
                for v in node.values():
                    walk(v)
            elif isinstance(node, list):
                for item in node:
                    walk(item)
        walk(data)
        if extracted:
            return "\n\n".join(extracted)
    except json.JSONDecodeError:
        pass

    # Fallback to transcript heuristic parsing (e.g., "User: ... \nAssistant: ...")
    user_blocks = []
    current_is_user = True
    for line in content.splitlines():
        line_clean = line.strip()
        user_match = re.match(r"^(User|Human|Me|Speaker 1|Alex|Engineer):\s*(.*)$", line_clean, re.IGNORECASE)
        ai_match = re.match(r"^(Assistant|AI|ChatGPT|Claude|Bot|System|Gemini):\s*(.*)$", line_clean, re.IGNORECASE)
        if user_match:
            current_is_user = True
            user_blocks.append(user_match.group(2))
        elif ai_match:
            current_is_user = False
        elif current_is_user and line_clean:
            user_blocks.append(line_clean)
            
    if user_blocks:
        return "\n".join(user_blocks)

    return content

def split_into_sentences(text: str) -> list[str]:
    """Split text into sentences handling common abbreviations."""
    # Temporarily protect common abbreviations
    protected = text
    abbreviations = [
        ("e.g.", "EG_TOKEN"),
        ("i.e.", "IE_TOKEN"),
        ("etc.", "ETC_TOKEN"),
        ("vs.", "VS_TOKEN"),
        ("dr.", "DR_TOKEN"),
        ("mr.", "MR_TOKEN"),
        ("ms.", "MS_TOKEN"),
        ("p99", "P99_TOKEN"),
        ("p95", "P95_TOKEN"),
        ("p50", "P50_TOKEN"),
        ("v1.", "V1_TOKEN"),
        ("v2.", "V2_TOKEN"),
    ]
    for abbr, token in abbreviations:
        protected = re.sub(re.escape(abbr), token, protected, flags=re.IGNORECASE)

    raw_sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'—\-])", protected)
    clean_sentences = []
    for s in raw_sentences:
        s = s.strip()
        if not s:
            continue
        for abbr, token in abbreviations:
            s = s.replace(token, abbr)
        # Filter out stray markdown symbols or numbers
        if re.search(r"[a-zA-Z]", s):
            clean_sentences.append(s)
    return clean_sentences

def estimate_syllables(word: str) -> int:
    """Heuristic syllable counter for Flesch readability."""
    word = word.lower()
    if len(word) <= 3:
        return 1
    word = re.sub(r'(?:[^laeiouy]|ed|es|e)$', '', word)
    word = re.sub(r'^y', '', word)
    matches = re.findall(r'[aeiouy]{1,2}', word)
    return max(1, len(matches))

def calculate_metrics(text: str) -> dict:
    cleaned = clean_text(text)
    sentences = split_into_sentences(cleaned)
    if not sentences:
        sentences = [cleaned]

    words = re.findall(r"\b[a-zA-Z0-9'-]+\b", cleaned)
    total_words = len(words)
    total_sentences = max(1, len(sentences))
    
    sentence_word_counts = []
    for s in sentences:
        s_words = re.findall(r"\b[a-zA-Z0-9'-]+\b", s)
        if s_words:
            sentence_word_counts.append(len(s_words))
            
    if not sentence_word_counts:
        sentence_word_counts = [total_words]

    mean_sentence_length = sum(sentence_word_counts) / len(sentence_word_counts)
    
    # Standard deviation of sentence length
    variance = sum((x - mean_sentence_length) ** 2 for x in sentence_word_counts) / len(sentence_word_counts)
    std_dev_sentence_length = math.sqrt(variance)

    # Length buckets
    short_sentences = sum(1 for x in sentence_word_counts if x < 10)
    medium_sentences = sum(1 for x in sentence_word_counts if 10 <= x <= 25)
    long_sentences = sum(1 for x in sentence_word_counts if x > 25)
    
    short_pct = (short_sentences / len(sentence_word_counts)) * 100
    med_pct = (medium_sentences / len(sentence_word_counts)) * 100
    long_pct = (long_sentences / len(sentence_word_counts)) * 100

    # Contractions analysis
    contracted_count = 0
    expanded_count = 0
    lower_text = cleaned.lower()
    for c_pattern, e_pattern in CONTRACTION_EXPANSION_PAIRS:
        contracted_count += len(re.findall(c_pattern, lower_text))
        expanded_count += len(re.findall(e_pattern, lower_text))
        
    total_contraction_opportunities = contracted_count + expanded_count
    contraction_ratio = (contracted_count / total_contraction_opportunities * 100) if total_contraction_opportunities > 0 else 50.0

    # Punctuation analysis
    em_dashes = len(re.findall(r"[—]|(?:--)", text))
    semicolons = text.count(";")
    colons = text.count(":")
    parentheses = text.count("(")
    exclamations = text.count("!")
    questions = text.count("?")

    # Pronoun analysis (I vs We)
    i_pronouns = len(re.findall(r"\b(i|me|my|mine|myself)\b", lower_text))
    we_pronouns = len(re.findall(r"\b(we|us|our|ours|ourselves)\b", lower_text))
    pronoun_total = i_pronouns + we_pronouns
    i_ratio = (i_pronouns / pronoun_total * 100) if pronoun_total > 0 else 50.0

    # Slop words found
    slop_found = Counter()
    for word in words:
        w_low = word.lower()
        if w_low in SLOP_KEYWORDS:
            slop_found[w_low] += 1
            
    slop_score = (sum(slop_found.values()) / max(1, total_words)) * 100

    # Readability
    total_syllables = sum(estimate_syllables(w) for w in words)
    flesch_reading_ease = 206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (total_syllables / max(1, total_words))
    flesch_reading_ease = max(0.0, min(100.0, flesch_reading_ease))
    
    fk_grade = 0.39 * (total_words / total_sentences) + 11.8 * (total_syllables / max(1, total_words)) - 15.59
    fk_grade = max(1.0, fk_grade)

    # Lexical Diversity
    unique_words = len(set(w.lower() for w in words))
    ttr = (unique_words / max(1, total_words))

    # Idioms and N-grams
    clean_words_lower = [w.lower() for w in words if w.isalpha() and w.lower() not in STOPWORDS_NGRAM]
    bigrams = [f"{clean_words_lower[i]} {clean_words_lower[i+1]}" for i in range(len(clean_words_lower)-1)]
    trigrams = [f"{clean_words_lower[i]} {clean_words_lower[i+1]} {clean_words_lower[i+2]}" for i in range(len(clean_words_lower)-2)]
    
    top_bigrams = [item for item, count in Counter(bigrams).most_common(6) if count >= 2]
    top_trigrams = [item for item, count in Counter(trigrams).most_common(4) if count >= 2]

    # Variance qualitative assessment
    if std_dev_sentence_length > 8.0:
        variance_label = "High (Dynamic rhythmic contrast: punchy verdicts followed by detailed explanations)"
    elif std_dev_sentence_length > 4.5:
        variance_label = "Medium (Balanced natural conversational rhythm)"
    else:
        variance_label = "Low (Uniform sentence lengths)"

    return {
        "word_count": total_words,
        "sentence_count": total_sentences,
        "mean_sentence_length": round(mean_sentence_length, 1),
        "std_dev_sentence_length": round(std_dev_sentence_length, 1),
        "variance_label": variance_label,
        "distribution": {
            "short_pct": round(short_pct, 1),
            "med_pct": round(med_pct, 1),
            "long_pct": round(long_pct, 1)
        },
        "contraction_ratio": round(contraction_ratio, 1),
        "punctuation": {
            "em_dashes": em_dashes,
            "semicolons": semicolons,
            "colons": colons,
            "parentheses": parentheses,
            "exclamations": exclamations,
            "questions": questions
        },
        "pronouns": {
            "i_count": i_pronouns,
            "we_count": we_pronouns,
            "i_ratio": round(i_ratio, 1)
        },
        "slop": {
            "score": round(slop_score, 2),
            "detected": dict(slop_found)
        },
        "readability": {
            "flesch_ease": round(flesch_reading_ease, 1),
            "grade_level": round(fk_grade, 1),
            "lexical_diversity": round(ttr, 3)
        },
        "top_phrases": top_bigrams + top_trigrams
    }

def generate_voice_profile(metrics: dict, author: str, role: str, domain: str, source_desc: str) -> str:
    """Format quantitative metrics and inferred tone into a complete VOICE.md profile."""
    m_len = metrics["mean_sentence_length"]
    cont_ratio = metrics["contraction_ratio"]
    slop_score = metrics["slop"]["score"]
    slop_detected = metrics["slop"]["detected"]
    
    # Infer Directness (1-10)
    # Higher for shorter sentences, low slop, high first-person ownership
    directness = min(10, max(1, int(10 - (m_len - 10) * 0.4 - slop_score * 2)))
    
    # Infer Formality (1-10)
    # Lower with high contraction ratio, higher with semicolons and long sentences
    formality = min(10, max(1, int(10 - (cont_ratio / 12) + (metrics["punctuation"]["semicolons"] * 0.5))))

    punc_notes = []
    if metrics["punctuation"]["em_dashes"] > 0:
        punc_notes.append(f"Em-dashes active ({metrics['punctuation']['em_dashes']} observed) for sharp parenthetical turns")
    if metrics["punctuation"]["semicolons"] == 0:
        punc_notes.append("Zero semicolons observed (avoids academic stuffiness)")
    else:
        punc_notes.append(f"Sparse semicolons ({metrics['punctuation']['semicolons']} observed)")
    if metrics["punctuation"]["parentheses"] > 0:
        punc_notes.append("Parentheses used for dry side-commentary and technical clarifications")
    punc_summary = "; ".join(punc_notes) if punc_notes else "Standard declarative punctuation"

    slop_report = "Pristine (0 detected buzzwords)" if not slop_detected else f"Detected: {', '.join(slop_detected.keys())}"

    phrases_str = "\n".join([f"- \"{p}\"" for p in metrics["top_phrases"]]) if metrics["top_phrases"] else "- [Add signature turns of phrase from calibration interview]"

    return f"""---
version: 1.0.0
author: "{author}"
target_role: "{role}"
primary_domain: "{domain}"
created_at: "2026-11-22"
calibration_source: "{source_desc}"
metrics_summary:
  words_analyzed: {metrics["word_count"]}
  mean_words_per_sentence: {m_len}
  contraction_rate: {cont_ratio}%
  slop_index: {slop_score}%
---

# Voice DNA Profile: {author}

> Extracted via `voice-dna` engine. Calibrated for authentic, grounded writing that satisfies professional and ATS rigor without corporate slop.

---

## 1. Linguistic Cadence

- **Mean Sentence Length**: {m_len} words per sentence.
- **Rhythm & Cadence**: {metrics["variance_label"]}.
- **Length Distribution**:
  - Short sentences (<10 words): **{metrics["distribution"]["short_pct"]}%** (staccato punchlines & verdicts)
  - Medium sentences (10–25 words): **{metrics["distribution"]["med_pct"]}%** (core technical exposition)
  - Long sentences (>25 words): **{metrics["distribution"]["long_pct"]}%** (complex architectural sequences)
- **Contraction Ratio**: **{cont_ratio}%**. Prefers natural contractions (*don't*, *can't*, *it's*) over stiff expansions unless laying down an unyielding boundary.
- **Punctuation Fingerprint**: {punc_summary}.
- **Fragment Tolerance**: Permitted for deliberate emphasis and post-mortem verdicts (e.g., *"Not optimal. But stable."*).

---

## 2. Tone Spectrum

| Dimension | Score (1–10) | Calibration Notes |
| :--- | :--- | :--- |
| **Directness** | **{directness} / 10** | Unflinching clarity; states root causes and decisions directly without euphemism. |
| **Formality** | **{formality} / 10** | Conversational peer-to-peer authority; avoids stiff corporate protocol. |
| **Wit & Dryness** | **7 / 10** | Understated, dry technical realism; zero corporate cheerleading. |
| **Warmth** | **6 / 10** | Collaborative and generous with knowledge, but respects the reader's time. |
| **Skepticism** | **9 / 10** | Demands production metrics, flamegraphs, and benchmarks before accepting claims. |
| **Ego Baseline** | **5 / 10** | Grounded technical authority ({metrics["pronouns"]["i_ratio"]}% individual vs team attribution). Takes direct ownership of decisions. |

---

## 3. Vocabulary & Jargon Profile

- **Grounded Technical Nouns**: Anchor every sentence to concrete objects (`PostgreSQL connection pool`, `WAL buffer`, `etcd leader leases`, `kernel thread contention`).
- **Mechanical Action Verbs**: Exclusively use active, unvarnished verbs:
  - *Built, Led, Cut, Deleted, Rewrote, Benchmarked, Profiled, Shipped, Diagnosed, Replaced*.
- **The Banned Lexicon**:
  - Current Input Status: {slop_report}.
  - Absolutely forbidden: *spearheaded, leveraged, orchestrated, synergized, holistic, seamless, mission-critical, transformative, ideated, robust*.

---

## 4. Anti-Slop Enforcement Rules

1. **The Coffee Table Test**: Never output a sentence that the author wouldn't say aloud to an engineering peer across a table.
2. **No AI Throat-Clearing**: Ban phrases like *"In today's fast-paced landscape..."* or *"A testament to..."*. Start directly with the subject and action.
3. **Active Voice Mandate**: Never write *"Issues were mitigated"*. Write *"I patched the memory leak and stabilized the service"*.
4. **Substantiated Adjectives**: Never claim a system is "resilient" without citing the failure mode it survived.

---

## 5. Core Philosophy & Signature Idioms

### Problem-Solving Philosophy
- *"Measure before touching; verify in production logs before claiming victory."*
- *"The most reliable code is the code you deleted."*
- *"Operational simplicity beats architectural cleverness every single time."*

### Recurring Idioms & Key Phrases
{phrases_str}

---

## 6. Document Ghostwriting Adaptations

### A. Resume / CV Bullets
- Format: `[Direct Verb] + [Specific System/Problem] + [Measurable Delta / Production Metric]`
- Example: *"Led 3-engineer migration of 14TB Postgres cluster; eliminated connection exhaustion and dropped p99 latency from 850ms to 42ms."*

### B. Executive & Public Bio
- Tone: Quiet, confident authority. No corporate buzzwords.
- Focus: Hard problems actually solved, unpretentious track record, pragmatic philosophy.

### C. Case Studies & Post-Mortems
- Cadence: Rapid 4-step sequence (The Reality -> The Investigation -> The Cut -> The Ground Truth).
- Honesty: Transparent about constraints and trade-offs made.
"""

def main():
    parser = argparse.ArgumentParser(
        description="voice-dna: Extract a human's linguistic fingerprint from raw text or chat logs."
    )
    parser.add_argument("--input", "-i", required=True, help="Path to input text, markdown, or chat log (JSON/JSONL)")
    parser.add_argument("--output", "-o", help="Path to write the generated VOICE.md")
    parser.add_argument("--author", default="Engineering Lead", help="Name of the person being profiled")
    parser.add_argument("--role", default="Principal Systems Engineer", help="Target role or professional title")
    parser.add_argument("--domain", default="Distributed Systems & Infrastructure", help="Primary technical domain")
    parser.add_argument("--json", action="store_true", help="Output raw calculated metrics as JSON")

    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file '{args.input}' not found.", file=sys.stderr)
        sys.exit(1)

    raw_content = input_path.read_text(encoding="utf-8", errors="replace")

    # Ingest and filter assistant messages if structured log
    filtered_text = extract_user_messages_from_json(raw_content)

    metrics = calculate_metrics(filtered_text)

    if args.json:
        print(json.dumps(metrics, indent=2))
        return

    source_desc = f"Analysis of {input_path.name} ({metrics['word_count']} words, {metrics['sentence_count']} sentences)"
    voice_md = generate_voice_profile(metrics, args.author, args.role, args.domain, source_desc)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(voice_md, encoding="utf-8")
        print(f"[voice-dna] Successfully generated Voice DNA profile -> {args.output}")
        print(f"[voice-dna] Words analyzed: {metrics['word_count']} | Mean WPS: {metrics['mean_sentence_length']} | Contraction Rate: {metrics['contraction_ratio']}% | Slop Score: {metrics['slop']['score']}%")
    else:
        print(voice_md)

if __name__ == "__main__":
    main()
