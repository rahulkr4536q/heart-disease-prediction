# 🩺 Heart Disease Risk Prediction

An end-to-end Machine Learning project that started as an Exploratory Data Analysis (EDA) project and was extended into an interactive **Heart Disease Risk Prediction web application** using **K-Nearest Neighbors (KNN)** and **Streamlit**.

🚀 **Live Demo:** [Heart Disease Risk Prediction App](https://heart-disease-prediction-bsneu2lwtnnzft73kkftsa.streamlit.app/)

---

## 📌 Project Overview

This project analyzes cardiovascular health indicators and builds a Machine Learning pipeline to predict the presence of heart disease.

The project covers the complete workflow:

**Data Analysis → Data Cleaning → Preprocessing → Feature Scaling → Machine Learning → Prediction → Streamlit Deployment**

The final application allows users to enter clinical parameters through an interactive web interface and receive a model-based prediction.

> ⚠️ **Disclaimer:** This application is created for educational and demonstration purposes only. It is not a medical diagnostic tool and should not be used as a substitute for professional medical advice.

---

## 🎯 Objectives

- Perform Exploratory Data Analysis on cardiovascular health data
- Identify and handle data quality issues
- Encode categorical variables
- Scale numerical features
- Train a K-Nearest Neighbors classification model
- Save the trained model and preprocessing objects
- Build an interactive Streamlit application
- Deploy the application as a live web app

---

## 📊 Dataset

The dataset contains **918 records** and **12 initial attributes** related to cardiovascular health.

### Features

| Feature | Description |
|---|---|
| Age | Age of the patient in years |
| Sex | Sex of the patient |
| ChestPainType | Type of chest pain |
| RestingBP | Resting blood pressure |
| Cholesterol | Serum cholesterol level |
| FastingBS | Fasting blood sugar indicator |
| RestingECG | Resting electrocardiogram results |
| MaxHR | Maximum heart rate achieved |
| ExerciseAngina | Exercise-induced angina |
| Oldpeak | ST depression |
| ST_Slope | Slope of the peak exercise ST segment |
| HeartDisease | Target variable |

### Target

- `1` → Heart disease
- `0` → Normal

---

## 🔍 Exploratory Data Analysis

The initial phase of the project focused on understanding the dataset and identifying potential data quality issues.

### Key EDA Steps

- Checked for missing values
- Checked for duplicate records
- Investigated invalid zero values
- Analyzed categorical and numerical features
- Studied feature relationships and correlations
- Examined the target distribution

---

## 🛠️ Data Cleaning & Preprocessing

Several preprocessing steps were performed before training the Machine Learning model.

### 1. Missing & Duplicate Values

The dataset was checked for explicit missing values and complete duplicate rows.

### 2. Handling Invalid Values

Invalid `0` values were identified in medical features such as:

- `Cholesterol`
- `RestingBP`

These values were replaced using the calculated mean of their respective columns.

### 3. Categorical Encoding

Categorical variables were converted into numerical representations using **One-Hot Encoding**.

### 4. Feature Scaling

Numerical features were standardized using Scikit-Learn's `StandardScaler`.

Scaled features include:

- Age
- RestingBP
- Cholesterol
- MaxHR
- Oldpeak

---

## 🤖 Machine Learning Model

### K-Nearest Neighbors (KNN)

The project uses the **K-Nearest Neighbors (KNN)** classification algorithm to predict the target class.

The trained model is saved as:

```text
KNN_heart_project.pkl
The preprocessing objects are also saved for consistent prediction:

scaler.pkl
columns.pkl

This allows the deployed application to use the same preprocessing pipeline that was used during model development.

🌐 Streamlit Web Application

The Machine Learning model was integrated into an interactive Streamlit application.

User Inputs

The application accepts clinical parameters such as:

Age
Sex
Resting Blood Pressure
Cholesterol
Fasting Blood Sugar
Chest Pain Type
Resting ECG
Maximum Heart Rate
Exercise-Induced Angina
Oldpeak
ST Slope

The application processes the input, applies the saved preprocessing pipeline, and passes the transformed data to the trained KNN model.

Prediction Flow
User Input
    ↓
Create Input DataFrame
    ↓
Match Expected Features
    ↓
Feature Scaling
    ↓
KNN Model
    ↓
Prediction
    ↓
Streamlit Result


🎨 Application Preview
The application provides a clean dashboard-style interface with:

Patient input controls
Clinical parameter sections
KNN model information
Prediction button
Prediction result display

🧰 Tech Stack
Programming Language
Python
Data Analysis & Visualization
Pandas
NumPy
Matplotlib
Seaborn
Machine Learning
Scikit-Learn
K-Nearest Neighbors
StandardScaler
Model Persistence
Joblib
Frontend / Deployment
Streamlit
Streamlit Community Cloud

📁 Project Structure
heart-disease-prediction/
│
├── app.py
├── heart.csv
├── Heart.ipynb
├── KNN_heart_project.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
└── README.md

🚀 Run Locally
1. Clone the repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
2. Navigate to the project directory
cd heart-disease-prediction
3. Install dependencies
pip install -r requirements.txt
4. Run the Streamlit application
streamlit run app.py

The application will open in your browser.

📦 Requirements
The project uses the following Python libraries:
streamlit
pandas
scikit-learn
joblib
numpy


💡 Key Insights from EDA

Some notable observations from the exploratory analysis include:

The dataset has a relatively balanced distribution of the target variable.
Several records contained 0 values for medical measurements such as cholesterol.
Features such as Exercise Angina, Oldpeak, and ST Slope showed notable relationships with the target variable.
Maximum heart rate and ST Slope also showed inverse relationships with the presence of heart disease.


🔮 Future Improvements

Potential improvements for future versions:

Compare multiple classification algorithms
Perform hyperparameter tuning
Add model evaluation metrics to the dashboard
Add probability/confidence visualization
Improve input validation
Add interactive EDA visualizations to the Streamlit application
Improve UI/UX and responsive design
Add model explainability using techniques such as SHAP

👨‍💻 Author
Rahul

Built as a Machine Learning and Data Analytics project to explore the complete journey from raw data analysis to a deployed ML application.

⭐ Support

If you found this project interesting, consider giving the repository a ⭐ on GitHub.

