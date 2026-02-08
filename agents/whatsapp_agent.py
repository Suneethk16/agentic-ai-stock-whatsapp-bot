from twilio.rest import Client
import os

class WhatsAppAgent:
    def __init__(self):
        self.client = Client(
            os.getenv("TWILIO_ACCOUNT_SID"),
            os.getenv("TWILIO_AUTH_TOKEN")
        )
        self.from_number = os.getenv("TWILIO_WHATSAPP_FROM")
        self.to_number = os.getenv("TWILIO_WHATSAPP_TO")

    def send_message(self, message):
        msg = self.client.messages.create(
            from_=self.from_number,
            to=self.to_number,
            body=message
        )
        return msg.sid
