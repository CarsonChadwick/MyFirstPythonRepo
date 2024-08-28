from openpyxl import Workbook

myWorkbook = Workbook()
currWS = myWorkbook.active

currWS.title = "More Data"

currWS["A1"] = "This is some data"
currWS["B1"] = "hello"

currWS.column_dimensions["A"].width = len(currWS["A1"].value)
myWorkbook.save(filename="test3.xlsx")
myWorkbook.close()