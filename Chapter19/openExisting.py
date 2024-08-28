import openpyxl

myWorkbook = openpyxl.load_workbook('test6.xlsx')

currWS = myWorkbook.active

currWS["A4"] = 100
for row in currWS.iter_rows(values_only=True) :
    print(row)

myWorkbook.save(filename="test6.xlsx")
myWorkbook.close()
