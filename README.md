# house-prediction-linear-regression
A simple machine learning project that predicts house prices based on house area using Linear Regression in Python, with data visualization using Matplotlib.
🏠 House Price Prediction using Linear Regression

This project predicts the price of a house based on its **area in square feet** using **Linear Regression** in Python.

## 📌 Project Overview

The model learns the relationship between:

* **House Area (sqft)** → Input
* **House Price (Lakhs)** → Output

After training the model with the data in the CSV file, the user can enter a new house area and get the predicted house price.

The project also displays a **graph** showing the actual data points, regression line, and the new prediction.

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib
* Linear Regression
* CSV Dataset

## 📂 Project Structure

```text
HousePrediction/
│
├── house_prediction.py
├── house_data.csv
└── README.md
```

## 📊 Dataset

The dataset contains two columns:

| Column | Description               |
| ------ | ------------------------- |
| Area   | House area in square feet |
| Price  | House price in lakhs      |

Example:

```csv
Area,Price
500,15
600,18
700,21
800,24
900,27
1000,30
1200,36
1500,45
1800,54
2000,60
```

## ⚙️ Installation

Make sure Python is installed on your computer.

Install the required libraries:

```bash
pip install pandas scikit-learn matplotlib
```

If you are using VS Code, you can also use:

```bash
python -m pip install pandas scikit-learn matplotlib
```

## ▶️ How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Make sure `house_prediction.py` and `house_data.csv` are in the same folder.
4. Open the VS Code terminal.
5. Run:

```bash
python house_prediction.py
```

## 💻 Example

The program asks:

```text
Enter house area in sqft: 1450
```

Output:

```text
Predicted House Price: 43.5 Lakhs
```

A graph is then displayed showing:

* Actual house price data
* Linear regression line
* New predicted house price

## 📈 Machine Learning Method

The project uses **Linear Regression**.

The basic equation is:

```text
y = mx + b
```

Where:

* `y` = predicted house price
* `x` = house area
* `m` = slope
* `b` = intercept

The model learns `m` and `b` from the training data and uses them to predict the price of a new house.

## 🎯 Objective

The main objective of this project is to demonstrate how **Supervised Machine Learning** and **Linear Regression** can be applied to a simple real-world problem such as house price prediction.

## 📷 Output

The project produces:

1. Predicted house price
2. Regression graph
3. Actual data points
4. New prediction point

## 👩‍💻 Author

**Deepasri J P**

B.Sc. Computer Science
