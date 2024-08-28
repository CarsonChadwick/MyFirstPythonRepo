#Carson CHadwick
#Practice Printing personal information frominput
sFirstName = input("Enter your first name: ")
sLastName = input("Enter your last name: ")
sAddress = input("Enter your address: ")
sCity = input("Enter your City: ")
sState = input("Enter your State: ")
iBirth = int(input("Enter your birth year: "))
iage = 2023 - iBirth

print("")
print(sFirstName.upper(), sLastName.upper() )
print(sAddress)
print(sCity, sState.upper(), sep="\t")
print("In 2023 " + sFirstName + " was " + str(iage) + " years old.")