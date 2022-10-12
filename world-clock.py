from strings.mainstrings import mainmenu, welcomemsg
from functions.invalidoption import invalidoption
from functions.showclocks import showclocks
from functions.initzones import initzones
from functions.tzpicker import tzpicker
from functions.goodbye import goodbye
import os, locale

locale.setlocale(locale.LC_ALL, "es_MX")

os.system("cls")
print(welcomemsg)
initzones()

while True:
    op = input(mainmenu)
    os.system("cls")

    if op == "1":
        tzpicker()
    elif op == "2":
        showclocks()
    elif op == "3":
        goodbye()
        break
    else:
        invalidoption()
