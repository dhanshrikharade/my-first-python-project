import pandas as pd
from sklearn.linear_model import LinearRegression

# Training data
data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "score": [35, 42, 50, 55, 65, 72, 80, 88]
}

df = pd.DataFrame(data)

# Features and target
X = df[["hours"]]
y = df["score"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Make prediction
hours = float(input("How many hours did you study? "))

prediction = model.predict([[hours]])

print(f"Predicted score: {prediction[0]:.2f}")