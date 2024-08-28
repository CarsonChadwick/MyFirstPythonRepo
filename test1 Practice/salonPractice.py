# Carson Chadwick
# Section 04
# This program simulates a Salon management system using OOP programing
import random
# Client Class
class Client () :
    def __init__(self, name, preferred_haircut) :
        self.name = name
        self.preferred_haircut = preferred_haircut
# Hairstyle Class
class Hairstylist ():
    def __init__(self, name) :
        self.name = name
        self.clients = []
    # Perform_Haircut method
    def perform_haircut(self, client) :
        self.clients.append(client)
        print( self.name + " is giving a " + client.preferred_haircut +" haircut to " + client.name)
    # show_clients method
    def show_clients(self) :
        print("\nThese are " + self.name + "'s clients")
        for client in self.clients :
            print(client.name + " has a preferred haircut of " + client.preferred_haircut)
# ColoristSpecialist Class inherited from Hairstylist
class ColoristSpecialist (Hairstylist):
    def __init__(self, name) :
        super().__init__(name)
    # perform_haircut
    def perform_haircut(self, client):
        self.clients.append(client)
        print(self.name + " is giving a special " + client.preferred_haircut +" haircut with additional coloring options to " + client.name)

# Create Hairstylist and ColoristSpecialist objects and store them in list
salon = [Hairstylist("Alex"), ColoristSpecialist("Taylor"),  Hairstylist("Jordan"), ColoristSpecialist("Morgan")]
people = [Client("Pat", "Buzz"), Client("Chris", "Layered"), Client("Alex", "Bob"), Client("Jordan", "Pixie"), Client("Morgan", "Special Shag"), Client("Taylor", "crew cut")]
# Create client objects with unique names and prefered haircuts and store them in a list
# Use loop to randomly assign each client to a hairstylist using perfor_haircut
for client in people: 
    stylist = random.choice(salon)
    stylist.perform_haircut(client) 
# Display Results using show_clients method
for stylist in salon:
    stylist.show_clients()