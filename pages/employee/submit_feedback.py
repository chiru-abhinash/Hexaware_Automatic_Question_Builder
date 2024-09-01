# pages/employee/submit_feedback.py
import streamlit as st
import sqlite3
from utils.notifications import display_notification
def submit_feedback():
    st.title("Submit Feedback")

    feedback_text = st.text_area("Enter your feedback here")
    
    if st.button("Submit Feedback"):
        conn = sqlite3.connect('app_database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback (user_id, feedback_text) VALUES (?, ?)", 
                       (st.session_state.user_id, feedback_text))
        conn.commit()
        conn.close()
        display_notification(
        "Thank you for your feedback! Your comments have been submitted successfully.",
        notification_type="success"
    )
        st.success("Feedback submitted successfully!")

if __name__ == "__main__":
    submit_feedback()
