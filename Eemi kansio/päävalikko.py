from geopy.distance import geodesic
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

    score_database = "SELECT highscores, COUNT(*) >= 5 FROM game, WHERE highscores = '" + highScore_str + "';"

    sql = "SELECT type, COUNT(*) FROM airport WHERE iso_country = '" + maakoodi + "' GROUP BY TYPE"
    scoreADD = "update game set highscores = '" + highScore_str + "' where screen_name = '" + userName + "';"
    select
    lemmikki_id, count(*)
    from omistaa

    group
    by
    lemmikki_id
    having
    count(*) >= 2;


elif mainmenu_int == "3":
    print("THIS GAME IS EAASY; JUST FLY INTO DIFFERENT COUNTRIES")


elif mainmenu_int == "4":
    print("You have quit the game.")

else:
    print("WTF BRO")