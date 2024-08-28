# Carson Chadwick
# Section 04
# Description: Creates a soccer team class, a sponsered team class, and a game class to print out a season of womens soccer

# needed to generate random scores
import random

class SoccerTeam:
    # constructor. Creates the soccerTeam object when called
    def __init__(self, team_name):
        self.team_name = team_name
        self.wins = 0
        self.losses = 0
        self.goals_scored = 0
        self.goals_allowed = 0

    # generates the score with the standard chance
    def generateScore(self):
        iRnd1 = random.randint(0, 4)
        return iRnd1
        
    def seasonStatus(self):
        # depending on the win rate, display different final messages.
        if self.wins / (self.wins + self.losses) >= .75:
            message = "Qualified for the NCAA Women's Soccer Tournament"
        elif self.wins / (self.wins + self.losses) >= .5:
            message = "You had a good season"
        else:
            message = "Your team needs to practice!"
        return message
    
# here create a class called SponsoredTeam that inherits from SoccerTeam. You need a constructor, and a generateScore method and seasonStatus method
# remember that you can call super().__init__() to get the instance variables from SoccerTeam. in your constructor.
class SponsoredTeam(SoccerTeam):
    def __init__(self, team_name, sponser_name):
        super().__init__(team_name)
        self.sponser_name = sponser_name

    
    def seasonStatus(self):
        if self.wins / (self.wins + self.losses) >= .75:
            message = "Qualified for the NCAA Women's Soccer Tournament. " + self.sponser_name + " is very happy."
        elif self.wins / (self.wins + self.losses) >= .6:
            message = self.sponser_name + "Thinks you had a good season but hopes you can do better."
        else:
            message = "You are in danger of " + self.sponser_name + " dropping you."
        return message
    
    def generateScore(self):
        iRnd1 = random.randint(1, 4)
        return iRnd1

    
# here create a class called Game. It doesn't inhereit anything, but should have a constructor that stores a home team, and an away team, as well as a method for gameStatus
class Game:
    def __init__(self, home_team, away_team, goals_scored, goals_allowed) :
        self.home_team = home_team
        self.away_team = away_team
        self.goals_scored = goals_scored
        self.goals_allowed = goals_allowed
        
        
    def gameStatus(self) :
        return ("The home team " + self.home_team.team_name + " scored: " + str(self.goals_scored) + " The away team " + self.away_team.team_name + " scored: " + str(self.goals_allowed)) 

# get the inputs
sHomeTeamName = input("Enter the name of your team (the home team): ")
sIsSponsoredTeam = input("If your team is sponsored, enter the name of the sponsor. Otherwise enter N: ")
iNumGamesPlayed = int(input("Enter the number of teams that " + sHomeTeamName + " will play (1-10): "))

# creates a soccerTeam object and stores it in the variable homeTeam
if sIsSponsoredTeam.upper() != "N":
    HomeTeam = SponsoredTeam(sHomeTeamName, sIsSponsoredTeam)
else:
    oHomeTeam = SoccerTeam(sHomeTeamName)

# this is creating an empty list for the away teams and an empty list for the games.
# We need to create the list outside the loop so it doesn't keep getting overwritten. Then in the loop, we just append to the list.
opponentTeamsList = []
gamesList = []

# run the loop for however many times the user entered
for game in range(1, iNumGamesPlayed +1):

    # get away team name
    sAwayTeamName = input(f"Enter the name of the away team for game {game}: " )

    # make the away team object. make sure to randomly make the away team a sponsored or normal team (50% chance)
    # randomly make the team a sponsored team or not:
    iTeamtype = random.randint(0,1)
    if iTeamtype == 0 :
        oAwayTeam = SoccerTeam(sAwayTeamName)
    else :
        oAwayTeam = SponsoredTeam(sAwayTeamName, "Enemy Sponser")

    # generate scores for both teams by calling generateScore()
    # make sure that if they are a sponsoredTeam, the odds are better for them (see instructions)
    # if you wrote your classes correctly, that means you don't need an if statement here. The SponsoredTeam generateScore() method
    # will just overwrite the original generateScore() method.
    iHomeScore = oHomeTeam.generateScore()
    iAwayScore = oAwayTeam.generateScore()

    # keep generating scores if they are the same
    while iHomeScore == iAwayScore:
        iHomeScore = oHomeTeam.generateScore()
        iAwayScore = oAwayTeam.generateScore()   
    
    # record goals scored & goals allowed
    # into the home team object (e.g. homeTeam.goals_scored += iHomeScore, awayTeam.goals_scored += iAwayScore, etc.)
    oHomeTeam.goals_scored += iHomeScore
    oHomeTeam.goals_allowed += iAwayScore
    #keep track of wins and losses for the home team and away team (similar to the above code)
    if iHomeScore > iAwayScore :
        oHomeTeam.wins += 1
        oAwayTeam.losses += 1
    else :
        oHomeTeam.losses += 1
        oAwayTeam.wins += 1

    # display the score for this game
    # depending on what you call your variables, something like the below:
    #print(f"{homeTeam.team_name}'s score: {iHomeScore} {sAwayTeamName}'s score: {iAwayScore}")
    print(oHomeTeam.team_name + "'s score: " + str(iHomeScore) + " " + sAwayTeamName + "'s score: " + str(iAwayScore))
    # CRUCIAL: make sure you append your away team to the team list, and create a new game object:
    # it will likely look like the below, but depending on what you call your variables/objects it could lookdifferent.
    #opponentTeamsList.append(opponentTeam)
    opponentTeamsList.append(oAwayTeam)
    #gamesList.append(Game(homeTeam, opponentTeam, iHomeScore, iAwayScore))
 
    gamesList.append(Game(oHomeTeam, oAwayTeam, iHomeScore, iAwayScore))

# At the end of the loop disply: team name, season record, goals score/allowed, and the season Status.
print(f"\nTeam Name: {oHomeTeam.team_name}")
print(f"Final season record: {oHomeTeam.wins} - {oHomeTeam.losses}")
print(f"Total goals scored: {oHomeTeam.goals_scored} - Total goals allowed: {oHomeTeam.goals_allowed}")
print(oHomeTeam.seasonStatus())

# This is a loop that will keep asking for a game number until you type exit.
# I've written most of it for you. You just need to write one morel line of code in the if statement
# to access the gamesList and call the gameStatus() method for whatever game the user inputs.
# remember that to access the first game, you would do gamesList[0]. So if they enter 1 for example, you'll have to
# translate that to 0, etc.
# once you have access to the game, you can call any method. Like gamesList[0].methodName()
gameSelector = 0
while gameSelector != "exit":
    gameSelector = input(f"\nEnter in a game number between 1 and {iNumGamesPlayed} to see the stats of that game. Otherwise type exit: ")

    if gameSelector.isdigit():
        gameSelector = int(gameSelector)
        print(gamesList[gameSelector-1].gameStatus())


 