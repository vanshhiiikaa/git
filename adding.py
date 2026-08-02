#adding columns
import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob", "Eve", "Charlie", "David", "Frank", "Grace"],
    "Age": [25, 30, 22, 28, 35, 29, 31, 27],
    "Salary": [50000, 60000, 45000, 55000, 70000, 52000, 58000, 62000],
    "Performance": [85, 90, 78, 88, 95, 82, 87, 91]
}

df = pd.DataFrame(data)
# square brackets are used to add a new column to the DataFrame
df["Bonus"] = df["Salary"] * 0.1  # Adding a new
print("Data Frame after adding Bonus column:")
print(df)

#using insert()
#df.insert(loc, column="", value=])  # Adding a new column at index 4
df.insert(0, "Employee ID", [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008])  # Adding a new column at index 4
print("Data Frame after adding Total Compensation column:") 
print(df)

#.loc[] is used to add a new column to the DataFrame
df .loc[0,'Salary'] = 55000  # Updating the Salary of the first employee
print(df)

#increasing the Salary of all employees by 5%
df["Salary"] = df["Salary"] * 1.05  # Increasing the Salary
print(df)
