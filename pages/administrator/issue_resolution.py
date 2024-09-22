import streamlit as st
import pandas as pd
from utils.database import fetch_all, execute_query, get_db_connection

def load_issues():
    """Load issues from the database and return as a DataFrame."""
    query = "SELECT * FROM issue_resolution"
    results = fetch_all(query)
    
    if results:
        columns = [column[0] for column in get_db_connection().execute(query).description]
        return pd.DataFrame(results, columns=columns)
    
    return pd.DataFrame()

def create_issue_from_feedback(user_id, issue_description):
    """Create a new issue in the issue_resolution table from feedback."""
    query = """
    INSERT INTO issue_resolution (reported_by, issue_description, resolution_status)
    VALUES (?, ?, 'Pending')
    """
    execute_query(query, (user_id, issue_description))

def update_issue_resolution(issue_id, resolution_notes, resolution_status):
    """Update the issue resolution notes and status."""
    query = """
    UPDATE issue_resolution
    SET resolution_notes = ?, resolution_status = ?, resolved_at = CURRENT_TIMESTAMP
    WHERE id = ?
    """
    try:
        execute_query(query, (resolution_notes, resolution_status, issue_id))
        st.success(f"Updated Issue ID {issue_id}: Status={resolution_status}, Notes={resolution_notes}")
    except Exception as e:
        st.error(f"Error updating issue: {e}")

def load_feedback():
    """Load feedback from the database and return as a DataFrame."""
    query = "SELECT * FROM feedback"
    results = fetch_all(query)
    
    if results:
        columns = [column[0] for column in get_db_connection().execute(query).description]
        return pd.DataFrame(results, columns=columns)
    
    return pd.DataFrame()

def show_issue_resolution_page():
    st.title("Issue Resolution")

    # Load and display feedback
    st.subheader("Feedback")
    feedback_df = load_feedback()
    st.dataframe(feedback_df)
    
    if feedback_df.empty:
        st.warning("No feedback found.")
    else:
        selected_feedback_id = st.selectbox("Select Feedback to Convert to Issue", feedback_df["id"])

        # Get the selected feedback details
        selected_feedback = feedback_df[feedback_df["id"] == selected_feedback_id]
        
        if not selected_feedback.empty:
            feedback_row = selected_feedback.iloc[0]
            st.write(f"**Feedback ID:** {feedback_row['id']}")
            st.write(f"**User ID:** {feedback_row['user_id']}")
            st.write(f"**Feedback Type:** {feedback_row['feedback_type']}")
            st.write(f"**Feedback Text:** {feedback_row['feedback_text']}")
        
            # Form to create an issue from the selected feedback
            if st.button("Create Issue from Feedback"):
                user_id = st.session_state.user_id  # Get user_id from session state
                if user_id is not None:
                    create_issue_from_feedback(user_id, feedback_row['feedback_text'])
                    st.success(f"Issue has been created from feedback ID {feedback_row['id']}.")
                else:
                    st.error("User ID is not available. Cannot create issue.")
                st.experimental_rerun()

    # Load and display existing issues
    st.subheader("Existing Issues")
    issues_df = load_issues()
    st.dataframe(issues_df)
    
    if issues_df.empty:
        st.warning("No issues found.")
    else:
        selected_issue_id = st.selectbox("Select Issue to Edit", issues_df["id"])
        selected_issue = issues_df[issues_df["id"] == selected_issue_id]

        if not selected_issue.empty:
            issue_row = selected_issue.iloc[0]
            st.write(f"**Issue ID:** {issue_row['id']}")
            st.write(f"**Reported By:** {issue_row['reported_by']}")
            st.write(f"**Issue Description:** {issue_row['issue_description']}")
            st.write(f"**Resolution Status:** {issue_row['resolution_status']}")
            st.write(f"**Resolution Notes:** {issue_row.get('resolution_notes', 'No notes added.')}")

            # Input for resolution notes
            resolution_notes = st.text_area("Add/Edit Resolution Notes", value=issue_row.get('resolution_notes', ''))

            # Dropdown for resolution status
            resolution_status = st.selectbox("Select Resolution Status", ["Pending", "Resolved"], 
                                              index=["Pending", "Resolved"].index(issue_row['resolution_status']))
            
            if st.button("Update Issue Resolution"):
                update_issue_resolution(issue_row['id'], resolution_notes, resolution_status)
                st.rerun()  # Refresh to show updated data

if __name__ == "__main__":
    show_issue_resolution_page()
