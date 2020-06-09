from twilio.rest import Client


# My Account Sid and Auth Token from twilio.com/console
account_sid = 'ACc75351ad26839498cb52f10141689b32'
auth_token = '3b95601d6d58a61f88e618e8b5b22b37'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello User",
                     from_='+15017122661',
                     to='+2348143142973'
                 )

print(message.sid)
