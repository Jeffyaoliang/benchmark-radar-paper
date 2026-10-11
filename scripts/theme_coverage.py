#!/usr/bin/env python3
"""Capability-theme coverage of the XBsleepy digest, cut at the paper's frozen inputs.

Evidence for the technical report's collaboration call (software-repo issue
#447): what the digest's capability-theme taxonomy adds to the radar's own
record-type categories, where agent-benchmark activity concentrates, and
which capability areas stay near-empty.

This is a source-side audit of ONE external curated feed, not a corpus count.
The paper's full-corpus baseline (1,259+ records across 4+ sources) is
untouched here; the digest's papers are one source's own taxonomy over its own
corpus, and every number below says so.

Inputs are frozen and hash-pinned, per the README's v0.11.0 cutoff rule:

  1. The digest's ``docs/data/index.json`` at upstream commit
     ``23617ba4aa1b53489d2b8fe36946c656e5870036`` (2026-09-07T18:39:57Z), the
     last index update on or before the 2026-09-07 discovery cutoff.
  2. The radar discovery snapshots shipped inside the v0.11.0 release archive
     ``benchmark-radar-paper-data-v0.11.0.zip`` (46 files, 2026-07-23 through
     2026-09-07), whose per-file hashes are recorded in that archive's
     ``release-data.json``.

The script refuses to run against inputs whose SHA-256 differs from the pins
below, so a committed table can never quietly describe a corpus that moved.
No credentials, no network.
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

PAPER = Path(__file__).resolve().parents[1]

DIGEST_COMMIT = "23617ba4aa1b53489d2b8fe36946c656e5870036"
DIGEST_SHA256 = "f44bf9f8df8a611efb31f1b5bdaa6b814e796bef10e2110edd0bd9c214a492d0"
SNAPSHOT_COUNT = 46
SNAPSHOTS_SHA256 = "fb7c995a0ffd9f882e8b05a8bded8466c2af642821ceb7a4fb0e9fbb558ebb75"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_snapshot_dir(directory: Path) -> tuple[int, str]:
    digest = hashlib.sha256()
    paths = sorted(directory.glob("*.json"))
    for path in paths:
        digest.update(sha256_file(path).encode())
        digest.update(path.name.encode())
    return len(paths), digest.hexdigest()


def load_digest(path: Path) -> list[dict]:
    found = sha256_file(path)
    if found != DIGEST_SHA256:
        raise SystemExit(
            f"digest index {path} hashes to {found}, expected {DIGEST_SHA256} "
            f"(upstream commit {DIGEST_COMMIT}); refusing to describe a moved corpus"
        )
    payload = json.loads(path.read_text(encoding="utf-8"))
    papers = payload["papers"]
    return [paper for paper in papers if isinstance(paper, dict)]


def radar_record_types(directory: Path) -> Counter:
    count, found = sha256_snapshot_dir(directory)
    if count != SNAPSHOT_COUNT or found != SNAPSHOTS_SHA256:
        raise SystemExit(
            f"snapshot dir {directory} has {count} files hashing to {found}, "
            f"expected {SNAPSHOT_COUNT} files hashing to {SNAPSHOTS_SHA256} "
            "(the v0.11.0 release archive); refusing to describe a moved corpus"
        )
    counts: Counter = Counter()
    for path in sorted(directory.glob("*.json")):
        snapshot = json.loads(path.read_text(encoding="utf-8"))
        items = snapshot.get("evidence_items") or snapshot.get("items") or []
        for item in items:
            for category in item.get("categories") or []:
                counts[str(category)] += 1
    return counts


def theme_counts(papers: list[dict]) -> Counter:
    counts: Counter = Counter()
    for paper in papers:
        for tag in paper.get("tags") or []:
            counts[str(tag)] += 1
    return counts


def monthly_theme_matrix(papers: list[dict], top: int = 8) -> tuple[list[str], dict]:
    months: Counter = Counter()
    per_theme: dict[str, Counter] = {}
    for paper in papers:
        month = str(paper.get("announced_date") or "")[:7]
        if not month:
            continue
        months[month] += 1
        for tag in set(paper.get("tags") or []):
            per_theme.setdefault(str(tag), Counter())[month] += 1
    top_themes = [tag for tag, _ in theme_counts(papers).most_common(top)]
    ordered = sorted(months)
    matrix = {
        tag: [per_theme.get(tag, {}).get(month, 0) for month in ordered] for tag in top_themes
    }
    return ordered, matrix


def cooccurrence(papers: list[dict], top: int = 8) -> list[tuple[str, str, int]]:
    common = {tag for tag, _ in theme_counts(papers).most_common(top)}
    pairs: Counter = Counter()
    for paper in papers:
        tags = sorted({str(tag) for tag in paper.get("tags") or [] if tag in common})
        for i, first in enumerate(tags):
            for second in tags[i + 1 :]:
                pairs[(first, second)] += 1
    return pairs.most_common(8)


def build_report(papers: list[dict], radar_types: Counter) -> str:
    themes = theme_counts(papers)
    fields = Counter(str(paper.get("field") or "other") for paper in papers)
    months, matrix = monthly_theme_matrix(papers)
    pairs = cooccurrence(papers)
    dates = [str(paper.get("announced_date") or "") for paper in papers]
    total_tags = sum(themes.values())
    top3 = themes.most_common(3)

    lines = [
        "# Capability-theme coverage: XBsleepy digest corpus",
        "",
        f"Corpus: {len(papers)} agent-benchmark papers, {min(dates)} .. {max(dates)} "
        "(announced dates). Multi-label themes per paper.",
        "",
        "## Frozen inputs",
        "",
        f"- Digest index: upstream commit `{DIGEST_COMMIT}` "
        f"(2026-09-07T18:39:57Z), SHA-256 `{DIGEST_SHA256}`.",
        f"- Radar snapshots: v0.11.0 release archive, {SNAPSHOT_COUNT} files "
        f"(2026-07-23 .. 2026-09-07), dir SHA-256 `{SNAPSHOTS_SHA256}`.",
        "- Software commit: `8f46bbfa91f5d9900c8b08a5d552c3df5c9597b0` (v0.11.0).",
        "",
        "## Theme distribution",
        "",
        "| Theme | Papers | Share |",
        "|---|---:|---:|",
    ]
    for theme, count in themes.most_common():
        lines.append(f"| {theme} | {count} | {count / len(papers):.0%} of papers |")
    lines += [
        "",
        f"Average themes per paper: {total_tags / len(papers):.2f}.",
        "",
        "## Radar record-type vs digest capability coverage",
        "",
        f"The radar's snapshot categories count records by TYPE "
        f"(total tagged sightings: {sum(radar_types.values())}):",
        "",
        "| Radar category | Sightings |",
        "|---|---:|",
    ]
    for category, count in radar_types.most_common():
        lines.append(f"| {category} | {count} |")
    lines += [
        "",
        "The digest adds the layer the radar's own taxonomy does not carry: "
        "WHICH capability an agent benchmark tests. The two are complementary, "
        "not overlapping.",
        "",
        "## Concentration and gaps",
        "",
        f"- Top-3 themes ({', '.join(tag for tag, _ in top3)}) cover "
        f"{sum(count for _, count in top3) / total_tags:.0%} of all tags.",
        f"- Sparsest themes: "
        f"{', '.join(f'{tag} ({count})' for tag, count in themes.most_common()[-4:])} "
        "-- candidate open areas for new benchmarks.",
        f"- Strongest theme pairs: {', '.join(f'{a}+{b} ({n})' for (a, b), n in pairs[:4])}.",
        "",
        "## Monthly arrivals, top themes",
        "",
        "| Theme | " + " | ".join(months) + " |",
        "|---|" + "---:|" * len(months),
    ]
    for theme, series in matrix.items():
        lines.append(f"| {theme} | " + " | ".join(str(v) for v in series) + " |")
    lines += ["", "## Assigned field (single-label, digest classifier)", ""]
    for field, count in fields.most_common():
        lines.append(f"- {field}: {count}")
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    digest_path = (
        Path(argv[1]).expanduser()
        if len(argv) > 1
        else Path("~/digest-index-2026-09-07.json").expanduser()
    )
    snapshot_dir = Path(argv[2]).expanduser() if len(argv) > 2 else Path("data/snapshots")
    out_dir = Path(argv[3]).expanduser() if len(argv) > 3 else PAPER / "analysis" / "theme-coverage"

    papers = load_digest(digest_path)
    radar_types = radar_record_types(snapshot_dir)
    text = build_report(papers, radar_types)

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "coverage.md").write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
