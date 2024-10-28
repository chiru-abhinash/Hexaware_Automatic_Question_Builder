import streamlit as st
import sqlite3
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
import io
import datetime

def load_question_banks():
    """Load the question banks from the database."""
    conn = sqlite3.connect('app_database.db')
    query = "SELECT id, technology, topic, num_questions, difficulty_level, questions, options FROM question_bank"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def load_user_details(username):
    """Load user details from the database based on the username."""
    conn = sqlite3.connect('app_database.db')
    query = "SELECT firstname, lastname FROM users WHERE username = ?"
    cursor = conn.cursor()
    cursor.execute(query, (username,))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        st.session_state['firstname'] = user[0]
        st.session_state['lastname'] = user[1]
    else:
        st.error("User not found.")

# def parse_question_data(questions, options):
#     """Parse questions and options into lists."""
#     questions_list = questions.split(':::')
#     options_list = options.split(':::')
    
#     parsed_data = []
    
#     for i, question in enumerate(questions_list):
#         opts_with_correct = options_list[i].split(";;") if i < len(options_list) else []
        
#         if opts_with_correct:
#             cleaned_options = [opt.strip() for opt in opts_with_correct]
#             correct_option = cleaned_options[0] if cleaned_options else None
            
#             parsed_data.append({
#                 'question': question.strip(),
#                 'options': cleaned_options,
#                 'correct_option': correct_option
#             })
#         else:
#             st.warning(f"Warning: No options available for question {i + 1}.")
#             parsed_data.append({
#                 'question': question.strip(),
#                 'options': [],
#                 'correct_option': None
#             })
    
#     return parsed_data

# def evaluate_answers(parsed_data):
#     """Evaluate the user's answers against the correct options."""
#     score = 0
#     total_questions = len(parsed_data)
    
#     for i, q in enumerate(parsed_data):
#         user_answer = st.session_state.get(f'answer_{i}', None)
#         if user_answer == q['correct_option']:
#             score += 1

#     return score, total_questions

def parse_question_data(questions, options):
    """Parse questions and options into lists."""
    questions_list = questions.split(':::')
    options_list = options.split(':::')
    
    parsed_data = []
    
    for i, question in enumerate(questions_list):
        opts_with_correct = options_list[i].split(";;") if i < len(options_list) else []
        
        if opts_with_correct:
            cleaned_options = [opt.strip() for opt in opts_with_correct]  # Keep labels
            correct_option = cleaned_options[0] if cleaned_options else None
            cleaned_options.sort()  # Sort options alphabetically for display
            
            parsed_data.append({
                'question': question.strip(),
                'options': cleaned_options,
                'correct_option': correct_option
            })
        else:
            st.warning(f"Warning: No options available for question {i + 1}.")
            parsed_data.append({
                'question': question.strip(),
                'options': [],
                'correct_option': None
            })
    
    return parsed_data



def evaluate_answers(parsed_data):
    """Evaluate the user's answers against the correct options."""
    score = 0
    total_questions = len(parsed_data)

    for i, q in enumerate(parsed_data):
        user_answer = st.session_state.get(f'answer_{i}', None)
        
        # Compare user's answer text directly
        if user_answer is not None and user_answer.strip() == q['correct_option'].strip():
            score += 1

    return score, total_questions






def generate_certificate(score, total_questions):
    """Generate a message indicating the score."""
    return f"You scored **{score} out of {total_questions}**!"

