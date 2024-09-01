import streamlit as st
import sqlite3
import pandas as pd

def load_question_banks():
    conn = sqlite3.connect('app_database.db')
    query = "SELECT * FROM question_bank"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def show_download_question_bank_page():
    st.title("Download Question Bank")
    
    df = load_question_banks()
    st.dataframe(df)
    
    selected_row = st.selectbox("Select a Question Bank to Download", df.index)
    if selected_row is not None:
        row = df.iloc[selected_row]
        file_data = row['questions']
        st.download_button("Download", file_data, file_name=f"{row['technology']}_{row['topic']}.xlsx")
