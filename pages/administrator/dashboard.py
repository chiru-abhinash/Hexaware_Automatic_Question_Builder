# File: pages/administrator/admin_dashboard.py
# import streamlit as st
# from utils.notifications import get_unseen_notifications, show_notifications_page
# from pages.administrator.user_management import show_user_management_page
# from pages.administrator.system_monitoring import show_system_monitoring_page
# from pages.administrator.report_generation import show_report_generation_page
# from pages.administrator.settings import show_settings_page
# from pages.administrator.issue_resolution import show_issue_resolution_page
# from pages.administrator.add_user import show_add_user_page  # Importing the add_user function

# def logout():
#     """Handle user logout and redirect to the login page."""
#     st.session_state.authenticated = False
#     st.session_state.role = None
#     st.session_state.username = ''
#     st.session_state.page = "login"
#     st.rerun()  # Rerun the app to redirect to the login page

# def show_admin_dashboard():
#     st.title("Administrator Dashboard")
#     st.write(f"Welcome, {st.session_state.username}")

#     # Fetch unseen notifications
#     user_id = st.session_state.user_id  # Assuming user_id is stored in session state
#     unseen_notifications = get_unseen_notifications(user_id)

#     st.subheader("Quick Links")
    
#     # Create a dictionary to map buttons to their corresponding pages
#     pages = {
#         "User Management": "user_management",
#         "Add User": "add_user",  # Link to Add User page
#         "System Monitoring": "system_monitoring",
#         "Report Generation": "report_generation",
#         "Settings": "settings",
#         "Issue Resolution": "issue_resolution",
#     }

#     # Add the notifications button with dynamic color
#     if unseen_notifications:
#         if st.button("Notifications", key="notifications", help="You have new notifications", 
#                      style="background-color: green; color: white;"):
#             st.session_state.page = "notifications"
#     else:
#         if st.button("Notifications", key="notifications", help="No new notifications"):
#             st.session_state.page = "notifications"

#     # Loop through pages to create buttons dynamically
#     for label, page in pages.items():
#         if st.button(label):
#             st.session_state.page = page

#     # Logout button is outside the loop
#     if st.button("Logout"):
#         logout()  # Directly call the logout function

#     # Load the correct page based on session state
#     if 'page' in st.session_state:
#         if st.session_state.page == "user_management":
#             show_user_management_page()
#         elif st.session_state.page == "add_user":
#             show_add_user_page()  # Call the function to display the add user page
#         elif st.session_state.page == "system_monitoring":
#             show_system_monitoring_page()
#         elif st.session_state.page == "report_generation":
#             show_report_generation_page()
#         elif st.session_state.page == "settings":
#             show_settings_page()
#         elif st.session_state.page == "issue_resolution":
#             show_issue_resolution_page()
#         elif st.session_state.page == "notifications":
#             show_notifications_page()  # Ensure notifications page is handled

# if __name__ == "__main__":
#     show_admin_dashboard()



import streamlit as st
from utils.notifications import get_unseen_notifications, show_notifications_page
from pages.administrator.user_management import show_user_management_page
from pages.administrator.system_monitoring import show_system_monitoring_page
from pages.administrator.report_generation import show_report_generation_page
from pages.administrator.settings import show_settings_page
from pages.administrator.issue_resolution import show_issue_resolution_page
from pages.administrator.add_user import show_add_user_page  # Importing the add_user function

def logout():
    """Handle user logout and redirect to the login page."""
    st.session_state.authenticated = False
    st.session_state.role = None
    st.session_state.username = ''
    st.session_state.page = "login"
    st.rerun()  # Rerun the app to redirect to the login page

