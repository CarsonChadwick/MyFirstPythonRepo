class SoccerTeam() :
  def __init__(self, sName, sCoach) :
    self.team_name = sName
    self.wins = 0
    self.losses = 0
    self.win_loss_pct = 0.0
    self.coach = Coach(sCoach)
  def calcWinLoss(self) :
    self.win_loss_pct = self.wins / (self.wins + self.losses)
  def displayInfo(self) :
    return (self.team_name + " has " + str(self.wins) + " wins")
  def newWin(self) :
    self.wins += 1
    self.coach.career_wins += 1
  def newLoss(self) :
    self.losses += 1
    self.coach.career_losses += 1
class Person() :
  def __init__(self, name) :
    self.name = name
class Coach(Person) :
  def __init__(self, name) :
    super().__init__ (name)
    self.career_wins = 0
    self.career_losses = 0
  def displayInfo(self) :
    return (self.name + " has " + str(self.career_wins) + " wins")
  

lstTeams = []
iNum = int( input("How many teams? "))
for iCount in range(0, iNum) :
  sTeam = input("enter team name: ")
  sCoach = input("Enter coach name: ")
  
  oTeam = SoccerTeam(sTeam, sCoach)
  lstTeams.append(oTeam)

#print(lstTeams[0].team_name)
#print(lstTeams[0].coach.name)
for icount in range (0, len(lstTeams)):
  print(lstTeams[icount].team_name)
  print(lstTeams[icount].coach.name)