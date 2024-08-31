# pages/employee/self_assessment.py
import streamlit as st

def show_self_assessment_page():
    st.title("Self-Assessment")
    
    # Example list of available question banks (to be dynamically loaded)
    available_question_banks = ["Python Basics", "Advanced Java", "SQL Fundamentals"]
    
    selected_bank = st.selectbox("Select Question Bank", available_question_banks)
    
    if st.button("Download"):
        st.success(f"{selected_bank} question bank downloaded successfully.")

    # Example assessment completion status
    st.progress(50, text="Assessment completion status: 50%")

if __name__ == "__main__":
    show_self_assessment_page()
