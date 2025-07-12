import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import os

df = pd.read_csv("data/car.csv")
df.drop_duplicates(inplace=True)

df['Fuel_Type'] = df['Fuel_Type'].map({'Petrol': 0, 'Diesel': 1, 'CNG': 2})
df['Seller_Type'] = df['Seller_Type'].map({'Dealer': 0, 'Individual': 1})
df['Transmission'] = df['Transmission'].map({'Manual': 0, 'Automatic': 1})

df.drop(columns=['Car_Name'], errors='ignore', inplace=True)

X = df.drop("Selling_Price", axis=1)
y = df["Selling_Price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = RandomForestRegressor(random_state=42)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
print("R2 Score :", round(r2_score(y_test, y_pred), 4))
print("MSE      :", round(mean_squared_error(y_test, y_pred), 4))

# Save model and scaler
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/car_price_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")
