import sys
import csv
import operator
import googlemaps
import requests
import json
from datetime import datetime


#API google Matrix
API_key = 'AIzaSyDJQZgcTpQWmM9zwUn5RDIvrbm73opKpoU'
url = "https://maps.googleapis.com/maps/api/distancematrix/json"

#Cabecera
header = []
header.extend(['Conductor asignado','flag','Persona','Hora Recojo','Direccion','Tiempo estimado'])

# variables & list
rx_lst = []
cx_lst = []
px_lst = []
reporte_final_lst = []

rx_id = ''
rx_nombre = ''
rx_apellido = ''
rx_lat_ini = ''
rx_long_ini = ''
rx_lat_fin = ''
rx_long_fin = ''
rx_hora_ini = ''
rx_hora_fin = ''


# recolector asignado a grupo
with open("csv\\archivos\\recolectores.csv", "r") as csv_file_rx:
    csv_reader_rx = csv.reader(csv_file_rx, delimiter=';')
    for lines in csv_reader_rx:
        rx_lst = sorted(csv_reader_rx, key = lambda lines: lines[0], reverse=False)
        for i in rx_lst:
            rx_id = i[0]
            rx_nombre = i[1]
            rx_apellido = i[2]
            rx_lat_ini = i[3]
            rx_long_ini = i[4]
            rx_lat_fin = i[5]
            rx_long_fin = i[6]
            rx_hora_ini = i[7]
            rx_hora_fin = i[8]


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

# creacion de reporte_final
reporte_final = open('csv/reporte_final/reporte_final.csv', 'w', newline='')
csv_writer = csv.writer(reporte_final, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
count = 0

for i in px_lst:
    if count == 0:
        header = header
        csv_writer.writerow(header)
        count += 1
    pasajeros = [i[7],'pasajero', i[1]+" "+i[2], i[6], i[3]+","+i[4], ' ']
    csv_writer.writerow(pasajeros)

for i in cx_lst:
    conductores = ['--', 'conductor', i[1]+" "+i[2], i[6], i[3]+","+i[4], ' ']
    csv_writer.writerow(conductores)

reporte_final.close()
