import streamlit as st
from utils.notifications import get_unseen_notifications, get_all_notifications, mark_notifications_as_read

def show_notifications_page():
    st.title("Trainer Notifications")

    # Check if user_id is in session_state
    if 'user_id' not in st.session_state:
        st.error("User not authenticated. Please log in.")
        return

    user_id = st.session_state.user_id

    # Fetch unseen notifications for the current trainer
    unseen_notifications = get_unseen_notifications(user_id)
    if unseen_notifications:
        st.subheader("New Notifications")
        for notification in unseen_notifications:
            st.write(f"• {notification['notification_text']} (Received: {notification['sent_at']})")
        # Mark notifications as read after displaying them
        mark_notifications_as_read(user_id)

    # Fetch all notifications for the current trainer
    all_notifications = get_all_notifications(user_id)
    if all_notifications:
        st.subheader("All Notifications")
        for notification in all_notifications:
            # Display each notification with a different style based on read status
            if notification['is_read']:
                st.write(f"✓ {notification['notification_text']} (Received: {notification['sent_at']})")
            else:
                st.write(f"• {notification['notification_text']} (Received: {notification['sent_at']})")
    else:
        st.write("No notifications available.")

    # Add a button to go back to the trainer dashboard
    if st.button("Back to Dashboard"):
        st.session_state.page = "trainer_dashboard"  # Adjust based on your navigation structure

if __name__ == "__main__":
    show_notifications_page()
