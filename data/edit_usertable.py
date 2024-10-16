import sqlite3

def update_database():
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    
    # Add firstname and lastname columns to the users table
    try:
        #cursor.execute('''
        #    ALTER TABLE users ADD COLUMN firstname TEXT NOT NULL DEFAULT ''
        #''')
        #cursor.execute('''
        #    ALTER TABLE users ADD COLUMN lastname TEXT NOT NULL DEFAULT ''
        #''')
        
        # Add email column without UNIQUE constraint first
        cursor.execute('''
            ALTER TABLE users ADD COLUMN email TEXT NOT NULL DEFAULT ''
        ''')
        
    except sqlite3.OperationalError as e:
        print(f"Error adding columns: {e}")
    
    # Create the password_reset_tokens table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS password_reset_tokens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            reset_token TEXT NOT NULL,
            expires_at DATETIME NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

    conn.commit()
    conn.close()

# Call this function to update the schema
update_database()
