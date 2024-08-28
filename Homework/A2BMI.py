# Carson Chadwick
# Section 04
# This program will prompt the user for height and weight and calculate their BMI

# Enters Name
sFirstName = input("Please enter your first name (ex. Josh): ")
sLastName = input("Please enter your last name (ex. Smith): ")

#Enters Height and weight
ifeet = int(input("Enter how many feet tall you are (Whole number with no abbreviations ex. if you are 5ft6in enter 5, we will ask for inches next): "))
iInches = float(input("Enter how many inches (No abbreviations Ex. If you are 5ft6in enter 6): "))
iWeight = float(input("Enter your weight in pounds: "))
iHeightInInch = ifeet*12 + iInches

#BMI Calculation
fBMI = round((iWeight/iHeightInInch/iHeightInInch)*703, 1)
sBMI = ""

#Finds BMI as a string
if fBMI < 18.5 :
    sBMI = "Underweight"
elif fBMI < 25 :
    sBMI = "Normal Weight"
elif fBMI < 30 :
    sBMI = "Overweight"
else :
    sBMI = "Obese"

#Print Statement
print(sFirstName + " " + sLastName + "\nhas a BMI of " + str(fBMI) + " and is " + sBMI)