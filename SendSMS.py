from twilio.rest import Client

def sendSMS():
    client = Client("Auth SID", "Auth Token")
    client.messages.create(to="Your number", from_="Your twilio number", body="Intruder ALERT!")
