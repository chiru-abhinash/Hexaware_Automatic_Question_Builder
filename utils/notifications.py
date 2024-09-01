# utils/notifications.py
import streamlit as st

def display_notification(message, notification_type="info"):
    if notification_type == "info":
        st.info(message)
    elif notification_type == "success":
        st.success(message)
    elif notification_type == "warning":
        st.warning(message)
    elif notification_type == "error":
        st.error(message)
