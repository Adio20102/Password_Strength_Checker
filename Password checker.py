import tkinter as tk
from tkinter import messagebox

def checkPassword(password):
    upperChars, lowerChars, specialChars, digits, length, spaces = 0, 0, 0, 0, 0, 0
    length = len(password)

    if(length==0):
        messagebox.showwarning("Password Strength Checker", "Password must not be blank!")
        return
    elif (length < 8):
        messagebox.showwarning("Password Strength Checker", "Password must be at least 8 characters long!")
        return
    else:
        for i in range(0, length):
            if (password[i].isupper()):
                upperChars += 1
            elif (password[i].islower()):
                lowerChars += 1
            elif (password[i].isdigit()):
                digits += 1
            else:
                specialChars += 1

    if (upperChars != 0 and lowerChars != 0 and digits != 0 and specialChars != 0):
        if (length >= 10):
            messagebox.showinfo("Password Strength Checker", "Password is strong.")
        else:
            messagebox.showinfo("Password Strength Checker", "Password is of medium strength.")
    else:
        messages = []
        if (upperChars == 0):
            messages.append("Password must contain at least one uppercase character!")
        if (lowerChars == 0):
            messages.append("Password must contain at least one lowercase character!")
        if (specialChars == 0):
            messages.append("Password must contain at least one special character!")
        if (digits == 0):
            messages.append("Password must contain at least one digit!")

        messagebox.showwarning("Password Strength Checker", "\n".join(messages))

def on_check_password():
    password = password_entry.get()
    checkPassword(password)

root = tk.Tk()
root.title("Password Strength Checker")

label = tk.Label(root, text="Enter Password :")
label.pack(pady=5, padx=100)

password_entry = tk.Entry(root)
password_entry.pack(pady=5, padx=100)

check_button = tk.Button(root, text=" Check ", command=on_check_password)
check_button.pack(pady=5, padx=100)

root.mainloop()