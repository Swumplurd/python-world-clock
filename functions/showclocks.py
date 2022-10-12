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
        while True:
            os.system("cls")
            for zone in zones:
                print(f"{datetime.now(pytz.timezone(zone)).strftime('%A %d de %B del %Y   ')}\t{datetime.now(pytz.timezone(zone)).strftime('|| %H:%M ||')}\t{zone}")
            sleep(15)