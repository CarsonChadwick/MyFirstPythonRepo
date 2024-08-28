# Carson Chadiwck
# Section 04

# ask for a number of employees
iNumEmps = int(input("How many employees?: "))
# Declare Variables
fWage = 0
fHours = 0
fEmpWage = 0
fTotalWage = 0 

for iCount in range(0, iNumEmps) : 
    fHours = float(input("Enter number of hours: "))
    fWage = float(input("Enter hourly wage: "))
    
    fEmpWage = round(fHours*fWage,2)
    print(fEmpWage)