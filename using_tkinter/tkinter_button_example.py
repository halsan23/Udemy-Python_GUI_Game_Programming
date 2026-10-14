import subprocess
import os
import tkinter as tk
from tkinter import *

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

# Button Examples


def button_clicked():
    print("Button clicked!")


root = tk.Tk()
root.title("Python Tkinter Button Example")

# Original Image
img = PhotoImage(file="images/yingYang.png")

# to enlarge the image
# img = img.zoom(3)

# to reduce the imagez
# img = img.subsample(2)

# Creating a button with specified options
button = Button(
    root,
    text="Click Me",
    command=button_clicked,
    activebackground="blue",
    activeforeground="white",
    anchor="center",
    bd=3,
    bg="lightgray",
    cursor="hand2",
    disabledforeground="gray",
    fg="black",
    font=("Arial", 24, "bold"),
    height=2,
    highlightbackground="black",
    highlightcolor="green",
    highlightthickness=2,
    justify="center",
    overrelief="raised",
    padx=40,
    pady=60,
    image=img,
    compound="left",
)

button.pack(padx=60, pady=50)

root.mainloop()
