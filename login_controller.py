from login_db_model import authenticate_user

def handle_login(username, password):
    # Call the authenticate_user function from user_model.py
    # This function checks if the provided username and password are valid.
    # Modify the logic based on your actual implementation in user_model.py.

    # Example: Assuming authenticate_user returns True for successful login
    if authenticate_user(username, password):
        # Additional logic if needed
        if username == "Admin":
            return "user_mgmt"
        else:
            return "least_user"
    else:
        return None  # Authentication failed
