import streamlit as st
from utils.auth import authenticate_user

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.role = None
    st.session_state.username = ''

def show_login_page():
    """Render the login page directly in this function."""
    st.title("Login Page")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        auth_success, role, user_id = authenticate_user(username, password)
        if auth_success:
            st.session_state.authenticated = True
            st.session_state.role = role  # Set the role based on authentication
            st.session_state.username = username
            st.session_state.user_id = user_id  # Set the user_id
            st.success("Login successful! Redirecting...")
            st.rerun()  # Corrected usage of st.experimental.rerun()
        else:
            st.error("Invalid username or password.")
    
    if st.button("Forgot Password"):
        st.info("Password recovery process here.")


def load_dashboard_page():
    """Load the dashboard page based on the user role."""
    role = st.session_state.role
    if role == 'Administrator':
        load_page('pages/administrator/dashboard.py')
    elif role == 'Trainer':
        load_page('pages/trainer/dashboard.py')
    elif role == 'Employee':
        load_page('pages/employee/dashboard.py')
    else:
        st.error("Invalid role detected. Please contact support.")

def load_page(page_path):
    """Load a Streamlit page from the given path."""
    try:
        with open(page_path, 'r') as file:
            code = file.read()
            exec(code, globals())
    except FileNotFoundError:
        st.error(f"File not found: {page_path}")

def main():
    st.set_page_config(page_title="Automated Question Builder", layout="wide")
    
    if not st.session_state.authenticated:
        show_login_page()
    else:
        load_dashboard_page()

if __name__ == "__main__":
    main()
