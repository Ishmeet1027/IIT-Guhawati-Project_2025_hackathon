import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('nhanes_age_group_model.pkl')

# ✅ Set page layout and sidebar state
st.set_page_config(
    page_title="NHANES Age Group Predictor",
    layout="wide",  # 👈 makes content full-width
    initial_sidebar_state="expanded"  # 👈 keeps sidebar open
)

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("📊 Prediction Menu")
option = st.sidebar.radio("Select Mode", ["🏠 Home", "🧍 Individual Prediction", "📁 Batch Prediction"])

# -----------------------------
# Header
# -----------------------------
st.markdown("""
    <h1 style='text-align: center; font-size: 42px;'>NHANES Age Group Prediction</h1>
    <hr style='margin-top: 10px; margin-bottom: 25px;'>
""", unsafe_allow_html=True)

# -----------------------------
# Home Screen Message
# -----------------------------
if option == "🏠 Home":
    st.markdown("""
        <div style='text-align: center; font-size: 20px; padding: 30px 20px;'>
            👋 Welcome to the NHANES Age Group Predictor!<br><br>
            Please select a prediction mode from the <b>left sidebar</b>:<br><br>
            🔹 <b>Individual Prediction</b> – Enter data manually<br>
            📁 <b>Batch Prediction</b> – Upload a CSV for bulk prediction<br><br>
            Get insights instantly! 🧠
        </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Individual Prediction
# -----------------------------
elif option == "🧍 Individual Prediction":
    st.markdown("<h2 style='color:#4CAF50;'>Enter Individual Data</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        RIDAGEYR = st.number_input("🧓 Age in Years (RIDAGEYR)", min_value=0, max_value=120, value=30)
        RIAGENDR = st.selectbox("⚥ Gender (RIAGENDR)", options=[1.0, 2.0], format_func=lambda x: "Male" if x == 1.0 else "Female")
        PAQ605 = st.number_input("🏃 Physical Activity (PAQ605)", min_value=0.0, max_value=10.0, value=2.0)
        BMXBMI = st.number_input("⚖️ BMI (BMXBMI)", min_value=0.0, max_value=100.0, value=25.0)

    with col2:
        LBXGLU = st.number_input("🩸 Glucose Level (LBXGLU)", min_value=0.0, max_value=500.0, value=100.0)
        DIQ010 = st.selectbox("🩺 Diabetes Status (DIQ010)", options=[1, 2])
        LBXGLT = st.number_input("📈 Glucose Tolerance (LBXGLT)", min_value=0.0, max_value=500.0, value=100.0)
        LBXIN = st.number_input("🧪 Insulin Level (LBXIN)", min_value=0.0, max_value=500.0, value=10.0)

    input_dict = {
        'RIDAGEYR': [RIDAGEYR],
        'RIAGENDR': [RIAGENDR],
        'PAQ605': [PAQ605],
        'BMXBMI': [BMXBMI],
        'LBXGLU': [LBXGLU],
        'DIQ010': [DIQ010],
        'LBXGLT': [LBXGLT],
        'LBXIN': [LBXIN]
    }

    input_df = pd.DataFrame(input_dict)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔍 Predict Age Group", use_container_width=True):
        prediction = model.predict(input_df)[0]
        label = "Senior" if prediction == 1 else "Adult"
        st.success(f"✅ **Predicted Age Group**: {label} (Label: {prediction})")

# -----------------------------
# Batch Prediction
# -----------------------------
elif option == "📁 Batch Prediction":
    st.markdown("<h2 style='color:#2196F3;'>Upload CSV for Batch Prediction</h2>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("📤 Upload a CSV file with the required columns", type=["csv"])

    required_cols = ['RIDAGEYR', 'RIAGENDR', 'PAQ605', 'BMXBMI', 'LBXGLU', 'DIQ010', 'LBXGLT', 'LBXIN']

    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        if all(col in df.columns for col in required_cols):
            predictions = model.predict(df[required_cols])
            df['Predicted_Label'] = predictions
            df['Age_Group'] = df['Predicted_Label'].apply(lambda x: "Senior" if x == 1 else "Adult")

            st.markdown("### 🔎 Prediction Results Preview")
            st.dataframe(df[['Predicted_Label', 'Age_Group']].head(10), use_container_width=True)

            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("⬇️ Download Full Predictions CSV", csv, file_name="age_group_predictions.csv", mime='text/csv')
        else:
            st.error(f"❌ The uploaded file is missing required columns: {', '.join(required_cols)}")