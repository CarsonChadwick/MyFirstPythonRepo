#Carson Chadwick
#Section 04
#This program has two people enter their testing info and says who had a better average

#person 1 Enters their info
sName1 = input("Enter your full name: ")
sBirthyear1 = input("Enter your birth year: ")
iTestSum1 = int(input("Enter your sum of all test scores: "))
iNumberOfTests1 = int(input("Enter the Numeber of Tests you took: "))
iAverage1 = round(iTestSum1 / iNumberOfTests1)

#Person 2 Enters their info
sName2 = input("Enter your full name: ")
sBirthyear2 = input("Enter your birth year: ")
iTestSum2 = int(input("Enter your sum of all test scores: "))
iNumberOfTests2 = int(input("Enter the Numeber of Tests you took: "))
iAverage2 = round(iTestSum2/iNumberOfTests2)


print(sName1.upper() + " born in " + sBirthyear1 + " scored " + str(iTestSum1) + " points on " + \
    str(iNumberOfTests1) + " tests for an average of " + str(iAverage1) + ".") 
print(sName2.upper() + " born in " + sBirthyear2 + " scored " + str(iTestSum2) + " points on " + \
    str(iNumberOfTests2) + " tests for an average of " + str(iAverage2) + ".") 
print("Did " + sName1 + " score higher than " + sName2 + "?")
print(iAverage1>iAverage2)
