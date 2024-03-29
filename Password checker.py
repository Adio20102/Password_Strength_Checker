import tkinter as tk
from tkinter import messagebox

def checkPassword(password):
    upperChars, lowerChars, specialChars, digits, length, spaces = 0, 0, 0, 0, 0, 0
    length = len(password)
    messages = []
    if(length==0):
        messages.append("Password must not be blank!")

    elif (length < 8):
        messages.append("Password must be at least 8 characters long!")
    blank_space = 0
    for i in range(0, length):
        if password[i] == " ":
            messages.append("Password must not contain blank spaces!")
            blank_space = 1
            break
    for i in range(0, length):
        if password[i].isupper():
            upperChars += 1
        elif password[i].islower():
            lowerChars += 1
        elif password[i].isdigit():
            digits += 1
        else:
            specialChars += 1

    if upperChars != 0 and lowerChars != 0 and digits != 0 and specialChars != 0 and blank_space == 0:
        if length >= 10:
            messagebox.showinfo("Password Strength Checker", "Password is strong.")
        elif 8 <= length < 10:
            messagebox.showinfo("Password Strength Checker", "Password is of medium strength.")
    else:

        if upperChars == 0:
            messages.append("Password must contain at least one uppercase character!")
        if lowerChars == 0:
            messages.append("Password must contain at least one lowercase character!")
        if specialChars == 0:
            messages.append("Password must contain at least one special character!")
        if digits == 0:
            messages.append("Password must contain at least one digit!")
    if len(messages) > 0:
        messagebox.showwarning("Password Strength Checker", "\n".join(messages))

def on_check_password():
    password = password_entry.get()
    checkPassword(password)

root = tk.Tk()
root.resizable(False, False)
root.title("Password Strength Checker")

label_font = ('Arial', 12)
label = tk.Label(root, text="Enter Password:",font=label_font)
label.pack(pady=5, padx=100)

entry_font = ('Arial', 16)
password_entry = tk.Entry(root,  font=entry_font, border=round(6))
password_entry.pack(pady=5, padx=100,ipady=4)

checkfont= ('Arial', 12)
check_button = tk.Button(root, text=" CHECK ", command=on_check_password,font=checkfont, width=10)
check_button.pack(pady=5, padx=100, ipady=2)

root.mainloop()
