import streamlit as st
import sqlite3
from utils.email_service import reset_password, generate_password_reset_token, send_email
from datetime import datetime 

# Database connection setup
def get_db_connection():
    try:
        conn = sqlite3.connect('app_database.db')
        conn.row_factory = sqlite3.Row  # Allows access to columns by name
        conn.execute('PRAGMA foreign_keys = ON')  # Enforce foreign key constraints
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None
    
def get_user_id_by_token(token):
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT user_id FROM password_reset_tokens
        WHERE reset_token = ? AND expires_at > ?
    ''', (token, datetime.now()))
    result = cursor.fetchone()
    conn.close()
    
    return result[0] if result else None

def reset_password(user_id, token, new_password):
    conn = get_db_connection()
    if not conn:
        return False
    
    try:
        # Update the password in the users table
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET password = ? WHERE id = ?', (new_password, user_id))
        
        # Delete the used token from password_reset_tokens table
        cursor.execute('DELETE FROM password_reset_tokens WHERE user_id = ? AND reset_token = ?', (user_id, token))
        
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error resetting password: {e}")
        return False
    finally:
        conn.close()

def show_reset_password_page():
    st.title("Reset Password")
    
    token = st.text_input("Enter your reset token")
    new_password = st.text_input("Enter your new password", type="password")
    
    if st.button("Reset Password"):
        user_id = get_user_id_by_token(token)  
        
        if user_id and reset_password(user_id, token, new_password):
            st.success("Your password has been reset successfully.")
        else:
            st.error("Failed to reset password. Invalid token or user.")

def main():
    # Place to call your password reset page
    show_reset_password_page()

if __name__ == "__main__":
    main()
