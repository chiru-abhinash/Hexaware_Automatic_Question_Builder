# pages/employee/request_learning_plan.py
import streamlit as st

def show_request_learning_plan_page():
    st.title("Request Learning Plan")
    
    technology = st.selectbox("Select Technology", ["Python", "Java", "JavaScript", "C++", "SQL"])
    areas_of_improvement = st.text_area("Areas of Improvement")
    learning_goals = st.text_area("Learning Goals")
    
    if st.button("Submit"):
        st.success("Learning plan requested successfully.")

if __name__ == "__main__":
    show_request_learning_plan_page()
