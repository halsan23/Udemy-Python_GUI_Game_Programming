import subprocess
import os

import tkinter as tk
from tkinter import *

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


# defines a name for the current window, in this case, 'root'
root = Tk()

# configure the window
# ---------------------------------
root.geometry("800x600")
# defines the WINDOW dimensions
root.config(bg="#12130F")
# set the background color for the WINDOW
# ---------------------------------


# Configure a LABEL
# ---------------------------------
label = Label(
    root,
    text="Python World",
    font=("Arial", 25, "bold"),
    fg="yellow",
    bg="teal",
    relief="raised",
    bd=10,
)
# root : tells it to place the label in the window defined as root
#       *** See NEXT ***

# text : sets the text for the label : 'Python World'
# font : sets the font options for the label
# fg : sets the text color for the LABEL text, (not the window)
# bg : sets the background color for the LABEL text, (not the window)
# relief : sets the border style
# bd : sets a border width
# ---------------------------------

# *** NEXT *** instead of setting the text for the label within the tk,Label definition, you can set it as a separate line of code, such as:
# label.config(text="Python World")
# or
# label["text"] = "Python World"
# ---------------------------------

# you may at times need to output the label text to the console, soy for debugging or other purposes.
# use the cget() method to do this:
# text = label.cget("text")
#   OR USE
text = label["text"]
#   then
print(text)
# this must be done BEFORE you 'pack' and run the 'mainloop'
# ---------------------------------


label.pack()
# actually places the label inside the 'root' window

root.mainloop()
# runs the GUI loop to show the window.
# this runs as an infinite loop until the window is closed or until the application is shut down by other means

# ---------------------------------------------------------------------------

# Example:
# In this example, a Tkinter window is created and display a styled label with custom font, colors, size and border. This shows how labels are used in real GUI applications.

# ---------------------------------
# import tkinter as tk

# root = tk.Tk()
# root.geometry("400x200")
# root.title("Label Example")

# lbl = tk.Label(
#     root,
#     text="Welcome to Tkinter",
#     font=("Arial", 16, "bold"),
#     bg="lightblue",
#     fg="darkblue",
#     width=20,
#     height=2,
#     relief="raised",
# )

# lbl.pack(pady=30)
# root.mainloop()
# ---------------------------------

# root.geometry("400x200") : sets the window size.
# tk.Label(... text="Welcome to Tkinter" ...) : creates the label with text.
# font=("Arial", 16, "bold") : styles the text.
# bg="lightblue" : sets label background color.
# fg="darkblue" : sets text color.
# relief="raised" : adds border style.
# lbl.pack(pady=30) : displays the label with spacing.

# ---------------------------------------------------------------------------
