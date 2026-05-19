import streamlit as st
import numpy as np
import pickle
import pandas as pd
from datetime import datetime
import os


def append_prediction_to_excel(df: pd.DataFrame, filename: str = "COVID_Predictions.xlsx"):
    """Append a prediction row to the Excel file, creating it if necessary."""
    if os.path.exists(filename):
        existing_df = pd.read_excel(filename)
        df = pd.concat([existing_df, df], ignore_index=True)

    df.to_excel(filename, index=False, engine="openpyxl")


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="COVID Vision AI",
    page_icon="🩺",
    layout="wide"
)

# =========================
# LOAD MODEL
# =========================
model_data = pickle.load(open("Model.pkl", "rb"))

if isinstance(model_data, dict):
    model = model_data["model"]
    scaler = model_data["scaler"]
else:
    model = model_data
    scaler = None

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(135deg,#fff7ed,#ffe4e6,#fef3c7);
    font-family: 'Poppins', sans-serif;
}

/* Hide Streamlit */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Main Heading */
.main-title{
    text-align:center;
    font-size:70px;
    font-weight:900;
    color:#7c2d12;
    margin-top:10px;
}

.sub-title{
    text-align:center;
    font-size:22px;
    color:#9a3412;
    margin-bottom:40px;
}

/* Sidebar */
.side-card{
    background:white;
    padding:25px;
    border-radius:25px;
    margin-bottom:20px;
    box-shadow:0 10px 25px rgba(0,0,0,0.08);
    border:2px solid #fed7aa;
}

/* Form Box */
.form-box{
    background:white;
    padding:35px;
    border-radius:30px;
    box-shadow:0 15px 35px rgba(0,0,0,0.08);
    border:2px solid #fde68a;
}

/* Inputs */
.stSelectbox div[data-baseweb="select"],
.stNumberInput input{
    background:#fff7ed !important;
    color:#7c2d12 !important;
    border-radius:15px !important;
    border:2px solid #fdba74 !important;
}

/* Labels */
label{
    color:#7c2d12 !important;
    font-weight:600 !important;
}

/* Button */
.stButton>button{
    width:100%;
    height:65px;
    border:none;
    border-radius:18px;
    background: linear-gradient(90deg,#f97316,#fb7185);
    color:white;
    font-size:22px;
    font-weight:bold;
    transition:0.3s;
    margin-top:25px;
}

.stButton>button:hover{
    transform:scale(1.02);
    box-shadow:0 10px 25px rgba(249,115,22,0.4);
}

/* Result Box */
.result-box{
    margin-top:30px;
    padding:30px;
    border-radius:25px;
    background:#fff7ed;
    border:2px solid #fdba74;
}

/* Feature Cards */
.feature-card{
    background:linear-gradient(135deg,#fff,#fff7ed);
    border-radius:20px;
    padding:20px;
    text-align:center;
    box-shadow:0 8px 20px rgba(0,0,0,0.05);
    border:1px solid #fed7aa;
}

/* Animation */
.fade{
    animation:fadeIn 1s ease;
}

@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(20px);
    }
    to{
        opacity:1;
        transform:translateY(0px);
    }
}

</style>
""", unsafe_allow_html=True)

# =========================
# LAYOUT
# =========================
left, right = st.columns([1,4])

# =========================
# SIDEBAR
# =========================
with left:

    st.markdown("""
    <div class="side-card fade">
        <h1 style="color:#ea580c;">🩺 COVID</h1>
        <h3 style="color:#9a3412;">VISION AI</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="side-card fade">
        <h2 style="color:#ea580c;">📋 About</h2>
        <p style="color:#7c2d12; line-height:1.8;">
        AI powered COVID analysis dashboard for smart healthcare prediction and patient monitoring.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="side-card fade">
        <h2 style="color:#ea580c;">⚡ Benefits</h2>
        <p style="color:#7c2d12; line-height:1.8;">
        ✔ Fast Prediction<br><br>
        ✔ Modern Dashboard<br><br>
        ✔ Smart AI Analysis<br><br>
        ✔ Accurate Results
        </p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# MAIN AREA
