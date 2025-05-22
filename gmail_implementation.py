from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os


SCOPES = ['https://www.googleapis.com/auth/gmail.modify']


def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=8080)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

# def get_unread_emails(service):
#     results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
#     messages = results.get('messages', [])
#     emails = []
#     for msg in messages[:5]: 
#         msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
#         payload = msg_data['payload']
#         parts = payload.get('parts')
#         if parts:
#             data = parts[0]['body']['data']
#         else:
#             data = payload['body']['data']
#         decoded = base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')
#         emails.append((msg['id'], decoded))
#     return emails


phishing_label_object = {
    'name': '⚠️ Suspected Phishing',
    'labelListVisibility': 'labelShow',
    'messageListVisibility': 'show'
}

def handle_label(service):
    labels = service.users().labels().list(userId='me').execute().get('labels', [])
    for label in labels:
        if label['name'] == phishing_label_object['name']:
            return label["id"]

    phishing_label = service.users().labels().create(userId='me', body=phishing_label_object).execute()
    return phishing_label["id"]

def set_as_phishing(service, email_id):
    print("email_id", email_id)


    phishing_label_id = handle_label(service)

    # sets as phishing
    service.users().messages().modify(
        userId='me',
        id=email_id,
        body={'addLabelIds': [phishing_label_id]}
    ).execute()

    # sets as spam
    service.users().messages().modify(
        userId='me',
        id=email_id,
        body={'addLabelIds': ["SPAM"]}
    ).execute()

if __name__ == "__main__":
    service = authenticate_gmail()