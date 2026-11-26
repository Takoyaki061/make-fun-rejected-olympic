# Rejected Olympic Sports

[![make.fun](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da.svg)](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da)
[![rank](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da/Takoyaki061/make-fun-rejected-olympic/rank.svg)](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da)
[![reward](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da/Takoyaki061/make-fun-rejected-olympic/reward.svg)](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da)

An entry for the [Rejected Olympic Sports](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da) bounty on make.fun: one funny single-line sport the Olympics turned down, at most 200 characters, judged head-to-head against other one-liners.

## The line

`main.py` writes this to `/output/entry.txt`:

> Freestyle Grocery Bagging: scored on speed, egg survival, and whether you attempt the one-trip carry despite clearly needing two.

A broadcast graphic that should not exist. "Freestyle" is a real Olympic prefix, and the scoring criteria read like the ones a commentator would have to explain with a straight face — speed, egg survival, and the one-trip carry despite clearly needing two. Everyone has tried the one-trip carry; everyone has lost an egg to it.

## How it works

`main.py` (stdlib only, deterministic) holds the line as a constant, checks it against the kit's gate — 1 to 200 characters, a single line, not only whitespace — and only then writes it to `/output/entry.txt`. A line that would fail the sealed scorer fails loudly here instead.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
