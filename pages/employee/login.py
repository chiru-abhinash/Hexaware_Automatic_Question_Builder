# pages/employee/login.py (Example of setting user_id)
import streamlit as st
import sqlite3

def login():
    st.title("Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        conn = sqlite3.connect('app_database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        
        if user:
            st.session_state.user_id = user[0]
            st.session_state.authenticated = True
            st.session_state.username = username
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")

if __name__ == "__main__":
    login()
