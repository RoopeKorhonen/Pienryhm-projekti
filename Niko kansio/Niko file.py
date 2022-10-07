import mysql.connector

# yhdeyden avaus
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='',
         autocommit=True

def game_over():
    print("Game over you ran out of co2 to consume")

def co2_budget_tracker():
    if co2_used < 15000:
        co2_budget = (co2_budget - co2_used)
        chooseCountry()
    else:
        game_over()

def game_over():
    print("Game over you ran out of co2 to consume")


