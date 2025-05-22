from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# load tokenizer and model
model_name = "ealvaradob/bert-finetuned-phishing"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def classify_email(email_data : dict[str, str]):
    prompt = f"""
    Email sender email: {email_data.get("from_email")}
    Email sender name: {email_data.get("from_name")}
    Email subject: {email_data.get("subject")}
    Email body:  {email_data.get("email")}
    """
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=-1)
        pred = torch.argmax(probs, dim=1).item()
        # label = "Phishing" if pred == 1 else "Safe"
        confidence = probs[0][pred].item()
        return pred, round(confidence * 100, 2)

