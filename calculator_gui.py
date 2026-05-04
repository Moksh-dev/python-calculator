import tkinter as tk

# Create main window
root = tk.Tk()
root.title("🔥 Crazy Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry box
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Button click function
def click(value):
    entry.insert(tk.END, value)

# Clear screen
def clear():
    entry.delete(0, tk.END)

# Calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    
    for btn in row:
        button = tk.Button(
            frame,
            text=btn,
            font=("Arial", 14),
            command=lambda b=btn: (
                clear() if b == "C" else
                calculate() if b == "=" else
                click(b)
            )
        )
        button.pack(side="left", expand=True, fill="both")

# Run app
root.mainloop()