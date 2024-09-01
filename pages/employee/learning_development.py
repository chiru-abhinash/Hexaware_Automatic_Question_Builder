# pages/employee/learning_development.py
import streamlit as st
import sqlite3

def fetch_learning_resources():
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM question_bank")
    resources = cursor.fetchall()
    conn.close()
    return resources

def learning_development():
    st.title("Learning and Development")

    resources = fetch_learning_resources()
    for resource in resources:
        st.subheader(f"Learning Resource: {resource[2]}")
        st.write(resource[5])  # Display questions or learning content
        if st.button(f"Access {resource[2]}"):
            st.write("Accessing resource...")  # Add functionality to view/download the resource

if __name__ == "__main__":
    learning_development()
