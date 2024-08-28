import sys

bValue = True
while (bValue == True) :
        iName = input("Enter your name: ")
        if iName.isalpha() == True:
            bValue = False
        else: 
            print("Error, please enter a valid name (ex. John )")

bValue = True
while (bValue == True) :
    try:
        id = int(input("Enter your Id: "))
        bValue = False
    except: 
        print("Error, please enter a valid Id (ex. 1434 )")

print(iName + " has an id of " + str(id))
