from task2 import Product

class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Price: Rs.{self.get_price()}")
        print(f"Category: {self.category}")
        print(f"Warranty: {self.warranty_years} Years")


laptop = ElectronicProduct("Dell Inspiron", 65000, "Electronics", 2)

laptop.get_info()