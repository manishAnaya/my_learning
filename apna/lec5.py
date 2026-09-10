# count = 1

# while count <=5:
#     print("Hello")
#     count += 1


# Print numbers from 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# Print numbers from 100 to 1
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# Print multiplication table of a number n
# n = 5
# i = 1
# while i <= 10:
#     print(f"{n} x {i} = ", n * i)
#     i += 1

# Print list of numbers

# numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# count = len(numbers)
# i = 0
# while(i < count):
#     print(numbers[i])
#     i += 1

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("Enter number u want to find : "))
# i = 0
# while i < len(tup):
#     if(tup[i] == x):
#         print(f"Found {x} at the {i} index")
#     i += 1

# numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("Enter number u want to find : "))
# for index, val in enumerate(numbers):
#     if(val == x):
#         print(f"found {x} at index : {index}")
#         break

# for i in range(1,101):
#     print(i)

# for i in range(100, 0, -1):
#     print(i)

# n = 5
# for i in range(1, 11):
#     print(i * 5)

# n = 5
# sum = 0
# while (n >= 0):
#     sum += n
#     n -= 1
# print(sum)


# n = 10
# sum = 0
# for i in range(n+1):
#     sum += i
# print(sum)

# num = int(input("Enter number for factorial : "))
# fact = 1
# for i in range(1, num + 1):
#     fact *= i

# print(fact) 
   
num = int(input("Enter number for factorial : "))
fact = 1

while(num > 1):
    fact *= num
    num -= 1
print(fact)