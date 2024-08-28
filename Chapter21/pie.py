import psycopg2
import pandas as pd
import matplotlib.pyplot as plot

conn = psycopg2.connect(dbname='food_essentials',
                         user= 'testuser',
                         password='test',
                         host='localhost',
                         port=5432)

sqlDropTable = "DROP TABLE IF EXISTS sales"

sqlCreateTable = "CREATE TABLE IF NOT EXISTS sales (id SERIAL PRIMARY KEY, description varchar(30), quantity int)";

cursor = conn.cursor()

cursor.execute(sqlDropTable)

cursor.execute(sqlCreateTable)

conn.commit()

aSales = [('Twix', 87), ('Snickers', 42), ('Nerds', 70), ('Starburst', 16), ('Skittles', 25), ('Kit Kat', 53)]

sqlInsert = "INSERT INTO sales VALUES (DEFAULT, %s, %s)"

cursor.executemany(sqlInsert, aSales)

conn.commit()

df = pd.read_sql("select description as candy_name, quantity as Sales from sales;", conn)

aLabels=[]
for aData in df.values:
    aLabels.append(aData[0])
df.plot.pie(y="sales", labels=aLabels, explode=[.2,0,0,0,0,0,], autopct='%1.1f%%', legend=False)
plot.show(block=True)

conn.close