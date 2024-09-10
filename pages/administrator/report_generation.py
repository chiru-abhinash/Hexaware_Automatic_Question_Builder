# pages/administrator/report_generation.py
import streamlit as st
import pandas as pd
import io
from datetime import datetime
from io import BytesIO
import xlsxwriter
from fpdf import FPDF

# Sample data generation function
def generate_report_data(report_type, start_date, end_date):
    # Generate sample data based on the report type and date range
    date_range = pd.date_range(start_date, end_date)
    data = {
        'Date': date_range,
        'Value': [i for i in range(len(date_range))]
    }
    df = pd.DataFrame(data)
    return df

# Function to export DataFrame to Excel
def export_to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Report', index=False)
        writer.save()
    output.seek(0)
    return output

# Function to export DataFrame to PDF
def export_to_pdf(df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Title
    pdf.cell(200, 10, txt="Report", ln=True, align='C')
    
    # Column headers
    pdf.cell(100, 10, txt="Date", border=1)
    pdf.cell(100, 10, txt="Value", border=1)
    pdf.ln()
    
    # Data rows
    for index, row in df.iterrows():
        pdf.cell(100, 10, txt=str(row['Date'].date()), border=1)
        pdf.cell(100, 10, txt=str(row['Value']), border=1)
        pdf.ln()
    
    output = BytesIO()
    pdf.output(output)
    output.seek(0)
    return output

def show_report_generation_page():
    st.title("Report Generation")
    
    report_type = st.selectbox("Select Report Type", ["User Activity", "System Performance", "Error Logs"])
    date_range = st.date_input("Select Date Range", [])
    
    if len(date_range) == 2:
        start_date, end_date = date_range
        if st.button("Generate Report"):
            df = generate_report_data(report_type, start_date, end_date)
            st.success(f"{report_type} report generated for the selected date range.")
            st.dataframe(df)  # Display report data

            # Export options
            st.subheader("Export Options")
            
            if st.button("Export as Excel"):
                excel_output = export_to_excel(df)
                st.download_button(label="Download Excel", data=excel_output, file_name=f"{report_type}_report.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            
            if st.button("Export as PDF"):
                pdf_output = export_to_pdf(df)
                st.download_button(label="Download PDF", data=pdf_output, file_name=f"{report_type}_report.pdf", mime="application/pdf")
    else:
        st.warning("Please select a valid date range.")

if __name__ == "__main__":
    show_report_generation_page()
