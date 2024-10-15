#This will be a basic number guessing game
import random

beginRange = int(input("We are gonna create a range for you to guess a number... What will be the first number?"))
endRange = int(input("Okay, what will be the end of the range?"))
answer = random.randrange(beginRange,endRange)
print(answer)

gGuess = 3

while gGuess != 0:
    holder = int(input("What number do you think it is?"))

    if holder == answer:
        print("You got it!! it was " + str(answer))
        gGuess = 0
    else:
        print("WRONG!!!")
        gGuess-=1
