import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob", "Eve", "Charlie", "David", "Frank", "Grace"],
    "Age": [25, 30, 22, 28, 35, 29, 31, 27],
    "Salary": [50000, 60000, 45000, 55000, 70000, 52000, 58000, 62000],
    "Performance": [85, 90, 78, 88, 95, 82, 87, 91]
}

df = pd.DataFrame(data)
print("Sample Data Frame is:")
print(df)   
print("Names (Single column returned as Series) of the DataFrame:")
print(df["Name"])  # returns a single column as Series

high = df[df["Salary"] > 60000]  # returns rows where Salary is greater than 60000
print("Rows where Salary is greater than 60000:")
print(high)

#Filtering rows based on multiple conditions
filtered = df[(df["Age"] > 25) & (df["Salary"] > 50000)]  # returns rows where Age is greater than 25 and Salary is greater than 50000
print("Rows where Age is greater than 25 and Salary is greater than 50000:")     
print(filtered)       

#using or condition
filtered_or = df[(df["Age"] > 30) | (df["Salary"]> 60000)]  # returns rows where Age is greater than 30 or Salary is greater than 60000      
print("Rows where Age is greater than 30 or Salary is greater than 60000:")
print(filtered_or)