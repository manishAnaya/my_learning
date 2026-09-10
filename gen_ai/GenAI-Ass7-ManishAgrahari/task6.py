class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product name : {self.name}, Price : {self.price}, Category : {self.category}"

    def __add__(self, other):
        return self.price + other.price

p1 = Product("Rice", 78, "Grocery")
p2 = Product("Milk", 60, "Dairy")
print(p1)
print(p2)

total_amount = p1 + p2

print(total_amount)