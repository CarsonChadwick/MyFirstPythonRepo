# Carson Chadwick
lstTeam = []
dTeam = {}
iNum = int(input("How many teams? "))
print()

for iCount in range(0, iNum) :
    # dTeam = {}
    sTeam = input("Enter a name: ")
    iWin = int(input("Enter how many wins: "))
    dTeam["team_name" ] = sTeam
    dTeam["wins" ] = iWin

    lstTeam.append(dTeam)

print()
for team in lstTeam :
    print(team["team_name"])

