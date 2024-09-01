import streamlit as st
from utils.notifications import display_notification
def save_feedback(username, feedback):
    # Implement feedback saving logic (e.g., save to a database or file)
    st.success("Feedback submitted successfully!")

def show_feedback_page():
    st.title("Feedback")
    
    feedback = st.text_area("Provide your feedback")
    
    if st.button("Submit"):
        if feedback:
            save_feedback(st.session_state.username, feedback)
            display_notification(
        "Thank you for your feedback! Your comments have been submitted successfully.",
        notification_type="success"
    )
        else:
            st.error("Please provide feedback before submitting.")
    