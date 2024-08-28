class Employee :
    def __init__(self) :
        self.first_name = ""
        self.last_name = ""
        print("Employee Constructor")
    def my_print(self) :
        print("Employee my_print()")

class Checker(Employee) :
    def __init__ (self) :
        super().__init__()
        self.til_number = 0
        self.balanced_til = True
        print("Checker Constuctor")        

    def my_print(self) :
        super().my_print()
        print("Checker my_print()")
        
class Stocker(Employee) :
    def __init__ (self) :
        super().__init__ ()
        self.can_lift_50lbs = False
        print("Stocker Constuctor")

    def my_print(self) :
        super().my_print()
        print("Stocker my_print()")

class Grocery_Employee(Checker, Stocker) :
    def __init__ (self) :
        super().__init__() 
        print("Grocery_Employee Constuctor")        
        
oEmp = Grocery_Employee()
print(Grocery_Employee.mro())
print("\n\n")
oEmp.my_print()