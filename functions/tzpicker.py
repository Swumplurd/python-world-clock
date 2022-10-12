from strings.mainstrings import tzselectmsg, tzisadded
from time import sleep
from pick import pick
import pytz, os

zones = []

def tzpicker():
    zone = pick(pytz.common_timezones, tzselectmsg, indicator = '=>', default_index = 0)
    if zones.count(zone[0]) == 0:
        zones.append(zone[0])
    else:
        print(tzisadded)
        sleep(3)
        os.system("cls")