price_dict = {
    "dove": 60,
    "rice": 45.50,
    "maggi": 60,
    "salt": 14.75,
    "laptop": 45000,
    "paneer": 240
}

# Adding new product
price_dict["Milk"] = 52
print(price_dict)

# Updating product price
price_dict["dove"] = 215
print(price_dict)

# Remove a product by name
product = "Milk"
if product in price_dict:
    del price_dict[product]
    print("product removed")
else:
    print("product not found")

print(price_dict)

# Average price of all products
total = sum(price_dict.values())
length = len(price_dict)
avg = total / length
print(round(avg))

# max and min price

max_price = max(price_dict, key=price_dict.get)
min_price = min(price_dict, key=price_dict.get)

print("Maximum Price Product")
print(max_price, price_dict[max_price])

print("Minimum Price Product")
print(min_price, price_dict[min_price])