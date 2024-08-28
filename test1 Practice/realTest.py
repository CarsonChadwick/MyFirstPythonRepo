# Carson Chadwick
# Section 4 Midterm 3/8/2024
# This program is for an automobile company that builds and sells cars. 
# Using OOP programming cars will be built and then sold to see if a profit is made after sales.

# Vehical Class
class Vehical():
    def __init__(self, make, model, color) :
        self.make = make
        self.model = model
        self.color = color
# Car Class inherited from Vehical, Car has an Engine, has tires
class Car(Vehical) :
    def __init__(self, make, model, color, vin, engine, tires, build_cost):
        super().__init__(make, model, color)
        self.vin = vin
        self.engine = engine
        self.tires = tires
        self.build_cost = build_cost
# Engine Class
class Engine():
    def __init__(self, engineSize):
        self.engineSize = engineSize
# Tire Class
class Tire():
    def __init__(self, position, size ):
        if position == 0 :
            self.position = "LF"
        elif position == 1 :
            self.position = "RF"
        elif position == 2 :
            self.position = "LR"
        else :
            self.position = "RR"
        self.size = size
# Company Class
class Company ():
    def __init__(self, company_name):
        self.company_name = company_name
        self.__cost = 0.0
        self.__earnings = 0.0
    # ChangedEarngins method
    def changeEarnings(self, earnings):
        self.__earnings += earnings
    # changeCost method
    def changeCost(self, cost) :
        self.__cost += cost
    # getEarnings method
    def getEarnings (self) :
        return(self.__earnings)
    # getCost method
    def getCost (self) :
        return(self.__cost)
# Print Cars Function
def printCars(carList):
    for icount in range(0, len(carList)) :
        print(str(icount + 1) + " - " + carList[icount].model + " " + carList[icount].make + \
               " " +  carList[icount].vin + " " + carList[icount].color + " " + str(carList[icount].build_cost) )
        
# inventoryCost, revenueMade, profit, and carList variable
lstCarList = []
# Accept User input for company name and create company object
sCompName = input("What is the company name? ")
oCarComp = Company(sCompName)
# Create a loop as long as the user wants to make cars
sContinue = input("\nWould you like to build a car? ").upper()[0]
while sContinue == "Y" :
    # Inside of loop ask for user input for car attributes
    sModel = input("\nWhat is the model? ")
    sMake = input("What is the make? ")
    sColor = input("What is the color? ")
    sVin = input("What is the VIN? ")
    sEngineSize = input("What is the engine size description? ")
    sTireSize = input("What is the tire size? ")
    fCost = float(input("What is the cost to build? "))
    # Keep the Cars made in a lsit
    lstTires = []
    for icount in range (0,4) :
        lstTires.append(Tire(icount, sTireSize))
    oCar = Car(sMake, sModel, sColor, sVin, sEngineSize, lstTires, fCost)
    lstCarList.append(oCar)
    
    # Keep track of total cost to make the cars
    oCarComp.changeCost(fCost)
    sContinue = input("\nWould you like to build another car? ").upper()[0]
# Ask user if they would like to sell a car
sContinueSell = input("\nWould you like to sell a car? ").upper()[0]
while sContinueSell == "Y" :
    # Prints the list of Car options for user to sell
    printCars(lstCarList)
    # User selects a car. Use if/then/while to make sure selection is valid
    bValue = True
    while (bValue == True) :
        iCarSelect = 0
        while iCarSelect < 1 or iCarSelect > len(lstCarList) :
            try:
                iCarSelect = int(input("\nWhich car would you like to sell? "))
                bValue = False
            except :
                print("Please enter a valid selection: ")
    # Ask for sales price
    iSellPrice = int(input("What is the sell price? "))
    # Update company total revenue
    oCarComp.changeEarnings(iSellPrice)
    # Remove the car from the list
    lstCarList.pop(iCarSelect-1)
    sContinueSell = input("\nWould you like to sell another car? ").upper()[0]
    if sContinueSell == "Y" and len(lstCarList) == 0 :
        sContinueSell = "N"
        print("Sorry, there are no more cars to sell.")
# If all cars have been sold say congrats, if not print the remaining cars
if len(lstCarList) == 0 :
    print("Congradulations! All cars have sold")
else :
    print("\nCars Unsold")
    printCars(lstCarList)
# Display the final inventory Cost, revenue made, and profit
fProfit = oCarComp.getEarnings() - oCarComp.getCost()
print("Inventory costs: " + str(oCarComp.getCost()) + " Revenue: " + str(oCarComp.getEarnings()) + \
       " Profit: " + str(fProfit))
