file_name = input("Enter file name you want to read: ")

try:
    with open(file_name, "r") as file:
        for i in range(3):
            print(file.readline())

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("You dont have permission to access this file")

finally:
    print("File Operation attempted")   

