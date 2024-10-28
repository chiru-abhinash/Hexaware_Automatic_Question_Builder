import sqlite3

def update_notifications_table():
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    
    # Alter the notifications table to add receiver_id
    try:
        # Add receiver_id column to the notifications table
        cursor.execute('''
            ALTER TABLE notifications ADD COLUMN receiver_id INTEGER NOT NULL DEFAULT 0
        ''')
        
    except sqlite3.OperationalError as e:
        print(f"Error altering notifications table: {e}")
    
    conn.commit()
    conn.close()

# Call this function to update the notifications table schema
update_notifications_table()
