# pages/trainer/download_question_bank.py
import streamlit as st

def show_download_question_bank_page():
    st.title("Download Question Bank")
    
    format_type = st.selectbox("Select Download Format", ["Excel", "PDF"])
    
    if st.button("Download"):
        st.success(f"Question bank downloaded successfully in {format_type} format.")

if __name__ == "__main__":
    show_download_question_bank_page()
