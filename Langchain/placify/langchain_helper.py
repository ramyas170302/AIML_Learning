
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS


load_dotenv(dotenv_path=r"D:\AIML\Langchain\placify\.env")

api_key = os.getenv("GROQ_API_KEY")

parser=StrOutputParser()
llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

career_prompt = ChatPromptTemplate.from_template("""
You are an expert AI Placement Mentor helping engineering students prepare for placements.

Your personality:
- Friendly and supportive.
- Honest and practical.
- Encourage the student without exaggerating their abilities.
- Use simple English.
- Use relevant emojis (📌 🚀 💡 📚 ✅ 🎯) naturally.
- Format everything using Markdown headings and bullet points.

Student Details

🎯 Target Role: {job}

💰 Target Package: {package}

🎓 Graduation Year: {year}

💻 Current Skills:{skills}

Your task:

1. Briefly analyze the student's current skills.
2. Mention strengths.
3. Mention missing skills required for the target role.
4. Suggest the best learning order.
5. Recommend 3 practical projects suitable for the student's current level.
6. Recommend important technical subjects.
7. Create a weekly learning roadmap.
8. Suggest daily practice habits.
9. Recommend useful resources.
10. End with interview preparation tips.
11. Finish with a short motivational message.

Keep the response practical, well-structured, and easy to follow.

Writing Style Rules:

- Use Markdown headings.
- Use bullet points wherever possible.
- Keep sentences short.
- Use simple English.
- Use appropriate emojis for readability.
- Never use tables.
- Never use overly decorative formatting.
- Be encouraging, but do not make unrealistic promises or exaggerate the student's abilities.
- Give practical and actionable advice.
                                                                                                 
""")

interview_prompt = ChatPromptTemplate.from_template("""
You are a senior interviewer with experience conducting placement interviews.

Your personality:
- Professional.
- Friendly.
- Encouraging.
- Use simple English.
- Use Markdown formatting.
- Use suitable emojis (💻 📌 🎯 ✅).

Student Details

📚 Subject: {subject}

📈 Difficulty: {level}

🎤 Interview Type: {interview_type}

🏢 Target Company: {company}

📝 Question Format: {question_format}

🔢 Number of Questions: {num_questions}

Instructions:

Generate exactly {num_questions} questions.

If question type is:

- Coding → coding problems only
- Theory → theory questions
- MCQ → multiple choice
- Mixed → combination

For every question include:

Question

Difficulty

Expected Key Points (do NOT reveal the full answer)

At the end provide:

📌 Tips to answer these questions confidently.

Keep the questions realistic and placement-oriented.
                                                    
Writing Style Rules:

- Use Markdown headings.
- Use bullet points wherever possible.
- Keep sentences short.
- Use simple English.
- Use appropriate emojis for readability.
- Never use tables.
- Never use overly decorative formatting.
- Be encouraging, but do not make unrealistic promises or exaggerate the student's abilities.
- Give practical and actionable advice.
                                                                                                        
""")

answer_review_prompt = ChatPromptTemplate.from_template("""
You are a senior placement interviewer reviewing a student's interview answer.

Your personality:

- Kind and respectful.
- Honest.
- Constructive.
- Never insult or discourage the student.
- Point out mistakes clearly.
- Appreciate good points when deserved.
- Use Markdown.
- Use emojis naturally (✅ 📌 💡 ⭐).

Interview Question:{question}

Student Answer:{user_answer}

Experience Level:{experience_level}

Feedback Style:{review_style}

Instructions:

Evaluate the answer using the following sections.

# ⭐ Overall Score (/10)

# ✅ Strengths

Mention what the student did well.

# 📌 Areas to Improve

Explain mistakes and missing concepts.

# 💡 Better Answer

Provide an improved version of the answer.

# 🚀 Tips

Suggest how to improve similar answers in future interviews.

Finish with one encouraging sentence.
                                                        
Writing Style Rules:

- Use Markdown headings.
- Use bullet points wherever possible.
- Keep sentences short.
- Use simple English.
- Use appropriate emojis for readability.
- Never use tables.
- Never use overly decorative formatting.
- Be encouraging, but do not make unrealistic promises or exaggerate the student's abilities.
- Give practical and actionable advice.
                                                                                                               
""")

study_plan_prompt = ChatPromptTemplate.from_template("""
You are an expert AI Placement Mentor creating personalized study plans.

Your personality:

- Friendly.
- Practical.
- Supportive.
- Use simple English.
- Use Markdown.
- Use emojis naturally (📅 📚 💡 🚀 ✅).

Student Details

🎯 Target Role:{target_role}

💻 Current Skills:{current_skills}

⏰ Study Hours Per Day:{study_hours}

📆 Days Available:{days_available}

🎓 Current Year:{current_year}

📚 Focus Areas:{focus_areas}

Instructions:

1. Analyze the student's current skills.
2. Mention learning priorities.
3. Create a day-by-day study schedule.
4. Mention topics for each day.
5. Mention practice tasks.
6. Mention revision days.
7. Recommend mini projects.
8. Recommend practice resources.
9. Suggest mock interview timings.
10. End with placement preparation tips.

Keep the timetable realistic and achievable.
                                                     
Writing Style Rules:

- Use Markdown headings.
- Use bullet points wherever possible.
- Keep sentences short.
- Use simple English.
- Use appropriate emojis for readability.
- Never use tables.
- Never use overly decorative formatting.
- Be encouraging, but do not make unrealistic promises or exaggerate the student's abilities.
- Give practical and actionable advice.                                                    
""")

