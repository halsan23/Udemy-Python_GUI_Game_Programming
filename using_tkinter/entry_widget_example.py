import subprocess
import os
import tkinter as tk
from tkinter import *

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

# Entry Widget Example | Create a Login Form

# Initialization
# --------------------------------------------------------------------------------
root = Tk()  # define the window

root.title("Tkinter Entry Widgets")  # Set the window title

# setting the windows size and background color
root.geometry("600x400")
root.config(bg="#362d2d")

# declaring string variables for name and password inputs
name_var = StringVar()
pswd_var = StringVar()
# --------------------------------------------------------------------------------


# FUNCTIONS
# delete the default name_var value for new input
# --------------------------------------------------------------------------------
def name_on_focus_in(event):
    if name_entry.get() != "":
        name_entry.delete(0, tk.END)


# restore the default name_var value if user clicks off of input without a value
# --------------------------------------------------------------------------------
def name_on_focus_out(event):
    if name_entry.get() == "":
        name_entry.insert(0, "User Name")


# delete the default password_var value for new input
# --------------------------------------------------------------------------------
def pswd_on_focus_in(event):
    if pswd_entry.get() != "":
        pswd_entry.delete(0, tk.END)
        pswd_entry.config(show="*")


# # restore the default name_var value if user clicks off of input without a value
# --------------------------------------------------------------------------------
def pswd_on_focus_out(event):
    if pswd_entry.get() == "":
        pswd_entry.insert(0, "Password")
        pswd_entry.config(show="")


# get the name and password to output them on the screen
# --------------------------------------------------------------------------------
def submit():

    name = name_var.get()
    password = pswd_var.get()

    print("The name is : " + name)
    print("The password is : " + password)

    name_var.set("")
    pswd_var.set("")


# userName Input
# --------------------------------------------------------------------------------
# creating a label for the name using widget Label
name_label = Label(root, text="Username", font=("calibre", 13, "bold"), padx=7, pady=3)

# creating an Entry for name using widget Entry
name_entry = Entry(root, textvariable=name_var, font=("calibre", 16, "normal"))
name_entry.insert(0, "User Name")
name_entry.bind("<FocusIn>", name_on_focus_in)
name_entry.bind("<FocusOut>", name_on_focus_out)
# --------------------------------------------------------------------------------


# password Input
# --------------------------------------------------------------------------------
# creating a label for password
pswd_label = Label(root, text="Password", font=("calibre", 13, "bold"), padx=7, pady=3)

# creating an entry for password
pswd_entry = Entry(root, textvariable=pswd_var, font=("calibre", 16, "normal"))
pswd_entry.insert(0, "Password")
pswd_entry.bind("<FocusIn>", pswd_on_focus_in)
pswd_entry.bind("<FocusOut>", pswd_on_focus_out)
# --------------------------------------------------------------------------------


# creating a Submit Button using the button
# --------------------------------------------------------------------------------
sub_btn = Button(root, text="Submit", font=("calibre", 13, "bold"), command=submit)
# --------------------------------------------------------------------------------


# Placing the label and entry in the required position using the grid method
# You could also us place() with less control on where items are placed
# --------------------------------------------------------------------------------
name_label.grid(row=0, column=0, padx=15, pady=10)
name_entry.grid(row=0, column=1, pady=10)

pswd_label.grid(row=1, column=0, padx=15, pady=10)
pswd_entry.grid(row=1, column=1, pady=10)

sub_btn.grid(row=2, column=1, pady=10)
# --------------------------------------------------------------------------------


# run the app
root.mainloop()
