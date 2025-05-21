import streamlit as st
import pandas as pd
from utils.analyzer import get_stats, plot_histograms
from utils.admission import calculate_percentile
from utils.dropout import train_and_predict

st.set_page_config(page_title="Student Insights Suite", layout="wide")
st.sidebar.title("🎓 Student Insights Suite")
app_choice = st.sidebar.radio("Choose Tool:", ["📊 Score Analyzer", "📈 Admission Estimator", "🌳 Dropout Predictor"])

if app_choice == "📊 Score Analyzer":
    st.title("📊 Student Score Analyzer")
    uploaded_file = st.file_uploader("Upload CSV of student scores", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.subheader("Data Preview")
        st.dataframe(df.head())
        st.subheader("Descriptive Statistics")
        st.dataframe(get_stats(df))
        st.subheader("Histograms")
        for fig in plot_histograms(df):
            st.pyplot(fig)

elif app_choice == "📈 Admission Estimator":
    st.title("📈 College Admission Percentile Estimator")
    score_input = st.number_input("Enter your entrance score", min_value=0.0)
    dataset_file = st.file_uploader("Upload CSV of all entrance scores", type="csv")
    if score_input and dataset_file:
        scores_df = pd.read_csv(dataset_file)
        if 'Score' in scores_df.columns:
            percentile = calculate_percentile(score_input, scores_df['Score'])
            st.success(f"Your score is higher than {percentile}% of applicants.")
        else:
            st.error("CSV must contain a 'Score' column.")

elif app_choice == "🌳 Dropout Predictor":
    st.title("🌳 Student Dropout Prediction Tool")
    dropout_file = st.file_uploader("Upload training data (CSV)", type="csv")
    if dropout_file:
        df = pd.read_csv(dropout_file)
        if 'Dropout' in df.columns:
            st.subheader("Enter Student Data to Predict:")
            input_vals = []
            for col in df.drop(columns=['Dropout']).columns:
                val = st.number_input(f"{col}", value=0.0)
                input_vals.append(val)
            if st.button("Predict Dropout"):
                pred, fig = train_and_predict(df, input_vals)
                st.write(f"Prediction: {'Dropout' if pred==1 else 'Continue'}")
                st.pyplot(fig)
        else:
            st.error("CSV must include a 'Dropout' column for training.")
