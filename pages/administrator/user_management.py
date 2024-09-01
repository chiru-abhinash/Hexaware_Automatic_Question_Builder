import streamlit as st
import pandas as pd
from utils.auth import add_user, load_users, edit_user, delete_user

def show_user_management_page():
    st.title("User Management")

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
                else:
                    st.error("User already exists or could not be added.")
                st.experimental_rerun()  # Refresh the page to reflect changes
    
    # Form to Edit User
    with col2:
        st.subheader("Edit User")
        with st.form(key='edit_user_form'):
            users_df = load_users()
            usernames = users_df['username'].tolist()
            selected_user = st.selectbox("Select User", usernames, key='selected_user')
            new_password = st.text_input("New Password", type="password", key='new_password_edit')
            new_role = st.selectbox("New Role", ["Administrator", "Trainer", "Employee"], key='new_role_edit')
            submit_button = st.form_submit_button(label='Update User')
            
            if submit_button:
                if edit_user(selected_user, new_password, new_role):
                    st.success("User updated successfully.")
                else:
                    st.error("User could not be updated.")
                st.experimental_rerun()  # Refresh the page to reflect changes

    # Form to Delete User
    with col3:
        st.subheader("Delete User")
        with st.form(key='delete_user_form'):
            users_df = load_users()
            usernames = users_df['username'].tolist()
            selected_user = st.selectbox("Select User to Delete", usernames, key='selected_user_delete')
            submit_button = st.form_submit_button(label='Delete User')
            
            if submit_button:
                if delete_user(selected_user):
                    st.success("User deleted successfully.")
                else:
                    st.error("User could not be deleted.")
                st.experimental_rerun()  # Refresh the page to reflect changes

    # View Current Users
    st.subheader("Current Users")
    users_df = load_users()
    st.dataframe(users_df)

if __name__ == "__main__":
    show_user_management_page()
