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
    country_selecting()

def country_selecting():
    country_select = input("Give country name: ")
    return country_select
    Searching_5_Airports()


def Searching_5_Airports(chosen):
    sql = "SELECT name FROM airport Where iso_country in (select iso_country from country where name = '" + chosen + "') ORDER BY RAND() limit 5"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def country_info(chosen):
    country_select = "SELECT * FROM country WHERE name = '" + chosen + "';"
    country_select_cursor = connection.cursor()
    country_select_cursor.execute(country_select)
    result = country_select_cursor.fetchall()
    return result

username_input()