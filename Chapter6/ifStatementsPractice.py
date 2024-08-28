# Carson Chadwick
# Section 04
# This program accepts a students name and number grade printing the letter grade

sFullName = input("Enter your full name: ")
iFinalGrade = int(input("Enter your final grade (as a whole number ex. 88): "))
sFinalLetterGrade = ""

if (iFinalGrade >= 94 ) :
    sFinalLetterGrade = "A"
elif (iFinalGrade >= 90) :
    sFinalLetterGrade = "A-"
elif (iFinalGrade >= 87) :
    sFinalLetterGrade = "B+"
elif (iFinalGrade >= 83) :
    sFinalLetterGrade = "B"
elif (iFinalGrade >= 80) :
    sFinalLetterGrade = "B-"
else :
    sFinalLetterGrade = "C"

print(sFullName.upper() + " had a final average of " + str(iFinalGrade) + " which resulted in a(n) " + \
      sFinalLetterGrade + " for the course")
