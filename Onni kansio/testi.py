salasana = input("Salasana: ")
from geopy.distance import geodesic
import random

import mysql.connector
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password=salasana,
         autocommit=True
         )

