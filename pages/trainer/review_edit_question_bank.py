import streamlit as st
import sqlite3
import pandas as pd
from io import BytesIO

def load_question_banks():
    conn = sqlite3.connect('app_database.db')
    query = "SELECT * FROM question_bank"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def show_review_edit_question_bank_page():
    st.title("Review and Edit Question Bank")
    
    df = load_question_banks()
    st.dataframe(df)
    
    selected_row = st.selectbox("Select a Question Bank to Edit", df.index)
    if selected_row is not None:
        row = df.iloc[selected_row]
        st.write("Editing:", row)
        # Provide options to edit or delete questions (implement as needed)
