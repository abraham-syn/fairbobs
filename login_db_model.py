import sys
import os
import sqlite3
import bcrypt



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Add project directories to the Python path
current_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(current_directory)
sys.path.append(project_directory)


def hash_password(password):
    # Hash password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

# Operation 1: User Registration
# def register_user(username, password):
#     # Hash the password
#     hashed_password = hash_password(password)

#     # Connect to the SQLite database
#     conn = sqlite3.connect("userbase.db")
#     c = conn.cursor()

#     # Insert user into the database
#     c.execute('''
#         INSERT INTO users (username, password)
#         VALUES (?, ?)
#     ''', (username, hashed_password))

#     # Commit changes and close the connection
#     conn.commit()
#     conn.close()

# Operation 2: User Authentication
def authenticate_user(username, password):
    conn = None
    try:
        # Connect to the SQLite database
        # database_path = os.path.join("database", "userbase.db")
        conn = sqlite3.connect(resource_path("database\\userbase.db"))
        c = conn.cursor()

        # Retrieve hashed password from the database
        c.execute('''
            SELECT password FROM users
            WHERE username = ?
        ''', (username,))

        stored_hashed_password = c.fetchone()

        # Check if the user exists and the password is correct
        if stored_hashed_password:
            # Compare the hashed entered password with the stored hashed password
            entered_password_hashed = bcrypt.hashpw(password.encode('utf-8'), stored_hashed_password[0])

            if entered_password_hashed == stored_hashed_password[0]:
                # Passwords match, authentication successful
                return True
            else:
                # Passwords don't match, authentication failed
                return False
        else:
            # User not found, authentication failed
            return False
    finally:
        # Close the connection in the finally block to ensure proper cleanup
        if conn:
            conn.close()


# Operation 3: User Retrieval
def get_user_info(username):
    # Connect to the SQLite database
    conn = sqlite3.connect("userbase.db")
    c = conn.cursor()

    # Retrieve user information based on the username
    c.execute('''
        SELECT id, username FROM users
        WHERE username = ?
    ''', (username,))

    user_info = c.fetchone()

    # Close the connection
    conn.close()

    return user_info

# Operation 4: User Update
def update_user_password(username, new_password):
    # Hash the new password
    new_hashed_password = hash_password(new_password)

    # Connect to the SQLite database
    conn = sqlite3.connect("userbase.db")
    c = conn.cursor()

    # Update the user's password in the database
    c.execute('''
        UPDATE users
        SET password = ?
        WHERE username = ?
    ''', (new_hashed_password, username))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Operation 5: User Deletion
def delete_user(username):
    # Connect to the SQLite database
    conn = sqlite3.connect("userbase.db")
    c = conn.cursor()

    # Delete the user from the database
    c.execute('''
        DELETE FROM users
        WHERE username = ?
    ''', (username,))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Operation 6: List All Users
def list_all_users():
    # Connect to the SQLite database
    conn = sqlite3.connect("userbase.db")
    c = conn.cursor()

    # Retrieve a list of all users in the database
    c.execute('''
        SELECT username FROM users
    ''')

    all_users = c.fetchall()

    # Close the connection
    conn.close()

    return all_users

# Operation 7: User Count
def get_user_count():
    # Connect to the SQLite database
    conn = sqlite3.connect("userbase.db")
    c = conn.cursor()

    # Get the total number of registered users
    c.execute('''
        SELECT COUNT(*) FROM users
    ''')

    user_count = c.fetchone()[0]

    # Close the connection
    conn.close()

    return user_count

