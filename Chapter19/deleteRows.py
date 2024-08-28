from openpyxl import Workbook

myWorkbook = Workbook()

currWS = myWorkbook.active

currWS["A1"] = "First Name"
currWS["B1"] = "Last Name"
currWS["C1"] = "Favorite Food"

currWS["A2"] = "Winnie"
currWS["B2"] = "Pooh"
currWS["C2"] = "Honey"

currWS["A3"] = "Bugys"
currWS["B3"] = "Bunny"
currWS["C3"] = "Carrots"

currWS.insert_rows(2,2)
currWS.insert_cols(3,2)
currWS.delete_rows(1,1)
currWS.delete_cols(1,2)
myWorkbook.save(filename="test5.xlsx")
myWorkbook.close()