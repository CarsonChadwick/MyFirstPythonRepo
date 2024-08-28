import random

iRandom = random.randint(1,50)

bContinue = True
iCount = 0

while(bContinue == True) :
    iGuess = int(input("Enter a number between and including 1 and 50: "))
    iCount += 1
    if (iGuess > iRandom) :
        print(str(iGuess) + " is too high")
    elif (iGuess < iRandom) :
        print(str(iGuess) + " is too low")
    else :
        print("You guessed it!")
        bContinue = False
print("It took you " + str(iCount) + " guesses.")