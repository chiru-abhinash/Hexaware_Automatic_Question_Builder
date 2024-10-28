
# Automated Question Builder Application

The Automated Question Builder is a Streamlit-based web application designed to assist trainers and administrators in generating, managing, and delivering assessments. This system leverages Google Gemini API to automatically generate customized question banks based on user-defined parameters such as technology, topic, and difficulty level.

## Features

- **User Role-based Access**: Separate dashboards for Administrators, Trainers, and Employees.
- **Question Generation**: Automatically generate question banks using the Google Gemini API.
- **Self-Assessment**: Employees can assess themselves using generated question banks.
- **Notifications**: Stay informed with real-time notifications for question bank generation, feedback submissions, and more.
- **Feedback & Learning Plans**: Submit feedback and request personalized learning plans based on performance.
- **Secure Authentication**: Role-based login with role selection on the main page.
- **Question Bank Management**: Store, edit, and retrieve question banks, with shuffle functionality for assessments.

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, SQLite
- **API Integration**: Google Gemini API
- **Database**: SQLite (with sqlite3 for database handling)

## Project Structure

```bash
|-- Automatic_Question_Builder/
    |-- pages/
        |-- administrator/
            |-- user_management.py   # Admin manages users
        |-- trainer/
            |-- question_bank.py     # Trainers generate question banks
        |-- employee/
            |-- self_assessment.py   # Employees access assessments
    |-- utils/
        |-- auth.py                  # User authentication
        |-- database.py              # Database connection and queries
        |-- notifications.py         # Notification handling
    |-- app.py                       # Main application entry point
