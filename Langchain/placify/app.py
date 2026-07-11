import streamlit as st
import os
from langchain_helper import(
    generate_career,
    generate_interview,
    review_answer,
    generate_study_plan,
    process_pdf,
    ask_pdf,
    generate_company
)

st.set_page_config(
    page_title="Placify",
    layout="wide"
)


with st.sidebar:

    

    st.title("Placify")

    st.caption("Learn. Practice. Get Hired.")

    st.divider()

    st.write("## 📌 Features")

    st.write("🏠 Home")
    st.write("🛣 Career Roadmap")
    st.write("💻 Interview Q&A")
    st.write("✅ Answer Review")
    st.write("📅 Study Planner")

    st.divider()

    st.write("## ℹ️ About")

    st.info("""
Version: **1.0**

Built with:

- Streamlit
- LangChain
- Groq AI
""")

    st.divider()

    st.success(
        "💡 **Daily Motivation**\n\n"
        "*Small daily improvements lead to big career success.* 🚀"
    )



st.header("Placify")
st.caption("Learn. Practice. Get Hired.")

st.divider()

if "page" not in st.session_state:
    st.session_state.page = "home"

st.write("""
Prepare for placements with the help of AI.

✔ Career Roadmap

✔ Interview Question Generator

✔ Answer Evaluation

✔ Daily Study Planner
""")

st.divider()

st.write("## Choose a Feature")

col1, col2 ,col3 = st.columns(3)

with col1:
    if st.button("🛣 Career Roadmap"):
        st.session_state.page = "career"

    if st.button("💻 Interview Q&A"):
        st.session_state.page = "interview"

with col2:
    if st.button("✅ Answer Review"):
        st.session_state.page = "answer"

    if st.button("📅 Study Planner"):
        st.session_state.page = "study"
    
with col3:
    if st.button ("📚 Placement Knowledge"):
        st.session_state.page="Knowledge"

    if st.button ("🏢 Company Experience"):
        st.session_state.page="company"


# ------------------------------
# Career Roadmap Page
# ------------------------------

if st.session_state.page == "career":

    st.subheader("🛣 Career Roadmap")

    job = st.selectbox(
        "Select Role",
        ("AI Engineer", "Software Engineer", "Data Scientist")
    )

    package = st.selectbox(
        "Target Package",
        ("5 LPA", "8 LPA", "12 LPA", "20 LPA")
    )

    year = st.selectbox(
        "Graduation Year",
        ("2026", "2027", "2028")
    )

    skills = st.text_area(
        "Current Skills",
        placeholder="Example: Java, Python, SQL"
    )

    if st.button("🚀 Generate Career Roadmap"):

        st.success("Information Submitted Successfully!")

        st.write("### Student Details")

        st.write("🎯 Role :", job)
        st.write("💰 Package :", package)
        st.write("🎓 Graduation Year :", year)
        st.write("💻 Skills :", skills)
        st.write("\n")
        st.write(" ### Here is your Roadmap")
        if not skills:
            st.warning("Please enter your Current skills!!..")
        else:
            with st.spinner("Generating response..."):
                response=generate_career(
                                    job,
                                    package,
                                    year,
                                    skills
                                    )
            
            st.markdown(response)   

# ------------------------------
# Interview Q&A Page
# ------------------------------

if st.session_state.page=="interview":
    subject=st.text_input(
        "Subject",
        placeholder="Example:Java, DBMS , OS ,CN , SQL , DSA , Aptitude"
    )
    
    Level=st.selectbox(
        "Level",
        ("Easy","Intermediate","Hard")
    )
    
    interview_type=st.selectbox(
        "Type",
        ("Technical","HR","Behavioral")
    )

    Num=st.slider(
        "Number of Question",
        1, # min
        20, #max
        1  # step
    )

    company=st.text_input(
        "Target Company",
        placeholder="Eg:Google , Microsoft , Amazon, Wipro..etc"
    )

    question=st.selectbox(
        "Type Question",
        ("Theory","Coding","MCQ","Mixed")
    )

    if st.button("📑 Generate Question"):
       
        st.write(" ### you provide below info:")
        st.write("🎯 Subject:", subject)
        st.write("💰 Level :", Level)
        st.write("🎓 Interview Type :",interview_type)
        st.write("💻 Number of Questions :", Num)
        st.write("Target Company: ",company)
        st.write("Question Format:",question)
        if not subject:
            st.warning("please Enter Subject")
        else:
            with st.spinner("Generating response..."):
                response=generate_interview(
                                        subject=subject,
                                        level=Level,
                                        interview_type=interview_type,
                                        company=company,
                                        question_format=question,
                                        num_questions=Num
                                    )
            
            st.markdown(response)
