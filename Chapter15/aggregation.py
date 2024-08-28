# Carson Chadwick
# Section 04
# Practice aggregation

class Baseball_Team :
    def __init__(self, name, wins, losses) :
        self.team_name = name
        self.wins = wins
        self.losses = losses

    def get_winloss_pct(self) :
        fPct = (self.wins / (self.wins + self.losses))* 100
        return (round(fPct, 1))
class Player :
    def __init__(self, player_name, team) :
        self.player_name = player_name
        self.team = team

    def get_info(self) :
        return (self.player_name + " plays on the " + self.team.team_name + " who wins " + 
                    str(self.team.get_winloss_pct()) + "% of the time")
oTeam = Baseball_Team("Rokies", 22, 28)
oPlayer = Player("Nolan Arenado", oTeam)

print(oPlayer.get_info())
print(oTeam.team_name)