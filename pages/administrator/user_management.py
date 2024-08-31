# pages/administrator/user_management.py
import streamlit as st
import pandas as pd
from utils.auth import add_user, load_users

def show_user_management_page():
    st.title("User Management")
    
    st.subheader("Add New User")
    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["Administrator", "Trainer", "Employee"])
    
    if st.button("Add User"):
        if add_user(new_username, new_password, role):
            st.success("User added successfully.")
        else:
            st.error("User already exists.")
    
    st.subheader("Current Users")
    users_df = load_users()
    st.dataframe(users_df)

if __name__ == "__main__":
    show_user_management_page()
