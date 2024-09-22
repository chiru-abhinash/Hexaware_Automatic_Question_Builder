import streamlit as st
import sqlite3

# Fetch available technologies
def fetch_available_technologies():
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT technology FROM question_bank")
    technologies = cursor.fetchall()
    conn.close()
    return [tech[0] for tech in technologies]

# Fetch available topics for the selected technology
def fetch_available_topics(technology):
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT topic FROM question_bank WHERE technology = ?", (technology,))
    topics = cursor.fetchall()
    conn.close()
    return [topic[0] for topic in topics]

# Main function for requesting a question bank
def request_question_bank():
    st.title("Request Question Bank")

    # Fetch available technologies
    technologies = fetch_available_technologies()
    if not technologies:
        st.warning("No technologies available. Please check back later.")
        return

    # Technology selection
    technology = st.selectbox("Select Technology", technologies)

    # Fetch and display available topics for the selected technology
    if technology:
        topics = fetch_available_topics(technology)
        if topics:
            topic = st.selectbox("Select Topic", topics)
        else:
            st.warning(f"No topics available for {technology}.")
            return
    else:
        topic = None

    # Input for the number of questions
    num_questions = st.number_input("Number of Questions", min_value=1, step=1)

    # Submit button for requesting a question bank
    if st.button("Request"):
        if technology and topic and num_questions > 0:
            # Logic to handle the request (e.g., save request to the database or notify the system)
            conn = sqlite3.connect('app_database.db')
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    INSERT INTO question_bank_requests (technology, topic, num_questions, employee_id)
                    VALUES (?, ?, ?, ?)
                ''', (technology, topic, num_questions, st.session_state.user_id))  # Assuming employee_id is stored in session state
                conn.commit()
                st.success(f"Request for the {technology} - {topic} question bank with {num_questions} questions submitted successfully!")
            except Exception as e:
                st.error(f"An error occurred while submitting the request: {e}")
            finally:
                conn.close()
        else:
            st.error("Please select a technology, topic, and specify the number of questions before submitting your request.")

if __name__ == "__main__":
    request_question_bank()
