import requests


def connect_customer_to_agent(
    sid,
    token,
    agent_no,
    customer_no,
    callerid,
    calltype
):
    return requests.post(
        'https://api.exotel.in/v1/Accounts/shoppingzoneindia1/Calls/connect.json',
        auth=(sid, token),
        data={
            'From': agent_no,
            'To': customer_no,
            'CallerId': callerid,
            'CallType': calltype

        }
    )


if __name__ == '__main__':
    r = connect_customer_to_agent(
        sid="shoppingzoneindia1",
        token="bbf19daeeef2109a6dbe8179835c71af3ace49b7e0e92373",
        agent_no="09600542512",
        customer_no="09962242251",
        callerid="04446274111",
        calltype="trans"
    )
    print(r.status_code)


def send_message(sid, token, sms_from, sms_to, sms_body):
    return requests.post(
        'https://api.exotel.in/v1/Accounts/shoppingzoneindia1/Sms/send.json',
        auth=(sid, token),
        data={
            'From': sms_from,
            'To': sms_to,
            'Body': sms_body
        }
    )


if __name__ == '__main__':
    r = send_message(
        sid="shoppingzoneindia1", 
        token="bbf19daeeef2109a6dbe8179835c71af3ace49b7e0e92373",
        sms_from='09600542512',
        sms_to='09962242251',
        sms_body='Hello'
    )
    print(r.status_code)
