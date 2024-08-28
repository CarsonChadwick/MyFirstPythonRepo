import psycopg2
conn = psycopg2.connect(dbname='food_essentials',
                        user = 'testuser', 
                        password='password', 
                        host='localhost', 
                        port=5432)

cur_food_essentials = conn.cursor()
cur_food_essentials.execute("SELECT id, description, price FROM candy;")
print(f"Current row is {cur_food_essentials.rownumber}")
cur_food_essentials.close()
conn.close()