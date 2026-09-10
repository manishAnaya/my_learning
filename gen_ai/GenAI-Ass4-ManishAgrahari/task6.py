# Task 6
import os
file_path = input("Enter the file name you want to open: ")

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        print(file.read())
else:
    print("File not found, Please check the file name...")