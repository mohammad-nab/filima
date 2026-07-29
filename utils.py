from kavenegar import *
from conf import settings


def send_otp_code(code):
    try:
        api = KavenegarAPI(settings.KAVENEGAR_API_KEY)
        params = {
            'sender': '2000660110',
            'receptor': settings.PHONE_NUMBER,
            'message':f'your code is {code}',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
