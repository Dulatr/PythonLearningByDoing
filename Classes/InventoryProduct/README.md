# Inventory Product

In this project the goal is to utilize classes in python to create an inventory management system for a store. Stores carry product and have to keep track of the product in some fashion to determine the costs of product lost or gained. The top module `classes` contains to class definitions:

* `Product`
* `Inventory`

The `Product` class stores the name, ID, price, and quantity in stock for that particular object. The `Inventory` class stores product information in a list that can be added to or removed from through `.addProduct` and `.delProduct` methods respectively. You can retrieve the item information from the inventory by using `.get(id)` if you know the id; this also will return the most recently added item to the inventory if no id is provided. Alternatively, you can access the product list directly from the inventory and display it's properties this way. Another useful feature of the inventory class is that you can retrieve the net value of the inventory through the `.value()` method. 

## Example 

```python
# import the classes module
from classes import Product,Inventory

# define your products (notice the apple doesn't define the quantity, it defaults to 0)
apple=Product('Apple',10,price=.44)
banana=Product('Banana',13,3,1.00)
lettuce=Product('Lettuce',100,8,1.44)

# create an inventory of the products with a store name and store code
myinv = Inventory('Boone',51439)

# add the products to the inventory
myinv.addProduct(apple)
myinv.addProduct(banana)
myinv.addProduct(lettuce)

# print the net value of products
print(myinv.value())
```