import sqlite3

def add_sample_data():
    # Connect to SQLite database
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()

    # Add sample users
    users = [
        ('admin', 'adminpass', 'Administrator'),
        ('trainer1', 'trainerpass', 'Trainer'),
        ('employee1', 'employeepass', 'Employee')
    ]
    cursor.executemany('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', users)

    # Add sample feedback
    feedbacks = [
        (1, 'This is feedback from admin.'),
        (2, 'This is feedback from trainer.'),
        (3, 'This is feedback from employee.')
    ]
    cursor.executemany('INSERT INTO feedback (user_id, feedback_text) VALUES (?, ?)', feedbacks)

    # Add sample curriculum (placeholder data)
    curriculum_data = b'Sample curriculum data'
    cursor.execute('INSERT INTO curriculum (trainer_id, technology, curriculum_file) VALUES (?, ?, ?)', (2, 'Python', curriculum_data))

    # Add sample question bank
    questions = 'What is Python?;What is a function?;Explain OOP in Python.'
    cursor.execute('INSERT INTO question_bank (technology, topic, num_questions, difficulty_level, questions) VALUES (?, ?, ?, ?, ?)',
                   ('Python', 'Basic', 3, 'Easy', questions))

    # Add sample learning plan
    learning_plan_details = 'A learning plan for improving Python skills.'
    cursor.execute('INSERT INTO learning_plans (employee_id, technology, areas_of_improvement, learning_goals, plan_details) VALUES (?, ?, ?, ?, ?)',
                   (3, 'Python', 'Advanced topics', 'Improve coding skills', learning_plan_details))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    add_sample_data()
