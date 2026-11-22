# Voice DNA Operational Workflow

An end-to-end operational manual for executing the 3-phase Voice DNA engine:
1. **Mine & Profile**
2. **Anti-Slop Calibration**
3. **Dual-Constraint Ghostwriting**

---

```
                       +-----------------------------+
                       |    RAW HUMAN ARTIFACTS      |
                       | Chat logs, commits, drafts  |
                       +--------------+--------------+
                                      |
                                      v
                       +-----------------------------+
                       |   PHASE 1: MINE & PROFILE   |
                       |  Filter AI bot responses    |
                       |  Calculate cadence metrics  |
                       |  Detect idioms & values     |
                       |  Generate draft VOICE.md    |
                       +--------------+--------------+
                                      |
                                      v
                       +-----------------------------+
                       | PHASE 2: ANTI-SLOP AUDIT    |
                       |  Scan against dictionary    |
                       |  Compute Slop Quotient      |
                       |  Enforce active voice       |
                       +--------------+--------------+
                                      |
                                      v
                       +-----------------------------+
                       |  PHASE 3: DUAL-CONSTRAINT   |
                       |        GHOSTWRITING         |
                       |  [A] Substance & Rigor      |
                       |  [B] Voice Fidelity         |
                       +--------------+--------------+
                                      |
                                      v
                       +-----------------------------+
                       |   THE COFFEE TABLE TEST     |
                       | Passes human ear & ATS gate |
                       +-----------------------------+
```

---

## Phase 1: Mine & Profile

### Step 1.1: Gather Raw Human Artifacts
Collect unvarnished text written by the author when they were not actively trying to "sound professional." The best sources are:
- Technical chat logs (Slack threads, Discord channels, internal IRC).
- Pull request descriptions and git commit messages.
- Incident post-mortems and debugging scratchpads.
- Email threads arguing for or against a technical decision.
- Direct interview transcripts answering: *"Walk me through the worst outage you ever diagnosed."*

> [!IMPORTANT]
> **Filter Out Assistant Turns**: When ingesting LLM conversation logs (ChatGPT, Claude, Antigravity transcripts), you MUST strip out all AI assistant turns. Ingest ONLY the user's queries, arguments, and replies. The CLI tool `extract_voice.py` does this automatically.

### Step 1.2: Run the Quantitative Extractor
Execute the Python extraction script against the input files:

```bash
# Ingest chat transcript or writing sample
python scripts/extract_voice.py --input examples/sample-chat-transcript.jsonl --output VOICE.md --author "Alex Vance" --role "Principal Systems Engineer"
```

The script measures:
- **Average Words Per Sentence (WPS)** and standard deviation.
- **Sentence Length Distribution**: percentage of Short (<10w), Medium (10-25w), and Long (>25w) sentences.
- **Contraction Frequency**: ratio of natural contractions (`can't`, `it's`, `we'll`) vs expanded forms.
- **Punctuation Fingerprint**: em-dash count, semicolon frequency, parentheses frequency.
- **First-Person Ratio**: balance of `I` (individual accountability) vs `we` (collective team ownership).
- **Lexical Diversity & Recurring Idioms**: signature n-grams and unvarnished phrases.

### Step 1.3: Qualitative Calibration Interview (5 Questions)
If the raw text leaves gaps in philosophy or tone, prompt the author with these five questions:
1. *"When an outage happens at 2 AM, what is the very first thing you look at before touching any code?"*
2. *"What is one popular industry practice or buzzword that you believe is complete nonsense?"*
3. *"Tell me about a time you had to say 'no' to a client, manager, or executive."*
4. *"What is the most boring, unglamorous tool you rely on every day to get work done?"*
5. *"How would you describe your job to a bright 14-year-old without using abstract corporate nouns?"*

Merge the answers directly into **Dimension 5 (Core Philosophy & Signature Idioms)** of `VOICE.md`.

---

## Phase 2: Anti-Slop Calibration

Before ghostwriting any line, calibrate the system against [anti-slop-dictionary.md](anti-slop-dictionary.md).

