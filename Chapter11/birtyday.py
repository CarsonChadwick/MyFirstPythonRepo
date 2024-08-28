from datetime import datetime
from myFunctions import calc_age, printAge

sName = input("Enter your name: ")
sMonth = input("Enter the birth month: ")
sDay = input ("Enter the birth day: ")
sYear = input("Enter your birth year: ")

dBirthday = datetime.strptime(sMonth + "/" + sDay + "/" + sYear, '%m/%d/%Y')

iYears = calc_age(dBirthday)

printAge(sName, iYears)