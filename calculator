import tkinter as tk

def evaluate_expression():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_click(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + char)

def clear_entry():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    if current:
        entry.delete(len(current) - 1)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

entry = tk.Entry(root, width=30, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', '<-'  # Added backspace button
]

row, col = 1, 0

for button_text in button_texts:
    if button_text == '=':
        tk.Button(root, text=button_text, command=evaluate_expression, width=10, height=2, font=('Arial', 16)).grid(row=row, column=col, padx=5, pady=5)
    elif button_text == 'C':
        tk.Button(root, text=button_text, command=clear_entry, width=10, height=2, font=('Arial', 16)).grid(row=row, column=col, padx=5, pady=5)
    elif button_text == '<-':
        tk.Button(root, text=button_text, command=backspace, width=10, height=2, font=('Arial', 16)).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=button_text, command=lambda char=button_text: button_click(char), width=10, height=2, font=('Arial', 16)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
