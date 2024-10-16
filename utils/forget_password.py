import streamlit as st
import sqlite3
from utils.email_service import send_email, generate_password_reset_token

def create_connection():
    """Create a database connection."""
    try:
        conn = sqlite3.connect('app_database.db')
        return conn
    except Exception as e:
        st.error(f"Error connecting to database: {e}")

def show_forget_password_page():
    st.title("Forgot Password")
    
    # Input field for email
    email = st.text_input("Enter your email address:", key='reset_email')
    
    if st.button("Submit Email for Password Reset"):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            reset_token = generate_password_reset_token(user[0])  # Get user_id
            reset_link = f"http://localhost:8501/reset_password?token={reset_token}"
            send_email(email, "Password Reset Request", f"Click here to reset your password: {reset_link}")
            st.info("Password recovery email has been sent.")
        else:
            st.error("No user found with this email address.")

if __name__ == "__main__":
    show_forget_password_page()
