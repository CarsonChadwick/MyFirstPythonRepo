from openpyxl import Workbook
import random
from openpyxl.utils import get_column_letter

myWorkbook = Workbook()
currWS = myWorkbook.active
currWS.title = "Customers"

cols = ["A", "B", "C", "D", "E", "F"]

for iRow in range(2,12) :
    for iCol in range(6) :
        currWS[cols[iCol] + str(iRow)] = random.randint(0,100)

currWS.auto_filter.ref = "A1:F11"

myWorkbook.save(filename="filters.xlsx")
myWorkbook.close()