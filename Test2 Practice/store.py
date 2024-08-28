# Carson Chadwick
# Section 04
# This program imports and processes product data for an online store from an excel speadsheet

import random
import pandas as pd
import math


class Product():
    def __init__(self, product_id, product_name, product_category, price):
        self.product_name = product_name
        self.product_category = product_category
        self.price = price
        self.product_id = product_id
    def display_info_and_return_price(self):
        print("\t" + self.product_name + ": " + str(self.price))
        return(self.price)

class ElectronicProduct(Product) :
    def __init__(self, product_id, product_name, product_category, price, warranty_type, warranty_price_percent):
        super().__init__(product_id, product_name, product_category, price)
        self.warranty_type = warranty_type
        self.warranty_price_percent = warranty_price_percent
    
    def display_info_and_return_price(self):
        warrantyBoostedPrice = round(self.price + self.price*self.warranty_price_percent, 2)
        print("\t" + self.product_name + ": " + str(self.price) + ". Price including " + str(self.warranty_type) + "warranty : " + str(warrantyBoostedPrice))
        return(warrantyBoostedPrice)
    
class Order():
    def __init__(self):
        self.order_id = random.randint(1,50000)
        self.list_of_products = []
    
    def add_products_to_order(self, productList, numToAdd):
        for integer in range (0,numToAdd):
            self.list_of_products.append(random.choice(productList))
        print("Added " + str(numToAdd) + " product(s) to order #" + str(self.order_id))

    def show_all_products_and_total(self):
        print("Order #" + str(self.order_id) + " has the following products:")
        totalPrice = 0
        for product in self.list_of_products:
            totalPrice += product.display_info_and_return_price()
        print("\tThe order total is " + str(round(totalPrice, 2)))

dfImportedProducts = pd.read_excel("product_data.xlsx")

lstProducts = []
for index, row in dfImportedProducts.iterrows():
    
    newProduct = Product(row["Product_ID"], row['Product_Name'], row['Product_Category'], row['Price'])
    x = row['Warranty_Price_Percent']
    if math.isnan(row['Warranty_Price_Percent']) == False:
        newProduct = ElectronicProduct(row["Product_ID"],row['Product_Name'], row['Product_Category'], row['Price'], row['Warranty_Type'], row['Warranty_Price_Percent'])

    lstProducts.append(newProduct)

orderList = []

list_of_orders = []
for _ in range(5):
    order_object = Order()
    orderList.append(order_object)


for order in orderList:
    numToAdd = random.randint(1,5)
    order.add_products_to_order(lstProducts, numToAdd)
print()
for order in orderList:
    order.show_all_products_and_total()
    print()
    
