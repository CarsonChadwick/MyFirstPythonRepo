# Carson Chadwick
# Practice composision
class Car :
    def __init__(self, make, model) :
        self.make = make
        self.model = model
        self.engine = Engine(self.make, self.model)

class Engine : 
    def __init__(self, make, model) :
        if (make == "FORD") :
            if (model == "MUSTANG ECOBOOST") :
                self.type = "2.3L EcoBoost"
                self.transmission = "10-speed Automatic"
                self.horsepower = 310
            elif (model == "MUSTANG GT500") :
                self.type = "5.2L V8"
                self.transmission = "7-speed dual clutch"
                self.horsepower = 760
            else :
                self.type = "4-cylinder"
                self.transmission = "automatic"
                self.horsepower = 200                
        else :
            self.type = "2.0 L 4-cylinder"
            self.transmission = "Automatic CVT"
            self.horsepower = 149 
sMake = input("Enter the make of the car: ").upper()
sModel = input("Enter the name of the model: ").upper()
oCar = Car(sMake, sModel) 

print("Type".ljust(20), "Transmission".ljust(20), "Horsepower".ljust(15))
print(oCar.engine.type.ljust(20), oCar.engine.transmission.ljust(20), str(oCar.engine.horsepower).ljust(15))