from openpyxl import Workbook
import random

myWorkbook = Workbook()

currWS = myWorkbook.active

cols = ["A", "B","C","D","E","F"]

for iRow in range(1,11) :
    for iCol in range(6) :
        currWS[cols[iCol] + str(iRow)] = random.randint(0,100)

currWS ["A12"] = 'SUM'
currWS["A13"] = '=SUM(A1:A10)'

currWS ["B12"] = 'MIN'
currWS["B13"] = '=MIN(B1:B10)'

currWS ["C12"] = 'MAX'
currWS["C13"] = '=MAX(C1:C10)'

currWS ["D12"] = 'COUNT'
currWS["D13"] = '=COUNT(D1:D10)'

currWS ["E12"] = 'AVERAGE'
currWS["E13"] = '=AVERAGE(E1:E10)'

currWS ["F12"] = 'COUNTIF'
currWS["F13"] = '=COUNTIF(F1:F10, "> 50")'

myWorkbook.save(filename="formulas.xlsx")
myWorkbook.close()