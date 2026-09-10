# TASK => 2
with open("sales_data.txt", "r") as file:
    print(file.read())

with open("sales_data.txt", "r") as file:
    print(file.readline())

with open("sales_data.txt", "r") as file:
    sales = [int(line.strip()) for line in file.readlines()]
    print(sales)