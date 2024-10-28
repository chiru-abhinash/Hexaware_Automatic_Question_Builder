import streamlit as st 
import sqlite3
import csv
import io
import google.generativeai as genai
import random
from utils.notifications import show_notifications_page
import re  # For more dynamic question parsing
from dotenv import load_dotenv  # type: ignore # Import dotenv
import os
# Initialize Google Gemini API
genai.configure(api_key="")  # Replace with your actual API key
'''
# Load environment variables
load_dotenv()

# Initialize Google Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("API key not found. Please check your .env file.")
'''



# Gemini model configuration
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
                if row:  
                    topics.add(row[0])  # Add topic from the first column in CSV file

    return list(topics)

def generate_questions(technology, topics, num_questions, difficulty_level):
    # Prompt construction
    prompt = (f"Generate {num_questions} {difficulty_level} questions about {', '.join(topics)} in {technology}. "
              "Include four answer options for each question, with the first option always being the correct one. "
              "Format each question and its options as follows:\n"
              "1. Question?\n"
              "(A) Option1\n"
              "(B) Option2\n"
              "(C) Option3\n"
              "(D) Option4\n"
              "Only provide the questions and options without any additional commentary.")
    
    # Start the chat with the model
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)

    if response:
        questions_data = [line.strip() for line in response.text.strip().split('\n') if line.strip()]
        
        questions = []
        current_question = {}

        # Regular expression to match question numbers
        question_regex = re.compile(r'^\d+\.')

        # Parsing the generated questions
        for line in questions_data:
            if question_regex.match(line):  # Dynamically match any number starting with "1.", "2.", "3." etc.
                if current_question:
                    questions.append(current_question)

                current_question = {
                    'question': line,
                    'options': [],
                    'correct_option': 'A'  # Set correct option to 'A'
                }
            elif line.startswith(('(A)', '(B)', '(C)', '(D)')):
                if 'options' in current_question:
                    current_question['options'].append(line)
            elif ' (Correct: ' in line:
                # Skip correct option line since we're controlling it
                continue

        if current_question:
            questions.append(current_question)

        # Shuffle options for each question
        for q in questions:
            random.shuffle(q['options'])

        # Notify the user about completion
        if questions:
            show_notifications_page(
                notification_text=f"Question bank generation complete! {num_questions} {difficulty_level} questions for {technology} on topics {', '.join(topics)}.",
                notification_type="success"
            )
        return questions
    else:
        st.error("Failed to generate questions. Please try again.")
        return []

def save_question_bank(trainer_id, technology, topic, num_questions, difficulty_level, questions):
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()

    try:
        # Preparing the questions and options in the required format
        questions_str = ":::".join([q['question'] for q in questions])  # Separate each question with ':::'
        options_str = ":::".join([";;".join(q['options']) for q in questions])  # Separate options with ';;' and question sets with ':::'
        correct_answers_str = ";;".join([q['correct_option'] for q in questions])  # Store correct answers (all 'A')

        # Insert into the database
        cursor.execute('''INSERT INTO question_bank (trainer_id, technology, topic, num_questions, difficulty_level, questions, options, correct_option)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
                       (trainer_id, technology, topic, num_questions, difficulty_level, questions_str, options_str, correct_answers_str))
        
        conn.commit()
        st.success("Questions saved successfully!")
    
    except Exception as e:
        conn.rollback()
        st.error(f"An error occurred: {str(e)}")

    finally:
        conn.close()

def show_generate_question_bank_page():
    st.title("Generate Question Bank")
    
    # Simulated trainer_id (for demonstration; replace with actual login-based value)
    trainer_id = 1  # This should be dynamic based on the logged-in trainer
    
    # Select technology
    technology = st.selectbox("Select Technology", ["Python", "Java", "C++"], key="technology_selectbox")

    #technology = st.selectbox("Select Technology", ["Python", "Java", "C++"])
    all_topics = fetch_topics_from_database(technology)
    
    if not all_topics:
        st.warning("No topics found for the selected technology. Please enter topics manually.")
        all_topics = FALLBACK_TOPICS
    
    # Allow user to input topics
    user_input = st.text_input("Enter topics (comma-separated)", placeholder="E.g. Introduction, Syntax")
    
    if user_input:
        topics = [topic.strip() for topic in user_input.split(',') if topic.strip()]
    else:
        topics = []

    # Input for number of questions and difficulty level
    num_questions = st.number_input("Number of Questions", min_value=1, max_value=50, value=5)
    difficulty_level = st.selectbox("Difficulty Level", ["easy", "medium", "hard"])
    
    # Generate button
    if st.button("Generate"):
        if topics:
            questions = generate_questions(technology, topics, num_questions, difficulty_level)
            if questions:
                save_question_bank(trainer_id, technology, ', '.join(topics), num_questions, difficulty_level, questions)
                st.write("Generated Questions:")
                for q in questions:
                    st.write(f"**{q['question']}**")
                    for i, option in enumerate(q['options']):
                        st.write(f"{chr(65 + i)}. {option}")
                st.write(f"Correct Option: A")  # Always display 'A' as correct option
        else:
            st.error("Please enter at least one topic.")

if __name__ == "__main__":
    show_generate_question_bank_page()
