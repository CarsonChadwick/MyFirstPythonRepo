from openpyxl import Workbook

myWorkbook = Workbook()
currWS = myWorkbook.active

currWS.title = "More Data"

currWS["A1"] = "This is some data that is long"
currWS["B1"] = "Hello"
currWS["C2"] = "How much wood could a woodchuck chuck"
currWS["D4"] = "Short Data Here"

iHoldLen = 0
iLen = 0

oCols = currWS.iter_cols()

for column in oCols :
    for singleCol in column :
        if singleCol.value is not None :
            iLen = len(singleCol.value)
            if (iLen > iHoldLen) :
                iHoldLen = iLen
            currWS.column_dimensions[singleCol.column_letter].width = iHoldLen

myWorkbook.save(filename="test4.xlsx")
myWorkbook.close()

