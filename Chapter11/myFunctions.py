#myFunc.py file/module
from datetime import datetime

def calc_age(dInputDate) :
    dToday = datetime.today()
    iCalcYears = dToday.year - dInputDate.year
    if (dToday.month - dInputDate.month < 0) :
        iCalcYears = iCalcYears - 1
    elif (dToday.month == dInputDate.month) :
        if (dToday.day < dInputDate.day) :
            iCalcYears = iCalcYears - 1

    return iCalcYears  

def printAge(sPersonName, iAge) :
    print(sPersonName + " is " + str(iAge) + " years old")   