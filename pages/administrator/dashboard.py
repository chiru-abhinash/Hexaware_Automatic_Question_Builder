import streamlit as st

def show_admin_dashboard():
    st.title("Administrator Dashboard")
    st.write(f"Welcome, {st.session_state.username}")

    # Example metrics
    st.metric(label="System Uptime", value="99.9%")
    st.metric(label="Active Users", value="124")
    
    st.subheader("Quick Links")

    # Buttons to redirect to different functionalities
    if st.button("User Management"):
        load_page('pages/administrator/user_management.py')
        
    if st.button("System Monitoring"):
        load_page('pages/administrator/system_monitoring.py')
        
    if st.button("Report Generation"):
        load_page('pages/administrator/report_generation.py')
        
    if st.button("Settings"):
        load_page('pages/administrator/settings.py')
        
    if st.button("Issue Resolution"):
        load_page('pages/administrator/issue_resolution.py')
    
    # Logout button
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.role = None
        st.session_state.username = ''
        st.experimental_rerun()  # Rerun the app to redirect to the login page

def load_page(page_path):
    """Load a Streamlit page from the given path."""
    try:
        with open(page_path, 'r') as file:
            code = file.read()
            exec(code, globals())
    except FileNotFoundError:
        st.error(f"File not found: {page_path}")

if __name__ == "__main__":
    show_admin_dashboard()
