import pandas as pd

students = {
    "Name": ["Amit", "Neha", "Rahul", "Sneha", "Pooja"],
    "Marks": [78, 85, 90, 66, 72],
    "Subject": ["Math", "Math", "Science", "Science", "Math"]
}

df = pd.DataFrame(students)

print(f"First 3 Rows: \n{df[0:3]}")
print(f"Last 2 Rows: \n{df[-2:]}")
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns}")