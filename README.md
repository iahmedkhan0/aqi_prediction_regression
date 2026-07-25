<div align="center">

# 🌍🌫️ AIR QUALITY INDEX (AQI) PREDICTION
### *Machine Learning Regression Project using Random Forest*

<img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit">
<img src="https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange?style=for-the-badge&logo=scikitlearn">
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">

---

## 🌎 Predict Air Quality Instantly with Machine Learning

*A smart Machine Learning application that predicts the Air Quality Index (AQI) using environmental parameters like PM2.5, PM10, Temperature, Date, and Location.*

---

</div>

# 📸 Application Preview

> *(Add your Streamlit Screenshot here)*

```
images/
   └── preview.png
```

---

# ✨ Features

✅ Beautiful Streamlit Interface

✅ Random Forest Regression Model

✅ Real-time AQI Prediction

✅ Location Encoding using Label Encoder

✅ Fast & Accurate Prediction

✅ Interactive User Interface

✅ Easy to Deploy

---

# 🧠 Machine Learning Workflow

```text
                  Air Quality Dataset
                           │
                           ▼
                  Data Cleaning
                           │
                           ▼
                Feature Engineering
                           │
                           ▼
               Label Encoding(Location)
                           │
                           ▼
             Train Test Split (80:20)
                           │
                           ▼
          Random Forest Regressor Model
                           │
                           ▼
                  Model Evaluation
                           │
                           ▼
                  Streamlit Deployment
```

---

# 📂 Project Structure

```text
AQI_Prediction/
│
├── app.py
├── rf_model.pkl
├── location_encoder.pkl
├── AQI_Dataset.xlsx
├── requirements.txt
├── README.md
│
├── images/
│      └── preview.png
│
└── notebooks/
       └── AQI_Model.ipynb
```

---

# 📊 Dataset Information

| Feature | Description |
|----------|-------------|
| Date | Observation Date |
| Location | City/Location |
| PM2.5 | Fine Particulate Matter |
| PM10 | Coarse Particulate Matter |
| Temperature | Temperature in °C |
| Predicted AQI | Target Variable |

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Scikit-Learn | Machine Learning |
| Streamlit | Web Application |
| Joblib | Saving Model |
| Random Forest | Regression Algorithm |

---

# 🚀 Model Performance

| Metric | Value |
|---------|--------|
| Algorithm | Random Forest Regressor |
| R² Score | **0.63** |
| Train-Test Split | 80 : 20 |
| Dataset Size | 1460 Records |

---

# 📈 How the Model Works

```text
User Inputs

      │

      ▼

Date
Location
PM2.5
PM10
Temperature

      │

      ▼

Feature Encoding

      │

      ▼

Random Forest Model

      │

      ▼

Predicted AQI
```

---

# 💻 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/AQI-Prediction.git
```

Move into the project

```bash
cd AQI-Prediction
```

Install dependencies

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

| Feature | Value |
|----------|-------|
| Date | 20230725 |
| Location | Hyderabad |
| PM2.5 | 55.4 |
| PM10 | 92.7 |
| Temperature | 31 |

---

# 🌫️ Example Output

```text
Predicted AQI

AQI : 104.82

Air Quality

🟡 Moderate
```

---

# 📚 Machine Learning Pipeline

```text
Dataset
   │
   ▼
Cleaning
   │
   ▼
Date Conversion
   │
   ▼
Label Encoding
   │
   ▼
Feature Selection
   │
   ▼
Random Forest Regressor
   │
   ▼
Model Training
   │
   ▼
Prediction
   │
   ▼
Streamlit App
```

---

# 🌟 Future Improvements

- 🌍 Live AQI Data Integration
- ☁️ Weather API Support
- 📊 AQI Trend Visualization
- 🗺️ Interactive Maps
- 📱 Mobile Responsive UI
- 🤖 Model Optimization

---

# 👨‍💻 Developed By

### **Abdullah Ahmed Khan**

**B.E Computer Science Engineering**

Lords Institute of Engineering and Technology

---

<div align="center">

# ⭐ If you like this project, don't forget to Star the Repository ⭐

### 🌍 Clean Air Begins with Smart Predictions 🌱

<img src="https://img.shields.io/badge/Made%20With-❤️-red?style=for-the-badge">

</div>
