import pandas as pd

data = {
    "name": ["Ali", "Sara", "John"],
    "marks": [85, 90, 78]
    }

df = pd.DataFrame(data)
print(df)

# df.head()
# df.info()
print(df.describe())
print(df[["marks","name"]])

# print(df["name"])
# print(df["marks"])
