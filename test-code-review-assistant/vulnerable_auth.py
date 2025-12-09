"""
Vulnerable authentication code for Code Review Assistant testing
Should trigger: OWASP Top 10, Python security patterns, authentication category
"""

import hashlib
import sqlite3

# VULNERABLE: SQL Injection in authentication
def authenticate_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABLE: Direct string concatenation in SQL query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        return {"authenticated": True, "user_id": user[0]}
    return {"authenticated": False}

# VULNERABLE: Weak password hashing (MD5)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# VULNERABLE: Hardcoded secret
API_SECRET_KEY = "TEST_SECRET_KEY_DO_NOT_USE_IN_PRODUCTION_12345"

# VULNERABLE: Missing rate limiting
def login_attempt(username, password):
    return authenticate_user(username, password)
