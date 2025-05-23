import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        name = entry_name.get()
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())
        
        birth_date = datetime(year, month, day)
        today = datetime.today()
        
        # Calculate age
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        message = f"Hello {name}, you are {age} years old."
        messagebox.showinfo("Age Result", message)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid date, month, and year.")

# Create the main window
root = tk.Tk()
root.geometry("400x400")
root.title("Age Calculator App")
root.configure(bg="#e6f2ff")  # Light blue background

# Labels and Entry Widgets
label_title = tk.Label(root, text="Age Calculator", font=("Arial", 16, "bold"), bg="#e6f2ff", fg="#003366")
label_title.grid(row=0, column=0, columnspan=2, pady=20)

tk.Label(root, text="Name:", bg="#e6f2ff", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_name = tk.Entry(root, width=25)
entry_name.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Date (DD):", bg="#e6f2ff", font=("Arial", 12)).grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_day = tk.Entry(root, width=25)
entry_day.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Month (MM):", bg="#e6f2ff", font=("Arial", 12)).grid(row=3, column=0, sticky="e", padx=10, pady=5)
entry_month = tk.Entry(root, width=25)
entry_month.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Year (YYYY):", bg="#e6f2ff", font=("Arial", 12)).grid(row=4, column=0, sticky="e", padx=10, pady=5)
entry_year = tk.Entry(root, width=25)
entry_year.grid(row=4, column=1, padx=10, pady=5)

# Submit Button
btn_submit = tk.Button(root, text="Calculate Age", command=calculate_age, bg="#3366cc", fg="white", font=("Arial", 12))
btn_submit.grid(row=5, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
