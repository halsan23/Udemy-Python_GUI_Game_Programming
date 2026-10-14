import subprocess
import os
import tkinter as tk
from tkinter import *

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

# Examples
root = tk.Tk()
root.title("Python Tkinter")

# widget(options)

# widget.pack(options)

root.mainloop()
