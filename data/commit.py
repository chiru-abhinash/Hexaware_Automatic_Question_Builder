import sqlite3

def get_db_connection():
    conn = sqlite3.connect('your_database.db')  # Adjust the path to your database
    return conn

def execute_query(query, params=()):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()  # Make sure to commit the changes
    cursor.close()
    conn.close()
