import pandas as pd

lstTeams = {    "Team Name":["Dogers", "Dbacks", "giants", "padres", "Rockies"],
                "Wins": [100, 84, 82, 79, 59],
                "Losses": [62,78,80,83,103]

           }

df = pd.DataFrame(lstTeams)

print(df[["Team Name", "Wins"]])