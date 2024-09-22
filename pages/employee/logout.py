# pages/employee/logout.py
import streamlit as st

def logout():
    st.title("Logout")
    st.write("You have been logged out successfully.")

    # Clear session state
    st.session_state.username = None
    st.session_state.user_id = None
    st.session_state.page = None
    
    # Button to redirect to the login page
    if st.button("Return to Login Page"):
        st.session_state.authenticated = False  # Ensure authentication state is cleared
        st.experimental_rerun()  # Rerun the app to load the login page

if __name__ == "__main__":
    logout()
