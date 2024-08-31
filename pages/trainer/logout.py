# pages/trainer/logout.py
import streamlit as st

def show_logout_page():
    st.title("Logout")
    
    if st.button("Confirm Logout"):
        st.session_state.authenticated = False
        st.session_state.role = None
        st.session_state.username = ''
        st.experimental_rerun()

if __name__ == "__main__":
    show_logout_page()
