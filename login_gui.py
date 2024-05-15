import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(current_directory)
sys.path.append(project_directory)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

from customtkinter import *
from customtkinter import CTkImage
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk



def sign_in_gui():
    app = CTk()
    app.geometry("1366x768")
    app.title("Fairbuy")
    app.resizable(True, True)

    global bg_image
    bg_image_path = os.path.join(current_directory, "assets", "bgimg.jpg")
    bg_image = Image.open(resource_path("assets\\bgimg.jpg"))
    bg_image1 = ImageTk.PhotoImage(bg_image)

    # CTkButton(master=root, image=bg_image1).pack(side=LEFT)
    bg_label = CTkLabel(master=app, image=bg_image1, text="")
    bg_label.place(relwidth=1, relheight=1)

    content_section = CTkFrame(master=app, fg_color="#ffffff", height=768, width=500)
    content_section.pack(expand=True)
    content_section.place(anchor="nw")

    greeting = CTkLabel(master=content_section, text="You are welcome", font=("segoe UI semibold", 28), text_color="#121212")
    greeting.place(relx=0.1, rely=0.2, anchor="nw")

    instruction = CTkLabel(master=content_section, text="You are welcome, enter your credentials to login.", font=("segoe UI", 14), text_color="#363636")
    instruction.place(relx=0.1, rely=0.26, anchor="nw")

    username = CTkLabel(master=content_section, text="Username", font=("segoe UI semibold", 16), text_color="#121212")
    username.place(relx=0.1, rely=0.37, anchor="nw")

    username_input = CTkEntry(master=content_section, placeholder_text="Enter your username", font=("segoe UI", 12), width=300, height=34, text_color="#121212", border_color="#B2B2B2", border_width=1, fg_color="#ffffff")
    username_input.place(relx=0.1, rely=0.41, anchor="nw")

    password = CTkLabel(master=content_section, text="Password", font=("segoe UI semibold", 16), text_color="#121212")
    password.place(relx=0.1, rely=0.48, anchor="nw")

    password_input = CTkEntry(master=content_section, show="*", placeholder_text="Enter your Password", width=300, height=34, font=("segoe UI", 12), text_color="#121212", border_color="#B2B2B2", border_width=1, fg_color="#ffffff")
    password_input.place(relx=0.1, rely=0.52, anchor="nw")

    caveat = CTkLabel(master=content_section, text="Ensure to type in the correct password", font=("segoe UI", 10), text_color="#757474")
    caveat.place(relx=0.1, rely=0.565, anchor="nw")

    def on_sign_in():
        entered_username = username_input.get()
        entered_password = password_input.get()
        from login_controller import handle_login
        login_result = handle_login(entered_username, entered_password)

        if login_result == "least_user":
            # Close the current window
            content_section.master.destroy()

            # Create and run the new window
            from vendor_gui import LeastUserGUI
            least_user_gui = LeastUserGUI()
            least_user_gui.run()
        elif login_result == "user_mgmt":
            # Close the current window
            content_section.master.destroy()

            # Create and run the new window
            from admin_ops_gui import admin_ops_page 
            admin_ops_page()
        else:
            # Display an error message
            messagebox.showerror("Authentication Failed", "Wrong password or user not found.")


    signinbtn = CTkButton(master=content_section, text="Sign In", corner_radius=5, fg_color="#165318", font=("segoe UI semibold", 16), hover_color="#184219", width=300, height=34, command=on_sign_in)
    signinbtn.place(relx=0.1, rely=0.638, anchor="nw")

    app.mainloop()
if __name__ == "__main__":
    sign_in_gui()