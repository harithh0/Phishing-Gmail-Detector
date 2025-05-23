from flask import Flask, request, jsonify
import phishing_ai_model
import gmail_implementation
import base64
import json
app = Flask(__name__)

@app.route('/email-webhook', methods=['POST'])
def receive_email():
    data = request.json
    # print(data.keys())
    # print(data)
    # print("Received Email:")
    # print("From:", data.get("from_email"))
    # print("Subject:", data.get("subject"))
    # print("Body:", data.get("email"))



    #runs the  phishing model here

    result, confidence = phishing_ai_model.classify_email(data)
    if result == 1:
        service = gmail_implementation.authenticate_gmail()
        gmail_implementation.set_as_phishing(service, data.get("email_id"))
        print(f"Email {data.get('subject')} has been flagged as phishing")

    return jsonify({"status": "received"}), 200






if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)