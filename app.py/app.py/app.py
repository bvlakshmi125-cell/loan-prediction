app.py
import streamlit as st
import pandas as pd
import joblib

# =========================
# LOAD TRAINED MODEL
# =========================

model = joblib.load('loan_prediction_model.pkl')

# =========================
# APP TITLE
# =========================

st.title("Loan Prediction System")

st.write("Enter Applicant Details")

# =========================
# INPUT FIELDS
# =========================

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

married = st.selectbox(
    "Married",
    ["Yes", "No"]
)

dependents = st.selectbox(
    "Dependents",
    ["0", "1", "2", "3+"]
)

education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

self_employed = st.selectbox(
    "Self Employed",
    ["Yes", "No"]
)

applicant_income = st.number_input(
    "Applicant Income",
    min_value=0
)

coapplicant_income = st.number_input(
    "Coapplicant Income",
    min_value=0
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0
)

loan_amount_term = st.number_input(
    "Loan Amount Term",
    min_value=0
)

credit_history = st.selectbox(
    "Credit History",
    [1.0, 0.0]
)

property_area = st.selectbox(
    "Property Area",
    ["Urban", "Semiurban", "Rural"]
)

# =========================
# MANUAL ENCODING
# =========================

gender = 1 if gender == "Male" else 0

married = 1 if married == "Yes" else 0

education = 0 if education == "Graduate" else 1

self_employed = 1 if self_employed == "Yes" else 0

dependents_mapping = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3+": 3
}

dependents = dependents_mapping[dependents]

property_mapping = {
    "Urban": 2,
    "Semiurban": 1,
    "Rural": 0
}

property_area = property_mapping[property_area]

# =========================
# CREATE DATAFRAME
# =========================

input_data = pd.DataFrame([[
    gender,
    married,
    dependents,
    education,
    self_employed,
    applicant_income,
    coapplicant_income,
    loan_amount,
    loan_amount_term,
    credit_history,
    property_area
]], columns=[
    'Gender',
    'Married',
    'Dependents',
    'Education',
    'Self_Employed',
    'ApplicantIncome',
    'CoapplicantIncome',
    'LoanAmount',
    'Loan_Amount_Term',
    'Credit_History',
    'Property_Area'
])

# =========================
# PREDICTION
# =========================

if st.button("Predict Loan Status"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Loan Approved")

    else:
        st.error("Loan Rejected")