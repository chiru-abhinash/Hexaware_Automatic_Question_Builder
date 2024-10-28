# # File: utils/notifications.py
# import sqlite3
# import streamlit as st
# from datetime import datetime

# # Database connection setup
# def get_db_connection():
#     try:
#         conn = sqlite3.connect('app_database.db')
#         conn.row_factory = sqlite3.Row  # Allows access to columns by name
#         conn.execute('PRAGMA foreign_keys = ON')  # Enforce foreign key constraints
#         return conn
#     except sqlite3.Error as e:
#         st.error(f"Database connection failed: {e}")
#         return None

# # Function to fetch unseen notifications for the current user
# def get_unseen_notifications(user_id):
#     conn = get_db_connection()
#     if not conn:
#         return []
#     try:
#         cursor = conn.execute(
#             'SELECT * FROM notifications WHERE user_id = ? AND is_read = FALSE',
#             (user_id,)
#         )
#         notifications = cursor.fetchall()
#         return notifications
#     except sqlite3.Error as e:
#         st.error(f"Failed to fetch notifications: {e}")
#         return []
#     finally:
#         conn.close()

# # Function to mark notifications as read
# def mark_notifications_as_read(user_id):
#     conn = get_db_connection()
#     if not conn:
#         return
#     try:
#         conn.execute(
#             'UPDATE notifications SET is_read = TRUE WHERE user_id = ?',
#             (user_id,)
#         )
#         conn.commit()
#     except sqlite3.Error as e:
#         st.error(f"Failed to update notifications: {e}")
#     finally:
#         conn.close()

# # Function to display notifications
# # File: utils/notifications.py

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

# Function to fetch all notifications for the current user
def get_all_notifications(user_id):
    conn = get_db_connection()
    if not conn:
        return []
    try:
        cursor = conn.execute(
            'SELECT * FROM notifications WHERE user_id = ? ORDER BY sent_at DESC',
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
            'UPDATE notifications SET is_read = TRUE WHERE user_id = ? AND is_read = FALSE',
            (user_id,)
        )
        conn.commit()
    except sqlite3.Error as e:
        st.error(f"Failed to update notifications: {e}")
    finally:
        conn.close()

# Function to add a new notification
def add_notification(user_id, sender_id, notification_text, notification_type=None, priority=0, valid_until=None):
    conn = get_db_connection()
    if not conn:
        return
    try:
        conn.execute(
            'INSERT INTO notifications (user_id, sender_id, notification_text, notification_type, priority, is_read, valid_until) '
            'VALUES (?, ?, ?, ?, ?, FALSE, ?)',
            (user_id, sender_id, notification_text, notification_type, priority, valid_until)
        )
        conn.commit()
    except sqlite3.Error as e:
        st.error(f"Failed to add notification: {e}")
    finally:
        conn.close()

def notify_admins_of_feedback(trainer_id, feedback_text):
    conn = get_db_connection()
    if not conn:
        return
    
    try:
        # Fetch all admin users
        cursor = conn.execute("SELECT id FROM users WHERE role = 'admin'")
        admin_ids = [row['id'] for row in cursor.fetchall()]

        # Create notifications for each admin
        for admin_id in admin_ids:
            conn.execute(
                'INSERT INTO notifications (user_id, sender_id, notification_text, notification_type, priority, is_read) '
                'VALUES (?, ?, ?, ?, ?, FALSE)',
                (admin_id, trainer_id, feedback_text, 'Feedback', 1)
            )

        # Acknowledge the trainer
        conn.execute(
            'INSERT INTO notifications (user_id, sender_id, notification_text, notification_type, priority, is_read) '
            'VALUES (?, ?, ?, ?, ?, FALSE)',
            (trainer_id, trainer_id, "Your feedback has been sent to the admins.", 'Acknowledgment', 1)
        )
        
        conn.commit()

    except sqlite3.Error as e:
        st.error(f"Failed to notify admins: {e}")
    finally:
        conn.close()





# import sqlite3
# import streamlit as st
# from datetime import datetime

# # Database connection setup
# def get_db_connection():
#     try:
#         conn = sqlite3.connect('app_database.db')
#         conn.row_factory = sqlite3.Row  # Allows access to columns by name
#         conn.execute('PRAGMA foreign_keys = ON')  # Enforce foreign key constraints
#         return conn
#     except sqlite3.Error as e:
#         st.error(f"Database connection failed: {e}")
#         return None

