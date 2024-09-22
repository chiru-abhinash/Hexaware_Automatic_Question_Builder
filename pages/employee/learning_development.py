import streamlit as st
import sqlite3

# Function to load data from the learning_resources table
def load_resources():
    conn = sqlite3.connect('app_database.db')
    query = "SELECT id, resource_name, resource_type FROM learning_resources"
    resources = conn.execute(query).fetchall()
    conn.close()
    return resources

# Function to track progress for a specific resource
def track_progress(user_id, resource_id, progress_value):
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    query = '''
        INSERT INTO learning_progress (user_id, resource_id, progress, updated_at)
        VALUES (?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(user_id, resource_id) DO UPDATE SET 
            progress=excluded.progress, 
            updated_at=CURRENT_TIMESTAMP;
    '''
    cursor.execute(query, (user_id, resource_id, progress_value))
    conn.commit()
    conn.close()

# Main function for the Learning and Development page
def learning_development():
    st.title("Learning and Development")

    # Retrieve user ID from session state
    user_id = st.session_state.get('user_id')

    if user_id is None:
        st.error("User not logged in. Please log in to access resources.")
        return

    # Load resources from the database
    resources = load_resources()

    if resources:
        # Create a form for tracking progress
        with st.form(key='progress_form'):
            selected_resource_id = st.selectbox("Select a resource to track progress", [r[0] for r in resources], format_func=lambda x: next(r[1] for r in resources if r[0] == x))

            # Get the selected resource details
            selected_resource = next(r for r in resources if r[0] == selected_resource_id)
            st.write(f"You have selected: **{selected_resource[1]}** ({selected_resource[2]})")

            # Progress slider
            progress_value = st.slider("Set progress for this resource:", 0, 100, 50)  # Default to 50%

            # Submit button
            submit_button = st.form_submit_button("Track Progress")
            if submit_button:
                track_progress(user_id, selected_resource_id, progress_value)
                st.success(f"Progress for '{selected_resource[1]}' tracked successfully at {progress_value}%!")
    else:
        st.warning("No resources available at the moment.")

# Show the learning development dashboard
if __name__ == "__main__":
    learning_development()
