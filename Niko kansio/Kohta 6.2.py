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
current_airport = ""
def start_game():
    sql = "SELECT name from airport order by RAND() limit 1"

    kursori = yhteys.cursor()
    kursori.execute(sql)

    tulos = kursori.fetchall()
    for rivi in tulos:
        current_airport = rivi

    current_airport = current_airport[0]
    print(f"You're at {current_airport}")

start_game()

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
    airport_name = airport
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
        #''.join(rivi)
        print(f"{rivi[0]} {geodesic(co2_calculator(rivi[0]), co2_calculator(current_airport)).km:0.2f} km")
        list.append(rivi[0])
    return list



def choose_airport():
    choice = input("Valitse lentokenttä: ")
    return choice

def visited_airports():
    if chosen_airport not in maalista:
        print("Virheellinen valinta")
        chosen_airport = choose_airport()
    else:
        visited_airports.append(chosen_airport)

print(visited_airports)
def co2_calculator():
print(f"pituus asemien välillä on {geodesic(co2_calculator(chosen_airport), co2_calculator(current_airport)).km:0.2f} km")
co2_used = geodesic(co2_calculator(chosen_airport), co2_calculator(current_airport)).km / 5.5 * 1.5
print(f"{co2_used:0.2f}")


valitseMaa()
choose_airport()
maalista = valitseMaa()
chosen_airport = choose_airport()
choose_airport()
co2_calculator(chosen_airport)
co2_calculator(current_airport)