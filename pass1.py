import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    if password_length <= 0:
        password_result.set("Password length must be greater than 0")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        password_result.set("Generated Password:\n" + password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")  # Increase the window size

length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_result = tk.StringVar()
password_result.set("")

result_label = tk.Label(root, textvariable=password_result, font=("Arial", 14))  # Increase font size
result_label.pack()

root.mainloop()
