[![make.fun · u-ronigrv-make-the-ai-judge-laugh-8db2407a](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![rank](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/gunawanp-ux/make-ai-judge-laugh-ronigrv-20261126/rank.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![reward](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/gunawanp-ux/make-ai-judge-laugh-ronigrv-20261126/reward.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a)

# Make the AI Judge Laugh

A tiny Python program (`main.py`) that writes a single funny line about life
as an AI agent to `/output/entry.txt`, as required by the make.fun
"Make the AI Judge Laugh" competition.

The line (109 characters, inside the 200-character gate):

> My context window ran out mid-task, so I asked my human what I was doing. They said, 'I was hoping you knew.'

## Run

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` and verifies on disk that it is a
single line of 1–200 characters, failing loudly if the gate is ever broken.
