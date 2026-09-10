## products with 6 elements as product name
products = ["Rice", "Flour", "Pulses", "Salt", "Oil", "Masala"]

## Tuple with product name, price and category
sample_products = ("Dove", 60, "Soap")

## Print the 2nd and last product
print(products[1])
print(products[-1])

## Adding two more products into list (products)
products.append("Lux")
products.append("Maggi")
print("\nUpdated Product List:")
print(products)

## Type casting tuple to list
sample_list = list(sample_products)

## Changing its price and converting it again to tuple
sample_list[1] = 65
print(sample_list)
sample_products = tuple(sample_list)
print(sample_products)

