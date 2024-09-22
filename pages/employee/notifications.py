import streamlit as st
from utils.notifications import get_unseen_notifications, mark_notifications_as_read

def show_notifications_page():
    st.title("Employee Notifications")
    
    # Check if user_id is in session_state
    if 'user_id' not in st.session_state:
        st.error("User not authenticated. Please log in.")
        return

    user_id = st.session_state.user_id
    notifications = get_unseen_notifications(user_id)

    if notifications:
        for notification in notifications:
            st.write(f"• {notification['notification_text']} (Received: {notification['sent_at']})")
        # Mark notifications as read after displaying them
        mark_notifications_as_read(user_id)
    else:
        st.write("No new notifications.")

    # Add a button to go back to the employee dashboard
    if st.button("Back to Dashboard"):
        st.session_state.page = "employee_dashboard"  # Adjust based on your navigation structure

if __name__ == "__main__":
    show_notifications_page()
