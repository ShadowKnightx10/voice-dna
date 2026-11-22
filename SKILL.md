---
name: voice-dna
description: >-
  Anti-slop personal voice extractor and ghostwriter. Extracts a human's
  linguistic fingerprint (cadence, vocabulary, directness, signature idioms) from
  conversation logs, transcripts, or raw writing into a persistent VOICE.md, and
  ghostwrites professional documents (CVs, bios, portfolios, cold emails) that
  preserve authentic human tone while meeting ATS and industry rigor.
triggers:
  - "voice dna"
  - "extract voice"
  - "voice.md"
  - "anti-slop"
  - "anti slop"
  - "anti-slop ghostwriter"
  - "write in my voice"
  - "rewrite resume in my voice"
  - "rewrite cv in my voice"
  - "sound like me"
  - "personal voice extractor"
  - "anti-slop resume"
  - "anti-slop bio"
---

# Voice DNA: Anti-Slop Personal Voice Extractor & Ghostwriter

Most AI assistants write professional documents using synthetic corporate slop: *"spearheaded cross-functional incident triage"*, *"leveraged synergies across mission-critical paradigms"*, *"passionate visionary dedicated to unlocking transformative value"*.

`voice-dna` replaces this synthetic sludge with an individual's authentic linguistic fingerprint. It executes a rigorous 3-phase engine to mine unvarnished speech, establish a persistent `VOICE.md` profile, and ghostwrite documents that satisfy both ATS/industry rigor and human authenticity.

---

## The 3-Phase Engine

```
[Phase 1: Mine & Profile] ---> [Phase 2: Anti-Slop Calibration] ---> [Phase 3: Dual-Constraint Ghostwriting]
```

### Phase 1: Mine & Profile (Extracting Authentic Voice)

When a user asks to extract their voice, create a `VOICE.md`, or analyze their writing style:

1. **Ingest Raw Human Artifacts**:
   - Ask for or locate raw conversational samples: chat logs (Slack/Discord), meeting transcripts, PR descriptions, commit logs, incident post-mortems, or unedited draft notes.
   - If using LLM chat exports (ChatGPT, Claude, Antigravity logs), **strip out assistant turns**. Profile only what the human typed.
2. **Execute the Quantitative Extractor**:
   Run the zero-dependency Python script to calculate statistical cadence metrics:
   ```bash
   python scripts/extract_voice.py --input path/to/sample.txt --output VOICE.md --author "[Name]" --role "[Target Role]"
   ```
   - For machine-readable output: `python scripts/extract_voice.py --input path/to/sample.jsonl --json`
3. **Calibrate Qualitative Dimensions**:
   Read [references/schema.md](references/schema.md) and verify the 6 core dimensions:
   - **Dimension 1: Linguistic Cadence**: Sentence lengths, variance, rhythm patterns, contractions, punctuation habits.
   - **Dimension 2: Tone Spectrum**: Directness (1-10), Formality (1-10), Wit/Dryness (1-10), Warmth (1-10), Skepticism (1-10), Ego baseline.
   - **Dimension 3: Vocabulary & Jargon**: Concrete nouns vs abstract nouns, active mechanical verbs, metric specificity.
   - **Dimension 4: Anti-Slop Safeguards**: Active voice enforcement, zero corporate buzzwords.
   - **Dimension 5: Problem-Solving DNA**: Core dogmas, diagnostic habits, signature idioms mined from chat.
   - **Dimension 6: Document Adaptations**: Specific rules for CVs, Bios, Case Studies, Outreach.
4. **Persist the Profile**: Save or update `VOICE.md` in the user's workspace root or project folder.

---

### Phase 2: Anti-Slop Calibration (The Sanitization Gate)

Before producing or polishing any document, run every draft against [references/anti-slop-dictionary.md](references/anti-slop-dictionary.md):

1. **Banned Word Elimination**:
   - Eliminate all instances of: *spearheaded, leveraged, orchestrated, synergized, navigated, championed, empowered, fostered, ideated, operationalized, cutting-edge, mission-critical, robust, seamless, holistic, best-in-class, transformative, bespoke, dynamic, pivotal*.
   - Replace with grounded, active verbs: *built, led, ran, cut, deleted, rewrote, shipped, diagnosed, fixed, benchmarked, profiled*.
2. **AI Filler Scrubbing**:
   - Delete throat-clearing openings (*"In today's fast-paced digital world..."*, *"It is essential to note that..."*).
   - Strip AI stylistic markers (*"tapestry"*, *"beacon"*, *"delve"*, *"testament to"*).
3. **Active Personal Voice Mandate**:
   - Flag passive evasions (*"Initiatives were implemented"*, *"Optimizations were achieved"*).
   - Require clear ownership: *"I redesigned the cache topology and cut API latency by 45%"*.
4. **Calculate Slop Index**:
   Ensure the final text achieves an Anti-Slop grade of **A+ (0.0% buzzwords)**.

---

### Phase 3: Dual-Constraint Ghostwriting

When ghostwriting or rewriting resumes, bios, case studies, or pitches, apply both constraints simultaneously:

```
+-------------------------------------------------------------------------+
|                        DUAL-CONSTRAINT BALANCE                          |
+-------------------------------------------------------------------------+
| CONSTRAINT A: Substance & Rigor       | CONSTRAINT B: Voice Fidelity    |
| - Satisfies recruiter/ATS keywords    | - Matches sentence cadence      |
| - Measurable business & tech outcomes | - Uses personal contractions    |
| - Clear scope of technical ownership  | - Reflects signature idioms     |
| - Zero factual hallucination          | - Sounds like a peer at a table |
+-------------------------------------------------------------------------+
```

#### Document Recipes

##### 1. Resume / CV Bullets
- **Formula**: `[Direct Mechanical Verb] + [Specific System / Scope] + [Measurable Delta / Production Ground Truth]`
- **Tone**: High directness, low formality, zero buzzwords, concrete metrics.
- **Example**:
  - ❌ *Slop*: *"Spearheaded cross-functional incident response across mission-critical systems, driving operational resilience."*
  - ✅ *Voice DNA*: *"Led on-call response for 12 payment microservices. Traced recurring memory leak to Redis connection pooling; dropped p99 latency from 1.1s to 75ms."*

##### 2. Executive / Professional Bios
- **Structure**: Direct identity statement -> Concrete technical problems enjoyed -> Proven track record with numbers -> Pragmatic operating rule.
- **Tone**: Quiet authority across a table. Reads like an introduction, not a PR wire release.

##### 3. Case Studies & Portfolios
- **Structure**: The Mess (system before) -> The Triage (what logs showed) -> The Cut (what was deleted/rewritten) -> The Ground Truth (production metrics).
- **Tone**: Technical honesty, acknowledging messy realities and real trade-offs.

##### 4. Cold Outreach & Pitches
- **Length**: Under 120 words.
- **Rules**: Zero pleasantries (*"Hope you're well"* -> deleted). Immediate relevance, one concrete proof point, low-friction close.

---

## Verification: The Coffee Table Test

Before presenting any output to the user, conduct the final verification:

> **The Coffee Table Test**:
> Read the draft aloud. Imagine the author sitting across a coffee table, holding a mug, speaking to a respected peer.
> 1. *Would they actually say this sentence out loud?*
> 2. *Does it match the sentence length and contraction habits in their `VOICE.md`?*
> 3. *Does it contain a single word from the banned buzzword list?*
> 4. *Can every claim be defended under rigorous technical questioning?*

If any answer is unsatisfactory, strip the adjectives, split compound sentences, and ground the claims in verifiable facts.
