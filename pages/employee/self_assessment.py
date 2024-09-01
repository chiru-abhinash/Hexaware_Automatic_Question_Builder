# pages/employee/self_assessment.py
import streamlit as st
import sqlite3

def fetch_question_banks():
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT technology FROM question_bank")
    technologies = cursor.fetchall()
    conn.close()
    return [tech[0] for tech in technologies]

def fetch_question_bank(technology):
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM question_bank WHERE technology = ?", (technology,))
    question_banks = cursor.fetchall()
    conn.close()
    return question_banks

def self_assessment():
    st.title("Self-Assessment")

    technology = st.selectbox("Select Technology", fetch_question_banks())
    
    if technology:
        question_banks = fetch_question_bank(technology)
        for bank in question_banks:
            st.subheader(f"Question Bank for {bank[2]} - Difficulty: {bank[4]}")
            st.write(bank[5])  # Assuming the questions are stored in the 'questions' field as text

    if st.button("Download Completion Certificate"):
        st.write("Download your completion certificate here.")
        # Logic to handle certificate download (e.g., generate and provide PDF download link)

if __name__ == "__main__":
    self_assessment()
