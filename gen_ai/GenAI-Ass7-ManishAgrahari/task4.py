from task2 import Product

class Laptop(Product):

    def __init__(self, name, price, category, ram):
        super().__init__(name, price, category)
        self.ram = ram

    def get_info(self):
        print(f"Name : {self.name}")
        print(f"Price : Rs.{self.get_price()}")
        print(f"Category : {self.category}")
        print(f"RAM : {self.ram}")

class Mobile(Product):

    def __init__(self, name, price, category, storage):
        super().__init__(name, price, category)
        self.storage = storage

    def get_info(self):
        print(f"Name : {self.name}")
        print(f"Price : Rs.{self.get_price()}")
        print(f"Category : {self.category}")
        print(f"Storage : {self.storage}")


laptop = Laptop("Dell Inspiron", 65000, "Electronics", "16 GB")
mobile = Mobile("Samsung Galaxy", 45000, "Electronics", "128 GB")

products = [laptop, mobile]

for product in products:
    product.get_info()
    print()
