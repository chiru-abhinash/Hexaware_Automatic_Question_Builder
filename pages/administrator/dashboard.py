# pages/administrator/dashboard.py
import streamlit as st

def show_dashboard():
    st.title("Administrator Dashboard")
    st.write(f"Welcome, {st.session_state.username}")
    
    # Example components - customize as needed
    st.metric(label="System Uptime", value="99.9%")
    st.metric(label="Active Users", value="124")
    
    st.subheader("Quick Links")
    st.button("User Management")
    st.button("System Monitoring")
    st.button("Report Generation")
    st.button("Settings")
    st.button("Issue Resolution")

if __name__ == "__main__":
    show_dashboard()
