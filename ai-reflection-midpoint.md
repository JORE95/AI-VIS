Jakub Drziak K12542246, Albin George Jose K12554967

Jakub's Report:

Name: Jakub Drziak
Number: K12542246
AI Model: Claude Sonnet 5.5 Medium

Main Uses: Visualization idea generation, code completion, model training suggestions

Overall, the AI understood the project very well and distinguished between Phase 1 and Phase 2 without a problem. Only issue was it couldnt grasp the model finetuning strain where it proposed preprocessing images while already training which made the training unreasonably long. Only after telling it what to do exactly it was fixed. 

In terms of visualizations, it explored a wide range of directions, investigating all the connections with metadata of the images. When I proposed a certain direction, it stuck to it and came up with ideas to support it. What also happened was that it explicitly rejected some ideas that wouldnt lead to any significant findings when it got access to test set results. The only deviation that happened was after many rounds of visualizations, when it started giving ideas better fit for phase 2. When i highlighted that, it immediately recognized it itself and called it a good sign to stop with phase 1.

By far the most important part of this process was the initial prompt where i explicitly presented the context of the entire project. I believe this laid a good foundation for the AI to stay within bounds and scope of the project and give relevant suggestions. After that i never had to reintroduce or correct behavior related to the goal of the project. Second important thing was to give precise descriptions of what i want it to do, which gave it less space for made up implementations or missing parts. And lastly, always first discussing and only after agreenment, implementing. I think this definitely saved a lot of credits and strengthened the allignment



Albin's Report:

# AI Reflection Report — Phase I (Albin)

**Name:** Albin George Jose
**Student ID:** 12554967
**Group:** AI/VISards
**Phase:** Midpoint (Phase I) — “How does the model behave?”
**AI tool used:** DeepSeek API

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
