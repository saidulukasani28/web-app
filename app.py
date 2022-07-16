import streamlit as st
import joblib
model = joblib.load('C:\Users\DELL\Downloads\trained_model (1).sav')
st.title('Diabetic Prediction')
Pragnencies = st.text_input('no.of Pragnencies')
Glucose = st.text_input('Glucose level')
BloodPressure = st.text_input('BloodPressure value')
Skinthickness = st.text_input('Skin thickness value')
Insulin = st.text_input('Insulin level')
BMI = st.text_input('BMI value')
DiabeticPedigreefunction = st.text_input('DiabeticPedigreefunction value')
Age = st.text_input('Age of the person')
diagnosis = ''
if st.button('Diabetic test result')
 diagnosis = diabetic_prediction([Pragnencies,Glucose,BloodPressure,Skinthickness,Insulin,BMI,DiabeticPedigreefunction,Age])
 st.success(diagnosis)
