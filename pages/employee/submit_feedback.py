# pages/employee/submit_feedback.py
import streamlit as st

def show_submit_feedback_page():
    st.title("Submit Feedback")
    
    feedback = st.text_area("Enter your feedback here...")
    
    if st.button("Submit"):
        st.success("Thank you for your feedback!")

if __name__ == "__main__":
    show_submit_feedback_page()
