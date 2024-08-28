from datetime import datetime

def calc_age_years(dDOB): 
    dtoday = datetime.today() 
    iAge = dtoday.year - dDOB.year
    if ((dtoday.month, dtoday.day) < (dDOB.month, dDOB.day)) :
        iAge = iAge - 1

    return iAge 

def combine_name(sFirst, sMiddle, sLast) :
    if (len(sMiddle) > 0) :
        sReturnName = sLast + ", " + sFirst + " " + sMiddle[0] + "."
    else :
        sReturnName = sLast + ", " + sFirst

    return sReturnName

sFirst = input("Enter the first name: ")
sMiddle = input("Enter the middle name: ")
sLast = input("Enter the last name: ")
dDOB = datetime.strptime(input("Enter date of birth (mm/dd/yyyy): "), "%m/%d/%Y")

sFullName = combine_name(sFirst, sMiddle, sLast)
iAge = calc_age_years(dDOB)

print(sFullName + " is " + str(iAge) + " years old")        