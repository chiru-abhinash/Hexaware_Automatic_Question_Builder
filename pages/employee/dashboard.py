# pages/employee/dashboard.py
import streamlit as st

def show_dashboard():
    st.title("Employee Dashboard")
    st.write(f"Welcome, {st.session_state.username}")
    
    st.subheader("Quick Links")
    st.button("Request Question Bank")
    st.button("Self-Assessment")
    st.button("Submit Feedback")
    st.button("Learning and Development")
    st.button("Request Learning Plan")

if __name__ == "__main__":
    show_dashboard()
