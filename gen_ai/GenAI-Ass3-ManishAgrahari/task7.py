prices_list = []

def add_price(prices_list, price):
    prices_list.append(price)

def get_average_price(prices_list):
    return sum(prices_list) / len(prices_list)

def get_max_price(prices_list):
    return max(prices_list)

while True:
    print("_"*40)
    print("Press '1' to Add Price to List")
    print("Press '2' to Get Average Price")
    print("Press '3' to Get Maximun Price")
    print("Press 'q' to Quit")
    print("_"*40)

    choice = input("Please enter: ")

    if choice == "1":
        price = input("Enter price you want to add: ")
        if price.isdigit():
            add_price(prices_list, int(price))
        else:
            print("Please enter valid number")
            continue

    elif choice == "2":
        if not prices_list:
            print("Price list is empty.. Please add some prices")
            continue
        avg = get_average_price(prices_list)
        print(f"Avearge Price : {avg}")

    elif choice == "3":
        if not prices_list:
            print("Price list is empty.. Please add some prices")
            continue
        max_price = get_max_price(prices_list)
        print(f"Max Price : {max_price}")

    elif choice == "q":
        print("_____________End of Program____________")
        break

    else:
        print("Please enter valid keyword...")
