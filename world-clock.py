from datetime import datetime
from time import sleep
from menus.mainmenu import mainmenu
import locale, os, pytz
from pick import pick

locale.setlocale(locale.LC_ALL, "es_MX")

os.system("cls")
zones = []
while True:
    op = input(mainmenu)

    if op == "1":
        zone = pick(pytz.all_timezones, "Selecciona las zonas horarias de tu interes", indicator = '=>', default_index = 0)
        if zones.count(zone[0]) == 0:
            zones.append(zone[0])
        else:
            print(f"La zona horaria {zone[0]} ya se encuentra configurada")
    elif op == "2":
        if len(zones) == 0:
            print("Por favor configura una zona horaria antes")
        else:
            control = 1
            while control == 1:
                os.system("cls")
                for zone in zones:
                    print(f"{zone} {datetime.now(pytz.timezone(zone)).strftime('%A %d de %B del %Y || %H:%M')}")
                sleep(15)
    elif op == "3":
        break
    else:
        print("Por favor selecciona una opcion valida")
