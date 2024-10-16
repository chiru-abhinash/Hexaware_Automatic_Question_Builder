import streamlit as st
from pages.trainer.upload_curriculum import show_upload_curriculum_page
from pages.trainer.generate_question_bank import show_generate_question_bank_page
from pages.trainer.review_edit_question_bank import show_review_edit_question_bank_page
from pages.trainer.download_question_bank import show_download_question_bank_page
from pages.trainer.feedback import show_feedback_page
from pages.trainer.notifications import show_notifications_page  # Import the notifications page
from utils.notifications import get_unseen_notifications  # Import notification utility function

def show_trainer_dashboard():
    st.title("Trainer Dashboard")
    st.write(f"Welcome, {st.session_state.username}")

    st.subheader("Quick Links")
    
    # Use buttons to navigate to different functionalities
    if st.button("Upload Curriculum"):
        st.session_state.page = "upload_curriculum"
    if st.button("Generate Question Bank"):
        st.session_state.page = "generate_question_bank"
    if st.button("Review and Edit Question Bank"):
        st.session_state.page = "review_edit_question_bank"
    if st.button("Download Question Bank"):
        st.session_state.page = "download_question_bank"
    if st.button("Feedback"):
        st.session_state.page = "feedback"
    
    # Logout button logic
    if st.button("Logout"):
        # Clear session state
        st.session_state.authenticated = False
        st.session_state.role = None
        st.session_state.username = ''
        st.session_state.user_id = None  # Clear user ID
        st.session_state.page = "login"  # Set the page to login
        st.rerun()  # Refresh to redirect to login page

    # Load the correct page based on session state
    if 'page' in st.session_state:
        if st.session_state.page == "upload_curriculum":
            show_upload_curriculum_page()
        elif st.session_state.page == "generate_question_bank":
            show_generate_question_bank_page()
        elif st.session_state.page == "review_edit_question_bank":
            show_review_edit_question_bank_page()
        elif st.session_state.page == "download_question_bank":
            show_download_question_bank_page()
        elif st.session_state.page == "feedback":
            show_feedback_page()

if __name__ == "__main__":
    show_trainer_dashboard()
