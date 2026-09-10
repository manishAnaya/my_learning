products = ["dove", "rice", "maggi", "salt", "laptop", "paneer"]

categories = ["Hair", "Grocery", "Grocery", "Grocery", "Electronics", "Dairy"]

price_dict = {
    "dove": 60,
    "rice": 45.50,
    "maggi": 60,
    "salt": 14.75,
    "laptop": 45000,
    "paneer": 240
}

# Creating catalog tuple for storing all above data index wise using loop
catalog = []
for i in range(len(products)):
    catalog.append(
        (
            products[i],
            price_dict[products[i]],
            categories[i]
        )
    )
print(catalog)

# category_to_products new dict
category_to_products = {}
for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product)

print(category_to_products)
    
# getting maximum products from a category
max_category = max(category_to_products, key=lambda x: len(category_to_products[x]))

print(max_category)
for product in category_to_products[max_category]:
    print(product)