### The Calibration Audit Checklist
1. **The Buzzword Scan**: Search for words like *spearhead*, *leverage*, *orchestrate*, *synergize*, *transformative*, *cutting-edge*, *mission-critical*. Flag and eliminate every match.
2. **The Filler Scrub**: Look for throat-clearing AI intros (*"In today's fast-paced world..."*, *"It is crucial to recognize..."*). Delete them.
3. **The Active Voice Audit**: Identify any sentence containing *"was [verb]ed"* without a clear subject. Replace with *"I [verb]ed"* or *"We [verb]ed"*.
4. **The Concreteness Rule**: Ensure every claim is anchored to a noun you can touch, compile, or query (e.g. `PostgreSQL query planner`, `Kubernetes node disk pressure`, `DNS propagation latency`).

---

## Phase 3: Dual-Constraint Ghostwriting

Ghostwriting succeeds only when it balances two opposing constraints simultaneously:

```
+------------------------------------------------------------------------+
|                     DUAL-CONSTRAINT DYNAMICS                           |
+------------------------------------------------------------------------+
| CONSTRAINT A: Substance & Rigor     | CONSTRAINT B: Voice Fidelity     |
| - ATS compatibility & keyword match | - Authentic sentence cadence     |
| - Measurable business/tech outcomes | - Personal contraction ratio     |
| - Clear scope of responsibility     | - Unvarnished direct vocabulary  |
| - Factually defensible details      | - Zero synthetic corporate fluff |
+------------------------------------------------------------------------+
```

### Document-Specific Ghostwriting Patterns

#### 1. Resumes & CVs
- **Traditional AI Slop**:
  > *"Spearheaded cross-functional incident triage for mission-critical enterprise platforms, driving synergy across DevOps and SRE teams to unlock operational resilience."*
- **Constraint A (Substance)**: Needs tools, metrics, team size, outcome.
- **Constraint B (Voice DNA)**: Needs short cadence, blunt verbs, concrete nouns.
- **Voice DNA Output**:
  > *"Led on-call triage for 14 core payment services across 5 SREs. Traced memory leak to unindexed Redis consumer groups and dropped p99 tail latency from 1.2s to 85ms."*

#### 2. Professional Bio (Website / LinkedIn / Speaker)
- **Traditional AI Slop**:
  > *"A passionate, forward-thinking engineering leader dedicated to crafting bespoke digital experiences and leveraging cutting-edge cloud architectures to empower global teams."*
- **Voice DNA Output**:
  > *"I build distributed backends that don't fall over when traffic spikes. Over the past twelve years, I've run infrastructure for high-throughput payment systems, debugged kernel locks at 3 AM, and deleted more code than I've written. My rule is simple: if you can't measure it in production logs, it's just an opinion."*

#### 3. Project Case Studies
- Follow the 4-beat structure:
  1. **The Reality**: What was broken or unmanageable?
  2. **The Investigation**: What did the logs, profiler, or users actually show?
  3. **The Intervention**: What did we rip out, rewrite, or automate?
  4. **The Ground Truth**: What were the real metrics after deployment?

#### 4. Cold Outreach / Inquiries
- Cap at 120 words.
- Sentence 1: The exact reason for the message (no pleasantries like *"Hope this finds you well"*).
- Sentence 2–3: Direct value proposition backed by a specific past benchmark.
- Sentence 4: Low-friction ask with a clear exit ("If not, no worries at all").

---

## The Verification Gate: The "Coffee Table Test"

Before delivering any ghostwritten draft to the user, run the final verification:

> **The Coffee Table Test**:
> Read the text aloud. Imagine the author sitting across a small coffee table, holding a mug, talking to a respected peer.
> 
> - *Would they say these words?*
> - *Does it sound like their natural cadence?*
> - *Does it make you cringe with corporate jargon?*
> - *Can every factual claim be backed up in a technical interview?*

If the text sounds like a marketing brochure, it fails. Return to Phase 2, strip the adjectives, tighten the sentence lengths, and ground the verbs.
