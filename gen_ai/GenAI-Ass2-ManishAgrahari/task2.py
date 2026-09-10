orders = [1200, 2500, 800, 1750, 3000]
total_revenue = 0
disc_item_count = 0
for order_amount in orders:
    discount_percent = 0

    if order_amount >= 2000:
        discount_percent = 15

    elif order_amount >= 1500:
        discount_percent = 10

    elif order_amount >= 1000:
        discount_percent = 7

    if discount_percent > 0 :
        disc_item_count += 1

    discount_amount = (discount_percent * order_amount) / 100
    final_amount = order_amount - discount_amount
    total_revenue += final_amount
    print("-" * 40)
    print(f"Order Amount => Rs.{order_amount:.2f}")
    print(f"Discount Applicable {discount_percent}% => Rs.{discount_amount:.2f}" if discount_percent > 0 else "No Discount Applied")
    print(f"Final Amount After Discount => Rs.{final_amount:.2f}")

print("-" * 40)
print(f"Number of orders that received discount => {disc_item_count}")
print(f"Total Revenue after discount => Rs.{total_revenue:.2f}")