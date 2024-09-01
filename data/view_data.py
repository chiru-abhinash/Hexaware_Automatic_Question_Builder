import sqlite3
import pandas as pd

# Correct path to your SQLite database
db_path = r'app_database.db'
conn = sqlite3.connect(db_path)

# Function to load data from the users table
def load_data():
    query = 'SELECT * FROM users'
    return pd.read_sql(query, conn)

def main():
    try:
        df = load_data()
        print(df)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Run the main function
if __name__ == "__main__":
    main()
