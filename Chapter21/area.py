import psycopg2
import pandas as pd
import matplotlib.pyplot as plot

conn = psycopg2.connect(dbname='food_essentials',
                         user= 'testuser',
                         password='test',
                         host='localhost',
                         port=5432)

sqlDropTable = "DROP TABLE IF EXISTS pizzas"

sqlCreateTable = "CREATE TABLE IF NOT EXISTS pizzas (id SERIAL PRIMARY KEY, day_of_week varchar(3), quantity int)";

cursor = conn.cursor()

cursor.execute(sqlDropTable)

cursor.execute(sqlCreateTable)

conn.commit()

aSales = [('Sun', 0), ('Mon', 7), ('Tue', 10), ('Wed', 9), ('Thu', 15), ('Fri', 42), ('Sat', 105)]

sqlInsert = "INSERT INTO pizzas VALUES (DEFAULT, %s, %s)"

cursor.executemany(sqlInsert, aSales)

conn.commit()

df = pd.read_sql("select day_of_week, quantity from pizzas;", conn)

df.plot.area(x="day_of_week", y="quantity", rot=15, title="Pizza Sales", color="red")
plot.show(block=True)

conn.close()