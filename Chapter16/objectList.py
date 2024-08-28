class Student :
    def __init__ (self, sFirst, sLast) :
        self.first_name = sFirst
        self.last_name = sLast

lstStudents = []

iCount = int(input("How many studends to add? "))

for iStudCnt in range (0, iCount) :
    sFirst = input("What is the student first name? ").upper()
    sLast = input("What is the student last name? ").upper()
    lstStudents.append(Student(sFirst, sLast))

for iStudCnt in range(0, len(lstStudents)) :
    print(lstStudents[iStudCnt].last_name + ", " + lstStudents[iStudCnt].first_name)
