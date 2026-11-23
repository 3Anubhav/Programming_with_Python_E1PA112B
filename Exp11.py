import pandas as pd

# Creating a Series
marks = pd.Series([85, 90, 75, 95])
print("Series:\n", marks)

# Creating a DataFrame
data = {
    "Name": ["Anubhav", "Rahul", "Aman", "Rohit"],
    "Age": [21, 20, 22, 21],
    "Marks": [85, 90, 75, 95]
}

df = pd.DataFrame(data)
print("\nOriginal DataFrame:\n", df)

# Selecting Columns
print("\nNames:\n", df["Name"])

# Selecting Rows
print("\nFirst Row:\n", df.iloc[0])

# Adding a Column
df["Course"] = ["BCA", "BCA", "BCA", "BCA"]

# Updating a Column
df["Marks"] = [88, 92, 78, 96]
print("\nUpdated DataFrame:\n", df)

# Sorting Data
print("\nSorted by Marks:\n", df.sort_values("Marks"))

# Minimum, Maximum and Average
print("\nMinimum Marks:", df["Marks"].min())
print("Maximum Marks:", df["Marks"].max())
print("Average Marks:", df["Marks"].mean())