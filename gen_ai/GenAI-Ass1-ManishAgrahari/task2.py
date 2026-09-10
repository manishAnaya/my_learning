products = ["Laptop", "Mouse", "Rice", "Paneer", "Milk", "Lizol"]

categories = ["Electronics", "Accesories", "Grocery", "Dairy", "Dairy", "Household"]

# Convert list to set
categories_set = set(categories)
print(categories_set)

# Add a new category
categories_set.add("Gaming")
print(categories_set)

# Adding duplicate category
categories_set.add("Dairy")
print(categories_set)

# Check if category exists
print(True if "Dairy" in categories_set else False)
print("Ice Cream" in categories_set)

# length of Categories Set
print(len(categories_set))

