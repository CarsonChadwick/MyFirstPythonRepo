class SoccerTeam() :
  def __init__(self, sName, sCoach) :
    self.__team_name = sName.upper()
    self.wins = 0
    self.losses = 0
    self.win_loss_pct = 0.0
    self.coach = Coach(sCoach)
    self.players = []

  def getTeam(self) :
    return self.__team_name
  def setTeam(self, sName) :
    self.__team_name = sName.upper()
    
  def calcWinLoss(self) :
    self.win_loss_pct = self.wins / (self.wins + self.losses)

  def displayInfo(self) :
    return (self.__team_name + " has " + str(self.wins) + " wins")
  
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
    sTeam = input("Enter team name: ")
    sCoach = input("Enter Coach Name: ")
    oTeam = SoccerTeam(sTeam, sCoach)
    lstTeams.append(oTeam)
for iCount in range(0, len(lstTeams)) :
    print(lstTeams[iCount].getTeam() )
    print(lstTeams[iCount].coach.name)