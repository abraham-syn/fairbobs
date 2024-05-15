import os
import sys
import sqlite3
from datetime import datetime

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def initialize_logs_database():
    # Use the current working directory to determine the database location
    # current_directory = os.getcwd()
    # database_path = os.path.join(current_directory, "Logs.db")

    # Connect to the SQLite database
    conn = sqlite3.connect(resource_path("database\\logs.db"))
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            meter_number TEXT NOT NULL,
            Units INTEGER NOT NULL,
            vending_code TEXT NOT NULL,
            datetime TEXT NOT NULL,
            amount REAL NOT NULL
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Beginning of operation 1: Log Transaction
def log_transaction(username, meter_number, Units, rate, vending_code, datetime, amount):
    # Use the current working directory to determine the database location
    # current_directory = os.getcwd()
    # database_path = os.path.join(current_directory, "Logs.db")

    # Connect to the SQLite database
    conn = sqlite3.connect(resource_path("database\\logs.db"))
    c = conn.cursor()

    # Log the transaction in the database
    c.execute('''
        INSERT INTO transactions (username, meter_number, Units, rate, vending_code, datetime, amount)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (username, meter_number, Units, rate, vending_code, datetime, amount))

    # Commit changes and close the connection
    conn.commit()
    conn.close()
# End of operation 1: Log Transaction

# Beginning of operation 2: Retrieve Transactions
def retrieve_transactions(username=None, meter_number=None, start_date=None, end_date=None):
    # Connect to the SQLite database
    conn = sqlite3.connect(resource_path("database\\logs.db"))
    c = conn.cursor()

    # Build SQL query based on provided criteria
    query = '''
        SELECT * FROM transactions
        WHERE (? IS NULL OR username = ?)
        AND (? IS NULL OR meter_number = ?)
        AND (? IS NULL OR datetime BETWEEN ? AND ?)
    '''

# Execute the query with provided parameters
    c.execute(query, (username, meter_number, meter_number, start_date, end_date, start_date, end_date))



    # Retrieve transactions based on the query
    result = c.fetchall()

    # Close the connection
    conn.close()

    return result
# End of operation 2: Retrieve Transactions

# Beginning of operation 3: Calculate Total Amount
def calculate_total_amount():
    # Connect to the SQLite database
    conn = sqlite3.connect(resource_path("database\\logs.db"))
    c = conn.cursor()

    # Get the total amount of all transactions
    c.execute('''
        SELECT SUM(amount) FROM transactions
    ''')

    total_amount = c.fetchone()[0] or 0

    # Close the connection
    conn.close()

    return total_amount
# End of operation 3: Calculate Total Amount

# Beginning of operation 4: Delete Transactions
def delete_transactions(username=None, start_date=None, end_date=None):
    # Connect to the SQLite database
    conn = sqlite3.connect(resource_path("database\\logs.db"))
    c = conn.cursor()

    # Build SQL query based on provided criteria
    query = '''
        DELETE FROM transactions
        WHERE (? IS NULL OR username = ?)
        AND (? IS NULL OR datetime BETWEEN ? AND ?)
    '''

    # Execute the query with provided parameters
    c.execute(query, (username, username, start_date, end_date))

    # Commit changes and close the connection
    conn.commit()
    conn.close()
# End of operation 4: Delete Transactions

# Beginning of operation 5: Retrieve Transaction Count
def get_transaction_count():
    # Connect to the SQLite database
    conn = sqlite3.connect(resource_path("database\\logs.db"))
    c = conn.cursor()

    # Get the total number of transactions
    c.execute('''
        SELECT COUNT(*) FROM transactions
    ''')

    transaction_count = c.fetchone()[0]

    # Close the connection
    conn.close()

    return transaction_count
# End of operation 5: Retrieve Transaction Count

# Beginning of operation 6: Retrieve Transactions by Amount Range
def retrieve_transactions_by_amount_range(min_amount, max_amount):
    # Connect to the SQLite database
    conn = sqlite3.connect(resource_path("database\\logs.db"))
    c = conn.cursor()

    # Retrieve transactions within the specified amount range
    c.execute('''
        SELECT * FROM transactions
        WHERE amount BETWEEN ? AND ?
    ''', (min_amount, max_amount))

    result = c.fetchall()

    # Close the connection
    conn.close()

    return result
# End of operation 6: Retrieve Transactions by Amount Range

if __name__ == "__main__":
    # Example usage:
    log_transaction("User1", "123456", 100, "token123", 50.0)
    log_transaction("User2", "789012", 150, "token456", 75.0)

    retrieved_transactions = retrieve_transactions(username="User1")
    print("Retrieved Transactions:", retrieved_transactions)

    total_amount = calculate_total_amount()
    print("Total Amount:", total_amount)

    delete_transactions(username="User2")
    remaining_transactions = get_transaction_count()
    print("Remaining Transactions:", remaining_transactions)

    amount_range_transactions = retrieve_transactions_by_amount_range(40.0, 60.0)
    print("Transactions within Amount Range:", amount_range_transactions)