def show_admin_dashboard():
    st.title("Administrator Dashboard")
    st.write(f"Welcome, {st.session_state.username}")

    # Fetch unseen notifications
    user_id = st.session_state.user_id  # Assuming user_id is stored in session state
    unseen_notifications = get_unseen_notifications(user_id)

    st.subheader("Quick Links")
    
    # Create a dictionary to map buttons to their corresponding pages
    pages = {
        "User Management": "user_management",
        "Add User": "add_user",  # Link to Add User page
        "System Monitoring": "system_monitoring",
        "Report Generation": "report_generation",
        "Settings": "settings",
        "Issue Resolution": "issue_resolution",
    }

    # Add the notifications button with dynamic color
    if unseen_notifications:
        if st.button("Notifications", key="notifications", help="You have new notifications"):
            st.session_state.page = "notifications"
    else:
        if st.button("Notifications", key="notifications", help="No new notifications"):
            st.session_state.page = "notifications"

    # Loop through pages to create buttons dynamically
    for label, page in pages.items():
        if st.button(label):
            st.session_state.page = page

    # Logout button is outside the loop
    if st.button("Logout"):
        logout()  # Directly call the logout function

    # Load the correct page based on session state
    if 'page' in st.session_state:
        if st.session_state.page == "user_management":
            show_user_management_page()
        elif st.session_state.page == "add_user":
            show_add_user_page()  # Call the function to display the add user page
        elif st.session_state.page == "system_monitoring":
            show_system_monitoring_page()
        elif st.session_state.page == "report_generation":
            show_report_generation_page()
        elif st.session_state.page == "settings":
            show_settings_page()
        elif st.session_state.page == "issue_resolution":
            show_issue_resolution_page()
        elif st.session_state.page == "notifications":
            show_notifications_page()  # Ensure notifications page is handled

if __name__ == "__main__":
    show_admin_dashboard()









# File: pages/administrator/admin_dashboard.py
#USE FOR TAB LAYOUT
# import streamlit as st
# from utils.notifications import get_unseen_notifications, show_notifications_page
# from pages.administrator.user_management import show_user_management_page
# from pages.administrator.system_monitoring import show_system_monitoring_page
# from pages.administrator.report_generation import show_report_generation_page
# from pages.administrator.settings import show_settings_page
# from pages.administrator.issue_resolution import show_issue_resolution_page
# from pages.administrator.add_user import show_add_user_page  # Importing the add_user function

# def logout():
#     """Handle user logout and redirect to the login page."""
#     st.session_state.authenticated = False
#     st.session_state.role = None
#     st.session_state.username = ''
#     st.session_state.page = "login"
#     st.rerun()  # Rerun the app to redirect to the login page

# def show_admin_dashboard():
#     st.title("Administrator Dashboard")
#     st.write(f"Welcome, {st.session_state.username}")

#     # Fetch unseen notifications
#     user_id = st.session_state.user_id  # Assuming user_id is stored in session state
#     unseen_notifications = get_unseen_notifications(user_id)

#     # Create tabs for different functionalities with increased font size
#     tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
#         ["User Management", "Add User", "System Monitoring", 
#          "Report Generation", "Settings", "Issue Resolution", 
#          "Notifications", "Logout"]
#     )

#     # Display the appropriate content in each tab
#     with tab1:
#         show_user_management_page()
    
#     with tab2:
#         show_add_user_page()  # Call the function to display the add user page
    
#     with tab3:
#         show_system_monitoring_page()
    
#     with tab4:
#         show_report_generation_page()
    
#     with tab5:
#         show_settings_page()
    
#     with tab6:
#         show_issue_resolution_page()
    
#     with tab7:
#         show_notifications_page()  # Ensure notifications page is handled

#     with tab8:  # Logout tab
#         st.write("You have been logged out. Thank you!")
#         if st.button("Confirm Logout"):
#             logout()  # Directly call the logout function

#     # Style the tabs with larger font size using Markdown
#     st.markdown("""
#         <style>
#             .streamlit-expanderHeader {
#                 font-size: 20px;  /* Adjust the size as needed */
#             }
#             .stTabs [data-baseweb="tab"] {
#                 font-size: 18px;  /* Tab name font size */
#             }
#         </style>
#         """, unsafe_allow_html=True)

# if __name__ == "__main__":
#     show_admin_dashboard()
