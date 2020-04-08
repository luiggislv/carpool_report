import sys
import csv
import operator
import googlemaps
import requests
from entidades.entidades import Recolectores, Conductores
import json
from datetime import datetime
from util import create_csv

#API google Matrix
API_key = 'AIzaSyDJQZgcTpQWmM9zwUn5RDIvrbm73opKpoU'
gmaps = googlemaps.Client(key=API_key)

#Cabecera
header = []
header.extend(['Conductor asignado','Pasajero','Hora Recojo','Direccion','Tiempo estimado'])


# variables & list
rx_lst = []
cx_lst = []
px_lst = []


# #recolector asignado a grupo
with open("csv\\archivos\\recolectores.csv", "r") as csv_file_rx:
    csv_reader_rx = csv.reader(csv_file_rx, delimiter=';')
    for lines in csv_reader_rx:
        rx_lst = (csv_reader_rx)
        for i in rx_lst:
            print(i[0] + ";" + i[1] + ";" + i[2])


#orden por hora_recojo - pasajeros
with open("csv\\archivos\\pasajeros.csv", "r") as csv_file_px:
   csv_reader_px = csv.reader(csv_file_px, delimiter=';')
   for lines in csv_reader_px:
        px_lst = sorted(csv_reader_px, key = lambda lines: datetime.strptime(lines[6], "%H:%M:%S"), reverse=False)


# #ordenar por tiempo de llegada - conductores
with open("csv\\archivos\\conductores.csv", "r") as csv_file_cx:
   csv_reader_cx = csv.reader(csv_file_cx, delimiter=';')
   for lines in csv_reader_cx:
       cx_lst = sorted(csv_reader_cx, key = lambda lines: datetime.strptime(lines[6], "%H:%M:%S"), reverse=False)


# print("pasajeros")
# for i in px_lst:
#     print(i[0] + ";" + i[1] + ";" + i[2] + ";" + i[3] + ";" + i[4] + ";" + i[5] + ";" + i[6] + ";" + i[7])
#
# print("conductores")
# for i in cx_lst:
#     print(i[0] + ";" + i[1] + ";" + i[2] + ";" + i[3] + ";" + i[4] + ";" + i[5] + ";" + i[6])
#
#
with open('csv/pasajeros.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, delimiter=';', quoting=csv.QUOTE_ALL)
     wr.writerow(px_lst)

print(px_lst)
print(cx_lst)
print(header)
#
#
#
# #ordenar conductores por tiempo_llegada y pasar a csv
# # recolector recoge a pasajeros y los deja con los conductores
# # los conductores se ordenan por tiempo_llegada y se alinean a la tabla de pasajeros
# # cada conductor esta asignado a un recolector
# # cada pasajero tiene un conductor asignado que lo deja en su destino final
