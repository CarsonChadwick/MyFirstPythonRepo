# practice Sets

stStudents = set()

iCount = int(input("How many students to add? "))
for iStudcnt in range(0, iCount) :
    stStudents.add(input("Enter the student name: ").upper())

for sName in stStudents :
    print(sName)

sSearch = input("Who should we find? ").upper()

stStudents.discard(sSearch)

print(stStudents)
