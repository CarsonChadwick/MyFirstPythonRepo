# prompt for number of students
# prompt for course final ave
# display letter dgrade for the final ave

# display average for the course and letter grade

iNumStudents = int( input("How many students? "))
iTotalAve = 0

for iCount in range(1, (iNumStudents), 2) :

    iAve = int( input("Enter student " + str(iCount) + "'s average: " ))

    if(iAve >= 90) :
        print("A")
    elif(iAve >= 80) :
        print("B")
    elif(iAve >= 70) :
        print("C")
    else :
        print("See you next semester")

    iTotalAve += iAve
    
fTotalAve = iTotalAve / iNumStudents
sAve = ""

print("The course average was " + str(float(fTotalAve)))
if(fTotalAve >= 90) :
     sAve = "A"
elif(fTotalAve >= 80) :
    sAve = "B"
elif(fTotalAve >= 70) :
    sAve = "C"
else :
    sAve = "not passing"

print("The course final grade was " + sAve)