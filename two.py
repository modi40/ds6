import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv('sports_performance.csv')

print("Dataset Preview:")
print(df.head())

X = df[['Training_Hours_Per_Week']]
y = df['Performance_Score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nR2 Score:", r2_score(y_test, y_pred))

plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
plt.title("Training Hours vs Performance Score")
plt.xlabel("Training Hours Per Week")
plt.ylabel("Performance Score")
plt.legend()
plt.tight_layout()
plt.show()
