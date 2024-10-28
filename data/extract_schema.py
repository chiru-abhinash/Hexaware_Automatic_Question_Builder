import sqlite3

# Function to get the schema of a table
def get_table_schema(table_name):
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    schema = cursor.fetchall()
    conn.close()
    return schema

# Function to display the schema in a readable format
def display_schema(table_name, schema):
    print(f"Schema for table {table_name}:")
    for column in schema:
        print(f"Column: {column[1]}, Type: {column[2]}, Not Null: {column[3]}, Default: {column[4]}, Primary Key: {column[5]}")
    print("\n")

# Function to get all table names in the database
def get_all_table_names():
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    conn.close()
    return [table[0] for table in tables]

if __name__ == "__main__":
    all_tables = get_all_table_names()
    for table_name in all_tables:
        schema = get_table_schema(table_name)
        display_schema(table_name, schema)
