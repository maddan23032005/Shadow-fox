import streamlit as st
import pandas as pd
import numpy as np
import joblib
import base64

st.set_page_config(page_title="🏠 Boston House Price Predictor", layout="centered")

model = joblib.load("model/boston_model.pkl")
scaler = joblib.load("model/scaler.pkl")

def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    bg_css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: #000000;
    }}
    .main-container {{
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(0,0,0,0.3);
    }}
    </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

set_bg("bg.jpg")

st.markdown("<div class='main-container'>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #2e7d32;'>🏠 Boston House Price Predictor</h1>", unsafe_allow_html=True)
st.write("🔢 Fill in the details below to estimate the house price in **$1000s**:")

# Input form
with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        CRIM = st.number_input("CRIM - Crime Rate", min_value=0.0, step=0.01)
        ZN = st.number_input("ZN - Residential Land (%)", min_value=0.0, step=1.0)
        INDUS = st.number_input("INDUS - Non-Retail Land (%)", min_value=0.0, step=0.1)
        CHAS = st.selectbox("CHAS - Bounded by River", [0, 1])
        NOX = st.number_input("NOX - Nitric Oxide Level", min_value=0.0, step=0.01)
        RM = st.number_input("RM - Avg. Rooms per Dwelling", min_value=1.0, step=0.1)
        AGE = st.number_input("AGE - % Built before 1940", min_value=0.0, step=1.0)

    with col2:
        DIS = st.number_input("DIS - Distance to Employment", min_value=0.0, step=0.1)
        RAD = st.number_input("RAD - Access to Highways", min_value=1.0, step=1.0)
        TAX = st.number_input("TAX - Property Tax Rate", min_value=100.0, step=10.0)
        PTRATIO = st.number_input("PTRATIO - Pupil-Teacher Ratio", min_value=10.0, step=0.1)
        B = st.number_input("B - 1000(Bk - 0.63)^2", min_value=0.0, step=1.0)
        LSTAT = st.number_input("LSTAT - % Lower Status Population", min_value=0.0, step=0.1)

    submitted = st.form_submit_button("🎯 Predict House Price")

# Prediction output
if submitted:
    input_df = pd.DataFrame([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE,
                              DIS, RAD, TAX, PTRATIO, B, LSTAT]],
                            columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM',
                                     'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'])

    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]

    st.success(f"🏷️ **Estimated House Price:** ${prediction * 1000:,.2f}")

st.markdown("</div>", unsafe_allow_html=True)
