cart = []

while True:
    try:
        price = input("Enter price or q to exit with total bill: ")
        if price.lower() == "q":
            break

        price = float(price)
        if price < 0:
            raise ValueError("Price cannot be negative")

        cart.append(price)
        
    except ValueError as e:
        print(f"Invalid Value entered {e}")

    except Exception as e:
        print(e)

print(f"Total Items : {len(cart)}")
print(f"Cart : {cart}")
print(f"Total Bill : Rs.{sum(cart):.2f}")