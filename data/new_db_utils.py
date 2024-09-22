import sqlite3

# Helper function for establishing the database connection
def get_db_connection():
    try:
        conn = sqlite3.connect('app_database.db')
        conn.row_factory = sqlite3.Row  # Enable accessing columns by name
        conn.execute('PRAGMA foreign_keys = ON')  # Enforce foreign key constraints
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Utility function for executing insert or update queries
def execute_query(query, params=()):
    conn = get_db_connection()
    if not conn:
        return False
    try:
        conn.execute(query, params)
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"SQL error: {e}")
        return False
    finally:
        conn.close()

# Utility function for fetching a single row
def fetch_one(query, params=()):
    conn = get_db_connection()
    if not conn:
        return None
    try:
        result = conn.execute(query, params).fetchone()
        return result
    except sqlite3.Error as e:
        print(f"SQL fetch error: {e}")
        return None
    finally:
        conn.close()

# Utility function for fetching multiple rows
def fetch_all(query, params=()):
    conn = get_db_connection()
    if not conn:
        return []
    try:
        result = conn.execute(query, params).fetchall()
        return result
    except sqlite3.Error as e:
        print(f"SQL fetch error: {e}")
        return []
    finally:
        conn.close()

# Add a new user
def add_user(username, password, role):
    return execute_query('INSERT INTO users (username, password, role) VALUES (?, ?, ?)',
                         (username, password, role))

# Get a user by username
def get_user_by_username(username):
    return fetch_one('SELECT * FROM users WHERE username = ?', (username,))

# Insert question bank
def insert_question_bank(trainer_id, technology, topic, num_questions, difficulty_level, questions):
    return execute_query('''
        INSERT INTO question_bank (trainer_id, technology, topic, num_questions, difficulty_level, questions) 
        VALUES (?, ?, ?, ?, ?, ?)''', 
        (trainer_id, technology, topic, num_questions, difficulty_level, questions))

# Get question bank by topic
def get_question_bank_by_topic(topic):
    return fetch_one('SELECT * FROM question_bank WHERE topic = ?', (topic,))

# Insert feedback
def insert_feedback(user_id, feedback_type, feedback_text):
    return execute_query('INSERT INTO feedback (user_id, feedback_type, feedback_text) VALUES (?, ?, ?)',
                         (user_id, feedback_type, feedback_text))

# Get feedback for a user
def get_feedback_for_user(user_id):
    return fetch_all('SELECT * FROM feedback WHERE user_id = ?', (user_id,))

# Insert learning plan
def insert_learning_plan(employee_id, technology, areas_of_improvement, learning_goals, plan_details):
    return execute_query('''
        INSERT INTO learning_plans (employee_id, technology, areas_of_improvement, learning_goals, plan_details)
        VALUES (?, ?, ?, ?, ?)''', 
        (employee_id, technology, areas_of_improvement, learning_goals, plan_details))

# Get learning plan for employee
def get_learning_plan_for_employee(employee_id):
    return fetch_one('SELECT * FROM learning_plans WHERE employee_id = ?', (employee_id,))

# Insert assessment record
def insert_assessment(employee_id, question_bank_id, score):
    return execute_query('''
        INSERT INTO assessments (employee_id, question_bank_id, score)
        VALUES (?, ?, ?)''', 
        (employee_id, question_bank_id, score))

# Get assessments by employee
def get_assessments_for_employee(employee_id):
    return fetch_all('SELECT * FROM assessments WHERE employee_id = ?', (employee_id,))

# Insert notification
def insert_notification(user_id, notification_text):
    return execute_query('''
        INSERT INTO notifications (user_id, notification_text, is_read)
        VALUES (?, ?, ?)''', 
        (user_id, notification_text, False))

# Get notifications for a user
def get_notifications_for_user(user_id):
    return fetch_all('SELECT * FROM notifications WHERE user_id = ?', (user_id,))
