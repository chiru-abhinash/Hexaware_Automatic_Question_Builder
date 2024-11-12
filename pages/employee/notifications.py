import streamlit as st
from utils.notifications import get_unseen_notifications, get_all_notifications, mark_notifications_as_read

def show_notifications_page():
    st.title("Employee Notifications")

    # Check if user_id is in session_state
    if 'user_id' not in st.session_state:
        st.error("User not authenticated. Please log in.")
        return

    user_id = st.session_state.user_id

    # Fetch unseen notifications for the current employee
    unseen_notifications = get_unseen_notifications(user_id)
    if unseen_notifications:
        st.subheader("New Notifications")
        for notification in unseen_notifications:
            st.write(f"• {notification['notification_text']} (Received: {notification['sent_at']})")
        # Mark notifications as read after displaying them
        mark_notifications_as_read(user_id)

    # Fetch all notifications for the current employee
    all_notifications = get_all_notifications(user_id)
    if all_notifications:
        st.subheader("All Notifications")
        for notification in all_notifications:
            # Display each notification with a different style based on read status
            if notification['is_read']:
                st.write(f"✓ {notification['notification_text']} (Received: {notification['sent_at']})")
            else:
                st.markdown(f"**• {notification['notification_text']}** _(Received: {notification['sent_at']})_")
    else:
        st.write("No notifications available.")

    # Add a button to refresh notifications or go back to the dashboard
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Refresh Notifications"):
            st.rerun()  # Rerun the page to check for new notifications
    with col2:
        if st.button("Back to Dashboard"):
            st.session_state.page = "employee_dashboard"  # Adjust based on your navigation structure

if __name__ == "__main__":
    show_notifications_page()
