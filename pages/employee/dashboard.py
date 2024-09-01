# pages/employee/dashboard.py
import streamlit as st
from pages.employee.request_question_bank import request_question_bank
from pages.employee.self_assessment import self_assessment
from pages.employee.submit_feedback import submit_feedback
from pages.employee.learning_development import learning_development
from pages.employee.request_learning_plan import request_learning_plan
from pages.employee.logout import logout

def show_employee_dashboard():
    st.title("Employee Dashboard")
    st.write(f"Welcome, {st.session_state.username}")

    st.subheader("Quick Links")
    if st.button("Request Question Bank"):
        st.session_state.page = "request_question_bank"
    if st.button("Self-Assessment"):
        st.session_state.page = "self_assessment"
    if st.button("Submit Feedback"):
        st.session_state.page = "submit_feedback"
    if st.button("Learning and Development"):
        st.session_state.page = "learning_development"
    if st.button("Request Learning Plan"):
        st.session_state.page = "request_learning_plan"
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.role = None
        st.session_state.username = ''
        st.session_state.page = "login"

    # Check and load the correct page
    if 'page' in st.session_state:
        if st.session_state.page == "request_question_bank":
            request_question_bank()
        elif st.session_state.page == "self_assessment":
            self_assessment()
        elif st.session_state.page == "submit_feedback":
            submit_feedback()
        elif st.session_state.page == "learning_development":
            learning_development()
        elif st.session_state.page == "request_learning_plan":
            request_learning_plan()
        elif st.session_state.page == "logout":
            logout()
        elif st.session_state.page == "login":
            # Redirect to the login page
            import main
            main.show_login_page()

if __name__ == "__main__":
    show_employee_dashboard()
