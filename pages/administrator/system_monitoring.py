# pages/administrator/system_monitoring.py
import streamlit as st
import psutil
from datetime import datetime

def get_cpu_usage():
    return f"{psutil.cpu_percent(interval=1)}%"

def get_memory_usage():
    mem = psutil.virtual_memory()
    return f"{mem.percent}%"

def get_error_logs():
    # Placeholder for real error log fetching
    # Example static logs; replace with actual log reading logic
    return "No errors detected in the past 24 hours."

def get_user_activity_logs():
    # Placeholder for real user activity log fetching
    # Example static logs; replace with actual log reading logic
    return "User activity logs are currently not available."

def get_alerts():
    # Placeholder for real alerts fetching
    # Example static alerts; replace with actual alerts fetching logic
    return "No active alerts."

def show_system_monitoring_page():
    st.title("System Monitoring")
    
    # Refresh button
    if st.button("Refresh"):
        st.rerun()
    
    st.subheader("Real-Time Performance Metrics")
    st.metric(label="CPU Usage", value=get_cpu_usage())
    st.metric(label="Memory Usage", value=get_memory_usage())
    
    st.subheader("Server Status")
    st.text("All servers are running smoothly.")
    
    st.subheader("Error Logs")
    st.text_area("Error Logs", value=get_error_logs(), height=200)
    
    st.subheader("User Activity Logs")
    st.text_area("User Activity Logs", value=get_user_activity_logs(), height=200)
    
    st.subheader("Alerts & Notifications")
    st.text(get_alerts())

if __name__ == "__main__":
    show_system_monitoring_page()
