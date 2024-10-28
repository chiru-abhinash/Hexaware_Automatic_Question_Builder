import sqlite3
import pandas as pd

def load_table_contents(table_name):
    """Load contents of a specified table from the database and return as a DataFrame."""
    # Connect to the existing database
    conn = sqlite3.connect('app_database.db')  # Update with your actual database path
    query = f"SELECT *  FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def display_table(table_name):
    """Display the contents of the specified table."""
    print(f"Contents of {table_name} Table:")
    table_df = load_table_contents(table_name)
    
    if not table_df.empty:
        print(table_df)
    else:
        print(f"No records found in the {table_name} table.")

if __name__ == "__main__":
    display_table("notifications")  # Change to your actual table name
