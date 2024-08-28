lstStudents = []

iCount = int(input("How many students to add? "))
for iStudCnt in range(0, iCount) :
    lstStudents.append(input("Enter the student name: ").upper())

for iStudCnt in range(0, len(lstStudents)) :
    print(lstStudents[iStudCnt])

sSearch = input("Who should we find? ").upper()
if sSearch in lstStudents :
    lstStudents.pop(lstStudents.index(sSearch))

print(lstStudents)