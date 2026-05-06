import tkinter as tk

# Function to update expression
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate final expression
def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the entry
def clear():
    global expression
    expression = ""
    equation.set("")

# Main window
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Python Calculator")
    root.geometry("300x400")
    root.configure(bg="black")

    expression = ""
    equation = tk.StringVar()

    entry = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
    entry.grid(row=0, column=0, columnspan=4)

    # Buttons
    buttons = [
        ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
        ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
        ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
        ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ]

    for (text, row, col) in buttons:
        if text == "=":
            tk.Button(root, text=text, padx=20, pady=20, command=equalpress).grid(row=row, column=col)
        else:
            tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: press(t)).grid(row=row, column=col)

    tk.Button(root, text="C", padx=20, pady=20, command=clear).grid(row=5, column=0, columnspan=4, sticky="we")

    root.mainloop()
