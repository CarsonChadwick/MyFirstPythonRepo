class Student:
    institution = "TechiesRUs University"

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.gpa = ""

oStud1 = Student()
oStud2 = Student()

oStud1.first_name = "John Smith"
oStud2.first_name = "Sally Witers"
oStud1.institution = "Bruh"
print(oStud1.first_name)
print(oStud2.first_name)
