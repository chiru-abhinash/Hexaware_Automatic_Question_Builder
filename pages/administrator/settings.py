import streamlit as st
from utils.database import fetch_one, execute_query

# Function to create the settings table if it doesn't exist
def create_settings_table():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS settings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        setting_name TEXT UNIQUE NOT NULL,
        setting_value TEXT NOT NULL
    );
    """
    execute_query(create_table_query)

def load_settings():
    """Load settings from the database."""
    settings = {}
    for setting_name in ["max_users", "allow_multiple_logins"]:
        result = fetch_one("SELECT setting_value FROM settings WHERE setting_name = ?", (setting_name,))
        settings[setting_name] = result[0] if result else "Default Value"
    return settings

def save_settings(max_users, allow_multiple_logins):
    """Save settings to the database."""
    execute_query("INSERT OR REPLACE INTO settings (setting_name, setting_value) VALUES (?, ?)", ("max_users", max_users))
    execute_query("INSERT OR REPLACE INTO settings (setting_name, setting_value) VALUES (?, ?)", ("allow_multiple_logins", allow_multiple_logins))

def reset_to_default():
    """Reset settings to default values."""
    default_settings = {
        "max_users": "100",  # Default max users
        "allow_multiple_logins": "No"  # Default setting for multiple logins
    }
    save_settings(default_settings["max_users"], default_settings["allow_multiple_logins"])

def show_settings_page():
    create_settings_table()  # Ensure the settings table exists
    
    st.title("Settings")
    
    # Load current settings
    settings = load_settings()
    
    st.subheader("Configure System Settings")
    
    # Configuration options
    max_users = st.text_input("Max Number of Users Allowed", value=settings.get("max_users", ""))
    
    # Handle case where allow_multiple_logins is not in the expected values
    allow_multiple_logins_value = settings.get("allow_multiple_logins", "No")
    if allow_multiple_logins_value not in ["Yes", "No"]:
        allow_multiple_logins_value = "No"  # Default to "No" if not valid
    
    allow_multiple_logins = st.selectbox(
        "Allow Multiple Logins", 
        ["Yes", "No"], 
        index=["Yes", "No"].index(allow_multiple_logins_value)
    )
    
    # Save Changes button
    if st.button("Save Changes"):
        save_settings(max_users, allow_multiple_logins)
        st.success("Settings updated successfully.")
    
    # Reset to Default button
    if st.button("Reset to Default"):
        reset_to_default()
        st.warning("Settings have been reset to default values.")
        st.rerun()  # Reload the page to reflect changes

if __name__ == "__main__":
    show_settings_page()
