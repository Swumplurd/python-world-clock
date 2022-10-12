from strings.mainstrings import tzwarning
from functions.tzpicker import zones
from datetime import datetime
from time import sleep
import os, pytz

def showclocks():
    if len(zones) == 0:
        print(tzwarning)
        sleep(3)
        os.system("cls")
    else:
        control = 1
    while control == 1:
        os.system("cls")
        for zone in zones:
            print(f"{datetime.now(pytz.timezone(zone)).strftime('%A %d de %B del %Y || %H:%M')}\t{zone}")
        sleep(15)