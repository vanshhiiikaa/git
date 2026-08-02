#sorting data in one column
import pandas as pd
data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 22],
    "Salary": [50000, 60000, 45000]
}
df = pd.DataFrame(data) 

#df.sort_values(by="Age", inplace=True)  # sorts the DataFrame by the "Age" column in ascending order
#print(df)

#for multiple columns
df.sort_values(by=["Age", "Salary"], ascending=[True, False], inplace=True)  # sorts the DataFrame by the "Age" and "Salary" columns in ascending order
print(df)
