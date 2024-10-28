import sqlite3

def test_update(issue_id, resolution_notes, resolution_status):
    conn = sqlite3.connect('app_database.db')
    cursor = conn.cursor()
    query = """
    UPDATE issue_resolution
    SET resolution_notes = ?, resolution_status = ?, resolved_at = CURRENT_TIMESTAMP
    WHERE id = ?
    """
    cursor.execute(query, (resolution_notes, resolution_status, issue_id))
    conn.commit()
    cursor.close()
    conn.close()

test_update(7, 'tested', 'Resolved')
