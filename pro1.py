
#Guess Number Project

import random

target = random.randint(1,100)
while True:
    userChoice = input("Guess the target or Quite(Q):")
    if(userChoice=="Q"):
        break

    userChoice= int(userChoice)
    if(userChoice==target):
        print("Success : Correct Guess")
        break
    elif(userChoice<target):
        print("your number was too small. take a bigger guess.")
    else:
        print("your number was too bigger. take a small guess.")


print("----Game Over----")