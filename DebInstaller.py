import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import os
import sys

def install(path):
    return os.system(f"sudo apt install {path} -y > log.txt")

def preform_install():
    path = fd.askopenfilename()
    install(path)
    console_output.delete("1.0", tk.END)
    with open("log.txt") as log:
        console_output.insert("1.0", log.read())
    
    console_output.insert(tk.END, "\nLooks like it finished installing!")


isRoot = os.geteuid() == 0

if not isRoot:
    print("Please run this script as root/sudo!")
    sys.exit(0)

window = tk.Tk()
window.option_add("*foreground", "#000000")
window.title(".deb Installer")
window.geometry("640x480")
window.configure(bg="#AAA")

console_output = tk.Text(window)
console_output.insert("1.0", "Console output will go here...")
console_output.configure(background="#AAA")
console_output.pack()

acceptable_filetypes = (
    ("Debian Installer Packages", ".deb")
)

open_button = tk.Button(window, text="Pick File", command=preform_install)
open_button.configure(background="#AAA")
open_button.pack()

window.mainloop()