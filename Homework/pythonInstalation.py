#Carson Chadwick
#Section 004
#This pogram prompts a user to enter the cost of an average 4 bedroom house in Bentonville Arkansas
    #and converts the cost in Taiwanses New Dollars.

#Establish Variables
iPrice = int(input("Enter how much an average 4 bedroom house in Bentonville Arkansas costs: "))
fTaiwanDollarConversionRate = 31.56
fConversion = round(iPrice*fTaiwanDollarConversionRate,2)

#Print results
print("The cost of a $" + str(iPrice) + " 4 bedroom home in Arkansas in Taiwanese dollars is \n"+ \
      "$" + str(fConversion) )