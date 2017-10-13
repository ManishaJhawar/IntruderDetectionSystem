from twilio.rest import Client

def dial_numbers():
    TWILIO_PHONE_NUMBER = "Your twilio number"

    DIAL_NUMBERS = ["Your number"] # list of one or more phone numbers to dial

    TWIML_INSTRUCTIONS_URL = "Twilio URL"

    client = Client("Account SID", "Auth token")

    for number in DIAL_NUMBERS:
        print("Dialing " + number)
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")
