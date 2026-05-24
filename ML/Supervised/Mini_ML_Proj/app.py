import streamlit as st
import pandas as pd
import model as model
import time 

st.image("ML/Supervised/Mini_ML_Proj/logo.png", width=200)

st.sidebar.header("🤖 Algorithm")
st.sidebar.write("Decision Tree Classifier")
st.sidebar.divider()

st.sidebar.header("💡 Daily Tips")
st.sidebar.write("✔ Sleep 7–8 hours")
st.sidebar.write("✔ Drink more water")
st.sidebar.write("✔ Reduce stress")
st.sidebar.write("✔ Exercise daily")
st.sidebar.divider()

st.sidebar.header("👩‍💻 Developed By")
st.sidebar.write("Ramya S")

st.sidebar.divider()
st.sidebar.caption("Developed using Machine Learning & Streamlit")

st.markdown(
    """
    <style>
    .stApp {
        background-color:white;
        color:black
    }
    hr {
        border-color: white;
    }
    label{
    color:black !important;
    font-weight:bold
    }

    button{
    color:white !important;
    }

    div.stButton > button:hover{
        background-color:blue;
        color:White;
    }

    .stSpinner > div {
    color: red !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)
st.header("🩺 Mental Health Risk Prediction System")
st.subheader("This AI-based system predicts mental health risk using lifestyle and behavioral patterns.")

col1,col2=st.columns(2)
with col1:


    sleepHours = st.number_input("😴 Sleep Hours", 2.0, 15.0, 7.0, 0.5)

    stress = st.selectbox("😟 Stress Level", ["Low", "Medium", "High"])

    if stress == "Low":
        stressLevel = 0
    elif stress == "Medium":
        stressLevel = 1
    else:
        stressLevel = 2

    screenTime = st.number_input("📱Screen Time per day", 1.0, 24.0, 5.0, 0.5)

    ExerciseHours = st.number_input("🏃 Exercise Hours Per day", 0.0, 10.0, 1.0, 0.5)


with col2:
    social=st.selectbox("👥 Social Interaction ",["Low","Medium","High"])

    if social=="Low":
        socialInteraction=0
    elif social=="Medium":
        socialInteraction=1
    else:
        socialInteraction=2

    waterIntake=st.number_input("💧 Water Intake Per Day (Litre)",1.0,4.0,1.0,0.3)

    work=st.selectbox("💼 Work Pressure",["Low","Medium","High"])

    if work=="Low":
        workPressure=1
    elif work=="Medium":
        workPressure=2
    else:
        workPressure=3

new_data = [[
    sleepHours,
    stressLevel,
    screenTime,
    ExerciseHours,
    socialInteraction,
    waterIntake,
    workPressure
]]

if st.button("Predict"):
    st.divider()
    with st.spinner("Loading...."):
        time.sleep(2)
        predict = model.model.predict(new_data)
        res = predict[0]

        if res == 1:
            st.error("⚠ Medium Risk Detected")
            st.write("Some lifestyle habits may require improvement.")
            st.write("Try reducing stress, limiting screen time, and improving sleep quality.")

        elif res == 2:
            st.error("🚨 High Risk Detected")
            st.write("Lifestyle patterns may negatively affect mental wellness.")
            st.write("Consider reducing workload, improving sleep, exercising regularly, and seeking support if needed.")

        else:
            st.success("✅ Low Risk Detected")
            st.write("Healthy lifestyle detected.")
            st.write("Sleep pattern and daily habits appear balanced.")
            st.write("Continue maintaining good routines and regular exercise.")




