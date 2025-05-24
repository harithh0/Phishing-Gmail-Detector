## Gmail Phishing Classifier using AI

This project uses machine learning to automatically detect and flag phishing emails in real-time using the Gmail API, Zapier, and a Hugging Face transformer model.

### 🚀 Features

- **Real-time email monitoring** using Zapier Gmail intergration
- **AI email classification** (Phishing vs. Safe)
- **Automatic spam and phishing labeling** through Gmail API


### Showcase
[![Watch the demo](thumbnail.png)](https://youtu.be/MRiKsjDFA4A?feature=shared)

### Description

Using [this](https://huggingface.co/ealvaradob/bert-finetuned-phishing) Hugging Face transformer, made by [ealvaradob](https://huggingface.co/ealvaradob/) and python Transformers & PyTorch library, I was able to create a function that would take email data and send it to the AI model. Then the model outputs 0 (safe) or 1 (phishing) flag and a confidence score all happening locally.

In the beggining I tried training my own model using data I found online, but it was both time consuming and difficult to get right. The data I found was either not well formatted or did not have enough entries. It did ended up working however, it was very innaccurate at times. So I just decided to use the premade model and fine tune it to my likeing.

### Workflow

Firstly I needed a way to be able to recieve new emails from the users Gmail account. One way was using Google Cloud's Pub/Sub to recieve updates whenever a new email comes through. This is a way better way to do things but also more complicated to setup. Another way is to use Zapier. Zapier is a SaaS application that has hundred of uses to automate tasks. I decided to use it to be able to create a **workflow that recieves new emails then sends the email data to my Flask API which will then take that data and run the AI model on it returning a score**. This way is much easier to setup but at the cost of using another application to handle that part. In the future however I want to implement it through Google Cloud instead as I will have more control over it and is better sutable for production.

After the model calculates the result, if it turns out to be flagged as phishing, using the Gmail API, is is able to set a label to that specific email and move it to the spam folder. The Gmail API does need permissions from the user first to be able to generate OAuth token, which will then be used in to authenticate the users account through the Gmail API.

### Technologies Used
- HuggingFace Transformers
- PyTorch
- Gmail API
- Flask
- Zapier
- Ngrok - for proxy to my Flask app without port forwarding



### 📈 Future Plans

- Implement false positive feedback
    - Use this feedback to fine tune and improve model
- Implement Pub/Sub for more control over real-time email updates instead of using Zapier
