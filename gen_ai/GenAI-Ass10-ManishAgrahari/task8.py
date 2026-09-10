import pandas as pd
import matplotlib.pyplot as plt

students = {
    "Name": ["Amit", "Neha", "Rahul", "Sneha", "Pooja"],
    "Marks": [78, 85, 90, 66, 72],
    "Subject": ["Math", "Math", "Science", "Science", "Math"]
}

df = pd.DataFrame(students)

df.plot(kind='bar', x= "Name", y="Marks")
plt.show()

df.plot(kind='line', y="Marks")
plt.show()

df.plot(kind='hist', y="Marks")
plt.show()