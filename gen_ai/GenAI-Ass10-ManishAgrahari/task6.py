import pandas as pd

students = {
    "Name": ["Amit", "Neha", "Rahul", "Sneha", "Pooja"],
    "Marks": [78, 85, 90, 66, 72],
    "Subject": ["Math", "Math", "Science", "Science", "Math"]
}

df = pd.DataFrame(students)
print("Students with more than 75 marks")
print(df[df["Marks"] > 75])

print("Students with subject Maths")
print(df[df["Subject"] == "Math"])

print("Students with more avg marks")
avg_marks = df['Marks'].mean()
print(df[df["Marks"] > avg_marks])

print("Students with less than 70 marks")
print(df[df["Marks"] < 70])