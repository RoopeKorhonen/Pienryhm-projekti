salasana = input("Salasana: ")
from geopy.distance import geodesic

import mysql.connector
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password=salasana,
         autocommit=True
         )
def update_location(location):
    current_location = location
    print(f"Your location is: {current_location}")
    chooseCountry()


def emission_calculator(chosen):
    #print(f"pituus asemien välillä on {geodesic(km_calculator(chosen), km_calculator(current_location)).km} km")
    co2_used = geodesic(km_calculator(chosen), km_calculator(current_location)).km
    print(f"You consumed {co2_used / 1.69 * multiplier:0.2f} of CO2")
    update_location(chosen)

def choose_airport(choices):
    list = choices
    choice = input("Choose an airport: ")
    while choice not in list:
        print("Error")
        choice = input("Choose an airport: ")
    global current_location
    emission_calculator(choice)
    return


def km_calculator(airport):
    sql = "SELECT latitude_deg, longitude_deg FROM airport Where name = %s"
    ap_2_list = [airport]
    kursori = connection.cursor()
    kursori.execute(sql, ap_2_list)
    tulos = kursori.fetchall()
    return tulos

def searchAirports(chosen_name):
    sql = "SELECT name FROM airport Where iso_country in (select iso_country from country where name = '" + chosen_name + "') ORDER BY RAND() limit 5"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def chooseCountry():
    country = input("Select a country to fly to: ")
    searchAirports(country)
    list = []
    for rivi in searchAirports(country):
        ''.join(rivi)
        print(f"{rivi[0]} {geodesic(km_calculator(rivi[0]), km_calculator(current_location)).km:0.2f} km")
        list.append(rivi[0])
    choose_airport(list)
def spawn_point():
    spawn_point_code = "SELECT name from airport order by RAND() limit 1"
    spawn_point_cursor = connection.cursor()
    spawn_point_cursor.execute(spawn_point_code)
    result = spawn_point_cursor.fetchall()
    for line in result:
        current_airport = line
        current_airport = current_airport[0]
        print(f"You're currently at: {current_airport}")
        global current_location
        current_location = current_airport
    chooseCountry()
def Difficulty():
    diff_level = input("Please choose a difficulty level: \nThe Difficulty levels are \nEasy\nNormal\nHard\n:")
    global multiplier
    while diff_level != "easy" or "normal" or "hard":
        if diff_level == "easy":
            print("Chose eazy mode, you lazy pleb\nLet's play")
            diff = 0.75
            return diff
        elif diff_level == "normal":
            print("You chose normal, kinda sus tbh\nLet's play")
            diff = 1.25
            return diff
        elif diff_level == "hard":
            print("You chose crazy mega hard mode you absolute unit!\nLet's play")
            diff = 1.75
            return diff
        else:
            print("ohh you're a funny guy haaa.")
        diff_level = input("Please choose a difficulty level: \nThe Difficulty levels are \nEasy\nNormal\nHard\n:")
def username_input():
    user = input("Hello user please stage your gamertag: ")
    print(f"Hello {user}, welcome to the world of flying games.\nI am your game engine Flying Ultimatum")
    return

username_input()
multiplier = Difficulty()
spawn_point()