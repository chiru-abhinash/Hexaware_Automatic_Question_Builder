# Function to create a new learning_resources table with an improved structure
import sqlite3
def create_new_learning_resources_table():
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()

    # Create the table with additional fields
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS learning_resources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resource_name TEXT NOT NULL,
            resource_type TEXT NOT NULL, -- e.g., Video, Article, PDF, etc.
            resource_content TEXT, -- Description or content of the resource
            category TEXT, -- e.g., Python, Data Science, Machine Learning
            difficulty_level TEXT, -- Easy, Medium, Hard
            author TEXT, -- The author or creator of the resource
            url TEXT, -- Link to the resource if applicable
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    ''')

    conn.commit()
    conn.close()
    print("New learning_resources table created successfully.")

# Call the function to create the new table
create_new_learning_resources_table()
