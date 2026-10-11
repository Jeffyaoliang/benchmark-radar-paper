# Capability-theme coverage: XBsleepy digest corpus

Corpus: 1103 agent-benchmark papers, 2026-01-01 .. 2026-09-04 (announced dates). Multi-label themes per paper.

## Frozen inputs

- Digest index: upstream commit `23617ba4aa1b53489d2b8fe36946c656e5870036` (2026-09-07T18:39:57Z), SHA-256 `f44bf9f8df8a611efb31f1b5bdaa6b814e796bef10e2110edd0bd9c214a492d0`.
- Radar snapshots: v0.11.0 release archive, 46 files (2026-07-23 .. 2026-09-07), dir SHA-256 `fb7c995a0ffd9f882e8b05a8bded8466c2af642821ceb7a4fb0e9fbb558ebb75`.
- Software commit: `8f46bbfa91f5d9900c8b08a5d552c3df5c9597b0` (v0.11.0).

## Theme distribution

| Theme | Papers | Share |
|---|---:|---:|
| planning | 419 | 38% of papers |
| tool-use | 391 | 35% of papers |
| safety | 295 | 27% of papers |
| coding | 177 | 16% of papers |
| multimodal | 161 | 15% of papers |
| memory | 150 | 14% of papers |
| multi-agent | 123 | 11% of papers |
| science | 89 | 8% of papers |
| gui | 72 | 7% of papers |
| research | 59 | 5% of papers |
| web | 48 | 4% of papers |
| conversation | 43 | 4% of papers |
| computer-use | 40 | 4% of papers |
| embodied | 38 | 3% of papers |
| workplace | 20 | 2% of papers |
| mobile | 13 | 1% of papers |
| rsi | 2 | 0% of papers |

Average themes per paper: 1.94.

## Radar record-type vs digest capability coverage

The radar's snapshot categories count records by TYPE (total tagged sightings: 19961):

| Radar category | Sightings |
|---|---:|
| benchmark | 7727 |
| evaluation | 5343 |
| dataset | 5108 |
| agentic | 1679 |
| data_quality | 104 |

The digest adds the layer the radar's own taxonomy does not carry: WHICH capability an agent benchmark tests. The two are complementary, not overlapping.

## Concentration and gaps

- Top-3 themes (planning, tool-use, safety) cover 52% of all tags.
- Sparsest themes: embodied (38), workplace (20), mobile (13), rsi (2) -- candidate open areas for new benchmarks.
- Strongest theme pairs: planning+tool-use (163), safety+tool-use (122), planning+safety (117), multimodal+planning (94).

## Monthly arrivals, top themes

| Theme | 2026-01 | 2026-02 | 2026-03 | 2026-04 | 2026-05 | 2026-06 | 2026-07 | 2026-08 | 2026-09 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| planning | 31 | 44 | 41 | 55 | 91 | 58 | 41 | 49 | 9 |
| tool-use | 27 | 30 | 33 | 45 | 85 | 53 | 59 | 55 | 4 |
| safety | 23 | 35 | 20 | 34 | 59 | 43 | 41 | 37 | 3 |
| coding | 8 | 14 | 17 | 16 | 45 | 20 | 33 | 19 | 5 |
| multimodal | 10 | 10 | 21 | 21 | 38 | 26 | 14 | 16 | 5 |
| memory | 9 | 15 | 11 | 9 | 38 | 23 | 20 | 22 | 3 |
| multi-agent | 5 | 12 | 15 | 23 | 28 | 17 | 6 | 17 | 0 |
| science | 4 | 10 | 7 | 12 | 18 | 16 | 15 | 6 | 1 |

## Assigned field (single-label, digest classifier)

- other: 451
- coding: 159
- multi-agent: 95
- multimodal: 82
- workplace: 56
- computer-use: 56
- safety: 39
- science: 37
- tool-use: 34
- web: 33
- conversation: 29
- embodied: 20
- mobile: 9
- rsi: 3
