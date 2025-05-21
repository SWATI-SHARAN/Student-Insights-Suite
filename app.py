import streamlit as st
import pandas as pd
from PIL import Image
from utils.analyzer import get_stats, plot_histograms
from utils.admission import calculate_percentile
from utils.dropout import train_and_predict

# --- MUST BE FIRST STREAMLIT COMMAND ---
st.set_page_config(page_title="Student Insights Suite", page_icon="logo.png", layout="wide")

# --- CUSTOM CSS FOR SIDEBAR STYLING ---
st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            font-size: 18px;
        }
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            font-size: 24px;
            font-weight: bold;
            color: #1f77b4;
        }
        section[data-testid="stSidebar"] label {
            font-size: 18px;
            font-weight: 600;
        }
        section[data-testid="stSidebar"] .stSlider > div[data-baseweb="slider"] {
            padding-top: 20px;
            padding-bottom: 20px;
        }
        section[data-testid="stSidebar"] .stSlider span {
            font-size: 16px !important;
        }
        section[data-testid="stSidebar"] {
            background-color: #f0f4f8;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR FILTERS ---
with st.sidebar:
    st.title("📊 Filters")
    st.selectbox("Choose Department", ["IT", "CS", "ECE"])
    st.slider("Select Year", 1, 4, 2)
    st.text_input("Enter Student Name")

# --- MAIN HEADER ---
st.header("Student Insights")
st.write("Adjust filters from the sidebar to refine student analytics.")

# --- LOAD LOCAL CSS ---
def local_css(path):
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/custom_style.css")  # Optional custom styling

# --- HEADER (LOGO + TITLE) ---
col1, col2 = st.columns([1, 6])
with col1:
    st.image("logo.png", width=170)
with col2:
    st.markdown("<h1 style='margin-top: 5px;'>Student Insights Suite</h1>", unsafe_allow_html=True)
    st.markdown("Analyze Scores • Estimate Admission Percentiles • Predict Dropouts")

st.write("---")

# --- NAVIGATION MENU ---
st.sidebar.title("🧭 Navigation")
option = st.sidebar.radio("Choose Tool", [
    " Score Analyzer",
    " Admission Estimator",
    " Dropout Predictor"
])

# --- TOOL: Score Analyzer ---
if option == " Score Analyzer":
    st.subheader(" Student Score Analyzer")
    st.info("Upload a marks CSV with subject scores (e.g., Math, Science, English).")
    uploaded_file = st.file_uploader("Upload CSV of student scores", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.subheader(" Data Preview")
        st.dataframe(df.head())
        st.subheader(" Descriptive Statistics")
        st.dataframe(get_stats(df))
        st.subheader(" Histograms")
        for fig in plot_histograms(df):
            st.pyplot(fig)

# --- TOOL: Admission Estimator ---
elif option == " Admission Estimator":
    st.subheader(" College Admission Percentile Estimator")
    st.info("Upload entrance exam scores to calculate percentile rankings.")
    score_input = st.number_input("Enter your entrance score", min_value=0.0)
    dataset_file = st.file_uploader("Upload CSV of all entrance scores", type="csv")
    if score_input and dataset_file:
        scores_df = pd.read_csv(dataset_file)
        if 'Score' in scores_df.columns:
            percentile = calculate_percentile(score_input, scores_df['Score'])
            st.success(f" Your score is higher than {percentile}% of applicants.")
        else:
            st.error("CSV must contain a 'Score' column.")

# --- TOOL: Dropout Predictor ---
elif option == " Dropout Predictor":
    st.subheader(" Student Dropout Prediction Tool")
    st.info("Upload student data to train a decision tree and predict dropout likelihood.")
    dropout_file = st.file_uploader("Upload training data (CSV)", type="csv")
    if dropout_file:
        df = pd.read_csv(dropout_file)
        if 'Dropout' in df.columns:
            st.subheader(" Enter Student Data to Predict:")
            input_vals = []
            for col in df.drop(columns=['Dropout']).columns:
                val = st.number_input(f"{col}", value=0.0)
                input_vals.append(val)
            if st.button(" Predict Dropout"):
                pred, fig = train_and_predict(df, input_vals)
                st.success(f"Prediction: **{'Dropout' if pred==1 else 'Continue'}**")
                st.pyplot(fig)
        else:
            st.error("CSV must include a 'Dropout' column for training.")
