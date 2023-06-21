import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# DistilBERT algorithm. 
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")



def check_emotion(data):
    inputs = tokenizer(data, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits
    print(logits)
    predicted_class_id = logits.argmax().item()
    return model.config.id2label[predicted_class_id]