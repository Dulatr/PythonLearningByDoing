# import the classes module
from classes import Product,Inventory

# define your products
apple=Product('Apple',10,price=.44)
banana=Product('Banana',13,3,1.00)
lettuce=Product('Lettuce',100,8,1.44)

# create an inventory of the products with a store name and ID
myinv = Inventory('Boone',51439)
myinv.addProduct(apple)
myinv.addProduct(banana)
myinv.addProduct(lettuce)

# Creating a neat table to display the contents of the inventory
def storeTable():
    print('-'*45)
    print(f"Store name: {myinv}\nStore code: {myinv.store_code}")
    print('-'*45)
    print("\nProducts available:\n")
    print("\tName\tID\tQuantity\tPrice\n")
    for item in myinv.product_list:
        print(f"{item.name : >12}{item.id : >6}{item.quantity : >14}{item.price : >13}")
    print('-'*45)
    print(f"\nNet Value:{myinv.value() : >35}")

print("Before deleting:\n")
storeTable()

print("\n\nAfter deleting:\n")
myinv.delProduct(apple)
storeTable()

print(f"\nRetrieving and individual item from list by id: {myinv.get(100).name}")