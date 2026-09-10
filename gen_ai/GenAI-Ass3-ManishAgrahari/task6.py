def process_prices(prices):
    discount = lambda price: price - (0.1 * price)
    discounted_prices = list(map(discount, prices))
    filtered_prices = list(filter(lambda x: x > 300, discounted_prices))
    return discounted_prices, filtered_prices

discounted, filtered = process_prices([100, 500, 900, 50, 750])
print(discounted)
print(filtered)
       