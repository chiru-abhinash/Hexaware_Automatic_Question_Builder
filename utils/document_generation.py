# utils/document_generation.py

from fpdf import FPDF

def generate_report(data, report_type):
    """
    Generates a report document in the specified format.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Add content to PDF
    pdf.cell(200, 10, txt="Report", ln=True, align="C")
    pdf.output(f"{report_type}_report.pdf")

def generate_question_bank(questions, format_type='pdf'):
    """
    Generates a question bank document.
    """
    if format_type == 'pdf':
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for question in questions:
            pdf.cell(200, 10, txt=question, ln=True)

        pdf.output("question_bank.pdf")
    elif format_type == 'excel':
        # Logic to generate Excel file
        pass
