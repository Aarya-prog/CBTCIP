import tkinter as tk
from tkinter import messagebox, ttk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def create_receipt(file_path, transaction_details):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Add title
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2.0, height - 40, "Payment Receipt")

    # Add transaction details
    c.setFont("Helvetica", 12)
    text = c.beginText(40, height - 80)
    for key, value in transaction_details.items():
        text.textLine(f"{key}: {value}")
    c.drawText(text)

    c.save()

def generate_receipt():
    transaction_details = {
        "Transaction ID": entry_trans_id.get(),
        "Customer Name": entry_customer_name.get(),
        "Date": entry_date.get(),
        "Time": entry_time.get(),
        "Amount": entry_amount.get(),
        "Payment Method": payment_method.get()
    }
    
    if all(transaction_details.values()):
        create_receipt("payment_receipt.pdf", transaction_details)
        messagebox.showinfo("Success", "Receipt generated successfully!")
        root.destroy()  # Close the window
    else:
        messagebox.showwarning("Input Error", "Please fill all the fields")

def set_current_datetime():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    entry_date.delete(0, tk.END)
    entry_date.insert(0, current_date)
    entry_time.delete(0, tk.END)
    entry_time.insert(0, current_time)

# Create the main window
root = tk.Tk()
root.title("Payment Receipt Generator")

# Create and place labels and entry widgets for input
labels = ["Transaction ID", "Customer Name", "Date", "Time", "Amount", "Payment Method"]
entries = {}

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
    if label == "Payment Method":
        payment_method = ttk.Combobox(root, values=["Cash", "Credit Card", "Debit Card", "Bank Transfer", "UPI"])
        payment_method.grid(row=i, column=1, padx=10, pady=5)
    else:
        entry = tk.Entry(root)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[label] = entry

entry_trans_id = entries["Transaction ID"]
entry_customer_name = entries["Customer Name"]
entry_date = entries["Date"]
entry_time = entries["Time"]
entry_amount = entries["Amount"]

# Set current date and time
set_current_datetime()

# Create and place the generate button
generate_button = tk.Button(root, text="Generate Receipt", command=generate_receipt)
generate_button.grid(row=len(labels), columnspan=2, pady=20)

# Run the GUI event loop
root.mainloop()
