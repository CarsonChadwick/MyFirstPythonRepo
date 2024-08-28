class Person :
    def __init__(self) :
        self.first_name = ""
        self.last_name = ""
        self._age = 20
    
    def full_name(self) :
        sFull_name = self.last_name + ", " + self.first_name
        return(sFull_name)

class Employee(Person) :
    def __init__(self) :
        self.__salary = 55000
    
    def set_salary(self, fSalary):
        self.__salary = fSalary

    def get_salary(self):
        return(self.__salary)
    
oEmp = Employee()
oEmp.first_name = "maria"
oEmp.last_name = "Teresa"
oEmp.set_salary(55000)
print(oEmp.get_salary())
print(oEmp.full_name())
print(oEmp._Employee__salary)



