import streamlit as st
import sqlite3

# Database functions
def create_connection():
    try:
        conn = sqlite3.connect('app_database.db')
        return conn
    except Exception as e:
        st.error(f"Error connecting to database: {e}")

def add_user(username, password, role):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        # Only add the user if username is not empty
        if username.strip():
            cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (username, password, role))
            conn.commit()
            return True
        else:
            st.error("Username cannot be empty.")
            return False
    except sqlite3.IntegrityError:
        st.error(f"User '{username}' already exists. Please choose a different username.")
        return False
    except Exception as e:
        st.error(f"Error adding user '{username}': {e}")
        return False
    finally:
        conn.close()

# Streamlit UI
def show_add_user_page():
    st.title("Add New User")

    # Clear the session state values for a fresh start
    if 'new_username' not in st.session_state:
        st.session_state.new_username = ''
    if 'new_password' not in st.session_state:
        st.session_state.new_password = ''
    if 'role' not in st.session_state:
        st.session_state.role = 'Administrator'  # Default role

    # Form to add new user
    with st.form(key='add_user_form'):
        new_username = st.text_input("Username", value=st.session_state.new_username)
        new_password = st.text_input("Password", type="password", value=st.session_state.new_password)
        role = st.selectbox("Role", ["Administrator", "Trainer", "Employee"], index=["Administrator", "Trainer", "Employee"].index(st.session_state.role))
        
        # Submit button inside the form
        submit_button = st.form_submit_button(label='Add User')

        if submit_button:
            # Store the values in session state for persistence
            st.session_state.new_username = new_username
            st.session_state.new_password = new_password
            st.session_state.role = role
            
            if add_user(new_username, new_password, role):
                st.success("User added successfully.")
                # Clear the input fields
                st.session_state.new_username = ''
                st.session_state.new_password = ''
                st.session_state.role = 'Administrator'  # Reset to default role
                # Optionally, display the updated user list
                display_users()
            else:
                st.error("Failed to add user.")

def display_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT username, role FROM users')
    users = cursor.fetchall()
    conn.close()
    
    if users:
        st.subheader("Current Users")
        for username, role in users:
            st.write(f"Username: {username}, Role: {role}")
    else:
        st.write("No users found.")

if __name__ == "__main__":
    show_add_user_page()
