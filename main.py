import streamlit as st
import os

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.role = None
    st.session_state.username = ''

def load_page(page_path):
    with st.spinner('Loading...'):
        try:
            # Construct the full path to the page file
            full_path = os.path.join(os.path.dirname(__file__), page_path)
            with open(full_path) as f:
                exec(f.read())
        except FileNotFoundError:
            st.error(f"File {full_path} not found. Please check the file path.")
        except Exception as e:
            st.error(f"An error occurred while loading the page: {e}")

def main():
    st.set_page_config(page_title="Automated Question Builder", layout="wide")
    if not st.session_state.authenticated:
        load_page('pages/login.py')
    else:
        role = st.session_state.role
        if role == 'Administrator':
            load_page('pages/administrator/dashboard.py')
        elif role == 'Trainer':
            load_page('pages/trainer/dashboard.py')
        elif role == 'Employee':
            load_page('pages/employee/dashboard.py')
        else:
            st.error("Invalid role detected. Please contact support.")

if __name__ == "__main__":
    main()
