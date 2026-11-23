import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Creating a Dataset
data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 70, 80]
}

df = pd.DataFrame(data)
print("Student Dataset:\n", df)

# Analysing Dataset using Pandas
print("\nAverage Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())

# Creating a Matplotlib Plot
plt.plot(df["Hours"], df["Marks"], marker="o")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()

# Predictive Analysis using Scikit-Learn
X = df[["Hours"]]
y = df["Marks"]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict(pd.DataFrame({"Hours": [6]}))

print("\nPredicted Marks for 6 Hours:", prediction[0])