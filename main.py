import tkinter as tk
import random
import string

def generate_password(length):
    password = []
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.punctuation))
    for i in range(length-3):
        password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
    random.shuffle(password)
    password = ''.join(password)
    return password

def generate_button_click():
    try:
        length = int(charlength.get())
        if length < 6:
            message_label.config(text="Password must be at least 6 characters long.", fg="red")
        else:
            password = generate_password(length)
            password_label.config(text=password)
            message_label.config(text="Password generated successfully!", fg="green")
    except ValueError:
        message_label.config(text="Invalid input. Enter a number for password length.", fg="red")

def clear_button_click():
    password_label.config(text="")
    message_label.config(text="")
    charlength.set("")

root = tk.Tk()
root.geometry("400x150")
root.config(bg="white")

charlength = tk.StringVar()

length_label = tk.Label(root, text="Enter desired password length", bg="white", font=("Arial", 12))
length_label.pack()

charlength_entry = tk.Entry(root, textvariable=charlength, font=("Arial", 12))
charlength_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_button_click, font=("Arial", 12), bg="lightblue")
generate_button.pack()

clear_button = tk.Button(root, text="Clear", command=clear_button_click, font=("Arial", 12), bg="lightgray")
clear_button.pack()

password_label = tk.Label(root, text="", font=("Arial", 12), bg="white")
password_label.pack()

message_label = tk.Label(root, text="", font=("Arial", 12), bg="white")
message_label.pack()

root.mainloop()
