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
sLetterGrade = input("What was your letter grade? ")
print("Your GPA for that class was a " + str(letterGrade(sLetterGrade)))