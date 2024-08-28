# Creat Team Class
class Team():
    # Contructor
    def __init__(self, teamName):
        # Team name attribute (protected)
        self._teamName = teamName
    # Getter and Setter Methods
    def getTeamName(self):
        return(self._teamName)
    def setTeamName(self, teamName):
        self._teamName = teamName

# SoccerTeam class that inherits from Team
class SoccerTeam (Team):
    # Contstructor
        # win, losses, Draws, players list (public attributes)
    def __init__(self, teamName, wins, losses, draws):
        super().__init__(teamName)
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.playerList = []

# Person class
class Person():
    # Constructor
        # FirstName, LastName attributes (protected)
    def __init__(self, firstName, lastName) :
        self._firstName = firstName
        self._lastName = lastName
    # Getter and Setter Methods
    def getFirstName(self):
        return(self._firstName)
    def getLastName(self):
        return(self._lastName)
    def setFirstName(self, firstName):
        self._firstName = firstName
    def setLastName(self, lastName):
        self._lastName = lastName

# Player Class that inherits from Person
class Player(Person):
    # Contructor
        # GoalsScored (private)
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        self.__goalsScored = 0
    # Getter and Setter Methods
    def getGoalsScored (self):
        return(self.__goalsScored)
    def setGoalsScored(self, goalsScored):
        self.__goalsScored = goalsScored

# Prompt user how many teams to enter
iTeams  = int(input("Enter how many teams: "))
print("")
lstSoccerTeams = []
# Create Soccer Team objects using a loop
for icount in range(1, (iTeams + 1)):
    teamName = input("Enter team " + str(icount) + "'s name: ")
    wins = input("Enter team " + str(icount) + "'s wins: ")
    losses = input("Enter team " + str(icount) + "'s losses: ")
    draws = input("Enter team " + str(icount) + "'s draws: ")
    oTeam = SoccerTeam(teamName, wins, losses, draws)
    # Within the loop ask how may players on the team
    players = int(input("Enter how many players are on team " + str(icount) + ": "))
    # Use a loop to load player information
    for icount in range(1, (players + 1)) :
        fName = input("What is the player " + str(icount) + "'s first name: ")
        lName = input("What is the player " + str(icount) + "'s last name: ")
        oPlayer = Player(fName, lName)
        oTeam.playerList.append(oPlayer)
    lstSoccerTeams.append(oTeam)
    print("\n")
# Nested for loop to print teams and players
for icount in range(0, len(lstSoccerTeams)) :
    print(lstSoccerTeams[icount].getTeamName()+ " has " + lstSoccerTeams[icount].wins + " win(s), " + \
           lstSoccerTeams[icount].losses + " loss(es), and " + lstSoccerTeams[icount].draws + " draw(s)")
    for icount2 in range(0, len(lstSoccerTeams[icount].playerList)) :
            print("\tPlayer " + str(icount2 + 1) + ": " + lstSoccerTeams[icount].playerList[icount2].getFirstName() + " " + \
                    lstSoccerTeams[icount].playerList[icount2].getLastName())




