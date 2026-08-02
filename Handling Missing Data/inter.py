import pandas as pd

data = {
    "Name": ["John", None, "Alice", "Bob", "Eve", "Charlie", "David","Frank"],
    "Age": [25, None, 22, 28, 35, 29, 31, 27],
    "Salary": [50000, None, 45000, 55000, 70000, 52000, 58000, 62000],
    "Performance": [85, None, 78, 88, 95, 82, 87, 91]
}
df = pd.DataFrame(data)
print(df)

df.interpolate(method='linear',axis = 0, inplace=True)  # fills missing values using linear interpolation
print(df)
