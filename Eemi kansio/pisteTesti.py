# Project Flight game

from geopy.distance import geodesic
import mysql.connector
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
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

def kursori_func(sql_komento):
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='RootWord1Salasana1',
        autocommit=True
    )
    kursori = yhteys.cursor()

    kursori.execute(sql_komento)

    tulos = kursori.fetchall()

    return tulos

userName = input("Choose your username ")
usernameADD = "INSERT INTO game (screen_name) values ('" + userName + "');"

kursori_func(usernameADD)

print(f"Hello {userName}! Welcome to flight_game; ")
print("Your purpose is to fly to airports hehe xd")
highScore = 0

while highScore != 2:
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
    highScore_str = str(highScore)
    scoreADD = "update table game (highscores) values (" + highScore_str + ") where screen_name = '" + userName + "';"
    kursori_func(scoreADD)

    print(f"Pistemääräsi on {highScore} horrayyyy")