# ------------------------------
# Answer Review Page
# ------------------------------

if st.session_state.page=="answer":
    question=st.text_area(
        "Enter Your Question"
    )

    user_answer=st.text_area(
        "Your Answer"
    )

    exp=st.selectbox(
        "Experience Level",
        ("Fresher","Beginner","Intermediate","Expert")
    )

    revi=st.selectbox(
        "Review Style",
        ("Detailed Feedback","Short Feedback","Score Only")
    )

    if st.button("📜 Review My Answer"):
        if not question:
            st.warning("Please enter the question!!..")
        elif not user_answer:
            st.warning("Please enter Your answer. If you Don't Know atleast Try , I will Correct!!!")
        else:
            
            with st.spinner("Generating response..."):
                response=review_answer(
                    question=question,
                    user_answer=user_answer,
                    experience_level=exp,
                    review_style=revi
                )
            
            st.markdown(response)


# ------------------------------
#  Daily Study Planner Page
# ------------------------------

if st.session_state.page=="study":
    target=st.selectbox(
        "Target Role",
        ("AI Engineer","Software Engineer","Data Scientist","Web Developer")
    )

    current_skills=st.text_area(
        "Current Skills",
        placeholder="Eg:Java, Python, SQL, Basic DSA"
    )

    hr=st.slider(
        "Study Hours Per Day",
        1,
        8,
        1
    )

    day=st.slider(
        "Days Available",
        7,
        90,
        1
    )

    current_year=st.selectbox(
        "Current Year",
        ("1st Year","2nd Year","3rd Year","4th Year","Graduate")
    )

    focus_area=st.text_area("Subject",
                            placeholder="Subject You Need to Learn")

    if st.button("🛣️ Generate Study Plan"):
        if not focus_area:
            st.warning("Please Enter subject You need to Learn!!!")
        elif not current_skills:
            st.warning("Please enter your current skills.!!")
        else:
            with st.spinner("Generating response..."):
                response=generate_study_plan(target_role=target,
                                            current_skills=current_skills,
                                            study_hours=hr,
                                            days_available=day,
                                            current_year=current_year,
                                            focus_areas=focus_area
                                            )
            
            st.markdown(response)


# ------------------------------
# Placement Knowledge Page
# ------------------------------

if st.session_state.page =="Knowledge":
    uploaded_file=st.file_uploader(
                "📄 Upload your placement notes (pdf)",
                type=["pdf"]
            )
   
    
    if uploaded_file is not None:
            st.success("✅ File uploaded successfully!")
            st.write(" #### Uploaded file:")
            st.write(uploaded_file.name)
            question=st.text_area(
                "Ask Your Question:",
                placeholder="Example:What is DeadLock?"
                )
            if st.button("Get Answer"):
                if question:
                    process_pdf(uploaded_file)
                    answer=ask_pdf(question=question)
                    st.markdown(answer)
                else:
                    st.warning("Please enter the question!")
    else:
        st.info("Please Upload a file to continue...")   


# ------------------------------
# company experience Page
# ------------------------------
           

if st.session_state.page=="company":
    company=st.text_area("Enter the company name",
                         placeholder="eg:google,microsoft,wipro")
    role=st.text_area("enter your preparing role",
                      placeholder="eg:AI engineer,Web Developer")

    question=st.selectbox(
        "What do You Want To know?",
        ("Interview Process","DSA Coding","HR Question",
         "Tecnical Subject","AI/LLM Topic","Projects Expected","Resume Tips",
         "Salary & Package")
    )
    if st.button("submit"):
        if not company:
            st.warning("please enter the comapny")
        elif not role:
            st.warning("please enter the role")
        elif not question:
            ("please enter the question !!")
        else:
            with st.spinner("generating Response...."):
                fun=generate_company(company=company,
                                role=role,
                                question=question)
                st.markdown(fun)