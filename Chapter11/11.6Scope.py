def letter_grade():
    global iTotal

    if (iTotal >= 90) :
        sLetter_Grade = "A"
    elif (iTotal >= 80) :
        sLetter_Grade = "B"
    elif (iTotal >= 70) :
        sLetter_Grade = "C"
    elif (iTotal >= 60) :
        sLetter_Grade = "D"
    else :
        sLetter_Grade = "E"
    
    iTotal = 0

    return sLetter_Grade
# This is the main program

iTotal = 92
sGrade = letter_grade()
print(sGrade)
print(iTotal)
