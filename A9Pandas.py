# Carson Chadwick
# Section 04
# This program practices importing a cvs file and storing it as a data frame to print information.
import pandas as pd

#read csv file
dfNames = pd.read_csv("practice_names.csv")

# print the city then name/age columns
print(dfNames["city"], end='\n\n')
print(dfNames[["name", "age"]], end='\n\n')

#Update the salary of "Joey Tribbiani" to 56000 and the age of "Jane Smith" to 29. 
dfNames.at[8,"salary"] = 56000
dfNames.at[1, "age"] = 29
# Print out the row for Joey Tribbiani and print out the row for Jane Smith.
print(dfNames.loc[[8]], end='\n\n')
print(dfNames.loc[[1]], end='\n\n')

# Use the .query() method to find all individuals who are older than 35 years and live in "Seattle", "Boston", or "San Francisco". 
dfNames = dfNames.query('age >= 35 and city in ["Seattle", "Boston", "San Francisco"]')
print(dfNames, end="\n\n")

# Sort the DataFrame based on the salary column in descending order 
dfNames.sort_values(['salary'], ascending=(False), inplace=True)
print(dfNames)