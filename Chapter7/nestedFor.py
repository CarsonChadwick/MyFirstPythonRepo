# prompt the user to enter the number of students
# prompt the user to enter the number of tests

iNumStudents = int(input("How many students? " ))

for iOuterCount in range (1, (iNumStudents + 1)) :
    sFullName = input("\nEnter the student" + \
                      str( iOuterCount ) + "'s full name: ")
    iNumTests = int(input("\nHow many tests for " + sFullName + "? "))

    iSumTest = 0

    for iTestCount in range(1, (iNumTests + 1)) :
        iScore = int (input("Enter test score for test " + str( iTestCount ) + ": "))
        iSumTest += iScore
    
    fTestAve = iSumTest/iNumTests
    print("\n" + sFullName + " has a test average of " + str(fTestAve) + "\n")