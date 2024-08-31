# pages/trainer/dashboard.py
import streamlit as st

def show_dashboard():
    st.title("Trainer Dashboard")
    st.write(f"Welcome, {st.session_state.username}")
    
    st.subheader("Quick Links")
    st.button("Upload Curriculum")
    st.button("Generate Question Bank")
    st.button("Review and Edit Question Bank")
    st.button("Download Question Bank")
    st.button("Feedback")

if __name__ == "__main__":
    show_dashboard()
