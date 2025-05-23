import tkinter as tk
from tkinter import messagebox

def convert_length():
    try:
        meters = float(entry_meters.get())
        kilometers = meters / 1000
        centimeters = meters * 100

        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"{meters} meters is:\n")
        result_text.insert(tk.END, f"{kilometers} kilometers\n")
        result_text.insert(tk.END, f"{centimeters} centimeters")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.geometry("400x400")
root.title("Length Converter App")
root.configure(bg="#e0f7fa")  # Light cyan background

# Title label
label_title = tk.Label(
    root,
    text="Length Converter",
    font=("Helvetica", 16, "bold"),
    bg="#e0f7fa",
    fg="#006064"
)
label_title.pack(pady=20)

# Input label and entry
label_meters = tk.Label(root, text="Enter length in meters:", font=("Arial", 12), bg="#e0f7fa")
label_meters.pack()
entry_meters = tk.Entry(root, width=30)
entry_meters.pack(pady=10)

# Convert button
btn_convert = tk.Button(
    root,
    text="Convert",
    command=convert_length,
    bg="#00838f",  # Teal
    fg="white",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=5
)
btn_convert.pack(pady=10)

# Result text box
result_text = tk.Text(root, height=6, width=40, font=("Arial", 10))
result_text.pack(pady=20)

# Run the app
root.mainloop()
