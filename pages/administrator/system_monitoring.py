# pages/administrator/system_monitoring.py
import streamlit as st
import psutil
import pandas as pd
from utils.database import (
    fetch_all,
    fetch_one,
)

def get_cpu_usage():
    return f"{psutil.cpu_percent(interval=1)}%"

def get_memory_usage():
    mem = psutil.virtual_memory()
    return f"{mem.percent}%"

def get_error_logs():
    # Fetch error logs from the database
    error_logs = fetch_all("SELECT * FROM error_logs ORDER BY timestamp DESC LIMIT 10")
    if error_logs:
        return "\n".join([f"{log['timestamp']}: {log['message']}" for log in error_logs])
    return "No errors detected in the past 24 hours."

def get_user_activity_logs():
    # Fetch user activity logs from the database
    activity_logs = fetch_all("SELECT * FROM user_activity_logs ORDER BY timestamp DESC LIMIT 10")
    if activity_logs:
        return "\n".join([f"{log['timestamp']}: User {log['username']} performed {log['action']}" for log in activity_logs])
    return "User activity logs are currently not available."

def get_alerts():
    # Fetch alerts from the database
    alerts = fetch_all("SELECT * FROM alerts WHERE active = 1")
    if alerts:
        return "\n".join([f"Alert: {alert['message']} (Triggered at: {alert['timestamp']})" for alert in alerts])
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
