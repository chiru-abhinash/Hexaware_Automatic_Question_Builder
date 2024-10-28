import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import datetime
import xlsxwriter
from fpdf import FPDF
from utils.database import fetch_all  # Ensure you have a fetch_all function in your database utility

# Function to generate report data
def generate_report_data(report_type, start_date, end_date):
    """Fetch data from the database based on report type and date range."""
    query = ""
    params = (start_date, end_date)

    if report_type == "User Activity":
        query = """SELECT username, action, timestamp FROM user_activity_logs WHERE timestamp BETWEEN ? AND ?"""
    elif report_type == "System Performance":
        query = """SELECT timestamp, cpu_usage, memory_usage FROM system_performance WHERE timestamp BETWEEN ? AND ?"""
    elif report_type == "Error Logs":
        query = """SELECT message, timestamp FROM error_logs WHERE timestamp BETWEEN ? AND ?"""
    elif report_type == "Feedbacks":
        query = """SELECT user_id, feedback_text, created_at FROM feedback WHERE created_at BETWEEN ? AND ?"""

    if query:
        data = fetch_all(query, params)  # Fetch data from the database
        return pd.DataFrame(data)  # Convert to DataFrame
    return pd.DataFrame()  # Return an empty DataFrame if no valid report type is provided

# Function to export DataFrame to Excel
def export_to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Report', index=False)
    output.seek(0)  # Seek to the beginning of the BytesIO object
    return output

# Function to export DataFrame to PDF
# Function to export DataFrame to PDF
def export_to_pdf(df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.cell(200, 10, txt="Report", ln=True, align='C')

    # Column headers
    for column in df.columns:
        pdf.cell(40, 10, txt=str(column), border=1)  # Convert column header to string
    pdf.ln()

    # Data rows
    for index, row in df.iterrows():
        for value in row:
            pdf.cell(40, 10, txt=str(value), border=1)  # Convert each cell value to string
        pdf.ln()

    output = BytesIO()
    pdf.output(dest='S').encode('latin1')  # Write the PDF content to BytesIO with encoding
    output.write(pdf.output(dest='S').encode('latin1'))
    output.seek(0)  # Seek to the beginning of the BytesIO object

    return output



# Main function for the Report Generation page
def show_report_generation_page():
    st.title("Report Generation")

    # Report type selection
    report_type = st.selectbox("Select Report Type", ["User Activity", "System Performance", "Error Logs", "Feedbacks"])

    # Date range selection
    date_range = st.date_input("Select Date Range", [])
    if len(date_range) == 2:
        start_date, end_date = date_range

        if st.button("Generate Report"):
            df = generate_report_data(report_type, start_date, end_date)
            if not df.empty:
                st.success(f"{report_type} report generated for the selected date range.")
                st.dataframe(df)  # Display report data

                # Export options
                st.subheader("Export Options")

                # Export as Excel download button
                excel_output = export_to_excel(df)
                st.download_button(
                    label="Download Excel",
                    data=excel_output,
                    file_name=f"{report_type}_report.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

                # Export as PDF download button
                pdf_output = export_to_pdf(df)
                st.download_button(
                    label="Download PDF",
                    data=pdf_output,
                    file_name=f"{report_type}_report.pdf",
                    mime="application/pdf"
                )
            else:
                st.error("No data available for the selected date range.")
    else:
        st.warning("Please select a valid date range.")

if __name__ == "__main__":
    show_report_generation_page()
