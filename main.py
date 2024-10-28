
# import streamlit as st
# import utils.email_service
# from utils.auth import authenticate_user
# from utils.forget_password import show_forget_password_page  # Import the forgot password page
# from utils.reset_password import show_reset_password_page  # Import the reset password page

# # Initialize session state
# if 'authenticated' not in st.session_state:
#     st.session_state.authenticated = False
#     st.session_state.role = None
#     st.session_state.username = ''
#     st.session_state.user_id = None
#     st.session_state.current_page = 'login'  # Track the current page

# def show_login_page():
#     """Render the login page."""
#     st.title("Login Page")
    
#     # Input fields for username and password
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
    
#     # Button to log in
#     if st.button("Login"):
#         auth_success, role, user_id = authenticate_user(username, password)
#         if auth_success:
#             st.session_state.authenticated = True
#             st.session_state.role = role
#             st.session_state.username = username
#             st.session_state.user_id = user_id
#             st.success("Login successful! Redirecting...")
#             st.session_state.current_page = 'dashboard'  # Redirect to dashboard after login
#             st.rerun()
#         else:
#             st.error("Invalid username or password.")
    
#     # Forgot Password link, shown only when user is not authenticated
#     if not st.session_state.authenticated:
#         col1, col2 = st.columns(2)
#         with col1:
#             if st.button("Forgot Password?"):
#                 st.session_state.current_page = 'forgot_password'  # Switch to forgot password page
#                 st.rerun()
#         with col2:
#             if st.button("Reset Password"):
#                 st.session_state.current_page = 'reset_password'  # Switch to reset password page
#                 st.rerun()

# def load_dashboard_page():
#     """Load the dashboard page based on the user's role."""
#     st.title(f"Welcome, {st.session_state.username}!")  # Personalized greeting
#     role = st.session_state.role
#     if role == 'Administrator':
#         load_page('pages/administrator/dashboard.py')
#     elif role == 'Trainer':
#         load_page('pages/trainer/dashboard.py')
#     elif role == 'Employee':
#         load_page('pages/employee/dashboard.py')
#     else:
#         st.error("Invalid role detected. Please contact support.")

# def load_page(page_path):
#     """Load a Streamlit page from the given path."""
#     try:
#         with open(page_path, 'r') as file:
#             code = file.read()
#             exec(code, globals())
#     except FileNotFoundError:
#         st.error(f"File not found: {page_path}")

# def main():
#     st.set_page_config(page_title="Automated Question Builder", layout="wide")
    
#     # Show login or dashboard based on the authentication status
#     if not st.session_state.authenticated:
#         if st.session_state.current_page == 'login':
#             show_login_page()
#         elif st.session_state.current_page == 'forgot_password':
#             if st.button("Back to Login"):
#                 st.session_state.current_page = 'login'  # Navigate back to login page
#                 st.rerun()
#             show_forget_password_page()  # Show forgot password page only when not authenticated
#         elif st.session_state.current_page == 'reset_password':
#             if st.button("Back to Login"):
#                 st.session_state.current_page = 'login'  # Navigate back to forgot password page
#                 st.rerun()
#             show_reset_password_page()  # Show reset password page only when not authenticated
#         else:
#             show_login_page()
#     else:
#         st.session_state.current_page = 'dashboard'  # Force page switch to dashboard after login
#         load_dashboard_page()

# if __name__ == "__main__":  # Fixed the entry point declaration
#     main()

import streamlit as st
from utils.email_service import send_email  # Ensure you have an email sending function
from utils.auth import authenticate_user
from utils.forget_password import show_forget_password_page
from utils.reset_password import show_reset_password_page
from utils.database import insert_user_activity  # Function to insert user activity logs
from datetime import datetime  # Import datetime

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.role = None
    st.session_state.username = ''
    st.session_state.user_id = None  # Initialize user_id
    st.session_state.current_page = 'login'

def log_user_activity(username, action):
    """Log user activity in the database."""
    try:
        params = (username, action, datetime.now())
        query = """INSERT INTO user_activity_logs (username, action, timestamp) VALUES (?, ?, ?)"""
        insert_user_activity(query, params)  # Ensure you have an insert_user_activity function
    except Exception as e:
        st.error(f"Error logging user activity: {e}")

def show_login_page():
    """Render the login page."""
    st.title("Login Page")
    
    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    # Button to log in
    if st.button("Login"):
        auth_success, role, user_id = authenticate_user(username, password)
        if auth_success:
            st.session_state.authenticated = True
            st.session_state.role = role
            st.session_state.username = username
            st.session_state.user_id = user_id  # Store user_id in session state
            st.success("Login successful! Redirecting...")
            log_user_activity(username, "Logged In")  # Log user activity
            st.session_state.current_page = 'dashboard'  # Redirect to dashboard after login
            st.rerun()  # Use experimental rerun to refresh the app state
        else:
            st.error("Invalid username or password.")
    
    # Forgot Password link
    if not st.session_state.authenticated:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Forgot Password?"):
                st.session_state.current_page = 'forgot_password'
                st.rerun()  # Use experimental rerun to refresh the app state
        with col2:
            if st.button("Reset Password"):
                st.session_state.current_page = 'reset_password'
                st.rerun()  # Use experimental rerun to refresh the app state

def load_dashboard_page():
    """Load the dashboard page based on the user's role."""
    st.title(f"Welcome, {st.session_state.username}!")
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
    
    # Show login or dashboard based on the authentication status
    if not st.session_state.authenticated:
        if st.session_state.current_page == 'login':
            show_login_page()
        elif st.session_state.current_page == 'forgot_password':
            if st.button("Back to Login"):
                st.session_state.current_page = 'login'
                st.experimental_rerun()  # Use experimental rerun to refresh the app state
            show_forget_password_page()
        elif st.session_state.current_page == 'reset_password':
            if st.button("Back to Login"):
                st.session_state.current_page = 'login'
                st.experimental_rerun()  # Use experimental rerun to refresh the app state
            show_reset_password_page()
        else:
            show_login_page()
    else:
        st.session_state.current_page = 'dashboard'  # Force page switch to dashboard after login
        load_dashboard_page()

if __name__ == "__main__":
    main()