def create_pdf_certificate(name, course_name, score, total_questions):
    """Create a visually enhanced PDF certificate."""
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Add a border
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(4)
    c.rect(40, 40, width - 80, height - 80)

    # Add a title
    c.setFont("Helvetica-Bold", 28)
    c.setFillColorRGB(0.2, 0.4, 0.6)
    c.drawCentredString(width / 2.0, height - 100, "Certificate of Completion")

    # Add the body of the certificate
    c.setFont("Helvetica", 16)
    c.setFillColorRGB(0, 0, 0)
    c.drawCentredString(width / 2.0, height - 150, "This is to certify that")

    # Add the recipient's name
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2.0, height - 180, name)

    # Add course name and details
    c.setFont("Helvetica", 16)
    c.drawCentredString(width / 2.0, height - 220, "has successfully completed the course")
    
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width / 2.0, height - 250, course_name)

    # Add score and total questions
    c.setFont("Helvetica", 16)
    c.drawCentredString(width / 2.0, height - 290, f"with a score of {score} out of {total_questions}.")

    # Add date issued
    issue_date = datetime.date.today().strftime("%B %d, %Y")
    c.drawCentredString(width / 2.0, height - 330, f"Issued on: {issue_date}")

    # Signature
    c.setFont("Helvetica", 14)
    c.drawString(width / 2.5, height - 420, "____________________________")
    c.drawString(width / 2.5, height - 440, "Authorized Signature")

    # Bottom border
    c.setLineWidth(2)
    c.setStrokeColor(colors.darkblue)
    c.line(50, 50, width - 50, 50)

    # Save the PDF content
    c.save()
    buffer.seek(0)
    
    return buffer

# def self_assessment():
#     st.title("Self-Assessment")

#     # Assuming the username is stored in session state after user login
#     if 'username' not in st.session_state:
#         st.error("Please log in to access the self-assessment.")
#         return
    
#     # Load user details from the database
#     load_user_details(st.session_state['username'])

#     df = load_question_banks()
#     selected_row = st.selectbox("Select Question Bank", df.index)
    
#     if selected_row is not None:
#         row = df.iloc[selected_row]
        
#         parsed_data = parse_question_data(row['questions'], row['options'])
        
#         for i, q in enumerate(parsed_data):
#             st.write(f"Q{i+1}: {q['question']}")
#             if q['options']:
#                 answer = st.selectbox(f"Select your answer for Q{i+1}", q['options'], key=f'answer_{i}')
        
#         if st.button("Submit"):
#             score, total_questions = evaluate_answers(parsed_data)
#             certificate_message = generate_certificate(score, total_questions)
#             st.write(certificate_message)
            
#             if score / total_questions >= 0.7:
#                 # Combine the user's first name and last name
#                 full_name = f"{st.session_state.get('firstname', '')} {st.session_state.get('lastname', '')}"
#                 pdf_buffer = create_pdf_certificate(full_name, row['technology'] + " - " + row['topic'], score, total_questions)
#                 st.download_button(
#                     label="Download Certificate",
#                     data=pdf_buffer,
#                     file_name="completion_certificate.pdf",
#                     mime="application/pdf"
#                 )
#             else:
#                 st.write("You need at least 70% to receive a certificate.")

def self_assessment():
    st.title("Self-Assessment")
    if 'username' not in st.session_state:
        st.error("Please log in to access the self-assessment.")
        return
    
    load_user_details(st.session_state['username'])
    df = load_question_banks()
    selected_row = st.selectbox("Select Question Bank", df.index)
    
    if selected_row is not None:
        row = df.iloc[selected_row]
        parsed_data = parse_question_data(row['questions'], row['options'])
        
        for i, q in enumerate(parsed_data):
            st.write(f"Q{i+1}: {q['question']}")
            if q['options']:
                user_answer = st.radio(f"Select your answer for Q{i+1}", q['options'], key=f'answer_{i}')
        
        if st.button("Submit"):
            score, total_questions = evaluate_answers(parsed_data)
            certificate_message = generate_certificate(score, total_questions)
            st.write(certificate_message)
            
            if score / total_questions >= 0.7:
                full_name = f"{st.session_state.get('firstname', '')} {st.session_state.get('lastname', '')}"
                pdf_buffer = create_pdf_certificate(full_name, row['technology'] + " - " + row['topic'], score, total_questions)
                st.download_button(
                    label="Download Certificate",
                    data=pdf_buffer,
                    file_name="completion_certificate.pdf",
                    mime="application/pdf"
                )
            else:
                st.write("You need at least 70% to receive a certificate.")
            # Track progress
            user_id = st.session_state.get('user_id')  # Ensure 'user_id' is properly set
            if user_id:
                resource_id = row['id']  # Assuming `id` is the primary key in the question bank table
                store_max_score(user_id, resource_id, score, total_questions)
            else:
                st.error("User ID not found. Please ensure you are logged in.")






