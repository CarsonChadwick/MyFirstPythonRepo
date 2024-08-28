# Name: Jacob
# Description: This creates hairstylists and color specialists, as well as clients at a Salon. Clients are randomly assigned to the stylists/specialists
# and all the clients of stylists/specialists are printed out at the end.

import random

class Client:
    def __init__(self, name, preferred_haircut):
        self.name = name
        self.preferred_haircut = preferred_haircut

class Hairstylist:
    def __init__(self, name):
        self.name = name
        self.clients = []

    def perform_haircut(self, client):
        print(f"\n{self.name} is giving a {client.preferred_haircut} haircut to {client.name}.")
        self.clients.append(client)

    def show_clients(self):
        print(f"\nThese are {self.name}'s clients")
        for client in self.clients:
            print(f"{client.name}, has a preferred haircut of {client.preferred_haircut}")

class ColoristSpecialist(Hairstylist):
    def __init__(self, name):
        super().__init__(name)

    def perform_haircut(self, client):
        print(f"\n{self.name} is giving a special {client.preferred_haircut} haircut with additional coloring options to {client.name}.")
        self.clients.append(client)


salon = [Hairstylist("Alex"), ColoristSpecialist("Taylor"), Hairstylist("Jordan"), ColoristSpecialist("Morgan")]

clients = [Client("Pat", "buzz cut"), Client("Chris", "layered"), Client("Alex", "bob"),
           Client("Jordan", "pixie"), Client("Morgan", "shag"), Client("Taylor", "crew cut")]


# Randomly assign clients for haircuts and coloring
for client in clients:
    stylist = random.choice(salon)

    stylist.perform_haircut(client)

# Show all stylists and their clients
for stylist in salon:
    stylist.show_clients()