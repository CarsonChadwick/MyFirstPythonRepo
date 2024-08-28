# Carson Chadwick
# Section 04
# This code will practice simple loops
# prompt user to see if they want to play
# Guessing Game
# prompt user for the guess
# Check if correct
# Display message

sAnswer = input("Do you want to play? (Y/N): ")
iSolution = 7
iCounter = 0

if (sAnswer.upper() == "Y") :
    while (iCounter < 5) :
        iGuess = int(input("Enter your guess from 0 to 10: "))
        iCounter += 1

        if (iGuess == iSolution) :
            print("You guessed the number!")
            print("Congrats!")
            break
        elif (iGuess > iSolution) :
            print("Too high") 
        else :
            print ("Too low")

    sGuessString = ""
    if (iCounter == 1) :
        sGuessString = " guess"
    else :
        sGuessString = " guesses"

    print ("You took " + str( iCounter) + sGuessString)
else :
    print("Hope you can play some other time.")           
