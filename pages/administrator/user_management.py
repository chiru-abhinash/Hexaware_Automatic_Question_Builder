import streamlit as st
import pandas as pd
import sqlite3

# Database functions
def create_connection():
    return sqlite3.connect('app_database.db')

def load_users():
    conn = create_connection()
    users_df = pd.read_sql_query('SELECT username, role FROM users', conn)
    conn.close()
    return users_df

def get_user_details(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT password, role FROM users WHERE username = ?', (username,))
    user_data = cursor.fetchone()
    conn.close()
    return user_data

def edit_user(username, new_password=None, new_role=None):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        if new_password:
            cursor.execute('UPDATE users SET password = ? WHERE username = ?', (new_password, username))
        if new_role:
            cursor.execute('UPDATE users SET role = ? WHERE username = ?', (new_role, username))
        conn.commit()
        return True
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
    col2, col3 = st.columns([1, 1])

    # Remove the Form to Add New User
    # The functionality to add a user is removed

    # Form to Edit User
    with col2:
        st.subheader("Edit User")
        if usernames:
            selected_user = st.selectbox("Select User", usernames, key='selected_user')

            if selected_user:
                # Load the current details of the selected user
                user_details = get_user_details(selected_user)
                if user_details:
                    current_password, current_role = user_details

                    # Pre-fill with current user data
                    with st.form(key='edit_user_form'):
                        new_password = st.text_input("New Password (Leave blank to keep current)", type="password", value="", key='new_password_edit')
                        new_role = st.selectbox("New Role", ["Administrator", "Trainer", "Employee"], 
                                                index=["Administrator", "Trainer", "Employee"].index(current_role), 
                                                key='new_role_edit')
                        submit_button = st.form_submit_button(label='Update User')

                        if submit_button:
                            # Only update fields that were modified
                            updated_password = new_password if new_password else None
                            updated_role = new_role if new_role != current_role else None

                            if edit_user(selected_user, updated_password, updated_role):
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
