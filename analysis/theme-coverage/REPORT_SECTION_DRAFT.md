# Capability-theme coverage of the agent-benchmark literature

*Draft section for the Benchmark Radar technical report — evidence backing:
`scripts/theme_coverage.py`, reproducible from two frozen public inputs (the
XBsleepy digest index at upstream commit `23617ba` and the radar discovery
snapshots shipped in the v0.11.0 release archive). All numbers below are from
that cut: 1,103 digest papers announced 2026-01-01 .. 2026-09-04, and the 46
snapshots of 2026-07-23 .. 2026-09-07. This is an audit of one external
curated feed's own taxonomy, not a count of the radar's corpus.*

---

## What the digest adds: capability themes over record types

The radar's own snapshot taxonomy classifies records by **what they are** —
of 19,961 category sightings across the frozen snapshots, 7,727 are
`benchmark`, 5,343 `evaluation`, 5,108 `dataset`, 1,679 `agentic`, and 104
`data_quality`. This answers "is this a benchmark?" but not "what does this
benchmark test?". The XBsleepy digest supplies exactly that second layer: a
two-stage classifier tags each agent-benchmark paper with capability themes
(planning, tool-use, safety, coding, multimodal, memory, and eleven more),
and the radar ingests those tags as source-native labels. The two layers are
complementary rather than overlapping. A reader-facing browse page over the
source themes is proposed in software-repo pull request #638; until that
lands, the join between the layers exists only in this analysis.

## Distribution

The digest corpus spans 1,103 agent-benchmark papers announced between
2026-01-01 and 2026-09-04, carrying 1.94 theme labels on average. Coverage is
heavily concentrated: the top three themes — planning (419 papers, 38% of
papers), tool-use (391, 35%), and safety (295, 27%) — account for 52% of all
theme labels. The strongest co-occurrences are planning+tool-use (163
papers), safety+tool-use (122), and planning+safety (117): the literature's
center of gravity is LLM agents that plan and act in software environments,
measured for capability and for safety. A mid tier follows (coding 177,
multimodal 161, memory 150, multi-agent 123, science 89), and the tail thins
fast: web (48), conversation (43), computer-use (40), embodied (38),
workplace (20), mobile (13), and recursive self-improvement (2).

## Gaps

The sparse end of the distribution is arguably its most decision-useful
signal. Embodied and robot-agent evaluation — benchmarks where an agent acts
on a physical world through a robot rather than a browser or a terminal —
amount to 38 papers, 3% of the corpus, against 419 for planning. Workplace,
mobile, and recursive-self-improvement coverage is thinner still. For a
reader deciding where a new benchmark can matter, these are the open areas;
for the radar, they are the themes where a new digest or source would add
the most coverage.

## Trend

Monthly arrivals of tagged papers grew from January (74 papers, 31 of them
carrying the planning label) to a May peak (229 papers, 91 planning), then
settled at 143–175 per month through August. The September figures are
partial at the cutoff (22 papers) and should not be read as a rate. Nothing
in the trend through August suggests saturation of the digest itself: it kept
finding new agent benchmarks at well over a hundred papers per month across
the whole window.

---

*Reproducibility: `python3 scripts/theme_coverage.py <digest index.json at
23617ba> <v0.11.0 archive>/data/snapshots analysis/theme-coverage` — no
credentials, no network. The script aborts if either input's SHA-256 differs
from the pins recorded in it and in `README.md`. The manuscript's own
capability figure (`fig:taxonomy-sankey`) covers the full catalog; this
analysis deliberately ships tables only.*
