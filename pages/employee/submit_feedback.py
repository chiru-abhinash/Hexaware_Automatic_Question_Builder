import streamlit as st
import sqlite3
from utils.notifications import show_notifications_page
from datetime import datetime
# Database connection function
def get_db_connection():
    """Establishes a database connection and enables foreign keys."""
    try:
        conn = sqlite3.connect('app_database.db')
        conn.row_factory = sqlite3.Row  # Allows access to columns by name
        conn.execute('PRAGMA foreign_keys = ON')  # Enforce foreign key constraints
        return conn
    except sqlite3.Error as e:
        st.error(f"Error connecting to database: {e}")
        return None

# Function to save employee feedback and show notifications
def save_employee_feedback(user_id, feedback, feedback_type="General"):
    conn = get_db_connection()
    if conn is None:
        return

    try:
        # Insert feedback into the feedback table
        conn.execute('''INSERT INTO feedback (user_id, feedback_type, feedback_text)
                        VALUES (?, ?, ?)''', (user_id, feedback_type, feedback))
        
        # Create an acknowledgment notification for the employee
        conn.execute('''INSERT INTO notifications (user_id, notification_text, sent_at, is_read)
                        VALUES (?, ?, ?, FALSE)''',
                     (user_id, "Thank you for your feedback! Your comments have been submitted successfully.", datetime.now()))
        
        conn.commit()
        st.success("Feedback submitted successfully!")
    except sqlite3.Error as e:
        st.error(f"Error saving feedback: {e}")
    finally:
        conn.close()

# Function to show feedback submission page for employees
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
        
        save_employee_feedback(st.session_state.user_id, feedback_text, feedback_type)
        # Instead of calling show_notifications_page directly, we rely on the insert to handle it
        show_notifications_page(
            notification_text="Thank you for your feedback! Your comments have been submitted successfully.",
            notification_type="success"
        )

# Main function to run the feedback submission page
if __name__ == "__main__":
    submit_feedback()
