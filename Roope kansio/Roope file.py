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
xdxdxdxdx testi
def country_selecting():
    country_select = input("Give country name")
    return country_select

def country_info(chosen):
    country_select = "SELECT * FROM country WHERE name = '" + chosen + "';"
    country_select_cursor = connection.cursor()
    country_select_cursor.execute(country_select)
    result = country_select_cursor.fetchall()
    return result

poll_country_selecting=country_selecting()
poll_country_selecting=country_info(poll_country_selecting)