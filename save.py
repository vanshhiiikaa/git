import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 22],
    "City": ["Delhi", "Mumbai", "Lucknow"]  
}

df = pd.DataFrame(data)
print(df)

#df.to_csv("students.csv", index=False)
#df.to_excel("students.xlsx", index=False)
df.to_json("students.json", orient="records", indent=4)