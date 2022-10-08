
def high_score_calculator(airport_amount):
    airports = len(airport_amount)*10
    return airports


airport = ["vantaa", "ruotsi", "kulli"]

print(high_score_calculator(airport))

#    while highScore != 2:
 #   print(f"{geodesic(hae(x),hae(y)).km:0.2f} kilometriä välimatkaa.")
  #  highScore = highScore + 1
   # print(f"Points:{highScore}")


##### TÄÄ VIELÄ FUNKTIOKSI. TÄMÄ LISÄÄ HIGHSCOREN DATABASEEN!!!!
    else:
        highScore_str = str(highScore)
        name_and_scoreADD = "INSERT INTO game (screen_name, highscores) values ('" + userName + "', '" + highScore_str + "');"
        scoreADD = "INSERT INTO game set highscores = '" + highScore_str + "';"
        kursori_func(name_and_scoreADD)

    print(f"Pistemääräsi on {highScore} horrayyyy")

high_score_calculator(player_airports)



#def laskin(määrä):
 #   pisteet = määrä * 10
  #  return pisteet
# tarvitsee lentokenttien arvot




#laskin(määrä)