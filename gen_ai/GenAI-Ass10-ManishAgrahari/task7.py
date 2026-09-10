import pandas as pd

students = {
    "Name": ["Amit", "Neha", "Rahul", "Sneha", "Pooja"],
    "Marks": [78, 85, 90, 66, 72],
    "Subject": ["Math", "Math", "Science", "Science", "Math"]
}

df = pd.DataFrame(students)

print("Avg marks per Subject")
print(df.groupby("Subject")["Marks"].mean())

print("Students per Subject")
print(df["Subject"].value_counts())

print("Max marks per Subject")
print(df.groupby("Subject")["Marks"].max())