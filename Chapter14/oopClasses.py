class Student :
   
    student_id = 0
    first_name = ""
    last_name = ""
    age = 0
    gpa = 0

    def __init__(self, fName, lName, iage):
        self.first_name = fName
        self.last_name = lName
        self.age = iage

    def get_fullname(self) :
        return (self.last_name + ", " + self.first_name)
    
    def load_gpa(self, fGpa) :
        if(fGpa > 4.0) :
            fGpa = 4.0
        elif (fGpa < 0.0) :
            fGpa = 0.0

        self.gpa = fGpa


first_name = input("Enter the student first name: ")
last_name = input("Enter the student last name: ")
age= input("Enter the student's age: ")

oStudent = Student(first_name, last_name, age)

oStudent.load_gpa(4.0)
print(oStudent.get_fullname())