# Queue first in first out practice

queCustomers = []

iCustomers = 3

for iCount in range(1, iCustomers + 1) :
    print("Your ticket # is " + str(iCount))
    sName = input("What is your name? ")
    queCustomers.append([iCount, sName])

print("\n")

print("Here is the customer list:")
for iCount in range(0, len(queCustomers)) :
    print(str(queCustomers[iCount][0]) + " for customer " + queCustomers[iCount][1])

print("\n")

while len(queCustomers) > 0 :
    print("Helping ticket " + str(queCustomers[0][0]) + " " + queCustomers[0][1])
    queCustomers.pop(0)
    print("\n")
    if len(queCustomers) >0 :
        print("Here is the customer list:")
        for iCount in range(0, len(queCustomers)) :
            print(str(queCustomers[iCount][0]) + " for customer " + queCustomers[iCount][1])
        print("\n")   