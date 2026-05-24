import streamlit as st
import time as t

st.title("Ramya")
st.header("weather APP")
st.subheader("Can I tell!!")

st.text("Hello user!!")
st.write("temperature:",20)
st.markdown("### hello")
st.success("Login successful")
st.error("Invalid password")
st.warning("Low battery!!")

st.info("Server running")

#input widgets

name=st.text_input("Enter Name:")

desc=st.text_area("Enter description:")

age=st.number_input("Enter your age:")

if st.button("Submitted"):
    st.text("Submitted!!")

# check box :True/false
agree=st.checkbox("I agree")

# radio Button:Choose one option
gender=st.radio("Select Gender",["male","Female"])

#select box : drop down selection
city=st.selectbox("Choose city",["Bangalore","Mysore"])

# multiselect:select multiple options
skills=st.multiselect("Skills",["Python","java","C"])

#slider :select value by sliding:
age=st.slider("select age",1,60)

#select slider:slider between text option
level=st.select_slider("Level",["Begineer","Intermediate","Advance"])

date=st.date_input("select date")

time=st.date_input("Select time")

file=st.file_uploader("Upload file")

photo=st.camera_input("Take photo")

#side bar
st.sidebar.title("menu")
col1,col2=st.columns(2)
with col1:
    st.write("Column1")
with col2:
    st.write("Column 2")

tab1,tab2=st.tabs(["Home","Profile"])

#spinner:Show loading animation
with st.spinner("Loading....."):
    t.sleep(3)

st.balloons()
st.snow()