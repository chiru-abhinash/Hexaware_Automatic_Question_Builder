import pandas as pd
from utils.database import get_db_connection

def generate_report(report_type, start_date=None, end_date=None):
    """Generate a report based on the specified type and date range."""
    conn = get_db_connection()
    if report_type == "User Activity":
        query = '''SELECT * FROM logs WHERE timestamp BETWEEN ? AND ?'''
        data = conn.execute(query, (start_date, end_date)).fetchall()
    elif report_type == "Feedback Summary":
        query = '''SELECT feedback_type, COUNT(*) as count FROM feedback GROUP BY feedback_type'''
        data = conn.execute(query).fetchall()
    conn.close()
    
    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data)
    return df
