# pages/employee/feedback_submission.py
import streamlit as st
import sqlite3
from datetime import datetime

def create_notification(user_id, notification_text, notification_type="Feedback", priority=1):
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO notifications (user_id, notification_text, notification_type, priority, sent_at, receiver_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, notification_text, notification_type, priority, datetime.now(), 0))  # Adjust receiver_id as needed
    conn.commit()
    conn.close()

def save_feedback(feedback_type, feedback, user_id):
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO feedback (user_id, feedback_type, feedback_text)
        VALUES (?, ?, ?)
    ''', (user_id, feedback_type, feedback))
    conn.commit()
    
    # Create a notification to inform the user that feedback has been submitted
    notification_text = f"Feedback on '{feedback_type}' has been submitted."
    create_notification(user_id, notification_text)

    conn.close()

def feedback_submission_page():
    st.title("Feedback Submission")

    # Check if user_id is in session_state
    if 'user_id' not in st.session_state:
        st.error("User not authenticated. Please log in.")
        return

    user_id = st.session_state.user_id

    # Feedback Form
    st.subheader("Provide Feedback")
    feedback_type = st.selectbox("Feedback Type", ["Learning Materials", "Question Banks"])
    feedback = st.text_area("Your Feedback", help="Provide detailed feedback.")
    
    if st.button("Submit Feedback"):
        if feedback:
            save_feedback(feedback_type, feedback, user_id)
            st.success("Thank you! Your feedback has been submitted.")
        else:
            st.error("Please provide your feedback before submitting.")

if __name__ == "__main__":
    feedback_submission_page()
