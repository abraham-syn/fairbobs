import sqlite3
import bcrypt
import os
import sys
from tkinter import messagebox

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def hash_password(password):
    # Hash password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

def get_users():
    conn = sqlite3.connect(resource_path("database\\userbase.db"))
    c = conn.cursor()
    c.execute("SELECT username FROM users")
    users = c.fetchall()
    conn.close()
    return [user[0] for user in users]  # Extract usernames from the fetched data

def change_password(username, new_password):
    conn = sqlite3.connect(resource_path("database\\userbase.db"))
    c = conn.cursor()
    try:
        hashed_password = hash_password(new_password)
        c.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_password, username))
        conn.commit()
        messagebox.showinfo("Success", "Password changed successfully")
    except Exception as e:
        print("Error:", e)  # Log the error
        messagebox.showerror("Error", "Failed to change password")
    finally:
        conn.close()


def get_meters():
    conn = sqlite3.connect(resource_path("database\\vendor.db"))
    c = conn.cursor()
    c.execute("SELECT meter_name FROM meters")
    meters = c.fetchall()
    conn.close()
    return [meter_name[0] for meter_name in meters]  # Extract meternames from the fetched data


def change_bill_switch(meter_name, bill_change):
    conn = sqlite3.connect(resource_path("database\\vendor.db"))
    c = conn.cursor()
    try:
        c.execute("UPDATE meters SET bill_switch = ? WHERE meter_name = ?", (bill_change, meter_name))
        conn.commit()
        if bill_change == 1:
            messagebox.showinfo("Success", "Bill added Succesfully")
        elif bill_change == 0:
            messagebox.showinfo("Success", "Bill removed Succesfully")
    except Exception as e:
        print("Error:", e)  # Log the error
        messagebox.showerror("Error", "Failed to remove or add bill")
    finally:
        conn.close()


def change_tariff(meter_name, new_tariff):
    conn = sqlite3.connect(resource_path("database\\vendor.db"))
    c = conn.cursor()
    try:
        # Update the rate for the specified meter
        c.execute("UPDATE meters SET rate = ? WHERE meter_name = ?", (new_tariff, meter_name))
        conn.commit()
        print("Tariff changed successfully")
    except sqlite3.Error as e:
        print(f"Error changing tariff: {e}")