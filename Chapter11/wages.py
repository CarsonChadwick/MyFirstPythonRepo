from wages_functions import calc_pay
sName = input("What is your name? ")
fHoursWorked = float((input("How many hours did you work? ")))
fHourlyWage = float(input("What was your hourly wage? "))
fTaxRate = float(input("What was the tax rate (as a decimal not %): "))
fFicaRate = float(input("What was the Fica rate (as a decimal not %? "))

print(sName + " worked " + str(fHoursWorked) + " hours in the week at $" + str(fHourlyWage) + " an hour and took home $" + str(calc_pay(fHoursWorked,fHourlyWage, fTaxRate, fFicaRate)))