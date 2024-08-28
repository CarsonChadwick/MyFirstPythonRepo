import psycopg2
import pandas as pd

conn = psycopg2.connect(dbname='food_essentials',
                         user= 'testuser',
                         password='test',
                         host='localhost',
                         port=5432)

df = pd.read_sql("select * from candy;", conn)

print(df)

conn.close