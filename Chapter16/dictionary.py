class Driver :
    def __init__ (self, sFirst, sLast) :
        self.first_name = sFirst
        self.last_name = sLast
        self.num_tickets = 0

dctDriver= {}

iNum_Drivers = int(input("How many drivers do you want to enter: "))

for iCOunt in range(0, iNum_Drivers) :
    iDL_number = int(input("What is the driver license #: "))
    sFirst = input("What is the first name? ")
    sLast = input("What is the last name: ")
    dctDriver[iDL_number] = Driver(sFirst, sLast)

iDL_number = int(input("Enter the id of the driver that just reieved a ticket: "))
iNum_Tickets = int(input("How many tickets? "))

if iDL_number in dctDriver : 
    dctDriver[iDL_number].num_tickets += iNum_Tickets

if dctDriver[iDL_number].num_tickets > 3 :
    print(dctDriver[iDL_number].first_name + " will be deleted")
    dctDriver.pop(iDL_number)

for iKey, oDriver in dctDriver.items() :
    print(str(iKey) + ":" + oDriver.first_name)



