daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0

for value in daily:
    if value == -1:
        break

    if value == 0:
        continue
    
    total_sales += value
    print(f"Total Sales: Rs.{total_sales}")

print("-"*40)
print(f"Total Sales: Rs.{total_sales}")