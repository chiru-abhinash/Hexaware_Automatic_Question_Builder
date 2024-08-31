# utils/auth.py
import pandas as pd
import hashlib

USER_DATA_PATH = 'data/users.csv'

def load_users():
    return pd.read_csv(USER_DATA_PATH)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user(username, password):
    users = load_users()
    hashed_input_password = hash_password(password)
    user = users[(users['username'] == username) & (users['password'] == hashed_input_password)]
    if not user.empty:
        return user.iloc[0]['role']
    return None

def add_user(username, password, role):
    users = load_users()
    if username in users['username'].values:
        return False  # User already exists
    new_user = pd.DataFrame([[username, hash_password(password), role]], columns=users.columns)
    users = pd.concat([users, new_user], ignore_index=True)
    users.to_csv(USER_DATA_PATH, index=False)
    return True
