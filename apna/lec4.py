# myDict = {
#     "name": "Manish",
#     "subjects": [],
#     "topics": (),
#     "price": 4565.23,
#     "qty": 12,
#     "isPaid": True
# }

# print(myDict)
# myDict["subjects"].append("Maths")
# myDict["subjects"].append("English")
# myDict["price"] = 4500
# print(myDict)

# student = {
#     "name": "Krish",
#     "marks": {
#         "phy": 45,
#         "maths": 0,
#         "chem": 0
#     },
#     "percentage": 0.0,
#     "result": "PASS"
# }

# print(student)

# student["marks"]["phy"] = 78

# print(student)

# student["percentage"] = (student["marks"]["phy"] + student["marks"]["maths"] + student["marks"]["chem"]) * 0.333
# student["result"] = student["percentage"] > 33

# print(list(student.values()))

# print(student.get("name"))

# student["city"] = "Jaipur"
# student.update({"location": "banglore"})
# print(student)

# collections = {1,2,3,4,5, "hello", "hii", "HELLO", "Hello", "hii"}
# print(collections)

allMarks = {}

mathsMarks = input("Enter marks obtained in Maths : ")
englishMarks = input("Enter marks obtained in English : ")
scienceMarks = input("Enter marks obtained in Science : ")

allMarks.update({"maths": mathsMarks, "english": englishMarks, "science": scienceMarks})

print(allMarks)