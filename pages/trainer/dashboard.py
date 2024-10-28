# import streamlit as st
# from pages.trainer.upload_curriculum import show_upload_curriculum_page
# from pages.trainer.generate_question_bank import show_generate_question_bank_page
# from pages.trainer.review_edit_question_bank import show_review_edit_question_bank_page
# from pages.trainer.download_question_bank import show_download_question_bank_page
# from pages.trainer.feedback import show_feedback_page
# from pages.trainer.notifications import show_notifications_page  # Import the notifications page
# from utils.notifications import get_unseen_notifications  # Import notification utility function

# def show_trainer_dashboard():
#     st.title("Trainer Dashboard")
#     st.write(f"Welcome, {st.session_state.username}")

#     st.subheader("Quick Links")
    
#     # Use buttons to navigate to different functionalities
#     if st.button("Upload Curriculum"):
#         st.session_state.page = "upload_curriculum"
#     if st.button("Generate Question Bank"):
#         st.session_state.page = "generate_question_bank"
#     if st.button("Review and Edit Question Bank"):
#         st.session_state.page = "review_edit_question_bank"
#     if st.button("Download Question Bank"):
#         st.session_state.page = "download_question_bank"
#     if st.button("Feedback"):
#         st.session_state.page = "feedback"
    
#     # Logout button logic
#     if st.button("Logout"):
#         # Clear session state
#         st.session_state.authenticated = False
#         st.session_state.role = None
#         st.session_state.username = ''
#         st.session_state.user_id = None  # Clear user ID
#         st.session_state.page = "login"  # Set the page to login
#         st.rerun()  # Refresh to redirect to login page

#     # Load the correct page based on session state
#     if 'page' in st.session_state:
#         if st.session_state.page == "upload_curriculum":
#             show_upload_curriculum_page()
#         elif st.session_state.page == "generate_question_bank":
#             show_generate_question_bank_page()
#         elif st.session_state.page == "review_edit_question_bank":
#             show_review_edit_question_bank_page()
#         elif st.session_state.page == "download_question_bank":
#             show_download_question_bank_page()
#         elif st.session_state.page == "feedback":
#             show_feedback_page()

# if __name__ == "__main__":
#     show_trainer_dashboard()




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
    
    # Notification section
    if st.button("View Notifications"):
        st.session_state.page = "notifications"  # Set the page to notifications
    else:
        unseen_notifications = get_unseen_notifications(st.session_state.user_id)  # Get unseen notifications
        if unseen_notifications:
            st.sidebar.warning(f"You have {len(unseen_notifications)} new notifications!")

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
        elif st.session_state.page == "notifications":
            show_notifications_page()  # Show the notifications page

if __name__ == "__main__":
    show_trainer_dashboard()


# import streamlit as st
# from pages.trainer.upload_curriculum import show_upload_curriculum_page
# from pages.trainer.generate_question_bank import show_generate_question_bank_page
# from pages.trainer.review_edit_question_bank import show_review_edit_question_bank_page
# from pages.trainer.download_question_bank import show_download_question_bank_page
# from pages.trainer.feedback import show_feedback_page
# from pages.trainer.notifications import show_notifications_page

# def show_trainer_dashboard():
#     st.title("Trainer Dashboard")
#     st.write(f"Welcome, {st.session_state.username}")

#     # Setting up the tabs for each feature in the Trainer Dashboard
#     tabs = st.tabs([
#         "Upload Curriculum", 
#         "Generate Question Bank", 
#         "Review/Edit Question Bank", 
#         "Download Question Bank", 
#         "Feedback", 
#         "Notifications"
#     ])

#     with tabs[0]:  # Upload Curriculum Tab
#         st.subheader("Upload Curriculum")
#         show_upload_curriculum_page()

#     with tabs[1]:  # Generate Question Bank Tab
#         st.subheader("Generate Question Bank")
#         technology = st.selectbox("Select Technology", ["Python", "Java", "C++"], key="generate_question_bank_technology")
#         show_generate_question_bank_page()

#     with tabs[2]:  # Review/Edit Question Bank Tab
#         st.subheader("Review and Edit Question Bank")
#         review_option = st.selectbox("Select Review Option", ["Option 1", "Option 2"], key="review_edit_question_bank_option")
#         show_review_edit_question_bank_page()

#     with tabs[3]:  # Download Question Bank Tab
#         st.subheader("Download Question Bank")
#         file_format = st.selectbox("Select File Format", ["PDF", "Excel"], key="download_question_bank_file_format")
#         show_download_question_bank_page()

#     with tabs[4]:  # Feedback Tab
#         st.subheader("Feedback")
#         feedback_text = st.text_area("Provide your feedback", key="feedback_text_area")
#         if st.button("Submit Feedback", key="submit_feedback"):
#             show_feedback_page()

#     with tabs[5]:  # Notifications Tab
#         st.subheader("Notifications")
#         show_notifications_page()

#     # Logout button logic
#     if st.button("Logout", key="logout_button"):
#         st.session_state.authenticated = False
#         st.session_state.role = None
#         st.session_state.username = ''
#         st.session_state.user_id = None
#         st.session_state.page = "login"
#         st.rerun()

# if __name__ == "__main__":
#     show_trainer_dashboard()
