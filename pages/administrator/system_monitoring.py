# pages/administrator/system_monitoring.py
import streamlit as st

def show_system_monitoring_page():
    st.title("System Monitoring")
    
    st.subheader("Real-Time Performance Metrics")
    st.metric(label="CPU Usage", value="15%")
    st.metric(label="Memory Usage", value="45%")
    
    st.subheader("Server Status")
    st.text("All servers are running smoothly.")
    
    st.subheader("Error Logs")
    st.text_area("Error Logs", height=200)
    
    st.subheader("User Activity Logs")
    st.text_area("User Activity Logs", height=200)
    
    st.subheader("Alerts & Notifications")
    st.text("No active alerts.")

if __name__ == "__main__":
    show_system_monitoring_page()
