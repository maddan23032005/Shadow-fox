import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error
import joblib

df = pd.read_csv("data/boston.csv")


for col in df.columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[col] = np.where(df[col] < lower, lower, df[col])
    df[col] = np.where(df[col] > upper, upper, df[col])

X = df.drop("MEDV", axis=1)
y = df["MEDV"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

joblib.dump(scaler, "model/scaler.pkl")

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)


# Random Forest Regressor
model = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "model/boston_model.pkl")


y_pred = model.predict(X_test)
print(f"R2 Score     : {r2_score(y_test, y_pred):.4f}")
print(f"MSE          : {mean_squared_error(y_test, y_pred):.4f}")

# Sample prediction
print(f"\nSample Actual     : {y_test.iloc[0]}")
print(f"Sample Predicted  : {model.predict([X_test[0]])[0]:.2f}")
