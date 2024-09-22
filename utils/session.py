import streamlit as st

# Set session state for authenticated user
def set_session_state(username, role, user_id):
    st.session_state.authenticated = True
    st.session_state.username = username
    st.session_state.role = role
    st.session_state.user_id = user_id

# Clear session state to log out the user
def clear_session_state():
    st.session_state.authenticated = False
    st.session_state.username = ''
    st.session_state.role = None
    st.session_state.user_id = None
    st.rerun()  # This will reload the app and show the login page again

# Get session state (to check if user is authenticated)
def get_session_state():
    return {
        "authenticated": st.session_state.get("authenticated", False),
        "username": st.session_state.get("username", ''),
        "role": st.session_state.get("role", None),
        "user_id": st.session_state.get("user_id", None)
    }

# Redirect to login page if the session is not authenticated
def ensure_authenticated():
    if not st.session_state.get("authenticated", False):
        st.warning("Unauthorized access. Please log in.")
        st.rerun()  # Redirect to the login page if not authenticated
