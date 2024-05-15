import sys
import os
from tkinter import *
from customtkinter import *
from datetime import datetime
from PIL import Image, ImageTk

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

















def user_mgmt(self):
    user_mngt_tab = CTkFrame(master=self.app, fg_color="#ffffff", height=555, width=1075.5)
    user_mngt_tab.place(anchor="nw", rely=0.255, relx= 0.185)

    task = CTkLabel(master=self.app, text="User Management", font=("segoe UI semibold", 22), text_color="#121212", fg_color="#F4F4F6", width=200)
    task.place(relx=0.185, rely=0.18, anchor="nw")
    # End of Navbar frame contents


    # Beginning of tab
    self.user_selection = CTkLabel(master=self.app, text="Select User", font=("segoe UI semibold", 20), text_color="#121212", fg_color="#ffffff")
    self.user_selection.place(relx=0.22, rely=0.38, anchor="nw")

    from admin_controller import get_users
    users = get_users()
    self.user_selection_dropdown = CTkComboBox(master=self.app, values=users, width=240, height=42, border_color="#B2B2B2", border_width=1)  # Pass fetched users to values parameter
    self.user_selection_dropdown.place(relx=0.22, rely=0.43, anchor="nw")

    self.new_password = CTkLabel(master=self.app, text="Enter New Password", font=("segoe UI semibold", 20), text_color="#121212", fg_color="#ffffff")
    self.new_password.place(relx=0.41, rely=0.38, anchor="nw")

    self.new_password_input = CTkEntry(master=self.app, placeholder_text="Enter New Password", font=("segoe UI", 12), width=240, height=42, text_color="#121212", border_color="#B2B2B2", border_width=1, fg_color="#ffffff")
    self.new_password_input.place(relx=0.41, rely=0.43, anchor="nw")


    from admin_controller import change_password
    self.change_password_btn = CTkButton(master=self.app, text="Change Password", corner_radius=5, fg_color="#165318", font=("segoe UI semibold", 16), hover_color="#184219", width=240, height=42, command=lambda: change_password_btn_clicked(self))
    self.change_password_btn.place(relx=0.62, rely=0.43, anchor="nw")

    # Function to handle 'change_password_btn_clicked' button.
    def change_password_btn_clicked(user_mgmt):
        from admin_ops_gui import user_mgmt
        username = self.user_selection_dropdown.get()  # Get selected username from dropdown
        new_password = self.new_password_input.get()  # Get new password from input field
        change_password(username, new_password)





def gen_report(self):
        
    # End of Navbar
    task_disp = CTkFrame(master=self.app, fg_color="#ffffff", height=555, width=1075.5)
    task_disp.place(anchor="nw", rely=0.255, relx= 0.185)

    task = CTkLabel(master=self.app, text="Report Generation", font=("segoe UI semibold", 22), text_color="#121212", fg_color="#F4F4F6", width=200)
    task.place(relx=0.185, rely=0.18, anchor="nw")

    # Beginning of task content
    Download_Report_btn = CTkButton(master=task_disp, text="Download Report", corner_radius=5, fg_color="#165318", font=("segoe UI semibold", 16), hover_color="#184219", width=350, height=42, command=lambda: download_report(self))
    Download_Report_btn.place(relx=0.04, rely=0.1, anchor="nw")

    def download_report(self):
        from logs_model import retrieve_transactions
        from report_generator import generate_pdf_report
        transactions_done = retrieve_transactions()
        generate_pdf_report(transactions_done)






def clear_tamper(self):
    task_disp = CTkFrame(master=self.app, fg_color="#ffffff", height=555, width=1075.5)
    task_disp.place(anchor="nw", rely=0.255, relx= 0.185)

    task = CTkLabel(master=self.app, text="Clear Tamper", font=("segoe UI semibold", 22), text_color="#121212", fg_color="#F4F4F6", width=200)
    task.place(relx=0.185, rely=0.18, anchor="nw")

    self.user_selection = CTkLabel(master=self.app, text="Select Meter", font=("segoe UI semibold", 20), text_color="#121212", fg_color="#ffffff")
    self.user_selection.place(relx=0.22, rely=0.38, anchor="nw")

    user_selection_dropdown = CTkComboBox(master=self.app, values=["Retail1", "Admin"], width=290, height=42, border_color="#B2B2B2", border_width=1)
    user_selection_dropdown.place(relx=0.22, rely=0.43, anchor="nw")

    clear_tamper_btn = CTkButton(master=self.app, text="Generate Tamper", corner_radius=5, fg_color="#165318", font=("segoe UI semibold", 16), hover_color="#184219", width=240, height=42)
    clear_tamper_btn.place(relx=0.45, rely=0.43, anchor="nw")






