Task:

Our goal is to explore and understand model behavior through visual analysis of its inputs and outputs, identifying interesting patterns, common misclassifications, and potential biases. Building on these findings, we will examine the model's internal representations to better understand which visual features it has learned and how these relate to its classification behavior.


Model:

https://huggingface.co/facebook/deit-tiny-patch16-224


Dataset: 

Hand gesture images, 19 classes
original - https://huggingface.co/datasets/cj-mills/hagrid-sample-500k-384p
We decided to use only 5 classes with 1000 samples from each. Includes data: Race, Gender, Leading Hand

Project Structure:

Two workflows: Separated the project into Phase1-Ai (AI-assisted) and Phase1-NoAI.

Data preparation: Used Data_handling.ipynb and Image_handling.py to process and prepare the image dataset.

Missing age imputation: Used an API to estimate missing age values in the dataset (missing_age.ipynb).

Hand detection: Developed bounding box estimation to locate hand regions in images (Image_box_estimator.ipynb).

Model development: Implemented model architecture and training pipelines using model.py and Training.ipynb, with trained models stored separately.

Model evaluation: Used Testing.ipynb to assess classification performance.

Occlusion experiments: Implemented hand and background occlusion tests in occlusion_test.ipynb to investigate which image regions influence predictions.

AI-assisted workflow: Organized model development, preprocessing, training, and team visualizations into dedicated folders under Phase1-Ai.

Documentation: Maintained project documentation, team information, and an AI reflection file (ai-reflection-midpoint.md).
