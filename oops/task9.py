class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Name: {self.name}, Price: Rs.{self.price}, Category: {self.category}"

    def __add__(self, other):
        return self.price + other.price

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added successfully")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"{product.name} removed successfully")
                return
        print("Product not found.")

    def get_total_value(self):
        total_sum = 0
        for product in self.products:
            total_sum += product.price
        return total_sum

    def get_all_products(self):
        print("\n--------------- Product List ---------------")
        for product in self.products:
            print(product)

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        name = input("Enter Product Name : ")
        price = float(input("Enter Price : "))
        category = input("Enter Category : ")
        product = Product(name, price, category)
        self.inventory.add_product(product)  

    def remove_product(self, name):
        self.inventory.remove_product(name)      

    def show_summary(self):
        print("-"*40)
        print(f"Store Name : {self.store_name}")
        print(f"Total Products : {len(self.inventory.products)}")
        print(f"Total Inventory Value : Rs.{self.inventory.get_total_value()}")
        self.inventory.get_all_products()

mystore = Store("Reliance Fresh")
mystore.add_new_product()
mystore.inventory.add_product(Product("Rice", 78, "Grocery"))
mystore.inventory.add_product(Product("Milk", 60, "Dairy"))
mystore.inventory.add_product(Product("Laptop", 65000, "Electronics"))
mystore.show_summary()