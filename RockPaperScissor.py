import random

#Hur löser vi detta? What's our plan? How do we solve and build this rock-, paper-, scissor-game?
#We need three objects that is supposed to symbolize scissor, rock and paper

#One random-object that is supposed to be used for the bot as a way to randomize the pick between rock,papper and scissor 
#And finally one object, some sort of scanner-object that the player can choose between scissor, rock and paper

#Before
#s = "Scissor" 
#r = "Rock"
#p = "paper"

#A array to store the string objects


toPick = ["Scissor", "Rock", "Paper"]


botPick = random.choice(toPick)

userPick = input("Choose between Scissor, Rock or Paper \n")

print("You picked " + userPick)

print("The bot picked " + botPick)

if botPick == userPick:
    print("Tie, try again")
else:
    if botPick == "Rock" and userPick == "Scissor":
        print("You lost")
    elif botPick == "Rock" and userPick == "Paper":
        print("You Won")
    elif botPick == "Scissor" and userPick == "Paper":
        print("You Lost")
    elif botPick == "Scissor" and userPick == "Rock":
        print("You Won")
    elif botPick == "Paper" and userPick == "Scissor":
        print("You Won")
    elif botPick == "Paper" and userPick == "Rock":
        print("You Lost")
