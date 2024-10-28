import streamlit as st
import sqlite3

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

# Function to load user progress from the database
def load_user_progress(user_id):
    conn = sqlite3.connect('app_database.db')
    query = '''
        SELECT lr.resource_name, lp.progress, lr.resource_type, lr.category 
        FROM learning_progress lp
        JOIN learning_resources lr ON lp.resource_id = lr.id
        WHERE lp.user_id = ?
    '''
    progress = conn.execute(query, (user_id,)).fetchall()
    conn.close()
    return progress

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
        st.subheader("Learning Resources")
        # Display resources in a more interactive format
        for resource in resources:
            resource_id, name, resource_type, content, category, difficulty, author, url = resource
            with st.expander(name, expanded=False):
                st.write(f"**Type:** {resource_type}")
                st.write(f"**Category:** {category}")
                st.write(f"**Difficulty Level:** {difficulty}")
                st.write(f"**Author:** {author}")
                st.write(f"**Description:** {content}")
                if url:
                    st.markdown(f"[Link to Resource]({url})", unsafe_allow_html=True)

    st.subheader("Your Progress")
    user_progress = load_user_progress(user_id)
    if user_progress:
        for progress in user_progress:
            resource_name, progress_value, resource_type, category = progress
            st.write(f"**Resource:** {resource_name}, **Progress:** {progress_value}%, **Type:** {resource_type}, **Category:** {category}")
    else:
        st.write("No progress tracked yet.")

# Show the learning development dashboard
if __name__ == "__main__":
    learning_development()
