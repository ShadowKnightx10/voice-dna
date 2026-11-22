# voice-dna 🧬
### Anti-Slop Personal Voice Extractor & Ghostwriter for AI Coding Assistants

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](scripts/extract_voice.py)
[![Antigravity Skill](https://img.shields.io/badge/Antigravity-Skill-orange.svg)](SKILL.md)
[![Anti-Slop Rating](https://img.shields.io/badge/Anti--Slop-Grade%20A%2B-purple.svg)](references/anti-slop-dictionary.md)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-success.svg)](scripts/extract_voice.py)

**`voice-dna`** extracts a human's unvarnished linguistic fingerprint from chat transcripts, PRs, commit logs, or scratchpads, establishes a persistent `VOICE.md` profile, and ghostwrites professional documents (CVs, bios, portfolios, cold emails) that satisfy **ATS and industry rigor** while sounding **100% like the human who did the work**—not a corporate LLM thesaurus.

---

## ⚡ The Problem: The Corporate Slop Epidemic

Ask any modern LLM to write a resume, bio, or cover letter, and you get synthetic, pompous sludge:

> ❌ *"Spearheaded cross-functional incident triage across mission-critical enterprise database clusters, leveraging cloud-native synergies to unlock robust operational excellence and drive transformative business value."*

Nobody speaks like that across a table. Recruiters, engineering leaders, and clients skim past it because it smells like an unprompted AI model masking a lack of real substance.

`voice-dna` replaces this synthetic fluff with grounded, evidence-backed human truth:

> ✅ *"Led on-call triage for 16 production database nodes across payments and orders. Diagnosed recurring 3 AM write stalls down to PostgreSQL checkpoint spikes on NVMe drives, tuned WAL buffers, and cut p99 write latency from 1.4s to 28ms while maintaining 99.995% uptime."*

---

## 📊 Before & After Comparison

| Dimension | AI Corporate Slop | Voice DNA Calibrated |
| :--- | :--- | :--- |
| **Verb Stance** | *Spearheaded, leveraged, orchestrated, synergized* | *Built, led, cut, deleted, diagnosed, tuned, shipped* |
| **Sentence Cadence** | Monotonous 28-word breathless run-ons | Natural variance: 11-word mean, punchy staccato verdicts |
| **Substance & Proof** | Abstract adjectives (*"mission-critical, robust, seamless"*) | Real production metrics (*"cut p99 latency from 1.4s to 28ms"*) |
| **ATS & Keyword Rigor** | Hollow generic buzzwords | High density of concrete technologies & architectures |
| **Coffee Table Test** | **FAILS**. Sounds like a corporate PR parody | **PASSES**. Sounds like an expert peer over coffee |

---

## ⚙️ The 3-Phase Engine

```
+-------------------------------------------------------------------------+
|                        THE 3-PHASE ENGINE                               |
+-------------------------------------------------------------------------+
|                                                                         |
|  [ Phase 1: Mine & Profile ]                                            |
|    • Ingests chat logs, Slack threads, commit history, or transcripts   |
|    • Automatically filters out AI assistant turns                       |
|    • Calculates sentence lengths, contraction rates, and idiom n-grams  |
|    • Generates a structured, persistent VOICE.md profile                |
|                                                                         |
|  [ Phase 2: Anti-Slop Calibration ]                                     |
|    • Scans drafts against the Banned Corporate Lexicon                  |
|    • Strips robotic AI throat-clearing ("In today's fast-paced...")     |
|    • Enforces active personal ownership ("I built", "We fixed")         |
|    • Computes a mathematical Slop Quotient (Target: 0.0%)              |
|                                                                         |
|  [ Phase 3: Dual-Constraint Ghostwriting ]                              |
|    • Constraint A (Substance & Rigor): Satisfies ATS/industry demands   |
|    • Constraint B (Voice Fidelity): Preserves personal human cadence    |
|    • Executes resumes, bios, case studies, and high-conversion outreach |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## 🚀 Quickstart

### 1. Installation

#### For Antigravity & AI Coding Assistants
Clone or copy into your local skills directory:

```bash
# Antigravity CLI / Global Skills
git clone https://github.com/your-username/voice-dna.git ~/.agents/skills/voice-dna
```

Or copy the folder into your project's `.agents/skills/voice-dna`.

#### Standalone Python CLI (Zero Dependencies)
`voice-dna` requires **Python 3.10+** and uses **only the standard library**:

```bash
git clone https://github.com/your-username/voice-dna.git
cd voice-dna
```

---

### 2. Extracting Your Voice Profile (`VOICE.md`)

Point the extractor at your raw writing, Slack/Discord exports, or LLM chat logs:

```bash
# Ingest raw text or post-mortem notes
python scripts/extract_voice.py \
  --input examples/sample-writing.txt \
  --output VOICE.md \
  --author "Alex Vance" \
  --role "Principal Systems Engineer" \
  --domain "Distributed Systems"

# Ingest chat transcript (JSON/JSONL automatically filters AI turns)
python scripts/extract_voice.py \
  --input examples/sample-chat-transcript.jsonl \
  --output VOICE.md \
  --author "Alex Vance"
```

The script analyzes:
- **Linguistic Cadence**: Mean sentence length, rhythm variance, staccato frequency.
- **Contraction Ratio**: Real human rate of `don't`, `it's`, `we've` vs stiff expansions.
- **Punctuation Fingerprint**: Em-dash count, semicolon frequency, parentheses usage.
- **Pronoun Ownership**: Ratio of `I` (direct accountability) to `we` (team attribution).
- **Anti-Slop Audit**: Verifies zero buzzwords in the source sample.

---

### 3. Ghostwriting with Antigravity / AI Coding Assistants

Once `voice-dna` is installed, your agent automatically activates it on natural triggers:
- *"Extract my voice from this chat history."*
- *"Rewrite my resume bullets using my VOICE.md profile."*
- *"Write an anti-slop executive bio for my personal website."*
- *"Audit this cover letter against the anti-slop dictionary."*

Example prompt in your editor or terminal:

```markdown
Read my VOICE.md profile and rewrite these 3 bullet points from my old CV.
Ensure every bullet follows Constraint A (ATS keywords, measurable deltas)
and Constraint B (my staccato cadence, active verbs, zero corporate slop).
```

---

## 📂 Repository Structure

```
voice-dna/
├── SKILL.md                          # Antigravity skill specification & triggers
├── README.md                         # Project documentation & anti-slop philosophy
├── LICENSE                           # MIT License
├── references/
│   ├── schema.md                     # Complete VOICE.md schema specification
│   ├── anti-slop-dictionary.md       # Banned buzzword blacklist & replacement lexicon
│   └── workflow.md                   # Step-by-step extraction & ghostwriting guide
├── scripts/
│   └── extract_voice.py              # Zero-dependency Python CLI extractor
└── examples/
    ├── VOICE.sample.md               # Realistic calibrated Voice DNA profile
    ├── cv-rewrite.md                 # Before/After CV bullet breakdowns
    ├── bio-rewrite.md                # Before/After executive bio breakdowns
    ├── sample-chat-transcript.jsonl  # Sample chat log for testing
    └── sample-writing.txt            # Sample engineering post-mortem
```

---

## 📖 The "Coffee Table Test"

Every sentence ghostwritten through `voice-dna` must pass the **Coffee Table Test**:

> Read the sentence aloud. Imagine sitting across a coffee table from a respected technical peer, holding a mug.
> - *Would you actually say this sentence to them?*
> - *Does it sound like your genuine rhythm?*
> - *Does it hide behind corporate jargon?*
> - *Can you prove every claim in an interview?*

If it sounds like marketing copy, reject it, strip the adjectives, and ground the verbs.

---

## 🤝 Contributing

Contributions are welcome! Please ensure:
1. All Python scripts remain **zero-dependency** (standard library only).
2. Any additions to `references/anti-slop-dictionary.md` must include the banned term, the reason why it is toxic, and concrete human alternatives.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
