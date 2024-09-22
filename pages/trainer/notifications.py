import streamlit as st
from utils.notifications import get_unseen_notifications, mark_notifications_as_read

def show_notifications_page():
    st.title("Notifications")
    
    user_id = st.session_state.user_id  # Make sure user_id is stored in session state

    # Fetch unseen notifications for the current trainer
    notifications = get_unseen_notifications(user_id)

    if notifications:
        for notification in notifications:
            st.write(f"• {notification['notification_text']} (Received: {notification['sent_at']})")
        
        # Mark all notifications as read after displaying them
        mark_notifications_as_read(user_id)
    else:
        st.write("No new notifications.")
