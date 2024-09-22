import streamlit as st
import sqlite3
from utils.notifications import show_notifications_page

def submit_feedback():
    st.title("Submit Feedback")

    # Check if user_id is in session_state
    if 'user_id' not in st.session_state:
        st.error("User not authenticated. Please log in.")
        return

    # Add a dropdown to select feedback type (e.g., suggestion, bug report, etc.)
    feedback_type = st.selectbox("Select Feedback Type", ["Suggestion", "Bug Report", "Other"])

    # Feedback text area
    feedback_text = st.text_area("Enter your feedback here", height=200)
    
    # Add a unique key to the st.button
    if st.button("Submit Feedback", key="submit_feedback_button"):
        if not feedback_text:
            st.warning("Please enter your feedback before submitting.")
            return
        
        try:
            conn = sqlite3.connect('app_database.db')
            cursor = conn.cursor()

            # Include feedback_type in the INSERT statement
            cursor.execute(
                "INSERT INTO feedback (user_id, feedback_type, feedback_text) VALUES (?, ?, ?)", 
                (st.session_state.user_id, feedback_type, feedback_text)
            )
            conn.commit()

            st.success("Feedback submitted successfully!")
            # Show notifications page instead of display_notification
            show_notifications_page(
                notification_text="Thank you for your feedback! Your comments have been submitted successfully.",
                notification_type="success"
            )
        except Exception as e:
            st.error(f"An error occurred while submitting feedback: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    submit_feedback()
