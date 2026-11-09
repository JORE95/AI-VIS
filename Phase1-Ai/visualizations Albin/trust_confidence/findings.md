# AI pair - Phase I : Trust in confidence

- Normal correct: 87.1% | side flip: 25.1%
- Sure(>=90%) normal right: 96.6% | after flip right: 24.2%
- Means: confidence is not a safe warning signal when images change.
- Not proven: which pixels cause it (Phase II).
- Confusion matrix (fig5): after a side flip, 56.2% of all predictions become 'dislike'
  (normal: 20.9%); accuracy 87.1% -> 25.1%.
