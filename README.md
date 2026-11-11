Task:

Our goal is to explore and understand model behavior through visual analysis of its inputs and outputs, identifying interesting patterns, common misclassifications, and potential biases. Building on these findings, we will examine the model's internal representations to better understand which visual features it has learned and how these relate to its classification behavior.


Model:

https://huggingface.co/facebook/deit-tiny-patch16-224


Dataset: 

Hand gesture images, 19 classes
original - https://huggingface.co/datasets/cj-mills/hagrid-sample-500k-384p
We decided to use only 5 classes with 1000 samples from each. Includes data: Race, Gender, Leading Hand