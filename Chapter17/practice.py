import numpy as np
import pandas as pd

dfEmployee = pd.read_csv("Employees.csv", index_col= False)
print(dfEmployee)
print("\n")

dfEmployee.at[0,"Last_Name"] = "Jones"
print(dfEmployee)
print("\n")

dfEmployee.sort_values(["Last_Name", "First_Name"], ascending=(False, True), inplace=True)
print(dfEmployee)
print("\n")

sSalary = input("Enter a Salary: ")
dfNewEmp = dfEmployee.query("Salary > " + sSalary)
print(dfNewEmp)
print("\n")

sCommission = input("Enter a sales commission: ")
dfNewEmp2 = dfEmployee.query("Sales_Commission >=" + sCommission)
print(dfNewEmp2)