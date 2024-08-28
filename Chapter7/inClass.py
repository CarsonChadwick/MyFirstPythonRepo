# Carson Chadwick
# Section 04
# Practice Loops in class

# Prompt for a number of grades

iLowGrade = 0
iTotal = 0
sContinue = input("Would you like to enter a grade?(Y,N) ").upper()[0]
iCount = 0
while sContinue == "Y" :
    iCurrGrade = int(input("Enter grade " + str(iCount + 1) + ": "))
# Drop the lowest grade
    if (iCount == 0) :
        iLowGrade = iCurrGrade
    
    if (iCurrGrade < iLowGrade) :
        iLowGrade = iCurrGrade
    iTotal += iCurrGrade
    iCount += 1
    sContinue = input("Would you like to enter a grade?(Y,N) ").upper()[0]
# Calculate the average
iTotal = iTotal - iLowGrade
iAve = iTotal/(iCount - 1)
# Display the average
print("The average grade (disregarding the lowest) is: " + str(iAve))