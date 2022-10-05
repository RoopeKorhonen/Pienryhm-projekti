# Project Flight game

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
# testaus




userName = input("Choose your username ")
#usernameADD = "INSERT INTO game (screen_name) values ('" + userName + "');"

#kursori_func(usernameADD)

print(f"Hello {userName}! Welcome to flight_game; ")
print("Your purpose is to fly to airports hehe xd")
highScore = 0

def high_score_calculator(airport_amount):
    while highScore != 2:
    print(f"{geodesic(hae(x),hae(y)).km:0.2f} kilometriä välimatkaa.")
    highScore = highScore + 1
    print(f"Points:{highScore}")
    else:
        highScore_str = str(highScore)
        name_and_scoreADD = "INSERT INTO game (screen_name, highscores) values ('" + userName + "', '" + highScore_str + "');"
        #scoreADD = "INSERT INTO game set highscores = '" + highScore_str + "';"
        kursori_func(name_and_scoreADD)

    print(f"Pistemääräsi on {highScore} horrayyyy")




def laskin(määrä):
    pisteet = määrä * 10
    return pisteet
# tarvitsee lentokenttien arvot




laskin(määrä)