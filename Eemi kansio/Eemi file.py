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

highScore = 0
distance = 0
def username_input ():
    user = input(print("Hello user please stage your gamertag: "))
    print(f"Hello {user}, welcome to the world of flying games.\nI am your game engine Flying Ultimatum")

def hae(lentoasema):
    sql = "select latitude_deg, longitude_deg from airport where ident = '" + lentoasema + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

username_input()
while highScore != "":
    x = input("Anna ensimmäinen ICAO-koodi: ")
    x = x.upper()
    hae(x)
    y = input("Anna toinen ICAO-koodi: ")
    y = y.upper()
    hae(y)
    print(f"{geodesic(hae(x),hae(y)).km:0.2f} kilometriä välimatkaa.")
    highScore = highScore + 1
    print(f"Points:{highScore}")
    distance = distance +
    print(f"Distance travelled {distance}km")
else:
    print(f"You got {highScore} points during this game!")
    print(f"You traveled {distance}km during this game!")
    print("Thank you for playing!")