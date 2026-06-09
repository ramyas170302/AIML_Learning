import streamlit as st
import time as time
import Loan

st.header("🏦 Smart Loan Approval Predictor")
st.markdown(" ##### Predict whether a loan application is likely to be approved based on applicant details.")

col1,col2,col3=st.columns(3)

with col1:
    st.markdown("### 📋 Applicant Information Section")
    depe=st.number_input("Dependents",min_value=0,max_value=10,step=1)
    edu=st.selectbox("Eduction",["Graduate","Not Graduate"])
    if edu=="Graduate":
        edu=1
    else:
        edu=0
    Self_em=st.selectbox("Self Employed",["Yes","No"])
    if Self_em=="Yes":
        Self_em=1
    else:
        Self_em=0

with col2:
    st.markdown("### 💰 Financial Information Section")
    Annu_Income=st.number_input("Annual Income",value=400000)
    Loan_Amt=st.number_input("Loan Amount",max_value=10000000,min_value=0)
    Loan_Term=st.slider("Loan Term",min_value=1,max_value=20)
    CIBIL_score=st.slider("CIBIL Score",min_value=300,max_value=900)

with col3:
    st.markdown("### 🏠 Asset Information Section")
    res_ass_value=st.number_input("residential_assets_value",min_value=0,value=1000000)
    commercial_assets = st.number_input("Commercial Assets Value",min_value=0,value=500000)
    luxury_assets = st.number_input("Luxury Assets Value",min_value=0,value=1000000)
    bank_assets = st.number_input("Bank Asset Value",min_value=0,value=500000)

new_data=[[depe,edu,Self_em,Annu_Income,Loan_Amt,Loan_Term,CIBIL_score,
          res_ass_value,commercial_assets,luxury_assets,bank_assets]]
if st.button("Predict Loan Status"):
    st.divider()
    with st.spinner("Loading...."):
        time.sleep(2)
        predict = Loan.model.predict(new_data)
        res = predict[0]
        if res==1:
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Rejected")

