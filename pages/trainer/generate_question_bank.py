import streamlit as st
import sqlite3
import csv
import io
import google.generativeai as genai
from utils.notifications import display_notification
# Initialize Gemini API
genai.configure(api_key="AIzaSyBhbAu6Fc2v7D92eR5NnxzfCosLEv59Y_Y")

# Create the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

# Predefined fallback topics
FALLBACK_TOPICS = ["Introduction", "Keywords", "Syntax", "Features"]

def fetch_topics_from_database(technology):
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT curriculum_file FROM curriculum WHERE technology = ?", (technology,))
    blobs = cursor.fetchall()
    conn.close()
    
    topics = set()

    for blob in blobs:
        curriculum_data = blob[0]
        if curriculum_data:
            csv_data = io.StringIO(curriculum_data.decode('utf-8'))
            reader = csv.reader(csv_data)
            for row in reader:
                if row:  # Check if the row is not empty
                    topics.add(row[0])  # Assuming the first column contains the topic

    return list(topics)

def suggest_related_topics(user_input, all_topics):
    user_input = user_input.lower()
    suggestions = [topic for topic in all_topics if user_input in topic.lower()]
    return suggestions

def generate_questions(technology, topics, num_questions, difficulty_level):
    prompt = f"Generate {num_questions} {difficulty_level} questions about {', '.join(topics)} in {technology}."

    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)

    if response:
        questions = response.text.strip().split('\n')
        display_notification(
        f"Question bank generation complete! {num_questions} {difficulty_level} questions for {technology} on topics {', '.join(topics)}.",
        notification_type="success"
    )
        return questions
    else:
        st.error("Failed to generate questions. Please try again.")
        return []

def save_question_bank(technology, topic, num_questions, difficulty_level, questions):
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO question_bank (technology, topic, num_questions, difficulty_level, questions)
        VALUES (?, ?, ?, ?, ?)
    ''', (technology, topic, num_questions, difficulty_level, "\n".join(questions)))
    conn.commit()
    conn.close()

def show_generate_question_bank_page():
    st.title("Generate Question Bank")
    
    technology = st.selectbox("Select Technology", ["Python", "Java", "C++"])
    all_topics = fetch_topics_from_database(technology)
    
    if not all_topics:
        st.warning("No topics found for the selected technology. Please enter topics manually.")
        all_topics = FALLBACK_TOPICS
    
    user_input = st.text_input("Enter topics (comma-separated)")
    
    if user_input:
        topics = [topic.strip() for topic in user_input.split(',') if topic.strip()]
    else:
        topics = FALLBACK_TOPICS

    num_questions = st.number_input("Number of Questions", min_value=1, max_value=50, value=5)
    difficulty_level = st.selectbox("Difficulty Level", ["easy", "medium", "hard"])
    
    if st.button("Generate"):
        if topics:
            questions = generate_questions(technology, topics, num_questions, difficulty_level)
            save_question_bank(technology, ', '.join(topics), num_questions, difficulty_level, questions)
            st.success("Questions generated and saved successfully!")
            st.write("Generated Questions:")
            st.write(questions)
        else:
            st.error("Please enter at least one topic.")

if __name__ == "__main__":
    show_generate_question_bank_page()
