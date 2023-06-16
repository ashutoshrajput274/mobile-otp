import requests
import random
from django.conf import settings


def send_otp_to_phone(phone_number):
    try:
        otp = random.randint(10000,99999)
        url =f'https://2factor.in/API/V1/{settings.API_KEY}/SMS/{phone_number}/{otp}'
        #url = f'https://2factor.in/API/R1/?module=TRANS_SMS&apikey=7c59cf94-d129-11ec-9c12-0200cd936042&to={phone_number}&from=MMBook&templatename=mymedbook&var1={otp_key}&var2={otp_key}'
        response = requests.get(url)
        return otp
    except Exception as e:
        return None 