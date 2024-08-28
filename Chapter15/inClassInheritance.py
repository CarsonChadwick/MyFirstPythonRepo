class Person():
    def __init__(self, fName, lName):
        self.first_name = fName
        self.last_name = lName
    
class Student(Person) :
    def __init__(self, fName, lName) :
        super().__init__(fName,lName)
        self.gpa = 4.0

class Mentor(Person):
    def __init__(self, fName, lName) :
        super().__init__(fName, lName)
        self.department = Department()

class Department() :
    def __init__(self, name) :
        self.dept_name = name