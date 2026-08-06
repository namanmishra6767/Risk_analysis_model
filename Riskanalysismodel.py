import streamlit as st
import pandas as pd
import joblib

model = joblib.load('Riskmodel1.impynb')

st.title = "Healthcare Risk Stratification"
age = st.number_input("Age", min_value=0)
lengthofstay = st.number_input("Length of stay (days)", min_value=0)
treatment_cost = st.number_input("Treatment cost", min_value=0.0)

if st.button('Predict'):
    input_data = pd.DataFrame(
        [[age, lengthofstay, treatment_cost]],
        columns=['Age', 'Lengthofstay', 'TreatmentCost'])
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.write(f"Risk Prediction: {'High Risk' if prediction == 1 else 'Low Risk'}")
    st.write(f"Risk Probability: {round(probability, 2)}")

