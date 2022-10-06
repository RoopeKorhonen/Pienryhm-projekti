salasana = input("Salasana: ")
from geopy.distance import geodesic


import mysql.connector
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password=salasana,
         autocommit=True
         )


visited_airports = []
current_airport = ""

def haeLentokenttia(chosen_name):
    sql = "SELECT name FROM airport Where iso_country in (select iso_country from country where name = '" + chosen_name + "') ORDER BY RAND() limit 5"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def choose_airport():
    choice = input("Valitse lentokenttä: ")
    haeLentokenttia(choice)
    return

def km_calculator(airport):
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
        # ''.join(rivi)
        print(f"{rivi[0]} {geodesic(co2_calculator(rivi[0]), co2_calculator(current_airport)).km:0.2f} km")
        list.append(rivi[0])
    return list

def start_game():
    sql = "SELECT name from airport order by RAND() limit 1"

    kursori = yhteys.cursor()
    kursori.execute(sql)

    tulos = kursori.fetchall()
    for rivi in tulos:
        current_airport = rivi

    current_airport = current_airport[0]
    print(f"You're at {current_airport}")
    valitseMaa()

start_game()