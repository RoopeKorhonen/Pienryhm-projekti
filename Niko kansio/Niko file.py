import mysql.connector

# yhdeyden avaus
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='',
         autocommit=True
         )


difficulty= input("Please choose a difficulty level")
    while diff_level ==" ":
        if diff_level == 1:
            print("Chose eazy mode, you lazy pleb")
        elif diff_level == 2:
            print("You chose normal, kinda sus tbh")
        elif diff_level == 3:
            print("You chose crazy mega hard mode you absolute unit")
        else
            print("ohh you're a funny guy haaa.")
username_input()
def username_input ():
    user = input(print("Hello user please stage your gamertag: "))
    print(f"Hello {user}, welcome to the world of flying games.\nI am your game engine Flying Ultimatum")

