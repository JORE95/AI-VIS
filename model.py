from transformers import AutoImageProcessor, AutoModelForImageClassification

model_name = "facebook/deit-tiny-patch16-224"
save_path = "./models/deit-tiny"

# Download model
processor = AutoImageProcessor.from_pretrained(model_name)
model = AutoModelForImageClassification.from_pretrained(model_name)

# Save locally
processor.save_pretrained(save_path)
model.save_pretrained(save_path)

print("Model saved to:", save_path)