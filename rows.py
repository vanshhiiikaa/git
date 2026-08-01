#head() tail() method is used to return the first n rows or last n rows of a DataFrame. By default, it returns 5 rows.
import pandas as pd

df = pd.read_json("students.json")

print(df.head(2)) #returns first 3 rows
print(df.tail(2)) #returns last 3 rows