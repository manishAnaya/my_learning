order_amount_str = input("Please enter order amount: ")

if order_amount_str.isdigit():
    order_amount = int(order_amount_str)
    print(f"order amount: Rs.{order_amount:.2f}")

    discount_percent = 0

    if order_amount >= 2000:
        discount_percent = 15

    elif order_amount >= 1500:
        discount_percent = 10

    elif order_amount >= 1000:
        discount_percent = 7

    discount = (discount_percent  * order_amount) / 100
    final_amount = order_amount - discount
    print(f"{discount_percent}% Discount applied with Rs.{discount}" if discount_percent > 0 else "No Discount Applied")
    print(f"Final Amount: Rs.{final_amount:.2f}")
    ## Add Tax
    tax_amount = (final_amount * 5) / 100
    print(f"Tax applied: Rs.{tax_amount:.2f}")
    final_total = final_amount + tax_amount
    print(f"Final Amount to be paid with taxes: Rs.{final_total:.2f}")
else:
    print("Please enter valid amount in digits")



