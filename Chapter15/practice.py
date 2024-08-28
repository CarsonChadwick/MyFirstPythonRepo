# Carson Chadwick
# Section 04
# Practice Problem OOP
class Account() :
    def __init__(self):
        self.balance = 0.0
        self.accountNumber = ""

    def set_balance(self, balance) :
        self.balance = balance
    def gen_account(self, name, address) :
        self.name = name
        self.address = address
        self.accountNumber = name[0:3] + address[0:3]

class Person() :
    def __init__(self, name, address, city, state, zip):
        self.name = name 
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

class Customer(Person) :
    our_company = "ABC Accounting"

    def __init__(self, name, address, city, state, zip, num_employees):
        super().__init__(name, address, city, state, zip)
        self.num_employees = num_employees
        self.account = Account()
        self.account.gen_account(self.name, self.address)

    def print_customer (self) :
        return  (self.our_company + " with account " + str(self.account.accountNumberC) + " owes $" + str(self.account.balance) )


sName = input("Enter your name: ")
sAddress = input("Enter your address: ")
sCity = input("Enter your city: ")
sState = input("Enter your state: ")
sZip = input("Enter your zip code: ")
iEmployees = input("Enter how many Employees work at your work: ")


oCustomer =Customer(sName, sAddress, sCity, sState, sZip, iEmployees)
oCustomer.account.set_balance(float(input("What is the customer's balance: ")))
print(oCustomer.print_customer())
