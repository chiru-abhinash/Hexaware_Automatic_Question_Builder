# pages/employee/submit_feedback.py
import streamlit as st
import sqlite3
from utils.notifications import display_notification

def submit_feedback():
    st.title("Submit Feedback")

    # Check if user_id is in session_state
    if 'user_id' not in st.session_state:
        st.error("User not authenticated. Please log in.")
        return

    feedback_text = st.text_area("Enter your feedback here")
    
    if st.button("Submit Feedback", key="submit_feedback_button_1"):
        if not feedback_text:
            st.warning("Please enter your feedback before submitting.")
            return
        
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
