import random
import time

#Hur löser vi detta? What's our plan? How do we solve and build this rock-, paper-, scissor-game?
#We need three objects that is supposed to symbolize scissor, rock and paper

#One random-object that is supposed to be used for the bot as a way to randomize the pick between rock,papper and scissor 
#And finally one object, some sort of scanner-object that the player can choose between scissor, rock and paper

#Before
#s = "Scissor" 
#r = "Rock"
#p = "paper"

#A array to store the string objects


toPick = ["scissor", "rock", "paper"]


botPick = random.choice(toPick)

userPick = input("Choose between Scissor, Rock or Paper \n")

time.sleep(1)

print("Processing...")

time.sleep(1)

print("You picked " + userPick)

time.sleep(1)

print("The bot picked " + botPick)

time.sleep(1)

print("Processing")

time.sleep(1)

if botPick.casefold() == userPick.casefold():
    print("Tie, try again")
else:
    if botPick.casefold() == "rock" and userPick.casefold() == "scissor":
        print("You lost")
    elif botPick.casefold() == "rock" and userPick.casefold() == "paper":
        print("You Won")
    elif botPick.casefold() == "scissor" and userPick.casefold() == "paper":
        print("You Lost")
    elif botPick.casefold() == "scissor" and userPick.casefold() == "rock":
        print("You Won")
    elif botPick.casefold() == "paper" and userPick.casefold() == "scissor":
        print("You Won")
    elif botPick.casefold() == "paper" and userPick.casefold() == "rock":
        print("You Lost")
