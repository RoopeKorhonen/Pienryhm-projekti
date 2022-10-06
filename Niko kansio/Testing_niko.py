# Project Flight game

import random
from geopy.distance import geodesic

import mysql.connector
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='',
         autocommit=True
         )



def username_input ():
    user = input("Hello user please stage your gamertag: ")
    print(f"Hello {user}, welcome to the world of flying games.\nI am your game engine Flying Ultimatum")
    Difficulty()


def Difficulty():
    diff_level = input("Please choose a difficulty level: \nEasy\nNormal\nHard\n:")
    while diff_level != "easy" or "normal" or "hard":
        if diff_level == "easy":
            print("Chose eazy mode, you lazy pleb\nLet's play")
            spawn_point()
            return 0.75
        elif diff_level == "normal":
            print("You chose normal, kinda sus tbh\nLet's play")
            spawn_point()
            return 1.25
        elif diff_level == "hard":
            print("You chose crazy mega hard mode you absolute unit!\nLet's play")
            spawn_point()
            return 1.75
        else:
            print("ohh you're a funny guy haaa.")
        diff_level = input("Please choose a difficulty level: \nThe Difficulty levels are \nEasy\nNormal\nHard\n:")


def spawn_point():
    spawn_point_code= "SELECT name from airport order by RAND() limit 1"
    spawn_point_cursor = connection.cursor()
    spawn_point_cursor.execute(spawn_point_code)
    result = spawn_point_cursor.fetchall()
    for line in result:
        current_airport = line
        current_airport = current_airport[0]
        print(f"You currently at: {current_airport}")
    search_airports()

def search_airports(chosen_name):
    sql = "SELECT name FROM airport Where iso_country in (select iso_country from country where name = '" + chosen_name + "') ORDER BY RAND() limit 5"
    list = []
    for rivi in haeLentokenttia(country_selecting()):
        print(f"{rivi[0]} {geodesic(co2_calculator(rivi[0]), co2_calculator(current_airport)).km:0.2f} km")
        list.append(rivi[0])
    print(list)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return list


def country_selecting():
    country = input("Anna country nimi: ")
    search_airports(country)
    list = []
    for rivi in search_airports(country):
        print(f"{rivi[0]} {geodesic(co2_calculator(rivi[0]), co2_calculator(current_airport)).km:0.2f} km")
        list.append(rivi[0])
    print(list)
    return list



def country_info(chosen):
    country_select = "SELECT * FROM country WHERE name = '" + chosen + "';"
    country_select_cursor = connection.cursor()
    country_select_cursor.execute(country_select)
    result = country_select_cursor.fetchall()
    return result
def co2_calculator():
    print(f"pituus asemien välillä on {geodesic(co2_calculator(chosen_airport), co2_calculator(current_airport)).km:0.2f} km")
    co2_used = geodesic(co2_calculator(chosen_airport), co2_calculator(current_airport)).km / 5.5 * multiplier
    return co2_used


username_input()
co2_calculator(chosen_airport)
co2_calculator(current_airport)