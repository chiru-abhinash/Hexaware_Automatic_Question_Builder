import sqlite3

def add_learning_resources_sample_data():
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()

    # Inserting sample data into the learning_resources table
    cursor.execute('''
        INSERT INTO learning_resources (resource_name, resource_type, resource_content)
        VALUES (?, ?, ?)
    ''', ('Python Learning Plan', 'Question Bank', 'Comprehensive set of questions to enhance Python skills.'))

    cursor.execute('''
        INSERT INTO learning_resources (resource_name, resource_type, resource_content)
        VALUES (?, ?, ?)
    ''', ('NumPy Basics', 'Guide', 'A guide to understanding NumPy functionalities.'))

    cursor.execute('''
        INSERT INTO learning_resources (resource_name, resource_type, resource_content)
        VALUES (?, ?, ?)
    ''', ('Data Science Roadmap', 'Guide', 'An extensive roadmap for learning data science from scratch.'))

    cursor.execute('''
        INSERT INTO learning_resources (resource_name, resource_type, resource_content)
        VALUES (?, ?, ?)
    ''', ('Machine Learning Basics', 'Video', 'Introductory video series on machine learning concepts.'))

    cursor.execute('''
        INSERT INTO learning_resources (resource_name, resource_type, resource_content)
        VALUES (?, ?, ?)
    ''', ('Pandas Cookbook', 'Book', 'A practical guide to data manipulation using pandas.'))

    # Commit and close the connection
    conn.commit()
    conn.close()

# Run the function to add sample learning resources
add_learning_resources_sample_data()
