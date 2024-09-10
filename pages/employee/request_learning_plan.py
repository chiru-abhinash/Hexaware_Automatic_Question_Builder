import streamlit as st
import sqlite3

def request_learning_plan():
    st.title("Request Learning Plan")

    # Initialize st.session_state.employee_id if not already initialized
    if 'employee_id' not in st.session_state:
        st.session_state.employee_id = None  # or set it to a specific default value

    technology = st.selectbox("Select Technology", ["Python", "Java", "C++"])
    areas_of_improvement = st.text_area("Areas of Improvement")
    learning_goals = st.text_area("Learning Goals")

    if st.button("Submit Request"):
        conn = sqlite3.connect('app_database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO learning_plans (employee_id, technology, areas_of_improvement, learning_goals)
            VALUES (?, ?, ?, ?)
        ''', (st.session_state.employee_id, technology, areas_of_improvement, learning_goals))
        conn.commit()
        conn.close()
        st.success("Learning plan requested successfully!")

if __name__ == "__main__":
    request_learning_plan()
