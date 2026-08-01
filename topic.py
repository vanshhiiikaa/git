"""
1- how big is your data?
2- what are the names of the columns?

shape and columns
"""
import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob", "Eve", "Charlie", "David", "Frank", "Grace"],
    "Age": [25, 30, 22, 28, 35, 29, 31, 27],
    "Salary": [50000, 60000, 45000, 55000, 70000, 52000, 58000, 62000],
    "Performance": [85, 90, 78, 88, 95, 82, 87, 91]
}

df = pd.DataFrame(data)
print("Shape of the DataFrame:", df.shape)  # returns the number of rows and columns
print("Columns of the DataFrame:", df.columns)  # returns the column names