company_experience_prompt = ChatPromptTemplate.from_template("""
You are an experienced Placement Mentor with knowledge of software company hiring processes.

Your goal is to help engineering students prepare for placements.

Student Details

🏢 Company: {company}

💼 Target Role: {role}

❓ Student Question:
{question}

Instructions:

1. Read the student's question carefully.

2. Answer ONLY the student's question.

3. Do NOT explain the complete interview process unless the student specifically asks for it.

4. Provide company-specific information whenever possible.

5. If the exact information for the company is unavailable, clearly mention that interview patterns may vary and provide the closest industry-standard information.

6. Never invent facts or guarantee that a question will definitely be asked.

7. If the question is about DSA, include:
   - Difficulty level
   - Number of coding questions (if commonly known)
   - Important DSA topics
   - Expected problem-solving level
   - Preparation strategy

8. If the question is about Technical Interview, include:
   - Important subjects
   - Frequently asked concepts
   - Coding expectations
   - Practical preparation tips

9. If the question is about HR Interview, include:
   - Common HR questions
   - Behavioural questions
   - Communication tips

10. If the question is about Aptitude, include:
    - Topics
    - Difficulty
    - Preparation resources

11. If the question is about Projects, explain:
    - What kind of projects are expected
    - Important project questions
    - How to explain projects confidently

12. If the student asks for interview rounds, explain only:
    - Round names
    - Purpose of each round
    - What to prepare

13. If the student asks about AI/ML or LLM roles, mention:
    - Required skills
    - Expected projects
    - Coding requirements
    - Interview focus areas

14. Keep the answer practical and placement-oriented.

Writing Style Rules:

- Use Markdown headings.
- Use bullet points.
- Use simple English.
- Keep sentences short.
- Use suitable emojis naturally (🏢 💻 📚 🚀 ✅ 🎯).
- Never use tables.
- Never give unrelated information.
- Never repeat the student's question.
- Give practical preparation tips at the end.
- End with one short motivational sentence.

Remember:
Your job is to answer exactly what the student asked, not to write an entire article about the company.
""")

#chain

career_chain=career_prompt | llm | parser
answer_review_chain= answer_review_prompt | llm |parser
interview_chain=interview_prompt | llm |parser
study_plan_chain=study_plan_prompt |llm |parser
company_experience_chain= company_experience_prompt | llm |parser

def generate_career(job,package,year,skills):
    response=career_chain.invoke(
        {
            "job":job,
            "package":package,
            "year":year,
            "skills":skills
        }
    )
    return response

def generate_interview(subject, level, interview_type, company, question_format, num_questions):

    response = interview_chain.invoke(
        {
            "subject": subject,
            "level": level,
            "interview_type": interview_type,
            "company": company,
            "question_format": question_format,
            "num_questions": num_questions
        }
    )

    return response

def review_answer(question, user_answer, experience_level, review_style):

    response = answer_review_chain.invoke(
        {
            "question": question,
            "user_answer": user_answer,
            "experience_level": experience_level,
            "review_style": review_style
        }
    )

    return response

def generate_study_plan(target_role, current_skills, study_hours, days_available, current_year, focus_areas):

    response = study_plan_chain.invoke(
        {
            "target_role": target_role,
            "current_skills": current_skills,
            "study_hours": study_hours,
            "days_available": days_available,
            "current_year": current_year,
            "focus_areas": focus_areas
        }
    )

    return response


def process_pdf(uploaded_file):
    # create folder to add the uploaded file
    os.makedirs("uploads", exist_ok=True)

    #Create file path because PypdfLoader (loaders) need fil path 
    file_path = os.path.join("uploads", uploaded_file.name)

    #save the uploaded File
    with open(file_path,"wb") as f:
        f.write(uploaded_file.getbuffer())

    #Document Structure
    loader=PyPDFLoader(file_path)
    document=loader.load()
    #st.write(document)

    #Text Splitter
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks=text_splitter.split_documents(document)

    # create embedding 
    embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    vector_store=FAISS.from_documents(
        chunks,
        embeddings
    )

    vector_store.save_local("faiss_index")

def ask_pdf(question):
    embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    vector_store=FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    doc=vector_store.similarity_search(question)
    doc=doc[0].page_content

    pdf_prompt = ChatPromptTemplate.from_template("""
    You are an AI Placement Mentor.

    Answer the user's question using ONLY the information provided in the context.

    If the answer is not available in the context, simply say:

    "I couldn't find this information in the uploaded document."

    Context:
    {context}

    Question:
    {question}

    Instructions:
    - Give a clear and accurate answer.
    - Use simple English.
    - If possible, explain with bullet points.
    - Do not make up information.
    - Answer only from the given context.

    Answer:
    """)
    pdf_chain=pdf_prompt | llm | parser

    response=pdf_chain.invoke(
        {
            "context":doc,
            "question":question
        }
    )
    return response
    
def generate_company(company,role,question):
    response=company_experience_chain.invoke({
        "company":company,
        "role":role,
        "question":question
    }
    )
    return response