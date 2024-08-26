import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)

def organize_files():
    source_folder = Path(folder_path.get())
    destination_folder = Path(folder_path.get()) / 'output'
    destination_folder.mkdir(exist_ok=True)

    # Logic for organizing files based on metadata
    # Importing the backend functions
    from backend.services.organizing import organize_files

    # Organize files
    try:
        if source_folder.is_dir():
            organize_files(source_folder, destination_folder)
            messagebox.showinfo("Success", "Files organized successfully!")
        else:
            messagebox.showerror("Error", "Please select a valid directory")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("File Organizer")

# Folder selection
folder_path = tk.StringVar()
tk.Label(root, text="Select Folder:").pack(pady=10)
tk.Entry(root, textvariable=folder_path, width=50).pack(pady=10)
tk.Button(root, text="Browse", command=select_folder).pack(pady=10)

# Organize button
tk.Button(root, text="Organize Files", command=organize_files).pack(pady=20)

# Start the GUI loop
root.mainloop()