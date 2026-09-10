# length should be more than 8 characters
# Must have atleast one uppercase
# Must have atleast one lowercase
# Must have atleast one special charater
# Must have atleast one numeric value


def check_pass_strength(password):
    # length check
    if len(password) < 8:
        print("Weak password (must be atleast 8 characters)")

    # lower case check
    elif not any (char.islower() for char in password):
        print("pass must have atleast 1 lower character, its weak")

    # upper case check
    elif not any (char.isupper() for char in password):
        print("pass must have atleast 1 upper character, its weak")

    # numeric value check
    elif not any (char.isdigit() for char in password):
        print("pass must have atleast 1 numeric value, its weak")

    # special charater check
    elif not any (char in "!@#$%^&*()" for char in password):
        print("pass must have atleast 1 special charater, its weak")

    # Its String
    else:
        print("Congratulations... Its Strong and Safe password")

# check_pass_strength("Name")
# check_pass_strength("Name123")
# check_pass_strength("Name12345")




def check_strength(password):
    special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|"
    has_lower = False
    has_upper = False
    has_special = False
    has_digit = False

    if len(password) < 8:
        return "Weak Password (Must be at least 8 characters)"

    for char in password :
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    if has_lower and has_upper and has_special and has_digit:
        return "Strong password! Congratulations..."

    if has_lower and has_upper and has_digit:
        return "Medium password! You can add one special charater to make this Strong"

    else:
        return "Sorry, Its Weak anf not safe"


# password = input("Enter Password: ")

# result = check_strength(password)
# print(result)


def check_palindrome(my_str):
    str_val = my_str.lower().replace(" ", "")
    print("Palindrome" if str_val == str_val[::-1] else "Not Palindrome")

# check_palindrome("abcder")
# check_palindrome("acvca")
# check_palindrome("abba")

cart = [
    {
        "item1": "Apple",
        "cost": 5,
        "qty": 8,
    },
    {
        "item1": "Banana",
        "cost": 4,
        "qty": 12,
    },
    {
        "item1": "Guavava",
        "cost": 3,
        "qty": 10,
    },
]

def cartTotal(cart):
    amount = 0
    for items in cart:
        amount += items["qty"] * items["cost"]
    print(amount)

cartTotal(cart)

square = lambda x: x**2