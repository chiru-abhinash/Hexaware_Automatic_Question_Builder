# pages/administrator/settings.py
import streamlit as st
import json
import os

SETTINGS_FILE = "settings.json"

def load_settings():
    """Load settings from a JSON file."""
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as file:
            return json.load(file)
    return {"setting_1": "Value 1", "setting_2": "Value 2"}

def save_settings(settings):
    """Save settings to a JSON file."""
    with open(SETTINGS_FILE, 'w') as file:
        json.dump(settings, file, indent=4)

def show_settings_page():
    st.title("Settings")
    
    # Load current settings
    settings = load_settings()
    
    st.subheader("System Configuration")
    setting_1 = st.text_input("Configuration Setting 1", value=settings.get("setting_1", ""))
    setting_2 = st.text_input("Configuration Setting 2", value=settings.get("setting_2", ""))
    
    # Save changes
    if st.button("Save Changes"):
        new_settings = {
            "setting_1": setting_1,
            "setting_2": setting_2
        }
        save_settings(new_settings)
        st.success("Settings updated successfully.")
    
    # Reset to default values
    if st.button("Reset to Default"):
        default_settings = {"setting_1": "Value 1", "setting_2": "Value 2"}
        save_settings(default_settings)
        st.warning("Settings reset to default values.")
        st.experimental_rerun()  # Reload the page to reflect changes

if __name__ == "__main__":
    show_settings_page()
