import streamlit as st

def set_session_state(username, role):
    """Set the session state variables."""
    st.session_state['username'] = username
    st.session_state['role'] = role

def get_session_state():
    """Get the session state variables."""
    username = st.session_state.get('username', None)
    role = st.session_state.get('role', None)
    return username, role

def clear_session_state():
    """Clear the session state variables."""
    st.session_state.clear()
