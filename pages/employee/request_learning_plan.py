# pages/employee/request_learning_plan.py
import streamlit as st
import sqlite3

def request_learning_plan():
    st.title("Request Learning Plan")

    technology = st.selectbox("Select Technology", ["Python", "Java", "C++"])
    areas_of_improvement = st.text_area("Areas of Improvement")
    learning_goals = st.text_area("Learning Goals")

    if st.button("Submit Request"):
        conn = sqlite3.connect('app_database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO learning_plans (employee_id, technology, areas_of_improvement, learning_goals)
            VALUES (?, ?, ?, ?)
        ''', (st.session_state.user_id, technology, areas_of_improvement, learning_goals))
        conn.commit()
        conn.close()
        st.success("Learning plan requested successfully!")

if __name__ == "__main__":
    request_learning_plan()
