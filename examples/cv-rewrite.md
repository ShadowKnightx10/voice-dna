# Before & After: CV / Resume Rewrites

This case study demonstrates how `voice-dna` transforms generic AI corporate slop into high-impact, ATS-optimized, authentic engineering bullets using Alex Vance's Voice DNA profile.

---

## Example 1: Database Migration & Incident Triage

### ❌ The AI Corporate Slop Version
> *"Spearheaded cross-functional incident triage and cloud modernization initiatives across mission-critical enterprise database clusters, leveraging cutting-edge PostgreSQL paradigms and synergizing DevOps teams to unlock robust operational excellence and drive transformative uptime improvements."*

#### Why It Fails:
- **Slop Words**: *Spearheaded, incident triage, mission-critical, enterprise, leveraging, cutting-edge, paradigms, synergizing, robust, operational excellence, transformative*.
- **Information Density**: Near zero. What broke? What version of PostgreSQL? How big was the cluster? Did uptime improve from 95% to 99% or 99.9% to 99.99%?
- **Tone**: Sounds like a marketing bot generated a satirical corporate parody.

---

### ✅ The Voice DNA Calibrated Version
> *"Led on-call triage for 16 production database nodes across payments and orders. Diagnosed recurring 3 AM write stalls down to PostgreSQL checkpoint spikes on NVMe drives, tuned WAL buffers, and cut p99 write latency from 1.4s to 28ms while keeping 99.995% uptime."*

#### Why It Wins:
- **Constraint A (Substance & ATS Rigor)**: Hits exact technical keywords (`PostgreSQL`, `checkpoint`, `WAL buffers`, `NVMe`, `p99 latency`, `uptime SLA`).
- **Constraint B (Voice Fidelity)**: Matches Alex's staccato cadence (average 11.5 words per sentence), uses grounded verbs (*led*, *diagnosed*, *tuned*, *cut*), and conveys authentic engineering realism (*"recurring 3 AM write stalls"*).

---

## Example 2: Architecture Simplification & Microservices

### ❌ The AI Corporate Slop Version
> *"Orchestrated a holistic architectural paradigm shift, championing microservice decoupling and empowering distributed engineering cohorts to streamline deployment velocity and foster a resilient cloud-native ecosystem."*

#### Why It Fails:
- **Slop Words**: *Orchestrated, holistic, architectural paradigm shift, championing, empowering, cohorts, streamline, foster, resilient, cloud-native ecosystem*.
- **The Lie**: Conceals whether the candidate actually wrote code or just sat in architecture steering meetings.

---

### ✅ The Voice DNA Calibrated Version
> *"Ripped out 8 unnecessary microservices and merged them back into a modular Go core service. Deleted 24,000 lines of brittle RPC glue code, reduced CI build times from 28 minutes to 4 minutes, and halved our monthly AWS ECS spend."*

#### Why It Wins:
- **Constraint A (Substance & ATS Rigor)**: High-dollar business impact (`AWS ECS spend halved`, `CI build time cut by 85%`), clear scale (`24,000 lines deleted`, `Go`).
- **Constraint B (Voice Fidelity)**: Pure Alex Vance. Embodies his core belief: *"The fastest code in production is the code you deleted."*

---

## Example 3: Kafka Streaming & Message Backpressure

### ❌ The AI Corporate Slop Version
> *"Leveraged best-in-class event-driven message architectures, seamlessly navigating streaming backpressure challenges to empower high-throughput data processing workflows with unparalleled reliability."*

#### Why It Fails:
- **Slop Words**: *Leveraged, best-in-class, event-driven, seamlessly navigating, empower, workflows, unparalleled reliability*.
- **Empty Vagueness**: "High-throughput" without numbers means nothing to a hiring manager.

---

### ✅ The Voice DNA Calibrated Version
> *"Built a custom partition consumer in Rust for our Kafka ingestion pipeline. Fixed a memory leak in thread-pool allocation that was crashing consumer groups under peak load; handled 180,000 events/sec steady-state with zero message loss."*

#### Why It Wins:
- **Constraint A (Substance & ATS Rigor)**: Specific language (`Rust`, `Kafka`, `partition consumer`, `thread-pool allocation`), verified throughput (`180,000 events/sec`).
- **Constraint B (Voice Fidelity)**: Direct, unadorned ownership (*"Built"*, *"Fixed"*, *"Handled"*).

---

## Quick Comparison Table

| Metric | AI Slop Version | Voice DNA Version |
| :--- | :--- | :--- |
| **Slop Word Count** | 28 buzzwords across 3 bullets | **0 buzzwords** |
| **Concrete Production Numbers** | 0 metrics | **8 verified metrics** |
| **Average Sentence Length** | 28 words (rambling run-on) | **12 words (clean, punchy)** |
| **Recruiter / ATS Keyword Score**| Generic noise | **High density (Go, Rust, Postgres, Kafka, WAL)** |
| **Coffee Table Test** | Fails completely (sounds like a bot) | **Passes 100% (sounds like an expert peer)** |
