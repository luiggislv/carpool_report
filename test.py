import sys
import csv
import operator
import googlemaps
import requests
import json
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDJQZgcTpQWmM9zwUn5RDIvrbm73opKpoU')

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
reporte_parcial = open('csv/reporte_final/reporte_parcial.csv', 'w', newline='')
csv_writer = csv.writer(reporte_parcial, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
count = 0

origin_ini = rx_lat_ini +","+rx_long_ini

for i in px_lst:
    if count == 0:
        header = header
        csv_writer.writerow(header)
        count += 1


    dest_ini_px = i[3]+","+i[4]
    my_dist_px = gmaps.distance_matrix(origin_ini, dest_ini_px)

    destination = my_dist_px['destination_addresses'][0]
    distance = my_dist_px['rows'][0]['elements'][0]['distance']['text']
    duration = my_dist_px['rows'][0]['elements'][0]['duration']['text']

    pasajeros = [i[7],'pasajero', i[1]+" "+i[2], i[6], destination, distance, duration]
    csv_writer.writerow(pasajeros)

for i in cx_lst:

    dest_ini_cx = i[3]+","+i[4]
    my_dist_cx = gmaps.distance_matrix(origin_ini, dest_ini_cx)

    destination = my_dist_cx['destination_addresses'][0]
    distance = my_dist_cx['rows'][0]['elements'][0]['distance']['text']
    duration = my_dist_cx['rows'][0]['elements'][0]['duration']['text']

    conductores = ['cx', 'conductor', i[1]+" "+i[2], i[6], destination, distance, duration]
    csv_writer.writerow(conductores)

reporte_parcial.close()
