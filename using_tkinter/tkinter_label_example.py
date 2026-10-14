import subprocess
import os
import tkinter as tk
from tkinter import *

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

# Label Examples

root = tk.Tk()
root.title("Python Tkinter Label Example")

label = tk.Label(
    root,
    text="Python Tkinter Labels",
    font=("Arial", 16, "bold"),
    bg="lightblue",
    fg="darkblue",
    width=20,
    height=2,
    relief="raised",
)

label.pack(padx=35, pady=50)

root.mainloop()
