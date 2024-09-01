import sqlite3

def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()

    # Create Users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    ''')

    # Create Feedback table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        feedback_text TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')

    # Create Curriculum table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS curriculum (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        trainer_id INTEGER,
        technology TEXT,
        curriculum_file BLOB,
        upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(trainer_id) REFERENCES users(id)
    )
    ''')

    # Create Question Bank table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS question_bank (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        technology TEXT,
        topic TEXT,
        num_questions INTEGER,
        difficulty_level TEXT,
        questions BLOB,
        creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create Learning Plans table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS learning_plans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER,
        technology TEXT,
        areas_of_improvement TEXT,
        learning_goals TEXT,
        plan_details BLOB,
        request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(employee_id) REFERENCES users(id)
    )
    ''')

 
    

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
