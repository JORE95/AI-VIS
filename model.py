# from transformers import AutoImageProcessor, AutoModelForImageClassification

# model_name = "facebook/deit-tiny-patch16-224"
# save_path = "./models/deit-tiny"

# # Download model
# processor = AutoImageProcessor.from_pretrained(model_name)
# model = AutoModelForImageClassification.from_pretrained(model_name)

# # Save locally
# processor.save_pretrained(save_path)
# model.save_pretrained(save_path)

# print("Model saved to:", save_path)


# from pathlib import Path
# from urllib.request import urlretrieve
# import mediapipe as mp
# import PIL.Image as Image
# import os
# import pandas as pd
# import matplotlib.pyplot as plt


# model_path = Path("gesture_recognizer.task").resolve()

# if not model_path.exists():
#     urlretrieve(
#         "https://storage.googleapis.com/mediapipe-models/"
#         "gesture_recognizer/gesture_recognizer/float16/latest/"
#         "gesture_recognizer.task",
#         str(model_path),
#     )

# print("Modell gespeichert:", model_path)