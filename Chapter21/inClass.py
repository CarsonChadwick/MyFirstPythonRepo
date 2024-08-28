#clearing screen
import os
import platform
def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
clear_screen()
#importing required libraries
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, text
import matplotlib.pyplot as plot
# define the connection parameters:
database_name = "baseball"
db_user = "testuser"
db_password = "test"
db_host = "localhost" #this just means the database is stored on your own computer
db_port = "5432" # default setting
# Connect to the PostgreSQL database
engine = sqlalchemy.create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{database_name}')
conn = engine.connect()
#dfImportedFile = pd.read_excel("/Users/profgreg/downloads/mlb.xlsx")
dfImportedFile = pd.read_excel("mlb.xlsx")
# saving a dataframe to postgres:
dfImportedFile.to_sql("mlb", engine, if_exists= 'replace', index = False)
#printing out “You've imported the excel file into your postgres database.”
print("You've imported the excel file into your postgres database.")
#getting data from postgreSQL
print("The following are all the categories that have been sold:")
query = text('select * from mlb')
dfFromPostgres = pd.read_sql_query(query, conn)
print(dfFromPostgres)