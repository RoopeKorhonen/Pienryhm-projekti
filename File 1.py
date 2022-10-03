# Project Flight game

import random

import mysql.connector
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='moodleroope',
         autocommit=True
         )



def username_input ():
    user = input(print("Hello user please stage your gamertag: "))
    print(f"Hello {user}, welcome to the world of flying games.\nI am your game engine Flying Ultimatum")



def Difficulty():
    diff_level = input("Please choose a difficulty level: \nThe Difficulty levels are \nEasy\nNormal\nHard\n:")
    while diff_level != "easy" or "normal" or "hard":
        if diff_level == "easy":
            print("Chose eazy mode, you lazy pleb\nLet's play")
            break
        elif diff_level == "normal":
            print("You chose normal, kinda sus tbh\nLet's play")
            break
        elif diff_level == "hard":
            print("You chose crazy mega hard mode you absolute unit!\nLet's play")
            break
        else:
            print("ohh you're a funny guy haaa.")
        diff_level = input("Please choose a difficulty level: \nThe Difficulty levels are \nEasy\nNormal\nHard\n:")

def country_selecting():
    country_select = input("Give country name")
    return country_select

def country_info(chosen):
    country_select = "SELECT * FROM country WHERE name = '" + chosen + "';"
    country_select_cursor = connection.cursor()
    country_select_cursor.execute(country_select)
    result = country_select_cursor.fetchall()
    return result


poll_country_selecting=country_info(country_selecting())

mainmenu_int = input("Main menu\n1.Play\n2.Scores\n3.Quit\n: ")
if mainmenu_int == "1":
    username_input()
    Difficulty()
    poll_country_selecting = country_info(country_selecting())
elif mainmenu_int == "2":
    print("highscores menu")
elif mainmenu_int == "3":
    ("You have quit the game")


