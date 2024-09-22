import sqlite3

# Function to drop the existing table
def drop_learning_resources_table():
    conn = sqlite3.connect('app_database.db')  # Update with your actual database path
    cursor = conn.cursor()

    # Drop the table if it exists
    cursor.execute('DROP TABLE IF EXISTS learning_progress')

    conn.commit()
    conn.close()
    print("Existing learning_resources table dropped successfully.")

# Call the function to drop the table
drop_learning_resources_table()
