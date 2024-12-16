import subprocess
import sys
import os

def install_requirements():
    """Install the packages from requirements.txt."""
    if not os.path.exists('requirements.txt'):
        print("requirements.txt file is missing!")
        return

    # Run pip to install the packages from requirements.txt
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Install required packages when the script starts
install_requirements()

# Your original code here...
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import messagebox
import webbrowser

def open_link(event):
    webbrowser.open("https://buymeacoffee.com/javisek")

def remove_framer_badge(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        updated_content = content.replace('<div id="__framer-badge-container"></div>', '')
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        messagebox.showinfo("Success", f"The badge div has been removed from {os.path.basename(file_path)}.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def on_drop(event):
    file_path = event.data.strip()
    if os.path.exists(file_path) and file_path.endswith('.html'):
        remove_framer_badge(file_path)
    else:
        messagebox.showerror("Error", "Invalid file. Please drag and drop a valid .html file.")

def create_gui():
    root = TkinterDnD.Tk()
    root.title("deFramer")
    root.geometry("850x650")
    root.resizable(False, False)
    root.configure(bg="#212121")

    header = tk.Label(
        root,
        text="deFramer Tool By Javaseq",
        font=("Arial", 16, "bold"),
        bg="#212121",
        fg="#F5F5F5",
        pady=60
    )
    header.pack()

    instruction = tk.Label(
        root,
        text="DROP your .html file",
        font=("Arial", 12),
        bg="#212121",
        fg="#888888",
    )
    instruction.pack(pady=25)

    drop_area = tk.Label(
        root,
        text="DROP FILE HERE",
        font=("Arial", 14, "bold"),
        bg="#151515",
        fg="#888888",
        width=30,
        height=5,
        relief="groove",
        bd=0
    )
    drop_area.pack(pady=20)

    root.drop_target_register(DND_FILES)
    root.dnd_bind("<<Drop>>", on_drop)

    footer = tk.Label(
        root,
        text="❤️ DONATE ❤️",
        font=("Arial", 10),
        bg="#2E3440",
        fg="#81A1C1",
        cursor="hand2"
    )
    footer.pack(side=tk.BOTTOM, pady=10)
    footer.bind("<Button-1>", open_link)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
