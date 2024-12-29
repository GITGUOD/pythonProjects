#Guess the Number:

#The program randomly selects a number, and the player guesses it.
#Give hints like "too high" or "too low."
#Add difficulty levels (e.g., range of numbers).

import random
import time

#Letting the user choose the first number of the interval
firstInterval = int(input("Select the difficulty by entering the first number of the interval(e.g., '1'): \n"))

#Having delays, for quality of life gameplay
time.sleep(1)

print("Processing...")

time.sleep(1)

#Letting the user pick the second interval number
secondInterval = int(input("Now, select the second number of the interval(e.g., '10'): \n"))

#Having repeatable delays
time.sleep(1)

print("Processing...")

time.sleep(1)

#Checking for valid range

if firstInterval >= secondInterval:
    print("Invalid range, the first number has to be smaller than the second number")

else:
    print("Valid range, time to start the game")

    #Letting the system determine the random number which you as the user have to guess
    rightNbr = random.randint(firstInterval, secondInterval)

    while True:
     
     guessNbr = int(input("Now, guess the right number!"))

     if rightNbr >= guessNbr:
        print("Try again, the number is higher!")

     elif rightNbr <= guessNbr:
        print("Try again, the number is lower!")
     else:
        print("You guessed it! You won")

