import sys
import os
import sqlite3
from datetime import datetime
from tkinter import messagebox
from PIL import Image, ImageTk

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_meter_num():
    conn = sqlite3.connect(resource_path("database\\vendor.db"))
    c = conn.cursor()
    c.execute("SELECT meter_number FROM meters")
    meters = c.fetchall()
    conn.close()
    return [meter[0] for meter in meters]  # Extract meter numbers from the fetched data


def vend_now_btn_clicked(least_user_gui):
    meter_number = least_user_gui.meter_number_input.get()
    selected_unit = least_user_gui.unit_selection_dropdown.get()

    try:
        from vendor_db_model import query_meter_details
        from vendor_db_model import query_vending_code
        from logs_model import log_transaction
        meter_number = least_user_gui.meter_number_input.get()
        print("Meter Number:", meter_number)
        selected_unit = int(least_user_gui.unit_selection_dropdown.get().split(" ")[0])  # Extract the numeric part

        # Fetch meter details from the meters table
        meter_details = query_meter_details(meter_number)

        if meter_details:
            meter_name = meter_details[0]
            rate = meter_details[1]
            bill_switch = meter_details[2]




            if bill_switch == 1:
                messagebox.showinfo("Bill Pending", "Please pay up your bill before you can vend.")
            
            else:
            # Fetch a vending code from the specific table based on the selected unit
                vending_code_details = query_vending_code(selected_unit)

                if vending_code_details:
                    # Update receipt labels
                    least_user_gui.receipt_vaue_b_content.configure(text=meter_name)
                    least_user_gui.receipt_vaue_c_content.configure(text=meter_number)
                    least_user_gui.receipt_vaue_d_content.configure(text=f"N{rate}/U")
                    least_user_gui.receipt_vaue_e_content.configure(text=f"{selected_unit} Units")
                    least_user_gui.receipt_vaue_f_content.configure(text=vending_code_details["vending_code"])
                    least_user_gui.receipt_vaue_g_content.configure(text=f"N{selected_unit * rate}")
                    
                    # Calculate the total amount
                    total_amount = selected_unit * rate

                    # Log the transaction
                    log_transaction("Retailer", meter_number, selected_unit, rate, vending_code_details["vending_code"], str(datetime.now()), total_amount)

                    messagebox.showinfo("Success", "Transaction logged successfully.")

                else:
                    messagebox.showerror("No Tokens Available", "All tokens for this unit are used up.")

        else:
            messagebox.showerror("Check Meter Number", "Meter not found in database")

    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    from vendor_gui import LeastUserGUI
    least_user_gui = LeastUserGUI()
    least_user_gui.vend_now_btn.bind("<Button-1>", lambda event: vend_now_btn_clicked(least_user_gui))
    least_user_gui.run()