def store_max_score(user_id, resource_id, score, total_questions):
    progress_value = (score / total_questions) * 100
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    query = '''
        INSERT INTO learning_progress (user_id, resource_id, progress, updated_at)
        VALUES (?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(user_id, resource_id) DO UPDATE SET
            progress = MAX(learning_progress.progress, excluded.progress),
            updated_at = CURRENT_TIMESTAMP;
    '''
    try:
        cursor.execute(query, (user_id, resource_id, progress_value))
        conn.commit()
    except sqlite3.OperationalError as e:
        st.error(f"Database operation failed: {e}")
    finally:
        conn.close()


def show_review_edit_question_bank_page():
    st.title("Review and Edit Question Bank")
    
    df = load_question_banks()
    st.dataframe(df)
    
    selected_row = st.selectbox("Select a Question Bank to Edit", df.index)
    
    if selected_row is not None:
        row = df.iloc[selected_row]
        st.write("Editing:", row)

        # Parse questions and options
        parsed_data = parse_question_data(row['questions'], row['options'])

        # Select specific question to edit
        question_list = [f"Q{i+1}: {q['question']}" for i, q in enumerate(parsed_data)]
        selected_question = st.selectbox("Select Question to Edit", question_list)

        # Load the current question and its options based on the selected question
        question_index = question_list.index(selected_question)
        
        if question_index is not None:
            current_question = parsed_data[question_index]['question']
            current_options = parsed_data[question_index]['options']
            
            # Display question and options for editing
            question = st.text_area("Question", value=current_question)
            option_a = st.text_input("Option A", value=current_options[0] if len(current_options) > 0 else "")
            option_b = st.text_input("Option B", value=current_options[1] if len(current_options) > 1 else "")
            option_c = st.text_input("Option C", value=current_options[2] if len(current_options) > 2 else "")
            option_d = st.text_input("Option D", value=current_options[3] if len(current_options) > 3 else "")
            
            # Save changes
            if st.button("Save Changes"):
                # Update the selected question and options
                parsed_data[question_index]['question'] = question
                parsed_data[question_index]['options'] = [option_a, option_b, option_c, option_d]
                
                # Reconstruct the questions and options strings for saving
                updated_questions = ':::'.join([q['question'] for q in parsed_data])
                updated_options = ':::'.join([';;'.join(q['options']) for q in parsed_data])
                
                update_question_bank(row['id'], row['technology'], row['topic'], row['num_questions'], row['difficulty_level'], updated_questions, updated_options)
        
        # Delete question bank
        if st.button("Delete Question Bank"):
            delete_question_bank(row['id'])
            st.rerun()  # Refresh the page after deletion

def update_question_bank(row_id, technology, topic, num_questions, difficulty_level, updated_questions, updated_options):
    """Update the question bank entry in the database."""
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE question_bank
                      SET technology = ?, topic = ?, num_questions = ?, difficulty_level = ?, questions = ?, options = ?
                      WHERE id = ?''', 
                   (technology, topic, num_questions, difficulty_level, updated_questions, updated_options, row_id))
    conn.commit()
    conn.close()
    st.success("Question bank updated successfully!")

def delete_question_bank(row_id):
    """Delete a question bank entry from the database."""
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM question_bank WHERE id = ?', (row_id,))
    conn.commit()
    conn.close()
    st.success("Question bank deleted successfully!")

if __name__ == "__main__":
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose Page", ["Self-Assessment", "Review and Edit Question Bank"])
    
    if app_mode == "Self-Assessment":
        self_assessment()
    elif app_mode == "Review and Edit Question Bank":
        show_review_edit_question_bank_page()
