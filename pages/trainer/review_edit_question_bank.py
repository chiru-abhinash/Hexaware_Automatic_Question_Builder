import streamlit as st
import sqlite3
import pandas as pd

def load_question_banks():
    """Load the question banks from the database."""
    conn = sqlite3.connect('app_database.db')
    query = "SELECT * FROM question_bank"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def parse_question_data(questions, options):
    """Parse questions and options into lists."""
    questions_list = questions.split(':::')
    options_list = options.split(':::')
    
    parsed_data = []
    
    for i, question in enumerate(questions_list):
        opts = options_list[i].split(";;")
        parsed_data.append({'question': question, 'options': opts})
    
    return parsed_data

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

if __name__ == "__main__":
    show_review_edit_question_bank_page()
