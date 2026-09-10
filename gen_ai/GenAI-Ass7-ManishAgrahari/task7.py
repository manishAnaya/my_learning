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
        print(f"{product.name} added successfully.")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"{name} removed successfully.")
                return

        print("Product not found.")

    def get_total_value(self):
        total_sum = 0

        for product in self.products:
            total_sum += product.price

        return total_sum

    def get_all_products(self):
        print("Product List")

        for product in self.products:
            print(product)


class Store:

    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))
        category = input("Enter Category: ")

        product = Product(name, price, category)

        self.inventory.add_product(product)

    def show_summary(self):
        print(f"Store Name: {self.store_name}")
        print(f"Total Products: {len(self.inventory.products)}")
        print(
            f"Total Inventory Value: "
            f"Rs.{self.inventory.get_total_value()}"
        )

        self.inventory.get_all_products()


store = Store("Reliance Fresh")

store.inventory.add_product(
    Product("Rice", 78, "Grocery")
)

store.inventory.add_product(
    Product("Milk", 60, "Dairy")
)

store.inventory.add_product(
    Product("Laptop", 65000, "Electronics")
)

store.show_summary()

p1 = Product("Rice", 78, "Grocery")
p2 = Product("Milk", 60, "Dairy")

print("\nCombined Price:", p1 + p2)