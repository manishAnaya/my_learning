orders = []

while True:

    print("-"*40)
    print("Press '1' to Add Order Amount")
    print("Press '2' to Show Orders Detail")
    print("Press 'q' to Quit")
    print("-"*40)

    choice = input("Enter your choice: ")
    if choice == "1":
        
        amount = input("Enter Amount to add: ")
        if amount.isdigit():
            orders.append(int(amount))
        else:
            print("Invalid Amount")
            continue
    
    elif choice == "2":

        if not orders:
            print("No Orders Available")
            continue

        for order_amount in orders:
            discount_percent = 0
            if order_amount >= 2000:
                discount_percent = 15
            
            elif order_amount >= 1500:
                discount_percent = 10
            
            elif order_amount >= 1000:
                    discount_percent = 7

            discount_amount = (discount_percent * order_amount) / 100
            final_amount = order_amount - discount_amount
            print("-" * 40)
            print(f"Order Amount => Rs.{order_amount:.2f}")
            print(f"Discount Applicable {discount_percent}% => Rs.{discount_amount:.2f}" if discount_percent > 0 else "No Discount Applied")
            print(f"Final Amount After Discount => Rs.{final_amount:.2f}")

    elif choice == "q":
        print("---------------Program End---------------")
        break

    else:
        print("Enter Valid Keywords i.e. 1, 2 or q to quit")