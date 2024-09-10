# pages/employee/logout.py
import streamlit as st

def logout():
    st.title("Logout")
    st.write("You have been logged out successfully.")
    st.session_state.username = None
    st.session_state.user_id = None
    st.session_state.page = None
    st.button("Login Page", on_click=lambda: st.rerun())

if __name__ == "__main__":
    logout()
