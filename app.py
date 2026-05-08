import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('best_model.pkl','rb'))
scaler = pickle.load(open('sclaer.pkl','rb'))

st.header('Heart Disease Prediction')
st.subheader("Enter Patient Details:")

age = st.number_input("Age", 20, 100, 50)
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0,1])
cp = st.selectbox("Chest Pain Type (0-3)", [0,1,2,3])
trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
chol = st.number_input("Cholesterol", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 (1=True, 0=False)", [0,1])
restecg = st.selectbox("Rest ECG (0-2)", [0,1,2])
thalach = st.number_input("Max Heart Rate", 60, 220, 150)
exang = st.selectbox("Exercise Induced Angina", [0,1])
oldpeak = st.number_input("Oldpeak", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope (0-2)", [0,1,2])
ca = st.selectbox("Number of vessels (0-4)", [0,1,2,3,4])
thal = st.selectbox("Thal (1-3)", [1,2,3])

if st.button("Predict"):
    data = np.array([[age,sex,cp,trestbps,chol,fbs,restecg
                      ,thalach,exang,oldpeak,slope,ca,thal]])
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)

    if prediction[0]==1:
        st.error("⚠️ High Risk of Heart Disease")

    else:
        st.success("Low Risk of Heart Disease")
