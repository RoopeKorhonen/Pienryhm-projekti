def visited_airport_list():
    visited_airports = []
    return visited_airports

player_list = visited_airport_list()

def high_score_calculator():
    highscore = len(visited_airport_list())*10
    return highscore

def cursor_func(connection_execute):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='SeOnSiina!?',
        autocommit=True
    )
    cursor = connection.cursor()

    cursor.execute(connection_execute)

    result = cursor.fetchall()

    return result

def high_score_add_to_database():
    #highScore_str = str(player_list)
    name_and_scoreADD: str = "INSERT INTO game (screen_name, highscores) values ('" + username_input() + "', '" + high_score_calculator(player_list) + "');"
    #scoreADD = "INSERT INTO game set highscores = '" + highScore_str + "';"
    cursor_func(name_and_scoreADD)






mainmenu_int = input("Main menu\n1.Play\n2.Scores\n3.Quit\n: ")
if mainmenu_int == "1":
    username_input()
    multiplier = Difficulty()
    current_airport = spawn_point()
    poll_country_selecting = country_info(country_selecting())
    high_score_add_to_database()
elif mainmenu_int == "2":
    score_database = "SELECT screen_name, highscores FROM game ORDER BY highscores DESC LIMIT 5;"

    result_highscore = cursor_func(score_database)
    for x in result_highscore:
        print(x)

elif mainmenu_int == "3":
    ("You have quit the game")
