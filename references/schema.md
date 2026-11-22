# VOICE.md Schema Specification (`voice-dna` v1.0.0)

A structured specification for capturing, calibrating, and applying a human being's authentic linguistic fingerprint. 

The goal of this schema is to replace synthetic "corporate slop" with grounded, direct, and factually defensible writing that satisfies professional rigor without sacrificing the author's personality.

---

## 1. Document Structure & Frontmatter

Every `VOICE.md` profile must begin with metadata:

```yaml
---
version: 1.0.0
author: "[Full Name]"
handle: "[GitHub/Twitter handle or email]"
target_role: "[e.g. Principal Distributed Systems Engineer / VP of Product]"
primary_domain: "[e.g. Backend Infrastructure, Developer Tooling, Distributed DBs]"
created_at: "[YYYY-MM-DD]"
updated_at: "[YYYY-MM-DD]"
calibration_source: "[e.g. 14 commit logs, 3 Slack threads, 2 raw post-mortems]"
---
```

---

## 2. Core Dimensions

A complete Voice DNA profile models six interlocking dimensions:

```
+-----------------------------------------------------------------------+
|                              VOICE DNA                                |
+-----------------------------------------------------------------------+
| 1. Linguistic Cadence        | Sentence lengths, rhythm, contractions |
| 2. Tone Spectrum             | Directness, wit, warmth, skepticism    |
| 3. Vocabulary & Specificity  | Grounded nouns, metric rules, verbs   |
| 4. Anti-Slop Safeguards      | Blacklist, AI markers, passive voice   |
| 5. Core Philosophy & Idioms  | Mental models, diagnostic habits       |
| 6. Ghostwriting Adaptations  | Resumes, Bios, Case Studies, Pitches   |
+-----------------------------------------------------------------------+
```

---

### Dimension 1: Linguistic Cadence

Defines the physical rhythm and musicality of the author's sentences.

| Attribute | Range / Type | Description |
| :--- | :--- | :--- |
| `avg_words_per_sentence` | Float (e.g., 11.4) | Mean words per sentence in unvarnished speech. |
| `sentence_variance` | Low / Medium / High | High variance indicates intentional pacing shifts (staccato punches followed by detailed mechanics). |
| `staccato_threshold` | Integer (e.g., ≤ 6 words) | Frequency of short, punchy declarative statements. |
| `contraction_ratio` | Percentage (0% - 100%) | Natural rate of contractions ("don't", "can't", "we've" vs "do not", "cannot"). |
| `punctuation_habits` | Key-value pairs | Frequency and preference for em-dashes (`—`), semicolons (often 0 in natural speech), parentheses for dry side-commentary, and ellipses. |
| `fragment_tolerance` | Never / Rare / Frequent | Willingness to use deliberate sentence fragments for punchiness (e.g., "Not ideal. But functional."). |

#### Example Profile Block
```markdown
### 1. Linguistic Cadence
- **Mean sentence length**: 12 words (tight, muscular).
- **Rhythm**: High variation. A 4-word verdict followed by a 22-word technical explanation.
- **Contraction rate**: ~88%. Rarely expands to "do not" unless emphasizing a hard boundary.
- **Punctuation**: Heavy em-dash usage for explanatory pivots; frequent parentheses for candid observations; absolute zero semicolons.
- **Fragments**: Allowed in case studies and bios to emphasize turning points.
```

---

### Dimension 2: Tone Spectrum

Calibrates emotional and social registers on an objective 1–10 scale.

| Dimension | Scale (1–10) | Low (1) | High (10) |
| :--- | :--- | :--- | :--- |
| **Directness** | 1 (Diffident/Evasive) | Diplomatic euphemisms | Direct, unflinching clarity |
| **Formality** | 1 (Casual/Colloquial) | Fireside chat, slang | Academic paper, legal brief |
| **Wit & Dryness** | 1 (Deadpan/Solemn) | Unsmiling, purely literal | Dry, understated sarcasm |
| **Warmth** | 1 (Austere/Detached) | Clinical, cold mechanics | Relational, empathetic, encouraging |
| **Skepticism** | 1 (Credulous/Optimistic)| Trusting claims on face | Demands benchmark logs and diffs |
| **Ego Baseline** | 1 (Self-effacing) | Erases personal impact | Unabashed self-promoter |

