import streamlit as st
from src.predict import predict_candidate

st.title("Resume Screening System")

st.write("Enter candidate details:")

years = st.number_input("Years of Experience", 0, 50)
skills = st.number_input("Skills Match Score", 0.0, 100.0)
education = st.selectbox("Education Level", ["High School", "Bachelors", "Masters"])
projects = st.number_input("Project Count", 0, 50)
length = st.number_input("Resume Length", 0, 2000)
github = st.number_input("GitHub Activity", 0, 1000)

if st.button("Predict"):

    edu_map = {
        "High School": 0,
        "Bachelors": 1,
        "Masters": 2
    }
    data = {
        "years_experience": years,
        "skills_match_score": skills,
        "education_level": edu_map[education],
        "project_count": projects,
        "resume_length": length,
        "github_activity": github
    }
    result = predict_candidate(data)
    
    st.success(result)