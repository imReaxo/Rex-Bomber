from time import sleep
from colorama import Fore as color
import sys, os



def banner():
    print(color.LIGHTRED_EX+"""

██████╗░███████╗░█████╗░██╗░░██╗░█████╗░
██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝██╔══██╗
██████╔╝█████╗░░███████║░╚███╔╝░██║░░██║
██╔══██╗██╔══╝░░██╔══██║░██╔██╗░██║░░██║
██║░░██║███████╗██║░░██║██╔╝╚██╗╚█████╔╝
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░
                                                               version 1.0""")

    sleep(0.1)

    print(color.RED+"""
-------------------------------------------
|||           Developer: Reaxo          |||
|||           Contact: Reaxo#0099       |||               
-------------------------------------------             
""")
    sleep(0.1)


def menu_respaws():
    try:
        print(color.RED+"[1] "+ color.LIGHTYELLOW_EX+"Sms-Bomber")
        print(color.CYAN+"*********************")
        sleep(0.1)
        
        print(color.RED+"[0] "+ color.LIGHTYELLOW_EX+"Exit")
        print(color.CYAN+"*********************")
        sleep(0.1)
    except:
        sleep(1)
        sys.exit()
