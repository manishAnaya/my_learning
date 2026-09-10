def apply_discount(price, discount_percent = 5):
    discount = (discount_percent * price) / 100
    final_amount = price - discount
    return final_amount

print(apply_discount(1000, 10))
print(apply_discount(500))