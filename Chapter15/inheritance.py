# Carson Chadwick
# Practice inheritance

class Person :
    def __init__(self) :
        self.first_name = ""
        self.last_name = ""
        self.age = 0
        self.address = ""
        self.city = ""
        self.state = ""
        self.phone = ""
    
    def print_demographics(self) :
        return (self.first_name + " " + self.last_name + " lives in " + \
                self.city + " and can be reached at the phone number " + self.phone)

class Employee(Person) :
    def __init__(self) :
        self.salary = 0
        self.state = "TX"
    def yearly_raise(self, increase) : 
        self.salary = self.salary + (self.salary * increase)
    def print_raise(self) :
        return (self.print_demographics() + " and has a new salary of " + str(self.salary))
    def print_demographics(self):
        return (self.first_name + " " + self.last_name)

oEmployee = Employee()
oEmployee.first_name = "Roger"
oEmployee.last_name = "Rabbit"
oEmployee.city = "Dallas"
oEmployee.phone = "(281)555-1212"
oEmployee.salary = 10254
oEmployee.yearly_raise(.03)

print(oEmployee.print_demographics())