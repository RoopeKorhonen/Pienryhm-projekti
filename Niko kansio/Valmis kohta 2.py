print("Hello this is the Flying game Ultimatum\nPlease take your time and enjoy the ride\n")
mainmenu_int = input("Main menu\n1.Play\n2.Scores\n3.Quit\n: ")

def Difficulty():
    diff_level = input("Please choose a difficulty level: \nThe Difficulty levels are \nEasy\nNormal\nHard\n:")

    if diff_level == "easy":
        print("Chose eazy mode, you lazy pleb")
    elif diff_level == "normal":
        print("You chose normal, kinda sus tbh")
    elif diff_level == "hard":
        print("You chose crazy mega hard mode you absolute unit!")
    else:
        print("ohh you're a funny guy haaa.")

if mainmenu_int == "1":
    Difficulty()
elif mainmenu_int == "2":
    print("highscores menu")
elif mainmenu_int == "3":
    ("You have quit the game")
