prices = [100, 250, 400, 1200, 50, 2000, 850]
 
expensive_prices = list(filter(lambda price: price > 500, prices))
lower_prices = list(filter(lambda price: price <= 500, prices))

print(f"Expensive Prices: {expensive_prices}")
print(f"Lower Prices: {lower_prices}")