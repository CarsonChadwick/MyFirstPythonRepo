# Carson Chadwick
# Section 04
# This program simulates a womens soccer team's season, calculates their win percentage based on teams played, and displays how they did.

# Import random and initialize some variables
import random
iTeamWins = 0
iTeamLoss = 0
# Input your home team
print("Welcome to the Women's Soccer simulation!")
sHomeTeam = input("What is the name of your home team? ")
# Input how many games they will play in the season (include exception test if not enter a number)
bValue = True
while (bValue == True) :
    try:
        iNumGames = int(input("Enter how many games " + sHomeTeam + " played: "))
        bValue = False
    except: 
        print("Error, please enter a valid input (ex. 2)")
# For loop for each team generating random scores and counting wins and losses
for icount in range(0,iNumGames) :
    sAwayTeam = input("Enter the name of the away team for game " + str(icount + 1) + ": ")
    iRnd1 = random.randrange(0, 10)
    iRnd2 = random.randrange(0, 10)
    # While loop to ensure no scores are the same
    while (iRnd1 == iRnd2) :
        iRnd1 = random.randrange(0, 10)
        iRnd2 = random.randrange(0, 10)
    # Count wins and losses
    if iRnd1 > iRnd2 :
        iTeamWins += 1
    else :
        iTeamLoss += 1
    # Print the outcome of the game
    print(sHomeTeam + "'s score: " + str(iRnd1) + " " + sAwayTeam + "'s score: " + str(iRnd2))
# print the final season record
print("\nFinal season record: " + str(iTeamWins) + "-" + str(iTeamLoss))
# Use if statement to print statement on how the season went.
if (iTeamWins/iNumGames >= .75) :
    print("Qualified for the NCAA Women's Soccer Tournament")
elif (iTeamWins/iNumGames >= .50):
    print("You had a good season")
else:
    print("Your team needs practice!")
