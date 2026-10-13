import subprocess
import os
import tkinter as tk
from tkinter import *

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


# Initialize the main application window
parent = tk.Tk()
parent.title("Image in Button Example")

# Load the image
image = PhotoImage(file="images/temp.gif")

# Create the Button widget and set the image
button = tk.Button(parent, image=image)
button.pack(padx=20, pady=20)

# Keep a reference to the image
# to prevent garbage collection
button.image = image

# Run the application
parent.mainloop()
