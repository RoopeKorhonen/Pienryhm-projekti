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


sql = "SELECT name from country order by RAND() limit 1"

kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}")

#def haeKoodi(name):
  #  return tulos

# Valitse maa ja printtaa sen 5 ensimmäistä lentokenttää V
def haeLentokenttia(chosen_name):
    sql = "SELECT name FROM airport Where iso_country in (select iso_country from country where name = '" + chosen_name + "') ORDER BY RAND() limit 5"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

maa = input("Anna maa nimi: ")
haeMaa(maa)

for rivi in haeMaa(maa):
    print(f"{rivi[0]}")
