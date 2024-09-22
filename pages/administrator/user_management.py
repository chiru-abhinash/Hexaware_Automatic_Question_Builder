import streamlit as st
import pandas as pd
import sqlite3

# Database functions
def create_connection():
    return sqlite3.connect('app_database.db')

def add_user(username, password, role):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (username, password, role))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def load_users():
    conn = create_connection()
    users_df = pd.read_sql_query('SELECT username, role FROM users', conn)
    conn.close()
    return users_df

def edit_user(username, new_password, new_role):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('UPDATE users SET password = ?, role = ? WHERE username = ?', (new_password, new_role, username))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        return False
    finally:
        conn.close()

def delete_user(username):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM users WHERE username = ?', (username,))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        return False
    finally:
        conn.close()

# Streamlit UI
def show_user_management_page():
    st.title("User Management")

    # Refresh user list before displaying it
    users_df = load_users()
    usernames = users_df['username'].tolist()

    # Display all forms in columns
    col1, col2, col3 = st.columns([1, 1, 1])

    # Form to Add New User
    with col1:
        st.subheader("Add New User")
        with st.form(key='add_user_form'):
            new_username = st.text_input("Username", key='new_username')
            new_password = st.text_input("Password", type="password", key='new_password')
            role = st.selectbox("Role", ["Administrator", "Trainer", "Employee"], key='role')
            submit_button = st.form_submit_button(label='Add User')
            
            if submit_button:
                if add_user(new_username, new_password, role):
                    st.success("User added successfully.")
                    st.rerun()  # Refresh the page after successful add
                else:
                    st.error("User already exists or could not be added.")

    # Form to Edit User
    with col2:
        st.subheader("Edit User")
        if usernames:
            with st.form(key='edit_user_form'):
                selected_user = st.selectbox("Select User", usernames, key='selected_user')
                new_password = st.text_input("New Password", type="password", key='new_password_edit')
                new_role = st.selectbox("New Role", ["Administrator", "Trainer", "Employee"], key='new_role_edit')
                submit_button = st.form_submit_button(label='Update User')

                if submit_button:
                    if edit_user(selected_user, new_password, new_role):
                        st.success("User updated successfully.")
                        st.rerun()  # Refresh the page after successful edit
                    else:
                        st.error("User could not be updated.")
        else:
            st.warning("No users available for editing.")

    # Form to Delete User
    with col3:
        st.subheader("Delete User")
        if usernames:
            with st.form(key='delete_user_form'):
                selected_user = st.selectbox("Select User to Delete", usernames, key='selected_user_delete')
                submit_button = st.form_submit_button(label='Delete User')

                if submit_button:
                    if delete_user(selected_user):
                        st.success("User deleted successfully.")
                        st.rerun()  # Refresh the page after successful delete
                    else:
                        st.error("User could not be deleted.")
        else:
            st.warning("No users available for deletion.")

    # View Current Users
    st.subheader("Current Users")
    st.dataframe(users_df)

if __name__ == "__main__":
    show_user_management_page()
