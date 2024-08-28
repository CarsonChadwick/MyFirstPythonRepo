class Customer :
    companyName = "ABC Accounting"

    def __init__(self, customerId, customerName, customerAccount, balance) :
        self.customerId = customerId
        self.customerName = customerName
        self.customerAccount = customerAccount
        self.balance = balance

    def display_customer (self) :
        return (self.customerName + " has a balance of $" + str((self.balance),))
sCustId = input("What is your customer ID: ")
sCustomerName = input("What is your name: ")
sCustomerAccount = input("What is your account numner: ")
fBalance = float(input("What is your currect balance: "))
john = Customer(sCustId, sCustomerName, sCustomerAccount, fBalance)
print(john.display_customer())