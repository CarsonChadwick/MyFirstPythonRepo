def printNames (lstNames) :
    for iCount in range (0,len(lstNames)) :
        print (lstNames[iCount])

lstNames = ["Joe", "Prof Ganderson", "Willy Wonka"]
sContinue = input("Do you want to enter a name?").upper()[0]
while (sContinue == "Y") :
    lstNames.append(input("Enter Name: "))
    sContinue = input("Do you want to enter a name?").upper()[0]

lstNames.pop(1)
printNames(lstNames)
