try:
    input1 = int(input("Please enter 1st number: "))
    input2 = int(input("Please enter 2nd number: "))

    result = input1 / input2
    print(result)

except ValueError:
    print("Please enter proper numbers for division")

except ZeroDivisionError:
    print("2nd number cannot be 0")

else:
    print("Operation Complete")