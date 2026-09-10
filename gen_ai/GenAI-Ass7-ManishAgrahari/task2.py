class Product:

    def __init__(self, name, price, category):
        self.name = name
        self._price = price
        self.category = category

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Price must be greater than 0.")

    def get_info(self):
        print(f"Name : {self.name}")
        print(f"Price : {self._price}")
        print(f"Category : {self.category}")

p1 = Product("Rice", 78, "Grocery")
print(p1.get_price())

p1.set_price(95)
p1.get_info()