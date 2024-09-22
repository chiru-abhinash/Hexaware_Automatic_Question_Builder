# pages/employee/request_learning_plan.py
import streamlit as st
import sqlite3

def get_employee_id(username):
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    employee_id = cursor.fetchone()
    conn.close()
    return employee_id[0] if employee_id else None

def request_learning_plan():
    st.title("Request Learning Plan")

    # Get the employee ID from the database
    if 'username' in st.session_state:
        if 'employee_id' not in st.session_state:
            st.session_state.employee_id = get_employee_id(st.session_state.username)

    technology = st.selectbox("Select Technology", ["Python", "Java", "C++"])
    areas_of_improvement = st.text_area("Areas of Improvement")
    learning_goals = st.text_area("Learning Goals")

    if st.button("Submit Request"):
        if st.session_state.employee_id:
            conn = sqlite3.connect('app_database.db')
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    INSERT INTO learning_plans (employee_id, technology, areas_of_improvement, learning_goals)
                    VALUES (?, ?, ?, ?)
                ''', (st.session_state.employee_id, technology, areas_of_improvement, learning_goals))
                conn.commit()
                st.success("Learning plan requested successfully!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
            finally:
                conn.close()
        else:
            st.error("Employee ID not found. Please ensure you are logged in.")

if __name__ == "__main__":
    request_learning_plan()