def tarrif_mgmt(self):
    # Beginning of task display
    task_disp = CTkFrame(master=self.app, fg_color="#ffffff", height=555, width=1075.5)
    task_disp.place(anchor="nw", rely=0.255, relx= 0.185)

    task = CTkLabel(master=self.app, text="Change Tarrif", font=("segoe UI semibold", 22), text_color="#121212", fg_color="#F4F4F6", width=200)
    task.place(relx=0.185, rely=0.18, anchor="nw")

    self.new_tarrif = CTkLabel(master=self.app, text="Enter New Tarrif", font=("segoe UI semibold", 20), text_color="#121212", fg_color="#ffffff")
    self.new_tarrif.place(relx=0.22, rely=0.38, anchor="nw")

    self.new_tarrif_input = CTkEntry(master=self.app, placeholder_text="Enter New Tarrif", font=("segoe UI", 12), width=240, height=42, text_color="#121212", border_color="#B2B2B2", border_width=1, fg_color="#ffffff")
    self.new_tarrif_input.place(relx=0.22, rely=0.43, anchor="nw")
    from admin_controller import change_tariff
    change_tarrif_btn = CTkButton(master=self.app, text="change Tarrif", corner_radius=5, fg_color="#165318", font=("segoe UI semibold", 16), hover_color="#184219", width=240, height=42, command=lambda: change_tarrif_btn_clicked(self))
    change_tarrif_btn.place(relx=0.45, rely=0.43, anchor="nw")

    def change_tarrif_btn_clicked():
        meter_name = self.selected_meter_name  # Get the selected meter name
        new_tariff = float(self.new_tariff_input.get())  # Get the new tariff from the input field
        change_tariff(meter_name, new_tariff)






def add_bill(self):
    task_disp = CTkFrame(master=self.app, fg_color="#ffffff", height=555, width=1075.5)
    task_disp.place(anchor="nw", rely=0.255, relx= 0.185)

    task = CTkLabel(master=self.app, text="Add Bill", font=("segoe UI semibold", 22), text_color="#121212", fg_color="#F4F4F6", width=200)
    task.place(relx=0.185, rely=0.18, anchor="nw")

    self.user_selection = CTkLabel(master=self.app, text="Select Meter", font=("segoe UI semibold", 20), text_color="#121212", fg_color="#ffffff")
    self.user_selection.place(relx=0.22, rely=0.38, anchor="nw")

    from admin_controller import get_meters
    meters = get_meters()
    self.bill_switch_selection_dropdown = CTkComboBox(master=self.app, values=meters, width=240, height=42, border_color="#B2B2B2", border_width=1)
    self.bill_switch_selection_dropdown.place(relx=0.22, rely=0.43, anchor="nw")

    self.new_password = CTkLabel(master=self.app, text="Billing Option", font=("segoe UI semibold", 20), text_color="#121212", fg_color="#ffffff")
    self.new_password.place(relx=0.41, rely=0.38, anchor="nw")

    from admin_controller import change_bill_switch
    self.new_bill_switch_input = CTkComboBox(master=self.app, values=["1", "0"], width=240, height=42, border_color="#B2B2B2", border_width=1)
    self.new_bill_switch_input.place(relx=0.41, rely=0.43, anchor="nw")

    change_bill_switch_btn = CTkButton(master=self.app, text="Make Changes", corner_radius=5, fg_color="#165318", font=("segoe UI semibold", 16), hover_color="#184219", width=240, height=42, command=lambda: change_bill_switch_btn_clicked(self))
    change_bill_switch_btn.place(relx=0.62, rely=0.43, anchor="nw")

    def change_bill_switch_btn_clicked(add_bill):
        # from admin_ops_controller import change_bill_switch
        meter_name = self.bill_switch_selection_dropdown.get()  # Get selected username from dropdown
        new_bill_switch = int(self.new_bill_switch_input.get())  # Get new password from input field
        change_bill_switch(meter_name, new_bill_switch)

