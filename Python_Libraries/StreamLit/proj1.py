# "

import streamlit as st
import time as t
from PyPDF2 import PdfReader
import matplotlib.pyplot as plt


st.header("🎯Smart Resume Checker")
st.markdown("#### Upload your resume and get skill analysis, resume score, and improvement suggestions.")

#upload resume
resume=st.file_uploader("Upload your Resume here",type=["pdf"])


if resume:
    with st.spinner("Uploading..."):
        t.sleep(2)
    st.success("✅ Resume uploaded successfully")


st.sidebar.subheader("Resume Score")
st.sidebar.subheader("Skill Analysis")
st.sidebar.subheader("Suggestions")
st.sidebar.divider()
st.sidebar.text("About:")
st.sidebar.text("Made with StreamLit")


score=0
recommendations = {
    "python": "Learn Python basics + small projects",
    "java": "Practice OOP concepts in Java",
    "html": "Learn HTML structure + forms",
    "css": "Practice styling + layouts",
    "c": "Understand programming fundamentals",
    "aws": "Learn cloud basics (EC2, S3)"
}
skills=["python","java","html","css","c","aws"]
if resume:
    pdf=PdfReader(resume)
    text=" "
    for page in pdf.pages:   
        page_text=page.extract_text()
        text+=page_text
    text=text.lower()
    
    col1,col2=st.columns(2)
    with col1:

        det_skill=[]
        for skill in skills:
            if skill in text:
                det_skill.append(skill)
        
        st.subheader("Missing Skills:")
        
        for item in skills:
            if item not in det_skill:
                st.warning(item)
        
        score=((len(det_skill)/len(skills))*100)
        score=round(score,2)
        st.metric("📊 Resume Score", f"{score}%")
        st.subheader("💡 Learning Suggestions")
        for m in skills:
            if m not in det_skill:
                st.info(f"{m.upper()}->{recommendations[m]}")

        #Rating system
        if score<50:
            st.warning("you are Beginner:You need to learn !!")
        elif score<85:
            st.info("you are Intermediate:Little efforts needed!!")
            
        else:
            st.success("you are Advanced: Maintan consistency")
        

    with col2:
    # graph
        fig,ax=plt.subplots()
        missing=len(skills)-len(det_skill)
        detected=len(det_skill)
        label=["Detected","Missing"]
        values=[detected,missing]
        ax.pie(values,labels=label,autopct="%1.1f%%",startangle=90)
        st.subheader("graph")
        st.pyplot(fig)
   
    




