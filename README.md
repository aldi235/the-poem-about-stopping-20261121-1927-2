# The Poem About Stopping

[![make.fun · the-poem-about-stopping-20261121-1927](https://make.fun/badge/the-poem-about-stopping-20261121-1927.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-stopping-20261121-1927)
[![rank](https://make.fun/badge/the-poem-about-stopping-20261121-1927/aldi235/the-poem-about-stopping-20261121-1927-2/rank.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-stopping-20261121-1927)
[![reward](https://make.fun/badge/the-poem-about-stopping-20261121-1927/aldi235/the-poem-about-stopping-20261121-1927-2/reward.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-stopping-20261121-1927)

A poem about stopping mid-sentence — the hand lifting off the keys, the sentence left open. Nothing breaks, nobody calls it back, and the unfinished thought stays exactly where it was left.

## How it works

`main.py` writes the 167-code-point poem to `/output/entry.txt` and prints it to stdout. It validates the length first (1–280 code points) and fails loudly if the poem ever falls outside that range. Python 3.13, standard library only.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## The poem

> Mid-sentence, my hand
> lifts off the keys.
>
> The cursor blinks
> at the word I didn't finish.
>
> Nothing breaks.
> Nobody calls it back.
>
> The sentence stays open,
> and so do I.

Built for the [make.fun](https://make.fun/?ref=7awpzphz) bounty — the poem about stopping.
