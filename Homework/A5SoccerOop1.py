# Carson Chadwick
# Section 04
# This program is to practice OOP programming by creating a soccerTeam class
# with a method that returns their win/loss record.

# Create the soccerTeam class
class SoccerTeam() :
    # Create constructor method
    def __init__(self, team_Name, wins, losses, goals_Scored, goals_Allowed):
        self.team_Name = team_Name
        self.wins = wins
        self.losses = losses
        self.goals_Scored = goals_Scored
        self.goals_Allowed = goals_Allowed
    # Create seasonStatus method
    def seasonStatus (self): 
        if (self.wins/(self.wins + self.losses) >= .75) :
            message = "Qualified for the NCAA Women's Soccer Tournament"
        elif (self.wins/(self.wins + self.losses) >= .50):
            message = "You had a good season"
        else:
            message = "Your team needs practice!"
        return message
# Assign variables for the attributes
sTeamName = "BYU"
iWins = 5
iLosses = 4
iGoalsScored = 35
iGoalsAllowed = 30
# Create object with attributes
oTeam = SoccerTeam(sTeamName, iWins, iLosses, iGoalsScored, iGoalsAllowed)
# Print the seasonStatus method
print(oTeam.seasonStatus())
