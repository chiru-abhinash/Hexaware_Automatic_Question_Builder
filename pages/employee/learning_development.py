# pages/employee/learning_and_development.py
import streamlit as st

def show_learning_and_development_page():
    st.title("Learning and Development")
    
    # Example list of learning resources (to be dynamically loaded)
    learning_resources = {
        "Python Tutorial": 75,
        "JavaScript Course": 50,
        "SQL Masterclass": 20
    }
    
    for resource, progress in learning_resources.items():
        st.write(f"{resource}")
        st.progress(progress)

    if st.button("Access Learning Materials"):
        st.success("Learning materials accessed successfully.")

if __name__ == "__main__":
    show_learning_and_development_page()
