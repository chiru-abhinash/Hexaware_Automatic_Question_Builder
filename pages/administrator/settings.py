# pages/administrator/settings.py
import streamlit as st

def show_settings_page():
    st.title("Settings")
    
    st.subheader("System Configuration")
    setting_1 = st.text_input("Configuration Setting 1", "Value 1")
    setting_2 = st.text_input("Configuration Setting 2", "Value 2")
    
    if st.button("Save Changes"):
        st.success("Settings updated successfully.")
    
    if st.button("Reset to Default"):
        st.warning("Settings reset to default values.")

if __name__ == "__main__":
    show_settings_page()
