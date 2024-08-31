# pages/employee/request_question_bank.py
import streamlit as st

def show_request_question_bank_page():
    st.title("Request Question Bank")
    
    technology = st.selectbox("Select Technology", ["Python", "Java", "JavaScript", "C++", "SQL"])
    
    if st.button("Request"):
        st.success(f"Question bank for {technology} requested successfully. It will be available in your dashboard soon.")

if __name__ == "__main__":
    show_request_question_bank_page()
