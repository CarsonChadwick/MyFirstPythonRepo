# Carson Chadwick
# Section 04
# Sample program for input and output

sFirstName = input("Enter your first name: ")
sLastName = input("Enter your last name: ")
iAge = int(input("Enter your age (ie. whole number like 27): "))
print(sLastName + ", " + sFirstName)
print(sLastName, sFirstName)
print(sLastName, sFirstName, sep =",")
print("{0}, {1}".format(sLastName,sFirstName))