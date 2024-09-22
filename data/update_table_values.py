import sqlite3

def update_database_schema():
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    
    # Add new columns for options and correct answer
    try:
        cursor.execute('''ALTER TABLE question_bank ADD COLUMN options TEXT;''')
        cursor.execute('''ALTER TABLE question_bank ADD COLUMN correct_option TEXT;''')
        conn.commit()
        print("Database schema updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating database schema: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    update_database_schema()
