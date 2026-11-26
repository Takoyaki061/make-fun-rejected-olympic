#!/usr/bin/env python3
"""Rejected Olympic Sports — one funny single-line sport, to /output/entry.txt.

Why this line wins
------------------
The joke is a broadcast graphic that should not exist. "Freestyle" is a
real Olympic prefix, and the scoring criteria read exactly like the ones a
commentator would have to explain with a straight face — speed, egg
survival, and then the twist: whether you attempt the one-trip carry
despite clearly needing two. Three escalating elements, each funnier than
the last, and the last one is the most universal human experience in the
set: everyone has tried the one-trip carry, everyone has lost an egg to
it. The absurdity comes from the sport itself, not from random words.

* One read, twist at the end. The line is a list of three scoring
  criteria; the reader expects dry sports jargon and gets, last of all,
  a confession of their own grocery-run hubris.
* Sounds like a real event. "Freestyle Grocery Bagging" could sit on a
  schedule between freestyle skiing and freestyle swimming, and the
  scoring reads like a real judged event's rubric.
* No wasted words. 129 characters, every phrase load-bearing: "egg
  survival" is the absurd-official phrase that sells the whole event,
  and "despite clearly needing two" is the punchline.
* Quotable. "Egg survival" and "the one-trip carry" are the sort of
  phrases someone repeats to a friend the same day.

Critique note (against the judge brief, own words): of the eight
candidates DeepSeek generated, this beat "Synchronized Excuse-Making"
(whose "raccoon alibi no one can verify" is the single funniest phrase
in the set, but whose missed-meeting setup is office-y rather than a
broadcast sport) and "Artistic Parking" (whose "judge breathes audibly"
is a great image, but whose closer — pretending the second attempt was
intentional — is weaker than the one-trip carry). The weakest candidates
were "Olympic Napping" (a passive event, no sport in it) and "Extreme
Waiting" (queueing is not a sport and the payoff is gentle). DeepSeek's
critique call failed (524 timeout, then an empty reply), so the pick is
my own judgment against the kit's criteria.

Stdlib only, deterministic. The program validates the line against the
gate (1-200 characters, single line, not only whitespace) before writing
it, so a bad line fails loudly here instead of failing the sealed scorer.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Gate limits from the kit: the sealed scorer accepts 1-200 characters.
LOWER_BOUND = 1
UPPER_BOUND = 200
DESTINATION = Path("/output/entry.txt")

JOKE = (
    "Freestyle Grocery Bagging: scored on speed, egg survival, and whether "
    "you attempt the one-trip carry despite clearly needing two."
)


def problems_with(line: str) -> list[str]:
    """Return every way *line* would fail the gate, empty when it passes."""
    faults: list[str] = []
    if not line.strip():
        faults.append("line is empty or only whitespace")
    if len(line) < LOWER_BOUND:
        faults.append(f"line is {len(line)} chars, below the {LOWER_BOUND} minimum")
    if len(line) > UPPER_BOUND:
        faults.append(f"line is {len(line)} chars, above the {UPPER_BOUND} maximum")
    if "\n" in line or "\r" in line:
        faults.append("line spans more than one line")
    if line != line.strip():
        faults.append("line has leading or trailing whitespace")
    return faults


def check_line(line: str) -> None:
    """Raise SystemExit naming the first gate failure, if any."""
    faults = problems_with(line)
    if faults:
        raise SystemExit("gate failed: " + "; ".join(faults))


def write_entry(line: str, destination: Path = DESTINATION) -> Path:
    """Validate *line*, then write it (with a trailing newline) to disk."""
    check_line(line)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(line + "\n", encoding="utf-8")
    return destination


def main() -> int:
    target = write_entry(JOKE)
    print(f"wrote {len(JOKE)} chars to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
