from datetime import tzinfo
from functions.tzpicker import zones
from io import open

def initzones():
    file = open("zones.txt", "r")
    lineas = file.readlines()
    file.close()
    if len(lineas) == 0:
        return
    else:
        for linea in lineas:
            zones.append(linea[:-1])