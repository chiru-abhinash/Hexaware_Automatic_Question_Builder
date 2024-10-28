import streamlit as st
import sqlite3
from datetime import datetime
from utils.notifications import show_notifications_page

# Database setup functions
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

# Function to save feedback to the database and notify the admin
def save_feedback(user_id, feedback, feedback_type="General"):
    conn = get_db_connection()
    if conn is None:
        return

    try:
        # Insert feedback into the feedback table
        conn.execute('''INSERT INTO feedback (user_id, feedback_type, feedback_text)
                        VALUES (?, ?, ?)''', (user_id, feedback_type, feedback))
        
        # Create a notification for the admin
        conn.execute('''INSERT INTO notifications (user_id, notification_text, sent_at, is_read)
                        VALUES ((SELECT id FROM users WHERE username = 'admin'), ?, ?, FALSE)''',
                     (f"New feedback received from user ID {user_id}: {feedback}", datetime.now()))
        
        # Create an acknowledgment notification for the trainer
        conn.execute('''INSERT INTO notifications (user_id, notification_text, sent_at, is_read)
                        VALUES (?, ?, ?, FALSE)''',
                     (user_id, "Thank you for your feedback! Your comments have been submitted successfully.", datetime.now()))
        
        conn.commit()
        st.success("Feedback submitted successfully!")
    except sqlite3.Error as e:
        st.error(f"Error saving feedback: {e}")
    finally:
        conn.close()

# Function to show feedback page for feedback submission
def show_feedback_submission_page():
    st.subheader("Feedback Submission")
    feedback_type = st.selectbox("Select Feedback Type", ["Question Quality", "Improvement Suggestion", "General"])
    feedback = st.text_area("Provide your feedback")

    if st.button("Submit Feedback"):
        if feedback:
            save_feedback(st.session_state.user_id, feedback, feedback_type)
            # Instead of calling show_notifications_page directly, we rely on the insert to handle it
        else:
            st.error("Please provide feedback before submitting.")

# Function to display feedback received from employees for trainers to review
def show_feedback_review_page():
    st.subheader("Feedback Review")

    conn = get_db_connection()
    if conn is None:
        return

    try:
        feedbacks = conn.execute('''SELECT u.username, f.feedback_type, f.feedback_text, f.created_at
                                    FROM feedback f
                                    JOIN users u ON f.user_id = u.id
                                    WHERE u.role = 'Employee' ''').fetchall()

        if feedbacks:
            for feedback in feedbacks:
                st.write(f"**From:** {feedback['username']} ({feedback['created_at']})")
                st.write(f"**Type:** {feedback['feedback_type']}")
                st.write(f"**Feedback:** {feedback['feedback_text']}")
                st.markdown("---")
        else:
            st.info("No feedback available for review.")
    except sqlite3.Error as e:
        st.error(f"Error retrieving feedback: {e}")
    finally:
        conn.close()

# Function to display question bank requests received by the trainer
def show_question_bank_requests():
    st.subheader("Question Bank Requests")

    conn = get_db_connection()
    if conn is None:
        return

    try:
        requests = conn.execute('''SELECT u.username, qbr.topic, qbr.technology, qbr.num_questions, qbr.requested_at, qbr.status
                                   FROM question_bank_requests qbr
                                   JOIN users u ON qbr.employee_id = u.id
                                   WHERE qbr.status = 'Pending' ''').fetchall()

        if requests:
            for request in requests:
                st.write(f"**Requested By:** {request['username']} ({request['requested_at']})")
                st.write(f"**Topic:** {request['topic']}")
                st.write(f"**Technology:** {request['technology']}")
                st.write(f"**Number of Questions:** {request['num_questions']}")
                st.write(f"**Status:** {request['status']}")
                st.markdown("---")
        else:
            st.info("No pending question bank requests.")
    except sqlite3.Error as e:
        st.error(f"Error retrieving question bank requests: {e}")
    finally:
        conn.close()

# Main function to display different feedback and request pages for the trainer
def show_feedback_page():
    st.title("Trainer Feedback and Requests")

    # Tabs for Feedback Collection, Feedback Review, and Question Bank Requests
    tab1, tab2, tab3 = st.tabs(["Submit Feedback", "Review Feedback", "View Requests"])

    with tab1:
        show_feedback_submission_page()

    with tab2:
        show_feedback_review_page()

    with tab3:
        show_question_bank_requests()

if __name__ == "__main__":
    show_feedback_page()
