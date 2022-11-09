import requests
from time import sleep
import json
from colorama import Fore as color  
import random
from datetime import datetime
def tapsi_bomber(number):
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
    try:

        tapsinumber = {"credential":{"phoneNumber": number,"role":"DRIVER"}}
        tapsi = 'https://tap33.me/api/v2/user'
        time = datetime.now()
        try:
            #originalrequest = requests.post(tapsi, json= tapsinumber, headers=rhead)
            try:
                print(color.GREEN+"[*] Tapsi Sent...!",end=' ')
                print(color.LIGHTGREEN_EX+ bold +'\t'+str(time.hour)+":"+str(time.minute)+":"+str(time.second))  
                sleep(1)
            except:
                print(color.RED+"Something Went Wrong...")         
        except:
            print(color.RED+"something went wrong...")
            
    except:
        print(color.RED+"Something went Wrong...")


