prices = [100, 250, 400, 1200, 50]
gst = lambda price: price * 1.18
prices_with_gst = list(map(gst, prices))

print(f"Original Prices: {prices}")
print(f"Prices after GST: {prices_with_gst}")
