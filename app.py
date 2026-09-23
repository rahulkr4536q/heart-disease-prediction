import streamlit as st
import pandas as pd
import joblib

# Page Configuration
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        height: 50px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #d32f2f;
        color: white;
    }
    .card {
        padding: 20px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Load Model, Scaler, and Columns
@st.cache_resource
def load_assets():
    model = joblib.load("KNN_heart_project.pkl")
    scaler = joblib.load("scaler.pkl")
    expected_columns = joblib.load("columns.pkl")
    return model, scaler, expected_columns

model, scaler, expected_columns = load_assets()

# Sidebar Info
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=400&auto=format&fit=crop&q=60", use_container_width=True)
    st.markdown("### About the App")
    st.info("This application uses a Machine Learning model (**K-Nearest Neighbors**) to predict the risk of heart disease based on clinical parameters.")
    st.markdown("---")
    st.markdown("Developed with ❤️ by **Rahul**")

# Main Title Header
st.title("❤️ Heart Disease Risk Prediction Dashboard")
st.markdown("Please fill out the patient's medical parameters below to evaluate the risk score.")

st.markdown("---")

# Input Layout using Columns
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("#### 👤 Patient Demographics & Vitals")
    age = st.slider("Age", 18, 100, 30, help="Age of the patient in years")
    sex = st.selectbox("Sex", ['M', 'F'])
    resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    cholesterol = st.number_input("Cholesterol Level (mg/dl)", 100, 600, 200)
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1], format_func=lambda x: "Yes (> 120 mg/dl)" if x==1 else "No (<= 120 mg/dl)")

with col2:
    st.markdown("#### 🩺 Cardiac & Clinical Tests")
    chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"], format_func=lambda x: {
        "ATA": "Atypical Angina (ATA)",
        "NAP": "Non-Anginal Pain (NAP)",
        "TA": "Typical Angina (TA)",
        "ASY": "Asymptomatic (ASY)"
    }[x])
    resting_ecg = st.selectbox("Resting ECG Results", ["Normal", "ST", "LVH"])
    max_hr = st.slider("Max Heart Rate Achieved", 60, 220, 150)
    exercise_angina = st.selectbox("Exercise-Induced Angina", ['Y', 'N'], format_func=lambda x: "Yes" if x=='Y' else "No")
    oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

st.markdown("<br>", unsafe_allow_html=True)

# Prediction Section
if st.button("🔮 Predict Heart Disease Risk"):
    with st.spinner("Analyzing medical parameters... Please wait."):
        raw_input = {
            'Age' : age,
            'RestingBP' : resting_bp,
            'Cholesterol' : cholesterol,
            'FastingBS' : fasting_bs,
            'MaxHR' : max_hr,
            'OldPeak' : oldpeak,
            'Sex_' + sex : 1,
            'ChestPainType_' + chest_pain : 1,
            'RestingECG_' + resting_ecg : 1,
            'ExerciseAngina_' + exercise_angina : 1,
            'ST_Slope_' + st_slope: 1
        }
        
        input_df = pd.DataFrame([raw_input])

        # Fill missing columns with 0
        for col in expected_columns:
            if col not in input_df.columns:
                input_df[col] = 0

        input_df = input_df[expected_columns]

        # Scale and Predict
        scaled_input = scaler.transform(input_df)
        prediction = model.predict(scaled_input)[0]

        st.markdown("---")
        st.subheader("📊 Prediction Results")

        if prediction == 1:
            st.error("### ⚠️ HIGH RISK Of Heart Disease Detected")
            st.warning("The model indicates a high probability of heart disease. It is strongly advised to consult a cardiologist immediately for professional diagnosis.")
        else:
            st.success("### ✅ LOW RISK Of Heart Disease")
            st.info("The model indicates a low risk profile. Maintain a healthy lifestyle, regular checkups, and a balanced diet!")
    
