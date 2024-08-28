tplStates = ("AL", "CO", "TX", "UT")

sSearch = input("Please enter a valid state: ").upper()

while sSearch not in tplStates : 
    print("The valid states are")
    for iCount in range(0, len(tplStates)) :
        print(tplStates[iCount], end = " ")
    sSearch = input("\nPlease enter the state: ").upper()