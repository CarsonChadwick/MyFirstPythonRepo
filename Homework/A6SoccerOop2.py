# Carson Chadwick
# Section 04
# This program combines the A4 womens soccer program and A5 soccer homeworks
# The program creats a soccer team object, takes input on the team name and games played, and displays a randomized score, and says how the team did.

# Create the soccerTeam class
class SoccerTeam() :
    # Create constructor method
    def __init__(self, team_Name):
        self.team_Name = team_Name
        self.wins = 0
        self.losses = 0
        self.goals_Scored = 0
        self.goals_Allowed = 0
    # Create seasonStatus method
    def seasonStatus (self): 
        if (self.wins/(self.wins + self.losses) >= .75) :
            message = "Qualified for the NCAA Women's Soccer Tournament"
        elif (self.wins/(self.wins + self.losses) >= .50):
            message = "You had a good season"
        else:
            message = "Your team needs practice!"
        return message

# Import random and initialize some variables
import random
iTeamWins = 0
iTeamLoss = 0
iGoalsScored = 0
iGoalsAllowed = 0

# Assign home name
sHomeTeam = input("Enter the name of your team (the home team): ")

# Create object
oTeam = SoccerTeam(sHomeTeam)

# How many teams we will play
bValue = True
while (bValue == True) :
    try:
        iNumGames = int(input("Enter how many teams " + sHomeTeam + " will play: "))
        bValue = False
    except: 
        print("Error, please enter a valid input (ex. 2)")
print("\n")

# For loop for each team generating random scores and counting wins and losses
for icount in range(0,iNumGames) :
    sAwayTeam = input("Enter the name of the away team for game " + str(icount + 1) + ": ")
    iRnd1 = random.randint(0, 10)
    iRnd2 = random.randint(0, 10)
    # While loop to ensure no scores are the same
    while (iRnd1 == iRnd2) :
        iRnd1 = random.randint(0, 10)
        iRnd2 = random.randint(0, 10)
    oTeam.goals_Scored += iRnd1
    oTeam.goals_Allowed += iRnd2
    # Count wins and losses
    if iRnd1 > iRnd2 :
        oTeam.wins += 1
    else :
        oTeam.losses += 1
    # Print the outcome of the game
    print(sHomeTeam + "'s score: " + str(iRnd1) + " " + sAwayTeam + "'s score: " + str(iRnd2))

# print the final season record with wins and total goals
print("\n" + "Team name: " + oTeam.team_Name)
print("Final season record: " + str(oTeam.wins) + "-" + str(oTeam.losses))
print("Total goals scored: " + str(oTeam.goals_Scored) + " - Total goals allowed: " + str(oTeam.goals_Allowed))
# Print the seasonStatus method
print(oTeam.seasonStatus())
