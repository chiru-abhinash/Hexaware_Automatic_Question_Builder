# pages/trainer/feedback.py
import streamlit as st

def show_feedback_page():
    st.title("Provide Feedback")
    
    feedback = st.text_area("Enter your feedback here...")
    
    if st.button("Submit"):
        st.success("Thank you for your feedback!")

if __name__ == "__main__":
    show_feedback_page()
