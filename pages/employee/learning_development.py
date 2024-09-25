import streamlit as st
import sqlite3
import pandas as pd

# Function to load data from the learning_resources table
def load_resources():
    conn = sqlite3.connect('app_database.db')
    query = "SELECT id, resource_name, resource_type, resource_content, category, difficulty_level, author, url FROM learning_resources"
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
        # Filter options
        resource_types = list(set(r[2] for r in resources))  # Unique resource types
        difficulty_levels = list(set(r[5] for r in resources))  # Unique difficulty levels

        selected_type = st.sidebar.multiselect("Filter by Resource Type", resource_types, default=resource_types)
        selected_difficulty = st.sidebar.multiselect("Filter by Difficulty Level", difficulty_levels, default=difficulty_levels)

        # Filter resources based on selection
        filtered_resources = [r for r in resources if r[2] in selected_type and r[5] in selected_difficulty]

        # Display resources in a more interactive format
        for resource in filtered_resources:
            resource_id, name, resource_type, content, category, difficulty, author, url = resource
            with st.expander(name, expanded=False):
                st.write(f"**Type:** {resource_type}")
                st.write(f"**Category:** {category}")
                st.write(f"**Difficulty Level:** {difficulty}")
                st.write(f"**Author:** {author}")
                st.write(f"**Description:** {content}")

                if url:
                    st.markdown(f"[Link to Resource]({url})", unsafe_allow_html=True)

                # Progress tracking section
                progress_value = st.slider("Set progress for this resource:", 0, 100, 50, key=f'progress_slider_{resource_id}')  # Default to 50%

                # Button to track progress
                if st.button("Track Progress", key=f'track_progress_{resource_id}'):
                    track_progress(user_id, resource_id, progress_value)
                    st.success(f"Progress for '{name}' tracked successfully at {progress_value}%!")

    else:
        st.warning("No resources available at the moment.")

# Show the learning development dashboard
if __name__ == "__main__":
    learning_development()
