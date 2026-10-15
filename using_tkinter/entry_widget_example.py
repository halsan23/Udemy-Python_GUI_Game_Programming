import subprocess
import os
import tkinter as tk
from tkinter import *

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

# Entry Widget Example
# Create a Login Form
# Initialization
# --------------------------------------------------------------------------------
root = Tk()

root.title("Tkinter Entry Widgets")

# setting the windows size
root.geometry("600x400")
root.config(bg="#362d2d")

# declaring string variables for name and password
name_var = StringVar()
pswd_var = StringVar()
# --------------------------------------------------------------------------------


# defining a function that will get the name and password
# to output them on the screen
# --------------------------------------------------------------------------------
def submit():

    name = name_var.get()
    password = pswd_var.get()

    print("The name is : " + name)
    print("The password is : " + password)

    name_var.set("")
    pswd_var.set("")


# --------------------------------------------------------------------------------


# Input
# --------------------------------------------------------------------------------
# creating a label for the name using widget Label
name_label = Label(root, text="Username", font=("calibre", 13, "bold"), padx=7, pady=3)

# creating a Inout Entry for name using widget Entry
name_entry = Entry(
    root, textvariable=name_var, font=("calibre", 18, "normal"), bg="#dcf6e3"
)
# name_entry.insert(0, "Email Address")


# creating a label for password
pswd_label = Label(root, text="Password", font=("calibre", 13, "bold"), padx=7, pady=3)

# creating a entry for password
pswd_entry = Entry(
    root,
    textvariable=pswd_var,
    font=("calibre", 18, "normal"),
    bg="#dcf6e3",
    show="*",
)


# creating a Submit Button using the button
# widget that will call the submit function
sub_btn = Button(root, text="Submit", font=("calibre", 13, "bold"), command=submit)
# --------------------------------------------------------------------------------


# Placement
# placing the label and entry in the required#
# position using the grid method
# --------------------------------------------------------------------------------
name_label.grid(row=0, column=0, padx=15, pady=10)
name_entry.grid(row=0, column=1, pady=10)

pswd_label.grid(row=1, column=0, padx=15, pady=10)
pswd_entry.grid(row=1, column=1, pady=10)

sub_btn.grid(row=2, column=1, pady=10)
# --------------------------------------------------------------------------------


# run the app
root.mainloop()
