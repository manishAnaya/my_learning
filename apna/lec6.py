def cal_sum(a, b) -> int:
    sum = a + b
    return sum


def calc_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

def check_odd(x):
    if(x%2 == 0):
        return "Even"
    else:
        return "Odd"

# Recurssion

def show(n):
    if(n == 11):
        return    #Base Case
    print(n)
    show(n+1)

# show(5)

def get_factorial(n):
    if(n == 0 or n == 1):
        return 1
    return n * get_factorial(n-1)

# print(get_factorial(5))

def get_sum(n):
    if(n == 0):
        return 0
    return n + get_sum(n-1)

# print(get_sum(100))

myList = [1,4,9,16,25,36,49,64,81,100]

def printLists(lists, n=0):
    if(n >= len(lists)):    
        return
    print(lists[n])
    printLists(lists, n+1)

printLists(myList)