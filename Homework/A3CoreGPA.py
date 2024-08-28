# Carson Chadwick
# Section 04
# This Program calculates the chances of getting into the IS core based on
# overall GPA, last 30 Credits GPA, Accounting 200 Grade, IS 201 Grade, IS 303 Grade and essay score

# Input user for overall GPA, last 30 Credits GPA, Accounting 200 Grade, IS 201 Grade, IS 303 Grade and essay score
fGpa = float(input("Enter your overall GPA: "))
fLastGpa = float(input("Enter your las 30 credits GPA: "))
sAcc200 = input("Enter your Accounting 200 letter grade (A, A-, B+, B-, C+, C, C-, D+, D, D-, E): ")
sIs201 = input("Enter your IS 201 letter grade (A, A-, B+, B-, C+, C, C-, D+, D, D-, E): ")
sIs303 = input("Enter your IS 303 letter grade (A, A-, B+, B-, C+, C, C-, D+, D, D-, E): ")
fEssay = float(input("Enter your essay score (between 0 and 4): "))
# Convert grade values to numbers
def letterGrade (sGrade) :
    if sGrade == "A" :
        sReturn = 4.0
    elif sGrade == "A-" :
        sReturn = 3.7
    elif sGrade == "B+" :
        sReturn = 3.4
    elif sGrade == "B" :
        sReturn = 3.0
    elif sGrade == "B-" :
        sReturn = 2.7
    elif sGrade == "C+" :
        sReturn = 2.4
    elif sGrade == "C" :
        sReturn = 2.0
    elif sGrade == "C-" :
        sReturn = 1.7
    elif sGrade == "D+" :
        sReturn = 1.4
    elif sGrade == "D" :
        sReturn = 1.0
    elif sGrade == "D-" :
        sReturn = 0.7
    else :
        sReturn = ""
    return (sReturn)

# Initialize weighting variables
iAcc200 = letterGrade(sAcc200)
iIs201 = letterGrade(sIs201)
iIs303 = letterGrade(sIs303)

# Calculate new GPA
fNewGpa = round((iAcc200*.05 + iIs201*.3 + iIs303*.3 + fGpa*.12 + fLastGpa*.18 + fEssay*.05), 3)

if (fNewGpa >= 3.8) :
    sChances = "Chances are very good"
elif (fNewGpa >= 3.5) :
    sChances = "Chances are good"
elif (fNewGpa >= 3.2) :
    sChances = "Chances are so-so"
else :
    sChances = "You might want to retake IS 201 and/or IS 303"
# Print Statement
print("\nTotal Apply GPA is " + str(fNewGpa) + '\n' + sChances)