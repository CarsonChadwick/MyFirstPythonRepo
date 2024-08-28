#Carson CHadwick
#Concatination
sFirstName = input("Enter your first name: ")
sLastName = input("Enter your last name: ")
iAge = int(input("Enter your age: "))

sFullName = sLastName + ", " + sFirstName  + " is " + \
    str(iAge) + " years old"
print(sFullName)