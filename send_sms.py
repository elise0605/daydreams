from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC4331708f06d853ac05e8ddee7b3fbb60'
auth_token = 'ce4d0f21d483d7b5d2f87e59ecb8c433'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+4759449207',
                     to='+4794502224'
                 )

print(message.sid)
