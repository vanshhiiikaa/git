import pandas as pd
data = {
    "Name": ["John", "John", "Bob", "Eve", "Charlie", "David", "Frank"],
    "Age": [28, 30, 22, 28, 35, 22, 31],
    "Salary": [50000, 60000, 45000, 55000, 70000, 52000, 58000]
}
df = pd.DataFrame(data) 

avg_salary = df["Salary"].mean()  # calculates the average salary
#print("Average Salary:", avg_salary)


#groupby
grouped = df.groupby("Age")["Salary"].sum()  # groups the DataFrame by the "Age" column and calculates the mean salary for each group
#print(grouped)

#for multiple
grouped_multiple = df.groupby(["Age","Name"])[["Salary"]].sum()  # groups the DataFrame by the "Age" column and calculates the sum of salary and name for each group
print(grouped_multiple)