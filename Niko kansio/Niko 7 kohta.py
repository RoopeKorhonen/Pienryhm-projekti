from geopy.distance import geodesic
import random

import mysql.connector
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password="",
         autocommit=True
         )
def cursor():
kursori = yhteys.cursor()
kursori.execute(sql)

def co2_calculator():
    cursor()
    co2_left = "SELECT co2_consumed FROM game where "+ user + "