# data/db_utils.py
import sqlite3

def get_connection():
    return sqlite3.connect('app_database.db')

def get_user_by_username(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

def insert_feedback(user_id, feedback_text):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO feedback (user_id, feedback_text) VALUES (?, ?)', (user_id, feedback_text))
    conn.commit()
    conn.close()

def get_feedback_for_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM feedback WHERE user_id = ?', (user_id,))
    feedback = cursor.fetchall()
    conn.close()
    return feedback

# Additional utility functions can be added here
