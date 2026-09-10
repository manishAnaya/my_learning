prices = [120, 350, "abc", 500, -200, 800]

total = 0

for price in prices:
    try:
        if price < 0:
            raise ValueError("Negative price not allowed")

        total += price

    except TypeError:
        print("Value is not a number")

    except ValueError as e:
        print(e)

    else:
        print(f"Running Total : {total}")

print("-" * 30)
print(f"Final Total : {total}")