# TASK => 3
with open("sales_data.txt", "a") as file:   
    file.write("5000\n2500\n1700")

with open("sales_data.txt", "r") as file:
    print(file.read())

# Optional
with open("sales_data.txt", "r") as file:
    print(len(file.readlines()))