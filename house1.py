import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Read CSV file
data = pd.read_csv("house_data.csv")

# Input and output
X = data[["Area"]]
y = data["Price"]

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Get new house area
area = float(input("Enter house area in sqft: "))

# Predict price
prediction = model.predict([[area]])

print("Predicted House Price:", round(prediction[0], 2), "Lakhs")

# Graph
plt.scatter(data["Area"], data["Price"], label="Actual Data")

plt.plot(
    data["Area"],
    model.predict(X),
    label="Regression Line"
)

# Show new prediction
plt.scatter(
    area,
    prediction[0],
    marker="*",
    s=200,
    label="New Prediction"
)

plt.xlabel("Area (sqft)")
plt.ylabel("Price (Lakhs)")
plt.title("House Price Prediction using Linear Regression")
plt.legend()
plt.show()
