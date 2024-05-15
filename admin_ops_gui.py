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




class admin_ops_page():
    def __init__(self):
        self.app = CTk()
        self.app.geometry("1366x768")
        self.app.resizable(False, False)
        self.app.title("Fairbuy Offline (Admin)")
        self.app.iconbitmap(resource_path("assets\\logo.ico"))
        self.app.configure(fg_color="#F4F4F6")
        set_appearance_mode("light")



        topbar = CTkFrame(master=self.app, fg_color="#ffffff", height=50, width=1300)
        topbar.pack(expand=True)
        topbar.place(anchor="center", rely=0.05, relx= 0.5)

        salutation = CTkLabel(master=topbar, text="Hi, you are welcome!", font=("segoe UI semibold", 18), text_color="#121212")
        salutation.place(relx=0.025, rely=0.20, anchor="nw")

        def update_time():
            current_time = datetime.now().strftime("%I:%M%p | %A, %B %d")
            timing.configure(text=current_time)
            topbar.after(1000, update_time)

        timing = CTkLabel(master=topbar, text="", font=("segoe UI semibold", 14), text_color="#757474")
        timing.place(relx=0.975, rely=0.24, anchor="ne")
        update_time()

        navbar = CTkFrame(master=self.app, fg_color="#FFFFFF", width=200, height=675)
        navbar.pack(expand=True)
        navbar.place(anchor="nw", rely=0.1, relx= 0.025)

        self.user_mngt = CTkButton(master=navbar, text="User Management", corner_radius=5, fg_color="transparent", font=("segoe UI Regular", 14), hover_color="#184219", width=150, height=42, text_color="#121212", anchor="w", command=lambda: show_user_mgmt(self))
        self.user_mngt.place(relx=0.1, rely=0.18, anchor="nw")

        self.report = CTkButton(master=navbar, text="Generate Report", corner_radius=5, fg_color="transparent", font=("segoe UI Regular", 14), hover_color="#184219", width=150, height=42, text_color="#121212", anchor="w", command=lambda: show_gen_report(self))
        self.report.place(relx=0.1, rely=0.28, anchor="nw")

        self.tamper = CTkButton(master=navbar, text="Clear Tamper", corner_radius=5, fg_color="transparent", font=("segoe UI Regular", 14), hover_color="#184219", width=150, height=42, text_color="#121212", anchor="w", command=lambda: show_clear_tamper(self))
        self.tamper.place(relx=0.1, rely=0.38, anchor="nw")

        self.tarrif = CTkButton(master=navbar, text="Tarrif Management", corner_radius=5, fg_color="transparent", font=("segoe UI Regular", 14), hover_color="#184219", width=150, height=42, text_color="#121212", anchor="w", command=lambda: show_tarrif_mgmt(self))
        self.tarrif.place(relx=0.1, rely=0.48, anchor="nw")
        
        self.billing = CTkButton(master=navbar, text="Add Bills", corner_radius=5, fg_color="transparent", font=("segoe UI Regular", 14), hover_color="#184219", width=150, height=42, text_color="#121212", anchor="w", command=lambda: show_add_bill(self))
        self.billing.place(relx=0.1, rely=0.58, anchor="nw")

        self.sign_out = CTkButton(master=navbar, text="Log Out", corner_radius=5, fg_color="transparent", font=("segoe UI Regular", 14), hover_color="#184219", width=150, height=42, text_color="#121212", anchor="w", command=lambda: show_vendor_gui(self))
        self.sign_out.place(relx=0.1, rely=0.92, anchor="nw")


        def show_user_mgmt(self):
            from admin_op_guis import user_mgmt
            user_mgmt(self)

        def show_gen_report(self):
            from admin_op_guis import gen_report
            gen_report(self)

        def show_clear_tamper(self):
            from admin_op_guis import clear_tamper
            clear_tamper(self)

        def show_tarrif_mgmt(self):
            from admin_op_guis import tarrif_mgmt
            tarrif_mgmt(self)

        def show_add_bill(self):
            from admin_op_guis import add_bill
            add_bill(self)

        def show_vendor_gui(self):
            from admin_op_guis import user_mgmt
            user_mgmt(self)
                    



        self.app.mainloop()


    


def run(self):
    self.app.mainloop()

if __name__ == "__main__":
    app = admin_ops_page()
    app.mainloop()



























