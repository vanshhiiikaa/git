# Handling Missing Data in Pandas
#dropna() is used to remove missing values from the DataFrame
import pandas as pd

data = {
    "Name": ["John", None, "Alice", "Bob", "Eve", "Charlie", "David","Frank"],
    "Age": [25, None, 22, 28, 35, 29, 31, 27],
    "Salary": [50000, None, 45000, 55000, 70000, 52000, 58000, 62000],
    "Performance": [85, None, 78, 88, 95, 82, 87, 91]
}
df = pd.DataFrame(data)
print(df)

#df.dropna(inplace=True)  # removes rows with missing values
#print(df)

#fillna() is used to fill missing values in the DataFrame
#df.fillna(0, inplace=True)  # fills missing values with 0
#print(df)

df["Age"].fillna(df["Age"].mean(), inplace=True)  # fills missing values in Age column with mean of Age
print(df)