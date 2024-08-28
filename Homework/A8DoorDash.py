# Author: Ryan Hagerty
# Section: 004
# Description: Randomly generate a list of customers and the number of burgers they ordered. Then, print the list of customers and the number of burgers they ordered in descending order by the number of burgers ordered.
import os
import random
os.system('clear')
class Order:
    def __init__(self):
        self.burger_count = self.randomBurgers()
    def randomBurgers(self):
        return random.randint(1,20)
class Person:
    def __init__(self):
        self.customer_name = self.randomName().ljust(19)
    def randomName(self):
        lsCustomers = [
            "Jefe",
            "El Guapo",
            "Lucky Day",
            "Ned Nederlander",
            "Dusty Bottoms",
            "Harry Flugleman",
            "Carmen",
            "Invisible Swordsman",
            "Singing Bush"
        ]
        return random.choice(lsCustomers)
class Customer(Person):
    def __init__(self):
        super().__init__()
        self.order = Order()
queue = []
for i in range(100):
    newCustomer = Customer()
    queue.append(newCustomer)
dictionary = {}
queueLength = len(queue)
for i in range(queueLength):
    currrent_customer = queue.pop(0)
    if currrent_customer.customer_name not in dictionary:
        dictionary[currrent_customer.customer_name] = int(currrent_customer.order.burger_count)
    else:
        dictionary[currrent_customer.customer_name] += int(currrent_customer.order.burger_count)
sortedDictionary = sorted(dictionary.items(), key=lambda x: x[1] ,reverse=True)
[print(i[0],i[1]) for i in sortedDictionary]
