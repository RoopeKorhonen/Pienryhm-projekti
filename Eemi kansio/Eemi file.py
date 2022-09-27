# Project Flight game

from geopy.distance import geodesic
import mysql.connector
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='RootWord1Salasana1',
         autocommit=True
         )
# testaus
def hae(lentoasema):
    sql = "select latitude_deg, longitude_deg from airport where ident = '" + lentoasema + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

userName = input("Choose your username ")
print(f"Hello {userName}! Welcome to flight_game; ")
print("Your purpose is to fly to airports hehe xd")
highScore = 0

while highScore != -1:
    x = input("Anna ensimmäinen ICAO-koodi: ")
    x = x.upper()
    hae(x)
    y = input("Anna toinen ICAO-koodi: ")
    y = y.upper()
    hae(y)
    print(f"{geodesic(hae(x),hae(y)).km:0.2f} kilometriä välimatkaa.")
    highScore = highScore + 1
    print(f"Points:{highScore}")
else:
    print(f"Pistemääräsi on {highScore} horrayyyy")
