# Carson Chadwick
# Section 04
# Takes the input of different teams, their scores, and finds wins/losses percentages

#Variables
# Enter the number of teams
iNumTeams = int(input("Enter how many teams : "))
# A for loop to name each team
for iOuterCount in range(1, (iNumTeams + 1)) :
    sTeamName = input("\nEnter team " + str(iOuterCount) + "'s name: ")
    sGamesPlayed = int(input("How many games did the " + sTeamName + " team play?: "))
    iGamesWon = 0
    for iInnerCount in range(1, (sGamesPlayed + 1)) :
        iTeamScore = int(input("Enter " + sTeamName + "'s score for game number " + str(iInnerCount) + " : "))
        iOpponantScore = int(input("Enter the opponants score: "))
        while (iTeamScore == iOpponantScore) : 
            print("You can not have a tie.")
            iTeamScore = int(input("ReEnter " + sTeamName + "'s score: "))
            iOpponantScore = int(input("ReEnter the opponants score: "))
        if (iTeamScore > iOpponantScore) :
            iGamesWon += 1
    iWinLoss = round(iGamesWon/sGamesPlayed*100)

    if (iOuterCount == 1) :
        sWinningTeam = sTeamName
        iWinningPercent = iWinLoss
    elif (iWinLoss > iWinningPercent) :
        sWinningTeam = sTeamName
        iWinningPercent = iWinLoss
    print(str(iWinLoss) + "%")
print("\nThe team with the best percentage of wins is the " + sWinningTeam + " team. They won " + str(iWinningPercent) + "%" + " of their games.")
# A nested for loop that asks for game scores determining who won (no ties)

# Calculate win loss percentage and post the best team