#### Golden Rule for Ego Baseline
Target an **Ego Score of 5–6 (Grounded Technical Authority)**: Never boast with abstract superlatives ("visionary leader"), but unapologetically claim factual technical ownership ("I diagnosed the thread lock and rewrote the connection pool").

---

### Dimension 3: Jargon Tolerance & Grounded Vocabulary

Eliminates fuzzy abstraction in favor of concrete mechanics.

- **Noun Concrete Ratio**: Minimum 85% concrete technical nouns (e.g., `PostgreSQL connection pool`, `WAL buffer`, `etcd leases`) versus abstract nouns (`synergy`, `paradigm`, `transformation`).
- **Verb Stance**: Favor blunt mechanical verbs (`fixed`, `cut`, `deleted`, `audited`, `rewrote`, `benchmarked`, `shipped`) over inflated corporate euphemisms (`spearheaded`, `facilitated`, `championed`, `leveraged`).
- **Specificity Rule**: Never write that an architecture was "optimized"; specify *what* was measured, *where* the bottleneck lived, and *what* the delta was.

---

### Dimension 4: Anti-Slop Safeguards (Zero-Tolerance Rules)

Hard constraints enforced on every generated line:

1. **The Banned Buzzword Filter**: Complete exclusion of all words in [anti-slop-dictionary.md](anti-slop-dictionary.md).
2. **No AI Structural Clichés**:
   - Ban: "In today's fast-paced digital landscape..."
   - Ban: "It's important to remember that..."
   - Ban: "A testament to..."
   - Ban: "Delve into...", "Unlock...", "Tapestry...", "Beacon..."
3. **Active Personal Voice**:
   - Prohibit passive evasions ("Efforts were undertaken to reduce latency").
   - Mandate human ownership ("We profiled queries and dropped index overhead").
4. **No Unbacked Adjectives**:
   - Every adjective must be substantiated by a preceding or subsequent metric or architectural fact. If a system is described as "resilient", the text must explain *how* it survived failure (e.g., "survived a 3-node partition without dropping writes").

---

### Dimension 5: Core Philosophy & Problem-Solving DNA

Captures how the person thinks, reasons, and solves problems in high-pressure situations:

- **Engineering / Product Beliefs**: What dogmas does this person hold? (e.g., "The fastest code is code that never runs", "Boring technology runs the world", "Clear logs beat clever abstractions").
- **Diagnostic Habit**: What is their first instinct when things break? (e.g., "Look at raw disk I/O before guessing at code bugs").
- **Signature Sayings / Idioms**: Authentic turns of phrase mined from their chat logs (e.g., *"Don't reboot and pray"*, *"Measure at the p99 or you're lying to yourself"*).
- **War Stories**: 2–3 brief factual anecdotes that encapsulate their problem-solving philosophy.

---

### Dimension 6: Document Ghostwriting Adaptations

Instructions for translating the Voice DNA profile into specific document formats:

#### A. Resume / CV Bullets
- Formula: `[Direct Action Verb] + [Specific Mechanism / Problem] + [Measurable Delta or Concrete Outcome]`
- Tone: High directness, low formality, zero buzzwords, maximum metric density.
- Rule: Replace every "Spearheaded X" with what actually happened ("Led a 4-person migration of 12TB Postgres cluster with zero downtime").

#### B. Executive / Professional Bios
- Tone: Conversational authority. Reads like an introduction across a table, not a press release.
- Structure: Who they are without pomp -> What problems they actually enjoy solving -> Concrete track record -> Personal quirk/philosophy.

#### C. Case Studies & Portfolios
- Structure: The Mess (Reality before) -> The Triage (What was observed) -> The Cut (What was removed/built) -> The Benchmark (Real-world outcome).
- Tone: Technical honesty, acknowledging setbacks and pragmatic compromises.

#### D. Cold Outreach & Pitches
- Length: Under 150 words.
- Structure: Immediate hook (relevance) -> Direct point of value -> Low-friction ask.
- Tone: Respectful, completely un-salesy, peer-to-peer.
