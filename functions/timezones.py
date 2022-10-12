import pytz

def timezones():
    i = 0
    print(len(pytz.all_timezones))
    for timezone in pytz.all_timezones:
        print(timezone)
