import sqlite3
import bcrypt
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# project_directory = os.path.dirname(os.path.abspath(__file__))
# database_path = os.path.join(project_directory, "database", "vendor.db")


def query_meter_details(meter_number):
    conn = sqlite3.connect(resource_path("database\\vendor.db"))
    cursor = conn.cursor()

    cursor.execute("SELECT meter_name, rate, bill_switch FROM meters WHERE meter_number=?", (meter_number,))
    meter_details = cursor.fetchone()

    conn.commit()
    conn.close()

    return meter_details

def query_vending_code(selected_unit):
    units_table = f"Units_{selected_unit}"
    conn = sqlite3.connect(resource_path("database\\vendor.db"))
    cursor = conn.cursor()

    # Use string formatting to insert the table name into the query
    cursor.execute(f"SELECT vending_code FROM {units_table} WHERE use_switch=0 LIMIT 1")
    vending_code = cursor.fetchone()[0]

    # Use string formatting to insert the table name and vending code into the query
    cursor.execute(f"UPDATE {units_table} SET use_switch=1 WHERE vending_code=?", (vending_code,))

    conn.commit()  # Commit changes to the database
    conn.close()

    return {"vending_code": vending_code}


