import streamlit as st

def show_logout_page():
    """Render the Logout page."""
    st.title("Logout")
    
    if st.button("Confirm Logout"):
        # Clear session state
        st.session_state.authenticated = False
        st.session_state.role = None
        st.session_state.username = ''
        st.session_state.user_id = None  # Clear user ID as well
        st.success("You have been logged out successfully.")
        st.experimental_rerun()  # Refresh the app to reflect the changes

if __name__ == "__main__":
    show_logout_page()
