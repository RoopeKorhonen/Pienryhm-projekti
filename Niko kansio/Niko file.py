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

sql = "SELECT name FROM airport Where iso_country in (select iso_country from country where name = '" + chosen_name + "') ORDER BY RAND() limit 5"
list = []
for rivi in haeLentokenttia(country_selecting()):
    print(f"{rivi[0]} {geodesic(co2_calculator(rivi[0]), co2_calculator(current_airport)).km:0.2f} km")
    list.append(rivi[0])
print(list)
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()
return list

