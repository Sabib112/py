import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        product = num1 * num2
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"The product of {num1} and {num2} is {product}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.geometry("400x300")
root.title("Getting Started with Widgets")
root.configure(bg="#f0f8ff")  # AliceBlue background

# Functionality description label
label_description = tk.Label(
    root, 
    text="This application multiplies two numbers entered by the user.",
    font=("Arial", 10),
    bg="#f0f8ff",
    wraplength=350,
    justify="left"
)
label_description.pack(pady=10)

# Labels for inputs
label_num1 = tk.Label(root, text="Enter first number:", bg="#f0f8ff", font=("Arial", 11))
label_num1.pack()
entry_num1 = tk.Entry(root, width=30)
entry_num1.pack(pady=5)

label_num2 = tk.Label(root, text="Enter second number:", bg="#f0f8ff", font=("Arial", 11))
label_num2.pack()
entry_num2 = tk.Entry(root, width=30)
entry_num2.pack(pady=5)

# Button to calculate the product
btn_calculate = tk.Button(
    root,
    text="Calculate Product",
    command=calculate_product,
    bg="#4CAF50",  # Green shade
    fg="white",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=5
)
btn_calculate.pack(pady=10)

# Text box to display the result
result_text = tk.Text(root, height=3, width=40, bg="#ffffff", fg="#000000", font=("Arial", 10))
result_text.pack(pady=10)

# Run the application
root.mainloop()
