# pages/trainer/login.py
import streamlit as st
from utils.auth import authenticate_user

def show_login_page():
    st.title("Trainer Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        role = authenticate_user(username, password)
        if role == 'Trainer':
            st.session_state.authenticated = True
            st.session_state.role = role
            st.session_state.username = username
            st.experimental_rerun()
        else:
            st.error("Invalid credentials or role. Please try again.")

if __name__ == "__main__":
    show_login_page()
