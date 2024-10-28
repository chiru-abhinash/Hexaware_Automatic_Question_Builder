# # pages/trainer/upload_curriculum.py
# import streamlit as st
# import sqlite3
# import pandas as pd

# def get_trainer_id(username):
#     """Fetch the trainer ID based on the username."""
#     conn = sqlite3.connect('app_database.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
#     trainer_id = cursor.fetchone()
#     conn.close()
#     return trainer_id[0] if trainer_id else None

# def show_upload_curriculum_page():
#     """Render the Upload Curriculum page."""
#     st.title("Upload Curriculum")
    
#     # Ensure user is logged in and has the correct role
#     if 'username' not in st.session_state or st.session_state.role != "Trainer":
#         st.error("Unauthorized access. Please log in as a Trainer.")
#         return
    
#     technology = st.selectbox("Select Technology", ["Python", "Java", "C++"])
#     file = st.file_uploader("Upload Curriculum File", type=["csv", "xlsx"])
    
#     if st.button("Submit", key="upload_curriculum_submit"):
#         if file:
#             # Get trainer ID from session state
#             trainer_id = get_trainer_id(st.session_state.username)
#             if trainer_id:
#                 try:
#                     # Read the file into a DataFrame
#                     if file.type == "text/csv":
#                         df = pd.read_csv(file)
#                     elif file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
#                         df = pd.read_excel(file)
#                     else:
#                         st.error("Unsupported file format")
#                         return
                    
#                     # Process and display the DataFrame
#                     st.write("Data preview:")
#                     st.write(df.head())  # Preview the first few rows
                    
#                     # Save the file to the database
#                     conn = sqlite3.connect('app_database.db')
#                     cursor = conn.cursor()
#                     cursor.execute('''INSERT INTO curriculum (trainer_id, technology, curriculum_file)
#                                       VALUES (?, ?, ?)''',
#                                    (trainer_id, technology, file.read()))
#                     conn.commit()
#                     conn.close()
#                     st.success("Curriculum uploaded successfully!")
#                 except pd.errors.ParserError as e:
#                     st.error(f"Error reading file: {e}")
#                 except Exception as e:
#                     st.error(f"An error occurred: {e}")
#             else:
#                 st.error("Trainer ID not found.")
#         else:
#             st.error("Please upload a file.")

# if __name__ == "__main__":
#     show_upload_curriculum_page()
# pages/trainer/upload_curriculum.py
import streamlit as st
import sqlite3
import pandas as pd

def get_trainer_id(username):
    """Fetch the trainer ID based on the username."""
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    trainer_id = cursor.fetchone()
    conn.close()
    return trainer_id[0] if trainer_id else None

def show_upload_curriculum_page():
    """Render the Upload Curriculum page."""
    st.title("Upload Curriculum")
    
    # Ensure user is logged in and has the correct role
    if 'username' not in st.session_state or st.session_state.role != "Trainer":
        st.error("Unauthorized access. Please log in as a Trainer.")
        return
    
    # Add a unique key to the selectbox to avoid DuplicateWidgetID errors
    technology = st.selectbox("Select Technology", ["Python", "Java", "C++"], key="upload_curriculum_technology")
    file = st.file_uploader("Upload Curriculum File", type=["csv", "xlsx"])
    
    # Add a unique key to the submit button
    if st.button("Submit", key="upload_curriculum_submit"):
        if file:
            # Get trainer ID from session state
            trainer_id = get_trainer_id(st.session_state.username)
            if trainer_id:
                try:
                    # Read the file into a DataFrame
                    if file.type == "text/csv":
                        df = pd.read_csv(file)
                    elif file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                        df = pd.read_excel(file)
                    else:
                        st.error("Unsupported file format")
                        return
                    
                    # Process and display the DataFrame
                    st.write("Data preview:")
                    st.write(df.head())  # Preview the first few rows
                    
                    # Save the file to the database
                    conn = sqlite3.connect('app_database.db')
                    cursor = conn.cursor()
                    cursor.execute('''INSERT INTO curriculum (trainer_id, technology, curriculum_file)
                                      VALUES (?, ?, ?)''',
                                   (trainer_id, technology, file.read()))
                    conn.commit()
                    conn.close()
                    st.success("Curriculum uploaded successfully!")
                except pd.errors.ParserError as e:
                    st.error(f"Error reading file: {e}")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.error("Trainer ID not found.")
        else:
            st.error("Please upload a file.")

if __name__ == "__main__":
    show_upload_curriculum_page()
