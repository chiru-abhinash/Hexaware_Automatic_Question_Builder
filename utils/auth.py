from utils.database import fetch_one, execute_query, fetch_all
import pandas as pd

# Authenticate user credentials
def authenticate_user(username, password):
    """Authenticate user credentials and return authentication status, role, and user_id."""
    try:
        query = 'SELECT id, password, role FROM users WHERE username = ?'
        result = fetch_one(query, (username,))
        
        if result and result['password'] == password:
            return True, result['role'], result['id']  # Return True, the user's role, and user_id
        return False, None, None  # Return False if authentication fails
    except Exception as e:
        print(f"Error during authentication: {e}")
        return False, None, None  # Return False if an exception occurs

# Administrator functions for managing users

# Add a new user
def add_user(username, password, role):
    """Add a new user to the database."""
    try:
        # Check if user already exists
        query_check = 'SELECT COUNT(*) FROM users WHERE username = ?'
        result = fetch_one(query_check, (username,))
        
        if result[0] > 0:
            return False  # User already exists

        # Insert new user
        query_insert = 'INSERT INTO users (username, password, role) VALUES (?, ?, ?)'
        return execute_query(query_insert, (username, password, role))
    except Exception as e:
        print(f"Error adding user: {e}")
        return False

# Edit an existing user
def edit_user(username, new_password, new_role):
    """Edit an existing user in the database."""
    try:
        query = 'UPDATE users SET password = ?, role = ? WHERE username = ?'
        success = execute_query(query, (new_password, new_role, username))
        return success
    except Exception as e:
        print(f"Error editing user: {e}")
        return False

# Delete a user from the database
def delete_user(username):
    """Delete a user from the database."""
    try:
        query = 'DELETE FROM users WHERE username = ?'
        success = execute_query(query, (username,))
        return success
    except Exception as e:
        print(f"Error deleting user: {e}")
        return False

# Load all users from the database
def load_users():
    """Load all users from the database."""
    try:
        query = 'SELECT username, role FROM users'
        users = fetch_all(query)
        return pd.DataFrame(users, columns=['username', 'role'])
    except Exception as e:
        print(f"Error loading users: {e}")
        return pd.DataFrame(columns=['username', 'role'])



