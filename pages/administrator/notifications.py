import streamlit as st
import sqlite3
from utils.notifications import get_unseen_notifications, mark_notifications_as_seen

def show_notifications_page():
    """Display the notifications page for the admin."""
    st.title("Notifications")

    # Assuming the user_id is stored in session state
    user_id = st.session_state.user_id
    unseen_notifications = get_unseen_notifications(user_id)

    if unseen_notifications:
        st.subheader("Unseen Notifications")
        for notification in unseen_notifications:
            st.write(f"**Notification ID:** {notification['id']}")
            st.write(f"**Message:** {notification['message']}")
            st.write(f"**Timestamp:** {notification['timestamp']}")
            # Optionally, a button to mark as seen
            if st.button(f"Mark as Seen (ID: {notification['id']})"):
                mark_notifications_as_seen(notification['id'])
                st.success("Notification marked as seen!")
    else:
        st.write("No new notifications.")

    # Optionally, a section to view all notifications
    if st.button("View All Notifications"):
        all_notifications = get_all_notifications(user_id)  # Implement this function to get all notifications
        if all_notifications:
            st.subheader("All Notifications")
            for notification in all_notifications:
                st.write(f"**Notification ID:** {notification['id']}")
                st.write(f"**Message:** {notification['message']}")
                st.write(f"**Timestamp:** {notification['timestamp']}")
                st.write("---")
        else:
            st.write("No notifications available.")

def get_all_notifications(user_id):
    """Retrieve all notifications for a user."""
    # Replace this with the actual logic to fetch notifications from your database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notifications WHERE user_id = ?", (user_id,))
    notifications = cursor.fetchall()
    conn.close()

    # Convert to a list of dictionaries for easier access
    return [{'id': n[0], 'message': n[1], 'timestamp': n[3]} for n in notifications]

def mark_notifications_as_seen(notification_id):
    """Mark a notification as seen."""
    # Replace this with the actual logic to mark a notification as seen in your database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE notifications SET seen = 1 WHERE id = ?", (notification_id,))
    conn.commit()
    conn.close()
