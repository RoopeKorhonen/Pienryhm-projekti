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
    country = str(input("Where do you wanna fly?"))
    lookingcountry = "SELECT continent WHERE iso_country = '" + country + '" "
    return country
