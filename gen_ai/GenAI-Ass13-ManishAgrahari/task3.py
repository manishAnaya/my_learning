import sqlite3
import pandas as pd

connection = sqlite3.connect('sample.db')

# Remove existing table if it exists
connection.execute('Drop table if exists employees')

# Create employees table
connection.execute("""
    Create table employees(
    id INTEGER,
    name TEXT,
    department TEXT
    )
""")

# Employee 5 records
employees = [
    (1, "Raghav", "IT"),
    (2, "Sita", "HR"),
    (3, "Laxman", "Finance"),
    (4, "Hanuman", "Marketing"),
    (5, "Bharat", "IT")
]

# Inserting records
connection.executemany(
    "Insert into employees VALUES (?,?,?)",
    employees
)

# Read SQL data into DataFrame
df = pd.read_sql_query('Select * from employees', connection)

# Printing DF
print(df)
