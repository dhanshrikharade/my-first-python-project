import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [85, 92, 76, 88]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())