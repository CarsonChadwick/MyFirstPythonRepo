# Carson Chadwick
# Section 04
# This program simulates a pet store that has customers with pets using OOP
from datetime import datetime

class Customer ():
    company_name = "Critter Watch"
    def __init__ (self, first_name, last_name, address1, address2, city, state, zip):
        self.first_name = first_name
        self.last_name = last_name
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zip = zip
        self.balance = 0.0
        self.cust_pet = None
        self.cust_id = self.gen_id(first_name, last_name, address1)

    def gen_id(self, first_name, last_name, address1):
        address = address1.replace(" ", "")
        return((first_name[0:4]) + (last_name[0:4]) + (address[0:4]))
    
    def return_bill(self):
        return("Customer " + self.cust_id + " with name " + self.first_name + " " + self.last_name + " owes $" + str(round(self.balance,2)) + " for " + self.cust_pet.pet_name + "'s stay from " + str(self.cust_pet.appointment.begin_date) + " to " + str(self.cust_pet.appointment.end_date))
    def make_payment(self, iPayment) :
        self.balance -= iPayment

class Pet ():
    def __init__(self, pet_name, breed, age, owner) :
        self.pet_name = pet_name
        self.breed = breed
        self.age = age
        self.appointment = Appointment(owner)

class Appointment():
    def __init__(self, owner) :
        self.begin_date = None
        self.end_date = None
        self.day_rate = 0.0
        self.total_days = 0
        self.total_cost = 0.0
        self.owner = owner
    def set_appointment(self, begin_date, end_date, day_rate) :
        self.total_days = self.calc_days(begin_date, end_date)
        self.total_cost = self.total_days*day_rate 
        self.owner.balance += self.total_cost
    def calc_days (self, begin_date, end_date) :
        self.total_days = (end_date - begin_date).days
        if self.total_days <= 0 :
            self.total_days = 1
        return self.total_days
    
sFirstName = input("Enter your first name: ")
sLastName = input("Enter your last name: ")
sAddress1 = input("Enter your address: ")
sAddress2 = input("Enter a second address: ")
sCity = input("Enter the city: ")
sState = input("Enter the state: ")
sZip = input("Enter the zip code: ")
oOwner = Customer(sFirstName, sLastName, sAddress1, sAddress2, sCity, sState, sZip)
sName = input("What is your pet's name? ")
sBreed = input("What is your pets breed? ")
sAge = input("What is your pet's age? ")
oPet = Pet(sName, sBreed, sAge, oOwner)
oOwner.cust_pet = oPet
oAppointment = Appointment(oOwner)
begin_date = datetime.strptime(input("Enter Start date in the format m/d/y: "), "%m/%d/%Y").date()
end_date = datetime.strptime(input("Enter Start date in the format m/d/y: "), "%m/%d/%Y").date()
oOwner.cust_pet.appointment.begin_date = begin_date
oOwner.cust_pet.appointment.end_date = end_date
fDayRate = float(input("Enter the day rate: "))
oAppointment.set_appointment(begin_date, end_date, fDayRate)
print(oOwner.return_bill())
oOwner.make_payment(oOwner.balance)
print(oOwner.return_bill())


