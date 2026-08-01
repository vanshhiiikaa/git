import pandas as pd

#read data from csv files into a data frame
#df = pd.read_csv("students.csv")
#df = pd.read_excel("students.xlsx", sheet_name="Sheet1")
df = pd.read_json("students.json")

print(df)

#gcsfs
