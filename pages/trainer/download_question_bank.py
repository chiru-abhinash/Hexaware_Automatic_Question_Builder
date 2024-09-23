import streamlit as st
import sqlite3
import pandas as pd
from io import BytesIO
from fpdf import FPDF  # For PDF export

def load_question_banks():
    """Load question banks from the database."""
    conn = sqlite3.connect('app_database.db')
    query = "SELECT * FROM question_bank"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def save_to_excel(df):
    """Save question bank data to an Excel file."""
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Question Bank')
    output.seek(0)
    return output

def save_to_pdf(df):
    """Save question bank data to a PDF file with enhanced layout."""
    pdf = FPDF()
    pdf.add_page()

    # Set Title
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, txt="Question Bank", ln=True, align='C')
    pdf.ln(10)  # Add space after the title

    # Set font for content
    pdf.set_font("Arial", size=12)

    # Loop through each question in the DataFrame
    for index, row in df.iterrows():
        # Question number and content
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(200, 10, txt=f"Question {index+1}: {row['Question']}", ln=True, border=1, align='L')
        pdf.ln(5)  # Add some space between the question and options

        # Options displayed with borders and on new lines
        options = row['Options'].split(" | ")
        pdf.set_font("Arial", size=12)
        for i, option in enumerate(options):
            option_text = f"Option {chr(65 + i)}: {option}"  # Convert to A, B, C, etc.
            pdf.cell(200, 10, txt=option_text, ln=True, border=1)
        
        pdf.ln(10)  # Add space after each question

    # Write PDF content to a BytesIO buffer
    output = BytesIO()
    pdf_output = pdf.output(dest='S').encode('latin1')  # Convert to byte-like object for writing
    output.write(pdf_output)
    output.seek(0)  # Move the cursor to the beginning of the stream for reading

    return output

def parse_question_data(questions, options):
    """Parse questions and options from the database into lists."""
    try:
        questions_list = questions.split(':::')
        options_list = options.split(':::')
    except AttributeError:
        # Handle cases where questions or options are None or not properly structured
        st.error("Error: Invalid data structure in questions or options.")
        return []

    parsed_data = []
    for i, question in enumerate(questions_list):
        opts = options_list[i].split(";;")
        parsed_data.append({'question': question, 'options': opts})
    
    return parsed_data

def prepare_data_for_download(parsed_data):
    """Prepare a DataFrame for download, containing the question and corresponding options."""
    question_data = []
    for entry in parsed_data:
        question = entry['question']
        options = ' | '.join(entry['options'])  # Combine options into a single string for display
        question_data.append({'Question': question, 'Options': options})
    
    return pd.DataFrame(question_data)

def show_download_question_bank_page():
    st.title("Download Question Bank")
    
    df = load_question_banks()
    st.dataframe(df)
    
    if not df.empty:
        selected_row = st.selectbox("Select a Question Bank to Download", df.index)
        
        if selected_row is not None:
            row = df.iloc[selected_row]
            
            # Parse questions and options for the selected question bank
            parsed_data = parse_question_data(row['questions'], row['options'])
            
            if parsed_data:
                # Prepare the DataFrame for download
                questions_df = prepare_data_for_download(parsed_data)
                
                # Format selection dropdown
                format_option = st.selectbox("Select Download Format", ["Excel", "PDF"])
                
                # Download button
                if st.button("Download"):
                    if format_option == "Excel":
                        excel_output = save_to_excel(questions_df)
                        st.download_button(
                            label="Download as Excel",
                            data=excel_output,
                            file_name=f"{row['technology']}_{row['topic']}.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        )
                    elif format_option == "PDF":
                        pdf_output = save_to_pdf(questions_df)
                        st.download_button(
                            label="Download as PDF",
                            data=pdf_output,
                            file_name=f"{row['technology']}_{row['topic']}.pdf",
                            mime="application/pdf"
                        )
    else:
        st.warning("No question banks available for download.")

if __name__ == "__main__":
    show_download_question_bank_page()
