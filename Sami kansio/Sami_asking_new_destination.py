# SAMI 9.) The program asks new destination(country) from the user.
import mysql

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='SeOnSiina!?',
         autocommit=True
         )


def countryselecting():


newDestination = input("Give a new destination country. The country needs to be a different one where you have already flown: ")
