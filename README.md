<div align="center">

# 🌍🌫️ AIR QUALITY INDEX (AQI) PREDICTION
### *Machine Learning Regression Project using Random Forest Regressor*

<img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit">
<img src="https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange?style=for-the-badge&logo=scikitlearn">
<img src="https://img.shields.io/badge/Random_Forest-Regressor-success?style=for-the-badge">
<img src="https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge">

---

# 🌎 Smart Air Quality Prediction using Machine Learning

Predict the **Air Quality Index (AQI)** instantly using **Random Forest Regression** based on environmental factors like **Date, Location, PM2.5, PM10, and Temperature**.

> 🌱 *Helping understand air pollution through intelligent machine learning.*

</div>

---

# ✨ Features

- 🌫️ Predict Air Quality Index (AQI)
- 🤖 Random Forest Regressor Model
- 📍 Location Encoding using LabelEncoder
- ⚡ Real-Time Prediction
- 📊 User-Friendly Streamlit Interface
- 💾 Saved ML Model using Joblib
- 📅 Date-Based Prediction
- 🌍 Supports Multiple Locations

---

# 🧠 Machine Learning Workflow

```text
                  AQI Dataset
                       │
                       ▼
               Data Cleaning
                       │
                       ▼
            Feature Engineering
                       │
                       ▼
        Label Encoding (Location)
                       │
                       ▼
          Train-Test Split (80:20)
                       │
                       ▼
      Random Forest Regressor Model
                       │
                       ▼
            Model Evaluation (R²)
                       │
                       ▼
           Streamlit Web Application
```

---

# 📂 Project Structure

```text
aqi_prediction_regression/
│
├── app.py
├── aqi_model.pkl
├── location_encoder.pkl
├── AQI_Dataset.xlsx
├── requirements.txt
├── README.md
│
└── notebooks/
    └── AQI_Model.ipynb
```

---

# 📊 Dataset Information

| Feature | Description |
|----------|-------------|
| 📅 Date | Date of Observation |
| 📍 Location | City / Area |
| 🌫️ PM2.5 | Fine Particulate Matter |
| 🌁 PM10 | Coarse Particulate Matter |
| 🌡️ Temperature | Temperature (°C) |
| 🎯 Predicted AQI | Target Variable |

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|----------|
| 🐍 Python | Programming Language |
| 📊 Pandas | Data Manipulation |
| 🔢 NumPy | Numerical Computing |
| 🤖 Scikit-Learn | Machine Learning |
| 🌐 Streamlit | Web Application |
| 💾 Joblib | Save & Load Model |
| 🌳 Random Forest | Regression Algorithm |

---

# 🚀 Model Performance

| Metric | Value |
|---------|-------|
| 🤖 Algorithm | Random Forest Regressor |
| 📈 R² Score | **0.63** |
| 📂 Dataset Size | **1460 Records** |
| ✂️ Train-Test Split | **80 : 20** |

---

# 📈 Prediction Pipeline

```text
              User Input

                    │

        ┌───────────┼───────────┐
        │           │           │
      Date      Location    Temperature
        │           │           │
        └───────────┼───────────┘
                    │
             PM2.5 & PM10
                    │
                    ▼
          Feature Preparation
                    │
                    ▼
      Random Forest Regressor
                    │
                    ▼
          Predicted AQI Value
                    │
                    ▼
      Air Quality Category
```

---

# 🖥️ Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/aqi_prediction_regression.git
```

Move into the project folder

```bash
cd aqi_prediction_regression
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📦 Requirements

```text
streamlit
pandas
numpy
scikit-learn
joblib
openpyxl
```

---

# 🎯 Example Input

| Feature | Sample Value |
|----------|--------------|
| Date | 20230725 |
| Location | Hyderabad |
| PM2.5 | 54.3 |
| PM10 | 90.6 |
| Temperature | 30.8 |

---

# 🌫️ Example Output

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━

Predicted AQI : 108.45

Air Quality

🟡 Moderate

━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

# 🔄 End-to-End Workflow

```text
Raw Dataset
     │
     ▼
Data Cleaning
     │
     ▼
Date Conversion
     │
     ▼
Location Encoding
     │
     ▼
Feature Selection
     │
     ▼
Random Forest Training
     │
     ▼
Model Saving (.pkl)
     │
     ▼
Streamlit Application
     │
     ▼
AQI Prediction
```

---

# 🌟 Future Scope

- 🌍 Live AQI Prediction
- ☁️ Weather API Integration
- 📈 AQI Trend Analysis
- 🗺️ Interactive Location Maps
- 📱 Mobile-Friendly UI
- 🚀 Hyperparameter Optimization
- 📊 Data Visualization Dashboard

---

# 🎓 Learning Outcomes

✔ Data Cleaning

✔ Feature Engineering

✔ Label Encoding

✔ Random Forest Regression

✔ Model Evaluation

✔ Streamlit Deployment

✔ Machine Learning Pipeline

---

# 👨‍💻 Developed By

## **Abdullah Ahmed Khan**

**Bachelor of Engineering (Computer Science Engineering)**

🏫 Lords Institute of Engineering and Technology

---

<div align="center">

## ⭐ Star this Repository if you found it useful ⭐

### 🌍 Better Data → Better Predictions → Better Environment 🌱

<img src="https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Built%20using-Streamlit-red?style=for-the-badge&logo=streamlit">
<img src="https://img.shields.io/badge/Machine%20Learning-Random%20Forest-success?style=for-the-badge">

</div>
