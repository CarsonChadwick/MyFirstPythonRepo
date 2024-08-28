from openpyxl import Workbook

myWorkbook = Workbook()
currSheet = myWorkbook.active
j = 10

for icount in range(1,11) :
    currSheet["A" + str(icount)] = j
    j = j-1

currSheet["A1"] = 15
currSheet["A2"] = "=A1*2"
myWorkbook.save(filename="inClass2.xlsx")

myWorkbook.close()