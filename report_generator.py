import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def generate_pdf_report(transactions):
    # Get the desktop folder path
    desktop_folder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    # Create 'fairbuy_receipts' folder if it doesn't exist
    fairbuy_receipts_folder = os.path.join(desktop_folder, 'fairbuy_receipts')
    if not os.path.exists(fairbuy_receipts_folder):
        os.makedirs(fairbuy_receipts_folder)
    
    # Create a PDF document
    pdf_filename = os.path.join(fairbuy_receipts_folder, "transactions_report.pdf")
    pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)

    # Define the data for the table
    data = [["ID", "Username", "Meter Number", "Units", "Rate", "Vending Code", "Date/Time", "Amount"]]
    for transaction in transactions:
        data.append(list(transaction))

    # Create a table with the data
    table = Table(data)

    # Add style to the table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)

    # Add the table to the PDF document
    pdf.build([table])

# Example usage:
transactions = [
    ["1", "user1", "123", "10", "2", "abc123", "2024-03-22", "20"],
    ["2", "user2", "456", "15", "3", "def456", "2024-03-23", "45"],
    ["3", "user3", "789", "20", "4", "ghi789", "2024-03-24", "80"]
]

generate_pdf_report(transactions)
