# SAMI 9.) The program asks new destination(country) from the user.

import mysql.connector
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='SeOnSiina!?',
         autocommit=True
         )

def countryselecting():
        country = input("Where do you wanna fly?")
        lookingcontinent = "SELECT DISTINCT continent from "' + country + '" "
        looking_continent_cursor = connection.cursor()
        looking_continent_cursor.execute(lookingcontinent)
        looking_continent_result = looking_continent_cursor.fetchall()

        lookingcountry = "SELECT DISTINCT name  from country where continent = "' + looking_continent_result + '" "
        looking_country_cursor = connection.cursor()
        looking_country_cursor.execute(lookingcountry)
        looking_country_result = looking_country_cursor.fetchall()

        chosencountry = "SELECT DISTINCT name from "' + looking_country_result +  '" = "' + country + '" "
        chosen_country_cursor = connection.cursor()
        chosen_country_cursor.execute(chosencountry)
        result = chosen_country_cursor.fetchall()
        return result
print(countryselecting())
