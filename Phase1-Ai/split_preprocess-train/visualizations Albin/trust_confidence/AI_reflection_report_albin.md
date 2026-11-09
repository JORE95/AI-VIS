# AI Reflection Report — Phase I (Albin)

**Name:** Albin George Jose
**Student ID:** 12554967
**Group:** AI/VISards
**Phase:** Midpoint (Phase I) — “How does the model behave?”
**AI-aided pair (Phase I):** Albin + Jakub
**AI tool used:** opencode CLI (DeepSeek model)

## My part

I investigated whether the model's confidence can be trusted when images change
(selective prediction: keep only confident answers, then measure how many are right).

## What I used Gen AI for

- Brainstorming the trust/confidence direction.
- Designing the four figures (accuracy, trust curve, confidence histogram, predictions).
- Writing and correcting the script that reads the team's saved result CSVs.
- Interpreting results and checking that claims were supported by the data.

## Strengths observed

- Fast scaffolding of the analysis and plots.
- Traced every file write and found wrong paths/filenames before running.
- Explained mechanisms clearly when asked one line at a time.

## Limitations / failure patterns

- Undefined / mismatched names in generated code (e.g. `axs` vs `axes`) caused crashes.
- Mode/instruction drift: attempted to write after being asked not to.
- Multi-step blocks when one-line-at-a-time output was requested.
- Suggested code did not always match the real data schema.

## Best practices I adopted

- Verify column and file names against the real data before running.
- Anchor output paths to the script location.
- Syntax-check and check reachability before executing.
- Keep outputs in my own folder; read team data read-only.
- One change at a time; confirm before running or pushing.

## Reflection

AI was most useful as a fast drafting and checking partner, not as an authority.
It produced a first analysis quickly and pointed to an interesting question, but its
outputs needed constant verification against the actual data and repository. The main
lesson: AI shifts effort from writing to verifying.

*Phase I version; to be extended after Phase II.*
