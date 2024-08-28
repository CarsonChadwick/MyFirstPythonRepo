iTotal = 542
iNumStudents = 0
try:
    fAve = iTotal/iNumStudents
    print(f)
except (ZeroDivisionError, OverflowError, FloatingPointError): 
    print("Error.")
except NameError:
    print("Error not found.")
finally :
    print("The game is over.")
