class SoccerTeam() :
    def __init__(self, teamName, wins) :
        self.team_name = teamName
        self.wins = wins
        self.losses = 0
        self.win_loss_pct = 0.0
        self.coach = Coach()
    
    def newWin(self) :
        self.wins += 1
    def newLoss(self) :
        self.losses += 1

    def calcWinLoss(self) :
        self.win_loss_pct = self.wins/(self.wins + self.losses)
    
    def displayTeamInfo(self) :
        return (self.team_name + " has " + str(self.wins) + " wins")

class Coach():
    def __init__(self) :
        self.name = ""
        self.career_wins = 0
        self.career_losses = 0

    def displayCoachInfo(self) :
        pass
sName = input("Enter team name: ")
iWins = int(input("How many wins: "))
oTeam = SoccerTeam(sName, iWins)
oTeam.coach.name = "Carson Chadwick"
for iCount in range(0,10) :
    oTeam.newWin()

oTeam.newLoss()

oTeam.calcWinLoss()

print(oTeam.displayTeamInfo())
