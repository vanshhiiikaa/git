import pandas as pd

#read data from csv files into a data frame
df = pd.read_csv("students.csv",encoding = "latin1")
print(df)
