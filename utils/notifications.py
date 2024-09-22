# File: utils/notifications.py
import sqlite3
import streamlit as st
from datetime import datetime

# Database connection setup
def get_db_connection():
    try:
        conn = sqlite3.connect('app_database.db')
        conn.row_factory = sqlite3.Row  # Allows access to columns by name
        conn.execute('PRAGMA foreign_keys = ON')  # Enforce foreign key constraints
        return conn
    except sqlite3.Error as e:
        st.error(f"Database connection failed: {e}")
        return None

# Function to fetch unseen notifications for the current user
def get_unseen_notifications(user_id):
    conn = get_db_connection()
    if not conn:
        return []
    try:
        cursor = conn.execute(
            'SELECT * FROM notifications WHERE user_id = ? AND is_read = FALSE',
            (user_id,)
        )
        notifications = cursor.fetchall()
        return notifications
    except sqlite3.Error as e:
        st.error(f"Failed to fetch notifications: {e}")
        return []
    finally:
        conn.close()

# Function to mark notifications as read
def mark_notifications_as_read(user_id):
    conn = get_db_connection()
    if not conn:
        return
    try:
        conn.execute(
            'UPDATE notifications SET is_read = TRUE WHERE user_id = ?',
            (user_id,)
        )
        conn.commit()
    except sqlite3.Error as e:
        st.error(f"Failed to update notifications: {e}")
    finally:
        conn.close()

# Function to display notifications
# File: utils/notifications.py

def show_notifications_page(notification_text=None, notification_type=None):
    st.title("Notifications")
    user_id = st.session_state.user_id  # Assuming user_id is stored in session state
    notifications = get_unseen_notifications(user_id)

    if notification_text:
        # Display the notification based on type
        if notification_type == "success":
            st.success(notification_text)
        elif notification_type == "error":
            st.error(notification_text)
        else:
            st.info(notification_text)

    if notifications:
        for notification in notifications:
            st.write(f"• {notification['notification_text']} (Received: {notification['sent_at']})")
        mark_notifications_as_read(user_id)
    else:
        st.write("No new notifications.")

