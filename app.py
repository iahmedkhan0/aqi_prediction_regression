import streamlit as st
import joblib
import pandas as pd

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="🌍 AQI Prediction",
    page_icon="🌫️",
    layout="wide"
)

# ---------------- LOAD MODEL ---------------- #

model = joblib.load("aqi_model.pkl")
location_encoder = joblib.load("location_encoder.pkl")

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

/* Background */

.stApp{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
background-size:400% 400%;
animation: gradient 15s ease infinite;
color:white;
}

@keyframes gradient{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

/* Title */

.title{
font-size:48px;
font-weight:bold;
text-align:center;
color:#ffffff;
margin-bottom:5px;
}

.subtitle{
text-align:center;
font-size:18px;
color:#dcdcdc;
margin-bottom:30px;
}

/* Card */

.card{
background:rgba(255,255,255,0.12);
backdrop-filter:blur(15px);
padding:25px;
border-radius:20px;
box-shadow:0 8px 30px rgba(0,0,0,0.4);
margin-bottom:20px;
}

/* Button */

.stButton>button{
width:100%;
height:55px;
border:none;
border-radius:12px;
font-size:20px;
font-weight:bold;
background:linear-gradient(90deg,#00c9ff,#92fe9d);
color:black;
transition:0.3s;
}

.stButton>button:hover{
transform:scale(1.03);
box-shadow:0px 0px 20px cyan;
}

/* Inputs */

div[data-baseweb="select"]{
color:black;
}

input{
border-radius:10px !important;
}

.metric{
background:#1f2937;
padding:15px;
border-radius:15px;
text-align:center;
color:white;
font-size:18px;
font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/4148/4148460.png",
    width=120
)

st.sidebar.title("🌍 AQI Prediction")

st.sidebar.markdown("""
### Machine Learning Model

- 🌳 Random Forest Regressor
- 📊 Dataset Size : **1460**
- 📈 R² Score : **0.63**
- 💾 Joblib Model
- 🌐 Streamlit Dashboard

---

### Input Features

✔ Date

✔ Location

✔ PM2.5

✔ PM10

✔ Temperature
""")

# ---------------- HEADER ---------------- #

st.markdown('<div class="title">🌫️ AIR QUALITY INDEX PREDICTION</div>', unsafe_allow_html=True)

st.markdown(
'<div class="subtitle">Predict Air Quality using Machine Learning</div>',
unsafe_allow_html=True)

# ---------------- INPUT CARD ---------------- #

st.markdown('<div class="card">', unsafe_allow_html=True)

col1,col2=st.columns(2)

with col1:

    date=st.number_input(
        "📅 Date (YYYYMMDD)",
        min_value=20200101,
        max_value=20301231,
        value=20230725
    )

    location=st.selectbox(
        "📍 Location",
        list(location_encoder.classes_)
    )

    pm25=st.number_input(
        "🌫 PM2.5",
        min_value=0.0,
        max_value=500.0,
        value=50.0
    )

with col2:

    pm10=st.number_input(
        "🌁 PM10",
        min_value=0.0,
        max_value=600.0,
        value=80.0
    )

    temperature=st.number_input(
        "🌡 Temperature (°C)",
        min_value=-10.0,
        max_value=60.0,
        value=30.0
    )

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- METRICS ---------------- #

m1,m2,m3=st.columns(3)

with m1:
    st.metric("🌫 PM2.5",pm25)

with m2:
    st.metric("🌁 PM10",pm10)

with m3:
    st.metric("🌡 Temperature",temperature)

# ---------------- PREDICTION ---------------- #

if st.button("🚀 Predict AQI"):

    location_encoded=location_encoder.transform([location])[0]

    input_df=pd.DataFrame({
        "date":[date],
        "location":[location_encoded],
        "pm2.5":[pm25],
        "pm10":[pm10],
        "temperature":[temperature]
    })

    prediction=model.predict(input_df)[0]

    st.markdown("---")

    st.markdown(
        f"""
        <div style='
        background:rgba(255,255,255,0.12);
        padding:30px;
        border-radius:20px;
        text-align:center;
        box-shadow:0px 0px 20px rgba(0,255,255,.5);'>

        <h1 style='color:white;'>Predicted AQI</h1>

        <h1 style='font-size:70px;color:#00FFD5;'>{prediction:.2f}</h1>

        </div>
        """,
        unsafe_allow_html=True
    )

    if prediction<=50:
        st.success("🟢 GOOD AIR QUALITY")
    elif prediction<=100:
        st.info("🟡 MODERATE AIR QUALITY")
    elif prediction<=150:
        st.warning("🟠 UNHEALTHY FOR SENSITIVE GROUPS")
    elif prediction<=200:
        st.warning("🔴 UNHEALTHY")
    elif prediction<=300:
        st.error("🟣 VERY UNHEALTHY")
    else:
        st.error("⚫ HAZARDOUS")

st.markdown("---")

st.caption("🌍 Developed by Abdullah Ahmed Khan | Random Forest Regression | Streamlit")