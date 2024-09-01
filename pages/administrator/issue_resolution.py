# pages/administrator/issue_resolution.py
import streamlit as st
import pandas as pd
from utils.notifications import display_notification
def show_issue_resolution_page():
    st.title("Issue Resolution")
    
    issues_df = pd.read_csv("data/issues.csv")  # Assuming you have an issues.csv file
    st.dataframe(issues_df)
    
    selected_issue = st.selectbox("Select Issue to Resolve", issues_df["Issue ID"])
    
    if st.button("Assign to Support"):
        st.success(f"Issue {selected_issue} has been assigned to the support team.")
    
    st.text_area("Comments")
    
    if st.button("Resolve Issue"):
        st.success(f"Issue {selected_issue} has been marked as resolved.")

if __name__ == "__main__":
    show_issue_resolution_page()
    