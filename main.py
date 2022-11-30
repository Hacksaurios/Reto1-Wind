#!/usr/bin/env python3
import sys
from xml import sax
from myparser import ContentGenerator

# --- Display usage error --- #


def displayError():
    return "usage: ./main.py windmills.xml\nusage: python3 main.py windmills.xml"

# --- Headcuarter class --- #


class Headcuarter():
    def __init__(self, city, lat, lon):
        self.city = city
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f'{self.city},{self.lat},{self.lon}'

# --- Get spoiled windmill coordinates --- #


def getWindmillCoords(Leon: Headcuarter, Santiago: Headcuarter, Madrid: Headcuarter, Barcelona: Headcuarter, Sevilla: Headcuarter):
    coords = list()
    coords.append('{:.6}'.format(3*Leon.lat - 4*Madrid.lat + 2*Sevilla.lat))
    coords.append('{:.6}'.format(6*Leon.lon - 4*Santiago.lon - 2*Barcelona.lon))
    return coords

# --- Parse windmill.xml --- #


def createWindmillList():
    windmillList = []
    try:
        sax.parse(sys.argv[1], ContentGenerator(windmillList))
    except:
        print(displayError())
        sys.exit(1)
    return windmillList

# --- MAIN --- #

if __name__ == '__main__':

    # --- Make sure using right amount of arguments --- #

    if len(sys.argv) != 2:
        print(displayError())
        sys.exit(1)

    # --- Create headcuarters --- #

    Leon = Headcuarter("León", 42.57682, -5.59698)
    Santiago = Headcuarter("Santiago de Compostela", 42.90510, -8.50701)
    Madrid = Headcuarter("Madrid", 40.51642,  -3.89502)
    Barcelona = Headcuarter("Barcelona", 41.40124, 2.19122)
    Sevilla = Headcuarter("Sevilla", 37.39523, -6.01029)

    # --- Parse windmill.xml into windmillList --- #

    windmillList = createWindmillList()

    # --- Get and print hints coordinates --- #

    print('Coords on spoiled windmill by hints:\n',getWindmillCoords(Leon, Santiago, Madrid, Barcelona, Sevilla))

    # --- Print windmills whose speed is higher than speedlimit --- #

    print('\nPrinting all windmills whose speed is higher than speedlimit:')
    for win in windmillList:
        speedlimit = win.speedlimit.split()
        speed = win.speed.split()
        if int(speedlimit[0]) < int(speed[0]):
            print(win)
