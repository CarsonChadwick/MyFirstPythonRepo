import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, text
import matplotlib.pyplot as plot

# define the connection parameters:
database_name = "is303"
db_user = "testuser"
db_password = "test"
db_host = "localhost" #this just means the database is stored on your own computer
db_port = "5432" # default setting
# Connect to the PostgreSQL database
engine = sqlalchemy.create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{database_name}')
conn = engine.connect()


# Have the user imput their choice
iChoice = 1
# While loop to allowing them to keep selecting an option.
while iChoice == 1 or iChoice == 2 :
    iChoice = int(input("If you want to import data, enter 1. If you want to see summaries of stored data, enter 2. Enter any other value to exit the program: "))
    # for option 1
    if iChoice == 1 :
        
        #dfImportedFile = pd.read_excel("/Users/profgreg/downloads/mlb.xlsx")
        dfImportedFile = pd.read_excel("Retail_Sales_Data.xlsx")
        dfSeparatedNames = dfImportedFile["name"].str.split("_", expand=True)
        dfImportedFile.insert(1,"first_name", dfSeparatedNames[0])
        dfImportedFile.insert(2,"last_name", dfSeparatedNames[1])
        del dfImportedFile['name']
        # Dictionary for different products
        productCategoriesDict = {
            'Camera': 'Technology',
            'Laptop': 'Technology',
            'Gloves': 'Apparel',
            'Smartphone': 'Technology',
            'Watch': 'Accessories',
            'Backpack': 'Accessories',
            'Water Bottle': 'Household Items',
            'T-shirt': 'Apparel',
            'Notebook': 'Stationery',
            'Sneakers': 'Apparel',
            'Dress': 'Apparel',
            'Scarf': 'Apparel',
            'Pen': 'Stationery',
            'Jeans': 'Apparel',
            'Desk Lamp': 'Household Items',
            'Umbrella': 'Accessories',
            'Sunglasses': 'Accessories',
            'Hat': 'Apparel',
            'Headphones': 'Technology',
            'Charger': 'Technology'}
        
        # match the category values to the dictionary key value pairs. 
        dfImportedFile['category'] = dfImportedFile['product'].map(productCategoriesDict)
        # Import it to the database
        dfImportedFile.to_sql("sale", engine, if_exists= 'replace', index = False)
        # Print statement
        print("You've imported the excel file into your postgres database.")    
    # for option 2
    if iChoice == 2 :
        # print the categories options
        print("The following are all the categories that have been sold.")
        dfImported = pd.read_sql_query('select * from sale', conn)
        # pd.read_sql_query('select distinct category from sale', conn)
        unique = dfImported['category'].unique()
        icount = 1
        dctCategory = {}
        for value in unique :
            dctCategory[icount] = value
            print(str(icount) + ":" + value)
            icount +=1 

        # Have them choose an option
        categoryNum = int(input("Please enter the number of the category you want to see summarized: "))
        chosen_category = dctCategory[categoryNum]
        # dfCategory = dfNew.query('category == chosen_category')
        dfCategory = dfImported[dfImported['category'] == chosen_category]
        total_sales_sum = dfCategory['total_price'].sum()
        average_sale_amount = dfCategory['total_price'].mean()
        total_units_sold = dfCategory['quantity_sold'].sum()
        # Print Averages
        print('\n')
        print(f"Total sales for {chosen_category}: {total_sales_sum:,.2f}")
        print(f"Average sale amount for {chosen_category}: {average_sale_amount:,.2f}")
        print(f"Total units sold for {chosen_category}: {total_units_sold}")
        # groupby product
        dfProductSales = dfCategory.groupby('product')['total_price'].sum()

        dfProductSales.plot(kind='bar')  # Creates the bar chart
        # Add title and labels to the chart
        plot.title(f'Total Sales in {chosen_category}')  # adds title to the top of the chart
        plot.xlabel("Product")  # Label for the x-axis
        plot.ylabel("Total Sales")  # label for the y-axis
        # Display the chart
        plot.show()  # Makes the chart pop up on the screen
        


print("Closing the program.")
