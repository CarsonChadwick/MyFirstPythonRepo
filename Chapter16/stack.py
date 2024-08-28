# Practice stack
stkCarParking = []
iGuests = 4

POSITION = 0
PLATE = 1
MAKE = 2
MODEL = 3

for iPos in range(0, iGuests) :
    sLicense = input("What is your license plate? ")
    sMake = input("What is the make? ")
    sModel = input("What is the model? ")
    stkCarParking.append([iPos + 1, sLicense, sMake, sModel])


print("\n")

print("Here is the parking order: ")
for iCount in range(len(stkCarParking)-1, -1, -1) :
    print(str("Position: " + str(stkCarParking[iCount][POSITION])) +
              " Plate: " + stkCarParking[iCount][PLATE] +
              " Make" + stkCarParking[iCount][MAKE] +
              " Model" + stkCarParking[iCount][MODEL] )
    
print("\n")

while len(stkCarParking) > 0: 
    print("Removing car " + str(stkCarParking[-1][POSITION]))
    stkCarParking.pop(-1)
    print("\n")
    if len(stkCarParking) > 0 :
        print("Here is the parking list:")
        for iCount in range(len(stkCarParking)-1,-1,-1) :
            print(str("Position: " + str(stkCarParking[iCount][POSITION])) +
              " Plate: " + stkCarParking[iCount][PLATE] +
              " Make" + stkCarParking[iCount][MAKE] +
              " Model" + stkCarParking[iCount][MODEL] )  
print("\n")  
