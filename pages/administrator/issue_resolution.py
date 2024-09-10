# pages/administrator/issue_resolution.py
import streamlit as st
import pandas as pd

# Function to load issues from CSV
def load_issues(file_path="data/issues.csv"):
    return pd.read_csv(file_path)

# Function to save updates to the issues CSV
def save_issues(df, file_path="data/issues.csv"):
    df.to_csv(file_path, index=False)

def show_issue_resolution_page():
    st.title("Issue Resolution")
    
    # Load issues from CSV
    issues_df = load_issues()
    st.dataframe(issues_df)
    
    # Select issue to resolve
    selected_issue_id = st.selectbox("Select Issue to Resolve", issues_df["Issue ID"])
    
    # Get the selected issue details
    selected_issue = issues_df[issues_df["Issue ID"] == selected_issue_id]
    
    if not selected_issue.empty:
        issue_row = selected_issue.iloc[0]
        st.write(f"**Issue ID:** {issue_row['Issue ID']}")
        st.write(f"**Description:** {issue_row['Description']}")
        st.write(f"**Status:** {issue_row['Status']}")
    
    # Form to assign issue to support
    if st.button("Assign to Support"):
        issues_df.loc[issues_df["Issue ID"] == selected_issue_id, "Status"] = "Assigned to Support"
        save_issues(issues_df)
        st.success(f"Issue {selected_issue_id} has been assigned to the support team.")
    
    # Text area for comments
    comments = st.text_area("Comments")
    
    # Form to resolve issue
    if st.button("Resolve Issue"):
        issues_df.loc[issues_df["Issue ID"] == selected_issue_id, "Status"] = "Resolved"
        if comments:
            issues_df.loc[issues_df["Issue ID"] == selected_issue_id, "Comments"] = comments
        else:
            issues_df.loc[issues_df["Issue ID"] == selected_issue_id, "Comments"] = "No comments provided."
        save_issues(issues_df)
        st.success(f"Issue {selected_issue_id} has been marked as resolved.")

if __name__ == "__main__":
    show_issue_resolution_page()
