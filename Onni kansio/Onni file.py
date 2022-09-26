# Project Flight game

salasana = input("Salasana: ")
from geopy.distance import geodesic
import random

import mysql.connector
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password=salasana,
         autocommit=True
         )

# Valitsee satunnaisen maan V


#sql = "SELECT name from country order by RAND() LIMIT 1"

#kursori = yhteys.cursor()
#kursori.execute(sql)

#tulos = kursori.fetchall()
#print(f"{tulos[0]}")

#def haeKoodi(name):
  #  return tulos

# Valitse maa ja printtaa sen 5 ensimmäistä lentokenttää V
def haeMaa(chosen_name):
    sql = "SELECT latitude_deg, longitude_deg FROM airport Where iso_country in (select iso_country from country where name = '" + chosen_name + "') limit 5"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

maa = input("anna maa nimi: ")
haeMaa(maa)

for rivi in haeMaa(maa):
    print(f"{rivi[0]}, {rivi[1]}")
