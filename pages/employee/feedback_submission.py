# pages/employee/feedback_submission.py
import streamlit as st
import sqlite3

def save_feedback(feedback_type, feedback):
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO feedback (feedback_type, feedback_text)
        VALUES (?, ?)
    ''', (feedback_type, feedback))
    conn.commit()
    conn.close()

def feedback_submission_page():
    st.title("Feedback Submission")

    # Feedback Form
    st.subheader("Provide Feedback")
    feedback_type = st.selectbox("Feedback Type", ["Learning Materials", "Question Banks"])
    feedback = st.text_area("Your Feedback", help="Provide detailed feedback.")
    
    if st.button("Submit Feedback"):
        if feedback:
            save_feedback(feedback_type, feedback)
            st.success("Thank you! Your feedback has been submitted.")
        else:
            st.error("Please provide your feedback before submitting.")

if __name__ == "__main__":
    feedback_submission_page()
