class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(f"Product name : {self.name}, Price : {self.price}, Category : {self.category}")

p1 = Product("Rice", 78, "Grocery")
p2 = Product("Milk", 60, "Dairy")

p1.get_info()
p2.get_info()