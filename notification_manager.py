from twilio.rest import Client
class NotificationManager:
    def __init__(self,c,p,d):

        account_sid = 'ACd398fe30ca13476f7a6ad5e9f2012e19'
        auth_token = '3d6b262d60dcf21c20e234e01cb8adfa'
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"The ticket to the{c},costs only {p}zł, in {d}",
            from_='+12018856420',
            to='+48792742657'
        )
