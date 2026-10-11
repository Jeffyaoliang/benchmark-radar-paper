# Theme-coverage analysis

Agent-benchmark research is not spread evenly across capabilities. In the
XBsleepy digest's frozen v0.11.0 cut — 1,103 agent-benchmark papers announced
between 2026-01-01 and 2026-09-04 — **planning (419 papers, 38% of the corpus),
tool-use (391, 35%) and safety (295, 27%) together carry 52% of every
capability tag**, while the physical and organisational corners are
near-empty: embodied and robot-agent evaluation holds 38 papers (3%),
workplace 20, mobile 13, and recursive self-improvement 2. For a reader
deciding where a new benchmark can still matter, that tail is the finding:
the literature's centre of gravity is LLM agents that plan and act inside
software environments, and a benchmark aimed at the sparse end would be novel
rather than incremental.

The radar's own taxonomy cannot show this on its own. It classifies records by
*what they are* — benchmark, evaluation, dataset — which answers "is this a
benchmark?" but not "what does this benchmark test?". The digest supplies
exactly that second layer, and this folder measures it and where the two
layers meet.

This is a **source-side audit of one external curated feed**, not a corpus
count. The paper's full-corpus baseline (1,259+ records across 4+ sources) is
untouched here; every number below describes the digest's own corpus and says
so.

## Contents

- `scripts/theme_coverage.py` — the reproducible analysis. Two public inputs,
  both frozen and hash-pinned (see below); no credentials, no network. Writes
  `coverage.md` and `themes_coverage.svg` here, and **refuses to run** if
  either input's SHA-256 differs from the pins in the script, so a committed
  table can never quietly describe a corpus that moved on.
- `coverage.md` — generated tables: theme distribution, record-type vs
  capability layers, concentration and gaps, monthly arrivals, assigned field.
- `themes_coverage.svg` — papers per capability theme.
- `REPORT_SECTION_DRAFT.md` — draft technical-report section built on those
  numbers, for the co-authors to edit.

## Data cut

- **Digest index**: `XBsleepy/daily-agent-benchmarks` commit
  `23617ba4aa1b53489d2b8fe36946c656e5870036` (2026-09-07T18:39:57Z), the last
  index update on or before the paper's 2026-09-07 discovery cutoff.
  SHA-256 `f44bf9f8df8a611efb31f1b5bdaa6b814e796bef10e2110edd0bd9c214a492d0`.
- **Radar snapshots**: the 46 discovery snapshots
  (2026-07-23 .. 2026-09-07) inside the v0.11.0 release archive
  `benchmark-radar-paper-data-v0.11.0.zip`, whose per-file hashes are recorded
  in that archive's `release-data.json`. Directory SHA-256
  `fb7c995a0ffd9f882e8b05a8bded8466c2af642821ceb7a4fb0e9fbb558ebb75`.
- **Software**: Benchmark Radar v0.11.0, commit
  `8f46bbfa91f5d9900c8b08a5d552c3df5c9597b0`.

## What remains uncertain

- **Theme assignment is the digest's own.** A two-stage classifier in the
  digest tags each paper with capability themes, multi-label. Those labels
  were not re-derived or spot-checked here, so mislabels propagate into every
  count.
- **The cut is a commit, not a wall clock.** The digest index is cumulative,
  so a paper announced before 2026-09-07 but ingested by the digest after that
  commit is absent from this cut by construction. Freezing at the cutoff
  commit is what keeps the numbers reproducible; it also means the corpus here
  is "what the digest knew at the cutoff", not "everything announced by then".
- **September is partial** in every table (22 papers against 147 in August),
  and the monthly series should not be read as a rate beyond August.

## Reproduce

From a clean checkout of this repository, with the two frozen inputs on disk:

```bash
python3 scripts/theme_coverage.py \
  <digest index.json at 23617ba> \
  <v0.11.0 archive>/data/snapshots \
  analysis/theme-coverage
```

The script prints `coverage.md` and rewrites it plus `themes_coverage.svg` in
the output directory. A SHA-256 mismatch on either input aborts with the
expected and actual hashes named.
