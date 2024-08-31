# pages/trainer/generate_question_bank.py
import streamlit as st

def show_generate_question_bank_page():
    st.title("Generate Question Bank")
    
    technology = st.selectbox("Select Technology", ["Python", "Java", "JavaScript", "C++", "SQL"])
    topics = st.multiselect("Select Topics", ["Data Structures", "Algorithms", "OOP", "Databases", "Networking"])
    num_questions = st.number_input("Number of Questions", min_value=1, max_value=100, value=10)
    difficulty = st.slider("Difficulty Level", min_value=1, max_value=5, value=3)
    
    if st.button("Generate"):
        st.success(f"Question bank for {technology} with {num_questions} questions generated successfully.")

if __name__ == "__main__":
    show_generate_question_bank_page()
