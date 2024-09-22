import sqlite3

def truncate_table(table_name):
    """Truncate the specified table in the database."""
    # Connect to the existing database
    conn = sqlite3.connect('app_database.db')  # Update with your actual database path
    cursor = conn.cursor()

    try:
        # Truncate the table (DELETE all records)
        cursor.execute(f"DELETE FROM {table_name}")
        conn.commit()
        print(f"All records from the {table_name} table have been deleted.")
    except sqlite3.Error as e:
        print(f"An error occurred while truncating the table: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    truncate_table("question_bank")  # Change to your actual table name
