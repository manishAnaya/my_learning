# Task 7
prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount = input("Enter Discount: ")

if discount.isdigit():
    discount = int(discount)
else:
    print("Invalid Discount")

total_items = 0
total_discounted_price = 0

with open("discount_report.txt", "w") as file:
    file.write("Product | Original Price | Discounted Price\n")
    for product, price in prices.items():
        discount_price = price - (price * discount / 100)
        total_items += 1
        total_discounted_price += discount_price
        file.write(f"{product} | {price} | {discount_price}\n")

    average_discounted_price = total_discounted_price / total_items
    file.write("\n")
    file.write(f"Total Items : {total_items}\n")
    file.write(f"Average Discounted Price : {average_discounted_price:.2f}")

with open("discount_report.txt", "r") as file:
    print(file.read())