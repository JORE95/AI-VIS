# AI Interaction Log — Phase I (AI-aided Pair) - trustconfidence

- **Project:** AI & Visualization — Hand Gesture Classification (HaGRID)
- **Group:** AI/VISards


| # | Type | Prompt | AI answer | Decision | Reason |
|---|---|---|---|---|---|
| 1 | Direction | Which model and dataset are being used? | Identified DeiT-Tiny, five classes, HaGRID subset | Accepted | Matched committed team artifacts |
| 2 | Bias | Which extra attributes (hand, age, gender, race) are available? | Class label only from the model; attributes can be used for bias checks if present in the result CSV | Accepted | Enabled the attribute comparison |
| 3 | Direction | Which novel question should the presentation focus on? | Checked existing team notebooks, then proposed: "Can we trust the model's confidence?" | Accepted | Old ideas (orientation, confidence) were already partly covered |
| 4 | Direction | Which candidate questions can be tested from the saved results? | Saved results already show a strong story: accuracy 87% -> 25% after flips; most flipped images predicted 'dislike'; confident-but-wrong rises. | Accepted | Proposed candidate directions |
| 5 | Direction | Is using an existing model to outline Phase 1 gesture data worthwhile, or redundant? | If you mean using an LLM (Claude/Copilot) to draft an outline/checklist for Phase I on HaGRID gestures (what figures to make, what | Accepted | explanation used |
| 6 | Design | How should the trust/confidence analysis be planned? | Suggested an approach: compare confidence with correctness using the saved team result CSVs. Learner implemented and verified the script. | Modified | Learner wrote and verified the code; AI proposed only the direction. |
| 7 | Design | Should the deliverable be the confusion matrix or a confidence plot? | Don’t just submit the figure — you need to show what it means. From your side (AI-aided pair, Phase I), try to capture: - What the | Modified | AI advice adjusted the plan |
| 8 | Design | Should the whole dataset be passed through the model for a heatmap, or one class per image? | For Phase I (behavior), you pass the whole eval dataset through the model and collect one prediction per image (the predicted clas | Accepted | method guidance used |
| 9 | Interpret | When classes are mixed up, what does that indicate, and how long does it take to find? | Finding which classes are mixed up: a few minutes — once you have the confusion matrix, just look at the off-diagonal cells (big n | Accepted | method guidance used |
| 10 | Interpret | Why does the linear probe have low accuracy? | A linear probe can have terrible accuracy because it only trains a small classifier on top of frozen features — it doesn’t change | Accepted | method guidance used |
| 11 | Interpret | Does longer training improve the linear probe? | Sometimes a little, but usually not much. If the linear probe is underfitting (hasn’t learned enough from the features), training | Accepted | method guidance used |
| 12 | Interpret | Are heatmaps part of Phase 2? | Yes — that fits. Grad-CAM heatmaps are usually Phase II (what the model learned/attribution). | Accepted | AI confirmed the approach |
| 13 | Interpret | What does 'gesture' mean as the output, and does dropping it remove the dataset's purpose? | You’re not dropping gestures — “gesture” is the thing you’re predicting (the hand sign/class). - Gesture classes = the actual labe | Accepted | method guidance used |
| 14 | Model/Data | Which model is used with the hagrid-sample-30k-384p dataset on Hugging Face? | HaGRID sample (30k, 384p) is the dataset (from cj-mills/hagrid-sample-30k-384p on Hugging Face), not the model. Your team hasn’t s | Accepted | method guidance used |
| 15 | Model/Data | Which exact Facebook tiny model is used, and what issue is reported? | Likely facebook/deit-tiny-patch16-224; ask which exact checkpoint and what the issue is. | Accepted | Clarified model identity |
| 16 | Model/Data | Are five classes sufficient, and should 'no classified gesture' be included? | You’re right — the messages are jumping around. They’re mixing different things: - Dataset choices: HaGRID has many gesture classe | Accepted | method guidance used |
| 17 | Code | Explain the code line by line, with why and what. | Explained each line (why and what); learner typed and executed the code. | Accepted | Learner typed and ran the code. |
| 18 | Code | Provide the remaining code from the x-axis label onward. | Here is everything from ax.setxlabel("confidence") to the end. Note the 8-space indent on the first line (it's inside the for loop | Accepted | explanation used |
| 19 | Verify | Verify the script writes only to the intended location. | Verified all writes go to the output folder; found a wrong folder name, wrong filename, and an undefined variable. | Accepted | Verification caught path/filename bugs |

---

## 2. Errors observed

**Introduced by the AI assistant:**
1. Undefined / mismatched names (`figures` without quotes; `axs` vs `axes`) → crashes.
2. Mode/instruction drift: attempted to write or publish after the learner asked it not to.
3. Asked for team intent instead of using evidence already present in the repository.
4. Delivered multi-step blocks when one-line-at-a-time output was requested.

**Note:** several learner-introduced errors were caught by the verification step
(syntax check + write-location check) before running. Both sides must verify.

---

## 3. Best practices

- Verify column and file names against the real data before running generated code.
- Anchor output paths to the script location so results land in the intended folder.
- Syntax-check and check code reachability before executing AI-suggested code.
- Keep analysis outputs in the pair's own folder; read team data read-only.
- Make one change at a time and confirm before running or pushing.
- Prefer evidence already in the repository over asking the team for intent.

---

## 5. Repository link

```
https://github.com/JORE95/AI-VIS
```
