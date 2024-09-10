import streamlit as st
from pages.administrator.user_management import show_user_management_page
from pages.administrator.system_monitoring import show_system_monitoring_page
from pages.administrator.report_generation import show_report_generation_page
from pages.administrator.settings import show_settings_page
from pages.administrator.issue_resolution import show_issue_resolution_page

def logout():
    """Handle user logout and redirect to the login page."""
    st.session_state.authenticated = False
    st.session_state.role = None
    st.session_state.username = ''
    st.session_state.page = "login"
    st.rerun()  # Rerun the app to redirect to the login page

def show_admin_dashboard():
    st.title("Administrator Dashboard")
    st.write(f"Welcome, {st.session_state.username}")

    st.subheader("Quick Links")
    if st.button("User Management"):
        st.session_state.page = "user_management"
    if st.button("System Monitoring"):
        st.session_state.page = "system_monitoring"
    if st.button("Report Generation"):
        st.session_state.page = "report_generation"
    if st.button("Settings"):
        st.session_state.page = "settings"
    if st.button("Issue Resolution"):
        st.session_state.page = "issue_resolution"
    if st.button("Logout"):
        logout()  # Directly call the logout function

    # Check and load the correct page
    if 'page' in st.session_state:
        if st.session_state.page == "user_management":
            show_user_management_page()
        elif st.session_state.page == "system_monitoring":
            show_system_monitoring_page()
        elif st.session_state.page == "report_generation":
            show_report_generation_page()
        elif st.session_state.page == "settings":
            show_settings_page()
        elif st.session_state.page == "issue_resolution":
            show_issue_resolution_page()

if __name__ == "__main__":
    show_admin_dashboard()
