import streamlit as st
import joblib
import pandas as pd

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Air Quality Index Prediction",
    page_icon="🌫️",
    layout="centered"
)

# ---------------- Load Model & Encoder ----------------
model = joblib.load("aqi_model.pkl")
location_encoder = joblib.load("location_encoder.pkl")

# ---------------- Title ----------------
st.title("🌫️ Air Quality Index Prediction")
st.markdown("Predict the AQI based on environmental parameters.")

st.divider()

# ---------------- Inputs ----------------

date = st.number_input(
    "Date (YYYYMMDD)",
    min_value=20200101,
    max_value=20301231,
    value=20230725
)

locations = list(location_encoder.classes_)

location = st.selectbox(
    "Location",
    locations
)

pm25 = st.number_input(
    "PM2.5",
    min_value=0.0,
    max_value=500.0,
    value=50.0
)

pm10 = st.number_input(
    "PM10",
    min_value=0.0,
    max_value=600.0,
    value=80.0
)

temperature = st.number_input(
    "Temperature (°C)",
    min_value=-10.0,
    max_value=60.0,
    value=30.0
)

# ---------------- Prediction ----------------

if st.button("Predict AQI", use_container_width=True):

    location_encoded = location_encoder.transform([location])[0]

    input_df = pd.DataFrame({
        "date": [date],
        "location": [location_encoded],
        "pm2.5": [pm25],
        "pm10": [pm10],
        "temperature": [temperature]
    })

    prediction = model.predict(input_df)[0]

    st.success(f"Predicted AQI : **{prediction:.2f}**")

    if prediction <= 50:
        st.success("🟢 Air Quality: Good")
    elif prediction <= 100:
        st.info("🟡 Air Quality: Moderate")
    elif prediction <= 150:
        st.warning("🟠 Air Quality: Unhealthy for Sensitive Groups")
    elif prediction <= 200:
        st.warning("🔴 Air Quality: Unhealthy")
    elif prediction <= 300:
        st.error("🟣 Air Quality: Very Unhealthy")
    else:
        st.error("⚫ Air Quality: Hazardous")