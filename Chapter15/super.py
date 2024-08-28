class Person :
    def __init__(self, sFist, sLast, sCity, sPhone, sState) :
        self.first_name = sFist
        self.last_name = sLast
        self.city = sCity
        self.state = sState
        self.phone = sPhone
    
    def print_demographics(self) :
        return (self.first_name + " " + self.last_name + " lives in " + \
                self.city + " and can be reached at the phone number " + self.phone)
     
class Employee(Person) :
    def __init__(self, sFist, sLast, sCity, sPhone, sState, iSalary):
        super().__init__(sFist, sLast, sCity, sPhone, sState)
        self.salary = iSalary
    
    def yearly_raise(self, increase) : 
            self.salary = self.salary + (self.salary * increase)
        
    def print_raise(self) :
            return (super().print_demographics() + " and has a new salary of " + str(self.salary))
    def print_demographics(self):
            return (self.first_name + " " + self.last_name)

sFist = "Roger"
sLast = "Rabbit"
sCity = "Dallas"
sPhone = "(281)555-1212"
sState = "TX"
iSalary = 10254

oEmployee = Employee(sFist, sLast, sCity, sPhone, sState, iSalary)

oEmployee.yearly_raise(.03)
print(oEmployee.print_raise())
print(oEmployee.print_demographics())