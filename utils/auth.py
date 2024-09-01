import sqlite3

def authenticate_user(username, password):
    """Authenticate user credentials and return authentication status and role."""
    try:
        conn = sqlite3.connect('app_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT password, role FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        conn.close()
        
        if result and result[0] == password:
            return True, result[1]  # Return True and the user's role
        return False, None  # Return False if authentication fails
    except Exception as e:
        print(f"Error during authentication: {e}")
        return False, None  # Return False if an exception occurs
    

import pandas as pd


#administrator pages functions
import sqlite3

def add_user(username, password, role):
    """Add a new user to the database."""
    try:
        conn = sqlite3.connect('app_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM users WHERE username = ?', (username,))
        if cursor.fetchone()[0] > 0:
            return False  # User already exists
        
        cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (username, password, role))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error adding user: {e}")
        return False

def edit_user(username, new_password, new_role):
    """Edit an existing user in the database."""
    try:
        conn = sqlite3.connect('app_database.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET password = ?, role = ? WHERE username = ?', (new_password, new_role, username))
        if cursor.rowcount == 0:
            return False  # User not found
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error editing user: {e}")
        return False

def delete_user(username):
    """Delete a user from the database."""
    try:
        conn = sqlite3.connect('app_database.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE username = ?', (username,))
        if cursor.rowcount == 0:
            return False  # User not found
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error deleting user: {e}")
        return False

def load_users():
    """Load all users from the database."""
    try:
        conn = sqlite3.connect('app_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT username, role FROM users')
        users = cursor.fetchall()
        conn.close()
        return pd.DataFrame(users, columns=['username', 'role'])
    except Exception as e:
        print(f"Error loading users: {e}")
        return pd.DataFrame(columns=['username', 'role'])
