import pandas as pd

df = pd.read_json("students.json")

print(df.info()) #returns the summary of the DataFrame