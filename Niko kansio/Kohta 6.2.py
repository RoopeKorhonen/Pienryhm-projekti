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

visited_airports = []

sql = "SELECT name from airport order by RAND() limit 1"

kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi}")
    current_airport = rivi

current_airport = current_airport[0]
print(current_airport)

#def haeKoodi(name):
  #  return tulos

# Valitse maa ja printtaa sen 5 ensimmäistä lentokenttää V
def haeLentokenttia(chosen_name):
    sql = "SELECT name FROM airport Where iso_country in (select iso_country from country where name = '" + chosen_name + "') ORDER BY RAND() limit 5"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def co2_calculator(airport):
    sql = "SELECT latitude_deg, longitude_deg FROM airport Where name = '" + airport + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def valitseMaa():
    maa = input("Anna maa nimi: ")
    haeLentokenttia(maa)
    list = []
    for rivi in haeLentokenttia(maa):
        print(f"{rivi[0]} {geodesic(co2_calculator(rivi[0]), co2_calculator(current_airport)).km:0.2f} km")
        list.append(rivi[0])
    print(list)
    return list

def choose_airport():
    choice = input("Valitse lentokenttä: ")
    return choice

maalista = valitseMaa()
chosen_airport = choose_airport()
if chosen_airport not in maalista:
    print("Virheellinen valinta")
    chosen_airport = choose_airport()
else:
    visited_airports.append(chosen_airport)

print(visited_airports)

co2_calculator(chosen_airport)
co2_calculator(current_airport)


print(f"pituus asemien välillä on {geodesic(co2_calculator(chosen_airport), co2_calculator(current_airport)).km:0.2f} km")
co2_used = geodesic(co2_calculator(chosen_airport), co2_calculator(current_airport)).km / 5.5 * 1.5
print(f"{co2_used}:2f")


valitseMaa()
choose_airport()