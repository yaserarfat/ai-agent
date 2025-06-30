from twilio.rest import Client
import os

def send_whatsapp_message(to_number, body):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_FROM_NUMBER")

    print(to_number)

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:' + from_number,
        to='whatsapp:' + to_number,
        body=body
    )
    return message.sid