# =========================
with right:

    st.markdown('<div class="main-title">COVID VISION AI</div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-title">Next Generation Smart Health Prediction System</div>', unsafe_allow_html=True)

    # Feature Cards
    f1, f2, f3 = st.columns(3)

    with f1:
        st.markdown("""
        <div class="feature-card fade">
            <h2>⚡ Fast</h2>
            <p>Instant Prediction Results</p>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class="feature-card fade">
            <h2>🧠 AI Powered</h2>
            <p>Machine Learning Model</p>
        </div>
        """, unsafe_allow_html=True)

    with f3:
        st.markdown("""
        <div class="feature-card fade">
            <h2>📊 Accurate</h2>
            <p>Advanced Risk Analysis</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="form-box fade">', unsafe_allow_html=True)

    st.markdown("## 🧾 Patient Information")

    patient_name = st.text_input("PATIENT NAME", placeholder="Enter patient full name")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        age = st.number_input("AGE",1,100,25)
        sex = st.selectbox("SEX",["Female","Male"])
        diabetes = st.selectbox("DIABETES",["Yes","No"])
        asthma = st.selectbox("ASTHMA",["Yes","No"])

    with c2:
        pneumonia = st.selectbox("PNEUMONIA",["Yes","No"])
        obesity = st.selectbox("OBESITY",["Yes","No"])
        tobacco = st.selectbox("TOBACCO",["Yes","No"])
        icu = st.selectbox("ICU",["Yes","No"])

    with c3:
        copd = st.selectbox("COPD",["Yes","No"])
        hipertension = st.selectbox("HIPERTENSION",["Yes","No"])
        cardiovascular = st.selectbox("CARDIOVASCULAR",["Yes","No"])
        renal = st.selectbox("RENAL CHRONIC",["Yes","No"])

    with c4:
        patient_type = st.selectbox("PATIENT TYPE",["Outpatient","Inpatient"])
        intubed = st.selectbox("INTUBED",["Yes","No"])
        pregnant = st.selectbox("PREGNANT",["Yes","No"])
        other = st.selectbox("OTHER DISEASE",["Yes","No"])
    
    # Additional row for missing features
    c5, c6, c7 = st.columns(3)
    
    with c5:
        inmsupr = st.selectbox("IMMUNOCOMPROMISED",["Yes","No"])
    
    with c6:
        usmer = st.selectbox("USED HEALTHCARE SYSTEM",["Yes","No"])
    
    with c7:
        medical_unit = st.selectbox("MEDICAL UNIT",["Hospital","Clinic","Other"])

    # =========================
    # BUTTON
    # =========================
    if st.button("🚀 ANALYZE PATIENT"):
        
        if not patient_name.strip():
            st.error("⚠️ Please enter patient name to proceed.")
        else:
            features = np.array([[

                age,
                1 if sex=="Male" else 0,
                1 if usmer=="Yes" else 0,
                1 if medical_unit=="Hospital" else (2 if medical_unit=="Clinic" else 0),
                1 if pneumonia=="Yes" else 0,
                1 if diabetes=="Yes" else 0,
                1 if copd=="Yes" else 0,
                1 if asthma=="Yes" else 0,
                1 if inmsupr=="Yes" else 0,
                1 if hipertension=="Yes" else 0,
                1 if cardiovascular=="Yes" else 0,
                1 if obesity=="Yes" else 0,
                1 if renal=="Yes" else 0,
                1 if tobacco=="Yes" else 0,
                1 if icu=="Yes" else 0,
                1 if intubed=="Yes" else 0,
                1 if pregnant=="Yes" else 0,
                1 if other=="Yes" else 0,
                1 if patient_type=="Inpatient" else 0

            ]])

            if scaler is not None:
                features = scaler.transform(features)

            prediction = model.predict(features)[0]
            
            # Create prediction report
            risk_status = "HIGH COVID RISK" if prediction == 1 else "LOW COVID RISK"
            risk_level = "High" if prediction == 1 else "Low"

            st.markdown("""
            <div class="result-box fade">
            """, unsafe_allow_html=True)

            st.markdown("## 📈 Prediction Report")

            if prediction == 1:
                st.error("⚠️ HIGH COVID RISK DETECTED")
                st.warning("Immediate medical attention recommended.")
            else:
                st.success("✅ LOW COVID RISK")
                st.info("Patient condition appears stable.")

            st.markdown("</div>", unsafe_allow_html=True)
            
            # Save to Excel
            try:
                excel_file = "COVID_Predictions.xlsx"
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Create a dataframe with the prediction data
                report_data = {
                    'Timestamp': [timestamp],
                    'Patient Name': [patient_name],
                    'Age': [age],
                    'Sex': [sex],
                    'USMER': [usmer],
                    'Medical Unit': [medical_unit],
                    'Pneumonia': [pneumonia],
                    'Diabetes': [diabetes],
                    'COPD': [copd],
                    'Asthma': [asthma],
                    'Immunocompromised': [inmsupr],
                    'Hypertension': [hipertension],
                    'Cardiovascular': [cardiovascular],
                    'Obesity': [obesity],
                    'Renal Chronic': [renal],
                    'Tobacco': [tobacco],
                    'ICU': [icu],
                    'Intubed': [intubed],
                    'Pregnant': [pregnant],
                    'Other Disease': [other],
                    'Patient Type': [patient_type],
                    'Risk Level': [risk_level],
                    'Prediction': [risk_status]
                }
                
                report_df = pd.DataFrame(report_data)
                
                # Save to Excel using helper for append/create behavior
                append_prediction_to_excel(report_df, excel_file)

                st.success(f"✅ Report saved to {excel_file}")
                st.info(f"Patient: {patient_name} | Prediction: {risk_status}")

            except Exception as e:
                st.error(f"❌ Error saving to Excel: {str(e)}")

    st.markdown("</div>", unsafe_allow_html=True)