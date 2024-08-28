# Carson Chadwick
# Section 05
# Practice Using built in functions

import random
from datetime import datetime

iMaxNumber = int(input("What is the maximum number to use? "))

iRandomNum = random.randrange(0, iMaxNumber, 1)

dStartTime = datetime.now()

bContinue = True
while (bContinue == True): 
    iGuess = int(input("\nEnter a number between 0 and " + str(iMaxNumber) + ": "))
    if (iGuess == iRandomNum) :
        dEndTime = datetime.now()
        bContinue = False
        print("Congrats! You guessed the number!")
    elif (iGuess > iRandomNum) :
        print ("Too high")
    else :
        print("Too low")
dTotalTime = dEndTime - dStartTime
print("It took " + str(dTotalTime.seconds) + " seconds")
