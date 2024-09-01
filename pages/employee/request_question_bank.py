# pages/employee/request_question_bank.py
import streamlit as st
import sqlite3

def fetch_available_technologies():
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT technology FROM question_bank")
    technologies = cursor.fetchall()
    conn.close()
    return [tech[0] for tech in technologies]

def request_question_bank():
    st.title("Request Question Bank")
    
    technology = st.selectbox("Select Technology", fetch_available_technologies())
    
    if st.button("Request"):
        st.write(f"Requesting question bank for {technology}.")
        # Logic to handle the request (e.g., save request to the database or notify the system)

if __name__ == "__main__":
    request_question_bank()
