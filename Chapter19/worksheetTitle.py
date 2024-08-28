from openpyxl import Workbook

myWorkbook = Workbook()
currWS = myWorkbook.active
myWorkbook.create_sheet("Customer Info", 0)

currWS.title = "More Data"
myWorkbook.active = currWS

myWorkbook.save(filename="test2.xlsx")
myWorkbook.close()