# # Function to fetch unseen notifications for the current user
# def get_unseen_notifications(user_id):
#     conn = get_db_connection()
#     if not conn:
#         return []
#     try:
#         cursor = conn.execute(
#             'SELECT * FROM notifications WHERE receiver_id = ? AND is_read = FALSE',
#             (user_id,)
#         )
#         notifications = cursor.fetchall()
#         return notifications
#     except sqlite3.Error as e:
#         st.error(f"Failed to fetch notifications: {e}")
#         return []
#     finally:
#         conn.close()

# # Function to fetch all notifications for the current user
# def get_all_notifications(user_id):
#     conn = get_db_connection()
#     if not conn:
#         return []
#     try:
#         cursor = conn.execute(
#             'SELECT * FROM notifications WHERE receiver_id = ? ORDER BY sent_at DESC',
#             (user_id,)
#         )
#         notifications = cursor.fetchall()
#         return notifications
#     except sqlite3.Error as e:
#         st.error(f"Failed to fetch notifications: {e}")
#         return []
#     finally:
#         conn.close()

# # Function to mark notifications as read
# def mark_notifications_as_read(user_id):
#     conn = get_db_connection()
#     if not conn:
#         return
#     try:
#         conn.execute(
#             'UPDATE notifications SET is_read = TRUE WHERE receiver_id = ? AND is_read = FALSE',
#             (user_id,)
#         )
#         conn.commit()
#     except sqlite3.Error as e:
#         st.error(f"Failed to update notifications: {e}")
#     finally:
#         conn.close()

# # Function to add a new notification
# def add_notification(receiver_id, sender_id, notification_text, notification_type=None, priority=0, valid_until=None):
#     conn = get_db_connection()
#     if not conn:
#         return
#     try:
#         conn.execute(
#             'INSERT INTO notifications (receiver_id, sender_id, notification_text, notification_type, priority, is_read, valid_until) '
#             'VALUES (?, ?, ?, ?, ?, FALSE, ?)',
#             (receiver_id, sender_id, notification_text, notification_type, priority, valid_until)
#         )
#         conn.commit()
#     except sqlite3.Error as e:
#         st.error(f"Failed to add notification: {e}")
#     finally:
#         conn.close()

# # Function to notify admins of feedback
# def notify_admins_of_feedback(trainer_id, feedback_text):
#     conn = get_db_connection()
#     if not conn:
#         return
    
#     try:
#         # Fetch all admin users
#         cursor = conn.execute("SELECT id FROM users WHERE role = 'admin'")
#         admin_ids = [row['id'] for row in cursor.fetchall()]

#         # Create notifications for each admin
#         for admin_id in admin_ids:
#             conn.execute(
#                 'INSERT INTO notifications (receiver_id, sender_id, notification_text, notification_type, priority, is_read) '
#                 'VALUES (?, ?, ?, ?, ?, FALSE)',
#                 (admin_id, trainer_id, feedback_text, 'Feedback', 1)
#             )

#         # Acknowledge the trainer
#         conn.execute(
#             'INSERT INTO notifications (receiver_id, sender_id, notification_text, notification_type, priority, is_read) '
#             'VALUES (?, ?, ?, ?, ?, FALSE)',
#             (trainer_id, trainer_id, "Your feedback has been sent to the admins.", 'Acknowledgment', 1)
#         )
        
#         conn.commit()

#     except sqlite3.Error as e:
#         st.error(f"Failed to notify admins: {e}")
#     finally:
#         conn.close()

# def show_notifications_page(notification_text=None, notification_type=None):
#     st.title("Notifications")
#     user_id = st.session_state.user_id  # Assuming user_id is stored in session state
#     notifications = get_unseen_notifications(user_id)

#     if notification_text:
#         # Display the notification based on type
#         if notification_type == "success":
#             st.success(notification_text)
#         elif notification_type == "error":
#             st.error(notification_text)
#         else:
#             st.info(notification_text)

#     if notifications:
#         for notification in notifications:
#             st.write(f"• {notification['notification_text']} (Received: {notification['sent_at']})")
#         mark_notifications_as_read(user_id)
#     else:
#         st.write("No new notifications.")
