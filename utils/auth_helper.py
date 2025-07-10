from datetime import datetime, timedelta

import requests
import json

def get_checkIndate():
    checkin_date = datetime.now().strftime("%Y-%m-%d")
    return checkin_date

def get_checkOutdate():
    checkOut_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    return checkOut_date

def get_authentication(config):
    url = config['base_url']
    payload = {
    "username" : "admin",
    "password" : "password123"
    }
    get_token = requests.post(f"{url}/auth",json=payload)
    assert get_token.status_code == 200
    return get_token.json()['token']

