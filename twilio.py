from twilio.rest import Client


account_sid = '<TWILIO-SID>'
auth_token = '<TWILIO-TOKEN>'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="hello! this is a programmed message",
                     from_='<TWILIO NUMBER>',
                     to='<NUMBER WITH EXTENSION>'
                 )

print(message.sid)
