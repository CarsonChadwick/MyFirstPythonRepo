# Carson Chadwick
# Section 04
# Generate two random numbers as long as they are not equal. Prompt the user for the range.
import random

iRange = int(input("Enter the max number to generate? "))
iRnd1 = 0
iRnd2 = 0
iCount = 0

while (iRnd1 == iRnd2) :
    iRnd1 = random.randrange(0, iRange)
    iRnd2 = random.randrange(0, iRange)
    iCount += 1

print(iRnd1, iRnd2)
print("It took " + str(iCount) + " tries.")