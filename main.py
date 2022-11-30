#!/usr/bin/env python3
import sys

from xml import sax
from myparser import ContentGenerator

if len(sys.argv) != 2:
    print("usage: ./main.py <graphML>")
    sys.exit(1)

# sedes = []
# # --- Clase sede --- #
# class sede():
#     def __init__(self, sede, lat, lon):
#         self.sede = sede
#         self.lat = lat
#         self.lon = lon

# # --- calcularCoordenadas --- #
# def calcularCoordenadas(self):
#     coordenadas= ""

#     lat = 3 * sedes
#     lon = 0

#     coordenadas = "{} , {}".format(lat,lon)

#     return coordenadas


# --- MAIN --- #

# Leon = sede("León", 42.57682, -5.59698)
# Santiago = sede("Santiago de Compostela", 42.90510, -8.50701)
# Madrid = sede("Madrid" , 40.51642,  -3.89502)
# Barcelona = sede("Barcelona", 41.40124 , 2.19122)
# Sevilla = sede( "Sevilla",37.39523, -6.01029)

# sedes= [Leon, Santiago, Madrid, Barcelona, Sevilla]

# resultado = calcularCoordenadas(sedes=sedes)

# print("El molino defectuoso se encuentra en las coordenadas: {}", resultado)
windmillList=[]
sax.parse(sys.argv[1], ContentGenerator(windmillList))
for win in windmillList:
    print(win)