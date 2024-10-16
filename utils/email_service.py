import sqlite3
import uuid
from datetime import datetime, timedelta
import requests
import hashlib

def send_email(to_email, subject, body):
    # Set up your Mailgun API credentials
    mailgun_domain = 'sandboxf82d6f6157164603a7eb52ceda0746b3.mailgun.org'  # Replace with your Mailgun domain
    mailgun_api_key = '06dfccd9b2f3192d79e47b7ff050125b-d010bdaf-4d16be3d'  # Replace with your Mailgun API key

    # Mailgun API URL for sending emails
    url = f'https://api.mailgun.net/v3/{mailgun_domain}/messages'

    # Set up the email data
    data = {
        'from': f'Excited User <mailgun@{mailgun_domain}>',
        'to': to_email,
        'subject': subject,
        'text': body
    }

    # Send the email via Mailgun API
    response = requests.post(url, auth=('api', mailgun_api_key), data=data)
    
    if response.status_code == 200:
        print("Email sent successfully.")
    else:
        print(f"Failed to send email: {response.status_code}, {response.text}")

def generate_password_reset_token(user_id):
    try:
        conn = sqlite3.connect('app_database.db')
        cursor = conn.cursor()
        
        # Generate a unique token and set expiration time (1 hour)
        reset_token = str(uuid.uuid4())
        expires_at = datetime.now() + timedelta(hours=1)

        # Insert the token into the database
        cursor.execute('''
            INSERT INTO password_reset_tokens (user_id, reset_token, expires_at)
            VALUES (?, ?, ?)
        ''', (user_id, reset_token, expires_at))

        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()
    
    return reset_token

def reset_password(user_id, token, new_password):
    try:
        conn = sqlite3.connect('app_database.db')
        cursor = conn.cursor()

        # Validate the token and ensure it hasn't expired
        cursor.execute('''
            SELECT id FROM password_reset_tokens 
            WHERE user_id = ? AND reset_token = ? AND expires_at > ?
        ''', (user_id, token, datetime.now()))
        
        result = cursor.fetchone()

        if result:
            # Hash the new password before saving it
            hashed_password = hashlib.sha256(new_password.encode()).hexdigest()

            # Update the password and delete the reset token
            cursor.execute('UPDATE users SET password = ? WHERE id = ?', (hashed_password, user_id))
            cursor.execute('DELETE FROM password_reset_tokens WHERE id = ?', (result[0],))
            conn.commit()
            return True
        else:
            print("Invalid token or token expired.")
            return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()
