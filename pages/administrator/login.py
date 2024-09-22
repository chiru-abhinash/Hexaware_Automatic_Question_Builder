# pages/administrator/login.py
import streamlit as st
from utils.auth import authenticate_user

def show_login_page():
    st.title("Administrator Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        auth_success, role, user_id = authenticate_user(username, password)
        if auth_success and role == 'Administrator':
            st.session_state.authenticated = True
            st.session_state.role = role
            st.session_state.username = username
            st.session_state.user_id = user_id  # Store user ID in session state
            st.success("Login successful! Redirecting...")
            st.rerun()  # Use st.rerun() to refresh the app and load the dashboard
        else:
            st.error("Invalid credentials or role. Please try again.")

if __name__ == "__main__":
    show_login_page()
