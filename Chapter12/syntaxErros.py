from datetime import datetime

def calc_age_years(dDOB) :
      dToday = datetime.today() 
      iAge = dToday.year - dDOB.year
      if (dToday.month < dDOB.month) :
        iAge = iAge - 1
      elif (dToday.month == dDOB.month) and (dToday.day < dDOB.day) :
        iAge = iAge - 1
    
      return iAge 

dDOB = datetime.strptime(input("Enter date of birth (mm/dd/yyyy): "), "%m/%d/%Y")

iAge = calc_age_years(dDOB)

print(str(iAge) + " years old") 