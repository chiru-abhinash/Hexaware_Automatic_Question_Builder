import streamlit as st
import sqlite3
from datetime import datetime  # Import datetime module
from utils.notifications import show_notifications_page

def save_feedback(user_id, feedback):
    """Save feedback to the database and notify the admin."""
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()

    # Insert feedback into the feedback table
    cursor.execute('''
        INSERT INTO feedback (user_id, feedback_type, feedback_text)
        VALUES (?, ?, ?)
    ''', (user_id, "General", feedback))  # Set feedback_type to "General"

    # Create a notification for the admin
    cursor.execute('''
        INSERT INTO notifications (user_id, notification_text, sent_at, is_read)
        VALUES ((SELECT id FROM users WHERE username = 'admin'), ?, ?, FALSE)
    ''', (f"New feedback received from user ID {user_id}: {feedback}", datetime.now()))  # Use datetime.now()

    conn.commit()
    conn.close()
    st.success("Feedback submitted successfully!")

def show_feedback_page():
    st.title("Feedback")
    
    feedback = st.text_area("Provide your feedback")
    
    if st.button("Submit"):
        if feedback:
            save_feedback(st.session_state.user_id, feedback)  # Use user_id instead of username
            show_notifications_page(
                "Thank you for your feedback! Your comments have been submitted successfully.",
                notification_type="success"
            )
        else:
            st.error("Please provide feedback before submitting.")

if __name__ == "__main__":
    show_feedback_page()
