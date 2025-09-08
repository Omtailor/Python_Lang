"""The game() function in a program lets a user play a game and returns score as an integer. You need to read a file Hi-Score.txt which
is either blank or contains previous High Score and update the High Score if break"""

import random

def game():
    print("You are playing the game: ")
    score = random.randint(1,100)
    # For fetching the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
    if (hiscore!=""):
        hiscore = int(hiscore)
    else:
        hiscore = 0
        
    print(f"Your score is {score}")
    if(score>hiscore):
    # Rewrite hiscore to file
        with open("hiscore.txt", "w") as f:
            f.write(str(score)) 
    return score

game()   