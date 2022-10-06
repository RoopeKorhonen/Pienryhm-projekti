from geopy.distance import geodesic

def kursori_func(sql_komento):
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='SeOnSiina!?',
        autocommit=True
    )
    kursori = yhteys.cursor()

    kursori.execute(sql_komento)

    tulos = kursori.fetchall()

    return tulos

import mysql.connector
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='SeOnSiina!?',
         autocommit=True
         )

print("Hello this is the Flying game Ultimatum\nPlease take your time and enjoy the ride\n")
mainmenu_int = input("Main menu\n1.Play\n2.Scores\n3.Guide\n4.Quit\n")

if mainmenu_int == "1":
    print("Roberto")

elif mainmenu_int == "2":

    score_database = "SELECT screen_name, highscores FROM game ORDER BY highscores DESC LIMIT 5;"

    result_highscore = kursori_func(score_database)
    for x in result_highscore:
        print(x)


elif mainmenu_int == "3":
    print("THIS GAME IS EAASY; JUST FLY INTO DIFFERENT COUNTRIES")


elif mainmenu_int == "4":
    print("You have quit the game.")

else:
    print("WTF BRO")