import pandas as pd

students = {
    "Name": ["Amit", "Neha", "Rahul", "Sneha", "Pooja"],
    "Marks": [78, 85, 90, 66, 72],
    "Subject": ["Math", "Math", "Science", "Science", "Math"]
}

df = pd.DataFrame(students)

print("Info")
df.info()
print("Describe")
print(df.describe())
print("Head")
print(df.head())
print("Tail")
print(df.tail())
print("Marks in descending order and index is reset")
print(df.sort_values(by="Marks", ascending=False).reset_index(drop=True))
