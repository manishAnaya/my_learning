# def findInLine(word):
#     with open("practice.txt", "r") as file:
#         for line_no, line in enumerate(file, start=1):
#             if word in line:
#                 return line_no
#     return -1

# print(findInLine("Gens"))

def findEvenFromFile():
    count = 0
    with open("practice.txt", "r") as file:
        for word in file:
            data = word.split(",")
            for index, num in enumerate(data):
                if int(num) % 2 == 0:
                    count += 1
        return count

print(findEvenFromFile())