import sys
import sqlite3
import os
from datetime import datetime
from customtkinter import CTk, CTkLabel, CTkFrame, CTkButton, CTkEntry, CTkComboBox
from PIL import Image, ImageTk
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from tkinter import messagebox

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



class LeastUserGUI:
    def __init__(self):
        self.app = CTk()
        self.app.geometry("1366x768")
        self.app.title("Fairbuy offline")
        self.app.resizable(True, True)
        self.app.iconbitmap(resource_path("assets\\logo.ico"))
        self.app.configure(fg_color="#F4F4F6")

        
        bg_image = Image.open(resource_path("assets\\bgimg.jpg"))
        bg_image = ImageTk.PhotoImage(bg_image)
        bg_label = CTkLabel(master=self.app, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)



        navbar = CTkFrame(master=self.app, fg_color="#ffffff", height=50, width=1300)
        navbar.pack(expand=True)
        navbar.place(anchor="center", rely=0.05, relx= 0.5)

        salutation = CTkLabel(master=navbar, text="Hi, you are welcome!", font=("segoe UI semibold", 18), text_color="#121212")
        salutation.place(relx=0.025, rely=0.20, anchor="nw")

        def update_time():
            current_time = datetime.now().strftime("%I:%M%p | %A, %B %d")
            timing.configure(text=current_time)
            navbar.after(1000, update_time)

        timing = CTkLabel(master=navbar, text="", font=("segoe UI semibold", 14), text_color="#757474")
        timing.place(relx=0.975, rely=0.24, anchor="ne")
        update_time()

        vending_section = CTkFrame(master=self.app, fg_color="#F4F4F6", height=674, width=935,)
        vending_section.pack(expand=True)
        vending_section.place(anchor="nw", rely=0.1, relx= 0.023)

        greeting = CTkLabel(master=vending_section, text="Buy Electricity", font=("segoe UI semibold", 28), text_color="#121212")
        greeting.place(relx=0.04, rely=0.10, anchor="nw")

        meter_number = CTkLabel(master=vending_section, text="Meter Number", font=("segoe UI semibold", 20), text_color="#121212")
        meter_number.place(relx=0.04, rely=0.28, anchor="nw")

        from vendor_controller import get_meter_num
        meter_num = get_meter_num()
        self.meter_number_input = CTkComboBox(master=vending_section, font=("segoe UI", 12), width=340, height=44, text_color="#121212", border_color="#B2B2B2", border_width=1, fg_color="#ffffff", values=meter_num)
        self.meter_number_input.place(relx=0.04, rely=0.33, anchor="nw")

        self.unit_selection = CTkLabel(master=vending_section, text="Number of Units", font=("segoe UI semibold", 20), text_color="#121212")
        self.unit_selection.place(relx=0.04, rely=0.43, anchor="nw")

        unit_selection_dropdown = CTkComboBox(master=vending_section, values=["5 Units", "10 Units", "20 Units", "50 Units", "100 Units", "200 Units", "500 Units", "1000 Units"], width=340, height=42, border_color="#B2B2B2", border_width=1)
        unit_selection_dropdown.place(relx=0.04, rely=0.48, anchor="nw")

        self.unit_selection_dropdown = unit_selection_dropdown  # Add this line
        from vendor_controller import vend_now_btn_clicked

        vend_now_btn = CTkButton(master=vending_section, text="Vend Now", corner_radius=5, fg_color="#165318", font=("segoe UI semibold", 16), hover_color="#184219", width=350, height=42, command=lambda: vend_now_btn_clicked(self))
        vend_now_btn.place(relx=0.04, rely=0.63, anchor="nw")

        receipt = CTkFrame(master=self.app, fg_color="#ffffff", height=614, width=350)
        receipt.pack(expand=True)
        receipt.place(anchor="ne", rely=0.1, relx= 0.975)

        receipt_greeting = CTkLabel(master=receipt, text="Receipt", font=("segoe UI semibold", 28), text_color="#121212")
        receipt_greeting.place(relx=0.05, rely=0.10, anchor="nw")

        def update_transaction_time():
            current_time = datetime.now().strftime("%B %d | %I:%M%p")
            receipt_vaue_a_content.configure(text=current_time)
            receipt.after(1000, update_time)

        receipt_vaue_a = CTkLabel(master=receipt, text="Date|time:", font=("segoe UI semibold", 16), text_color="#757474")
        receipt_vaue_a.place(relx=0.05, rely=0.22, anchor="nw")
        receipt_vaue_a_content = CTkLabel(master=receipt, text="", font=("segoe UI semibold", 16), text_color="#121212")
        receipt_vaue_a_content.place(relx=0.42, rely=0.22, anchor="nw")
        update_transaction_time()

        receipt_vaue_b = CTkLabel(master=receipt, text="Meter Name:", font=("segoe UI semibold", 16), text_color="#757474")
        receipt_vaue_b.place(relx=0.05, rely=0.29, anchor="nw")
        self.receipt_vaue_b_content = CTkLabel(master=receipt, text="", font=("segoe UI semibold", 16), text_color="#121212")
        self.receipt_vaue_b_content.place(relx=0.42, rely=0.29, anchor="nw")

        receipt_vaue_c = CTkLabel(master=receipt, text="Meter Number:", font=("segoe UI semibold", 16), text_color="#757474")
        receipt_vaue_c.place(relx=0.05, rely=0.36, anchor="nw")
        self.receipt_vaue_c_content = CTkLabel(master=receipt, text="", font=("segoe UI semibold", 16), text_color="#121212")
        self.receipt_vaue_c_content.place(relx=0.42, rely=0.36, anchor="nw")

        receipt_vaue_d = CTkLabel(master=receipt, text="Tarrif:", font=("segoe UI semibold", 16), text_color="#757474")
        receipt_vaue_d.place(relx=0.05, rely=0.43, anchor="nw")
        self.receipt_vaue_d_content = CTkLabel(master=receipt, text="", font=("segoe UI semibold", 16), text_color="#121212")
        self.receipt_vaue_d_content.place(relx=0.42, rely=0.43, anchor="nw")

        receipt_vaue_e = CTkLabel(master=receipt, text="Purchased units:", font=("segoe UI semibold", 16), text_color="#757474")
        receipt_vaue_e.place(relx=0.05, rely=0.50, anchor="nw")
        self.receipt_vaue_e_content = CTkLabel(master=receipt, text="", font=("segoe UI semibold", 16), text_color="#121212")
        self.receipt_vaue_e_content.place(relx=0.42, rely=0.50, anchor="nw")

        receipt_vaue_f = CTkLabel(master=receipt, text="Token:", font=("segoe UI semibold", 16), text_color="#757474")
        receipt_vaue_f.place(relx=0.05, rely=0.57, anchor="nw")
        self.receipt_vaue_f_content = CTkLabel(master=receipt, text="", font=("segoe UI semibold", 16), text_color="#121212")
        self.receipt_vaue_f_content.place(relx=0.42, rely=0.57, anchor="nw")

        receipt_vaue_g = CTkLabel(master=receipt, text="Total amount:", font=("segoe UI semibold", 16), text_color="#757474")
        receipt_vaue_g.place(relx=0.05, rely=0.64, anchor="nw")
        self.receipt_vaue_g_content = CTkLabel(master=receipt, text="", font=("segoe UI semibold", 16), text_color="#121212")
        self.receipt_vaue_g_content.place(relx=0.42, rely=0.64, anchor="nw")

        print_receipt = CTkButton(master=self.app, text="Print Receipt", corner_radius=5, fg_color="#165318", font=("segoe UI semibold", 16), hover_color="#184219", width=350, height=42, command=lambda: receipt_btn_clicked(self))
        print_receipt.place(relx=0.975, rely=0.922, anchor="ne")

        def receipt_btn_clicked(self):
            # Get content from the receipt frame
            content = [
                ("Date|time:", receipt_vaue_a_content.cget("text")),
                ("Meter Name:", self.receipt_vaue_b_content.cget("text")),
                ("Meter Number:", self.receipt_vaue_c_content.cget("text")),
                ("Tarrif:", self.receipt_vaue_d_content.cget("text")),
                ("Purchased units:", self.receipt_vaue_e_content.cget("text")),
                ("Token:", self.receipt_vaue_f_content.cget("text")),
                ("Total amount:", self.receipt_vaue_g_content.cget("text")),
            ]

            # Get the path to the desktop
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            
            # Specify the PDF file path
            pdf_file_path = os.path.join(desktop_path, "receipt.pdf")

            # Create a PDF file
            c = canvas.Canvas(pdf_file_path, pagesize=(58*mm, 100*mm))  # Adjusted for a 58mm printer

            # Set initial y coordinate for drawing
            y_coordinate = 95*mm
            
            # Set the font size and style for the title
            title_font_size = 10
            title_font = "Helvetica-Bold"

            # Write title to PDF
            c.setFont(title_font, title_font_size)
            c.drawString(10*mm, y_coordinate, "Fairbuy Offline Vending")

            # Set initial y coordinate for receipt content
            y_coordinate -= 5*mm  # Adjust spacing for the receipt content
            
            # Set the font size and style for labels
            label_font_size = 7
            label_font = "Helvetica"

            # Set the font size and style for values
            value_font_size = 7
            value_font = "Helvetica-Bold"  # Setting the font weight to bold

            # Write content to PDF
            for label, value in content:
                # Draw label
                c.setFont(label_font, label_font_size)
                c.drawString(5*mm, y_coordinate, label)
                
                # Draw value with bold font
                c.setFont(value_font, value_font_size)
                c.drawString(5*mm, y_coordinate - 10, value)  # Adjusted for margin between label and value
                
                # Adjust y coordinate for the next pair of label and value
                y_coordinate -= 10*mm  # Adjust spacing for the next pair

            # Save and close the PDF
            c.save()

            # Display success message
            messagebox.showinfo("Success", f"Receipt printed to PDF successfully!\nSaved to: {pdf_file_path}")


        self.app.mainloop()

def run(self):
    self.app.mainloop()

if __name__ == "__main__":
    least_user_gui = LeastUserGUI()
    least_user_gui.run()

