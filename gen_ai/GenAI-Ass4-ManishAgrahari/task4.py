# Task 4
with open("sales_data.txt", "r") as file:
    sales = [int(line.strip()) for line in file.readlines()]

    total_sales = sum(sales)
    highest_sale = max(sales)
    lowest_sale = min(sales)
    average_sale = total_sales / len(sales)

    print(f"Total Sales   : Rs.{total_sales}")
    print(f"Highest Sale  : Rs.{highest_sale}")
    print(f"Lowest Sale   : Rs.{lowest_sale}")
    print(f"Average Sale  : Rs.{average_sale:.2f}")