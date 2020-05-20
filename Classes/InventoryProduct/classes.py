"""
Classes module for Product-Inventory programs.
"""

class Product:
    """
    A class that defines a product in the store. 
    
    name=<str>, id=<int>,quantity=<int>
    
    Default is empty string name, and properties set to 0.
    """

    def __init__(self,name='',id=0,quantity=0,price=0.0):
        self._name = name
        self._id = id
        self._quantity=quantity
        self._price = price

    #####   Change the ID value of product   #####
    ##
    ##  INPUT(s): [id] : <int>
    ##            -ID to be set
    ##  OUTPUT(s): <None>
    def updateID(self,id):
        self._id = id
    
    def __str__(self):
        return(self.name)    
    @property
    def name(self):
        return self._name
    @property
    def id(self):
        return self._id    
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self,value):
        self._quantity = value
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,value):
        self._price = value

class Inventory:
    """
    A class that holds and inventories products from the store.
    
    name=<str>, store_code=<int>

    Default name is empty string, default store_code is 0.
    """
    
    def __init__(self,name='',store_code=0):
        self._store_code = store_code
        self._name = name
        self._product_list = []

    #####   Current inventory value   #####
    ##
    ##  INPUT(s): <None>
    ##           
    ##  OUTPUT(s): <float>
    ##             -Outputs the total inventory value of all products in the product list
    def value(self):
        
        if self._product_list == []:
            return 0
        else:
            total = 0.0
            for pr in self._product_list:
                total += pr.price * pr.quantity
            return total

    #####   Add and remove product to the inventory   #####
    ##
    ##  INPUT(s): [product] : <Product>
    ##            -takes a product instance and adds or deletes from the product_list
    ##  OUTPUT(s): <None>
    ##    
    def addProduct(self,product):
        self._product_list.append(product)
    def delProduct(self,product):
        self._product_list.remove(product)    

    #####   Returns the product based on id   #####
    ##
    ##  INPUT(s): [id] : <int>
    ##            -Product lookup id, default 0.
    ##  OUTPUT(s): <Product>
    ##             -Returns Product class reference with provided id. 
    ##              returning the first instance. If no id is provided
    ##              then it will return the most recent addition to the
    ##              list. 
    ##
    def get(self,id=0):
        if self._product_list == []:
            raise Exception("Empty product list")

        if id==0:
            return self._product_list[len(self._product_list)-1]
        else:
            for pr in self.product_list:
                if pr.id == id:
                    return pr          

    def __str__(self):
        return self._name
    @property 
    def store_code(self):
        return self._store_code
    @property
    def name(self):
        return self._name
    @property
    def product_list(self):
        return self._product_list

    
    