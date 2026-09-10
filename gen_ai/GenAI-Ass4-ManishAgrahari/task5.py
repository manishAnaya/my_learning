# Task 5
with open("products.txt", "w") as file:
    for i in range(3):
        product_name = input("Enter Product Name: ")
        product_price = input("Enter Product Price: ")
        if product_price.isdigit():
            file.write(f"{product_name} | {product_price}\n")
        else:
            print("Invalid Price")

with open("products.txt", "r") as file:
    for line in file:
        print(line.strip())