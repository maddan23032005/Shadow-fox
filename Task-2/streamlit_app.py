import streamlit as st
import numpy as np
import joblib

model = joblib.load("model/car_price_model.pkl")
scaler = joblib.load("model/scaler.pkl")

def set_background():
    st.markdown("""
        <style>
        .stApp {
            background-image: url('back.jpg_large');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            color: white;
        }
        .stTextInput>div>div>input {
            background-color: rgba(255, 255, 255, 0.85);
            color: black;
        }
        .stSelectbox>div>div>div {
            background-color: rgba(255, 255, 255, 0.85);
            color: black;
        }
        </style>
    """, unsafe_allow_html=True)

set_background()

st.title("🚗 Car Selling Price Prediction")
st.markdown("### Fill in the details below to predict the price")

# Input fields
year = st.number_input("Year of Purchase", min_value=1990, max_value=2024, step=1)
present_price = st.number_input("Showroom Price (in lakhs)", step=0.1)
kms_driven = st.number_input("Kilometers Driven", step=100)
owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])
fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'CNG'])
seller_type = st.selectbox("Seller Type", ['Dealer', 'Individual'])
transmission = st.selectbox("Transmission Type", ['Manual', 'Automatic'])

# Convert inputs
fuel_map = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
seller_map = {'Dealer': 0, 'Individual': 1}
trans_map = {'Manual': 0, 'Automatic': 1}

input_data = np.array([[year, present_price, kms_driven, owner,
                        fuel_map[fuel_type], seller_map[seller_type], trans_map[transmission]]])

scaled_input = scaler.transform(input_data)
prediction = model.predict(scaled_input)[0]

if st.button("Predict Price"):
    st.success(f"Estimated Selling Price: ₹ {round(prediction, 2)} Lakhs")
