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

def generate_learning_plan(technology, areas_of_improvement, learning_goals):
    """Generate a learning plan based on the provided details."""
    # Example learning plan content
    learning_plan = {
        "question_banks": f"Recommended question banks for {technology}",
        "study_materials": f"Study materials for improving {areas_of_improvement}",
        "timeline": f"Timeline: 4 weeks to achieve {learning_goals}"
    }
    return learning_plan

def request_learning_plan():
    st.title("Request Learning Plan for Technical Upskill")

    # Get the employee ID from the database
    if 'username' in st.session_state:
        if 'employee_id' not in st.session_state:
            st.session_state.employee_id = get_employee_id(st.session_state.username)

    # Technology selection
    technology = st.selectbox("Select Technology", ["Python", "Java", "C++"])

    # Text areas for detailed input
    areas_of_improvement = st.text_area("Areas of Improvement", placeholder="Detail the specific areas you want to improve.")
    learning_goals = st.text_area("Learning Goals", placeholder="Outline your learning goals.")

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

                # Generate and display the learning plan
                learning_plan = generate_learning_plan(technology, areas_of_improvement, learning_goals)
                st.subheader("Your Customized Learning Plan")
                st.write(f"- **Question Banks:** {learning_plan['question_banks']}")
                st.write(f"- **Study Materials:** {learning_plan['study_materials']}")
                st.write(f"- **Timeline:** {learning_plan['timeline']}")

            except Exception as e:
                st.error(f"An error occurred: {e}")
            finally:
                conn.close()
        else:
            st.error("Employee ID not found. Please ensure you are logged in.")
    
    # Display Submitted Learning Plans
    st.subheader("Submitted Learning Plans")
    if 'employee_id' in st.session_state:
        conn = sqlite3.connect('app_database.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT technology, areas_of_improvement, learning_goals
            FROM learning_plans WHERE employee_id = ?
        ''', (st.session_state.employee_id,))
        plans = cursor.fetchall()
        conn.close()

        if plans:
            for idx, plan in enumerate(plans, 1):
                st.write(f"**Plan {idx}:**")
                st.write(f"**Technology:** {plan[0]}")
                st.write(f"**Areas of Improvement:** {plan[1]}")
                st.write(f"**Learning Goals:** {plan[2]}")
        else:
            st.write("No learning plans found.")

if __name__ == "__main__":
    request_learning_plan()
