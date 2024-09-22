import sqlite3

# Function to delete a resource by ID
def delete_learning_resource(resource_id):
    conn = sqlite3.connect('app_database.db')  # Update with your actual database path
    cursor = conn.cursor()

    # Delete the resource with the specified ID
    cursor.execute('DELETE FROM question_bank WHERE id = ?', (resource_id,))

    conn.commit()
    conn.close()
    print(f"Learning resource with ID {resource_id} deleted successfully.")

# Call the function to delete a resource (replace with the actual ID you want to delete)
delete_learning_resource(53)
