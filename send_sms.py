import os
from twilio.rest import Client

# To get account SID and auth token: twilio.com/console
accountSID = ""
authToken = ""
client = Client(accountSID, authToken)


def sendMessage(content, fileName):
    recipients = open(fileName, mode="r")
    recipients.readline()
    for recipient in recipients:
        message = client.messages.create(
            from_=str(),
            body=content,
            to="+1" + str(recipient)
        )
        print(message.sid)
    recipients.close()

def main():

    message = """Thank you for signing up for our Free Food pilot program!
There is free food available right now on a first come, first serve basis for the next 30 minutes. 
Please see details below:

Date: Friday Nov 17
Time Frame: 5:00 - 5:30
Location: University Religious Center URC 108 at Trojan Table
Type of Food*: Chicken, brown rice, falafel, salad, desserts
Number of Servings: About 50

Containers and plates are limited, so bring your own if you can.
*Please be aware that this food may contain allergens."""

    print(message)
    sendMessage(message, "pilotprogram.csv")

main()