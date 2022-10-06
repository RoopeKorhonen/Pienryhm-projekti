# 4  Peli kysyy pelaajalta mihin maahan he haluavat lentää ,
# 6.1 antaa 5 lähimmästä lentokentät ja co2 hinnan,
# lopettaa ohjelman jos ei ole varaa mihinkään lähelle olevalle lentokentälle --> 10)
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


def countryselecting():
    country = input("Where do you wanna fly?")
    looking_continent = "SELECT DISTINCT continent from "' + country + '" "
    looking_continent_cursor = connection.cursor()
    looking_continent_cursor.execute(lookingcontinent)
    looking_continent_result = looking_continent_cursor.fetchall()

    looking_country = "SELECT DISTINCT name  from country where continent = "' + looking_continent_result + '" "
    looking_country_cursor = connection.cursor()
    looking_country_cursor.execute(looking_country)
    looking_country_result = looking_country_cursor.fetchall()

    chosen_country = "SELECT DISTINCT name from "' + looking_country_result +  '" = "' + country + '" "
    chosen_country_cursor = connection.cursor()
    chosen_country_cursor.execute(chosen_country)
    result = chosen_country_cursor.fetchall()
    return result

print(countryselecting())

