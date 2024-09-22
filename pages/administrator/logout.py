# pages/administrator/logout.py
import streamlit as st

def show_logout_page():
    st.title("Logout")
    
    st.write("Are you sure you want to log out?")
    
    if st.button("Confirm Logout"):
        # Clear session state
        st.session_state.authenticated = False
        st.session_state.role = None
        st.session_state.username = ''
        st.session_state.user_id = None  # Clear user ID as well
        st.success("You have been logged out successfully.")
        st.rerun()  # Use st.rerun() to refresh the app and redirect to the login page

if __name__ == "__main__":
    show_logout_page()
