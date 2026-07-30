import pandas as pd

data = {
    "Name": ["Alice", "Bob"],
    "Age": [25, 30]
}

df = pd.DataFrame(data)
df.to_excel("students.xlsx", index=False)

#print("Data saved!")

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 22],
    "City": ["Delhi", "Mumbai", "Lucknow"]
}

df = pd.DataFrame(data)

# Save data to CSV
df.to_csv("students.csv", index=False)

#print("Data saved successfully!")

import json

students = [
    {
        "Name": "Alice",
        "Age": 25,
        "City": "Delhi"
    },
    {
        "Name": "Bob",
        "Age": 30,
        "City": "Mumbai"
    },
    {
        "Name": "Charlie",
        "Age": 22,
        "City": "Lucknow"
    }
]

# Save data to JSON file
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Data saved successfully!")