# Carson Chadwick
# Section 04
# Practice Using Parameters and creating functions.

# Recieve student's name and an integer representing their final grade
def letter_grade(iGrade):
    if (iGrade >= 90) :
        sLetter_Grade = "A"
    elif (iGrade >= 80) :
        sLetter_Grade = "B"
    elif (iGrade >= 70) :
        sLetter_Grade = "C"
    elif (iGrade >= 60) :
        sLetter_Grade = "D"
    else :
        sLetter_Grade = "E"
    
    return sLetter_Grade
# Based on the integer, determine the letter grade

# Print the sutdent name and letter grade
sStudentName = "Jane"
iStudentGrade = 92
print(sStudentName + "'s grade is " + letter_grade(iStudentGrade) )