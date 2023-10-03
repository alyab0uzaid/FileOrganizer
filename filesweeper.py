import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Function to organize files and relocate them to "Organized Files" in Documents directory
def organize_and_relocate(directory_to_organize):
    documents_directory = os.path.expanduser("~/Documents")
    organized_files_directory = os.path.join(documents_directory, "Organized Files")

    # Define destination folders (same as in your original script)
    organized_folders = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".doc", ".docx", ".pdf", ".txt", ".rtf"],
        "Illustrator Projects": [".ai", ".eps"],
        "PDF": [".pdf"],
        "Audio": [".mp3", ".wav", ".flac", ".aac"],
        "Video": [".mp4", ".mov", ".avi", ".mkv"],
        "Other": [],
    }

    # Create "Organized Files" directory if it doesn't exist
    if not os.path.exists(organized_files_directory):
        os.makedirs(organized_files_directory)

    # List files in the specified directory
    files = os.listdir(directory_to_organize)

    for filename in files:
        file_path = os.path.join(directory_to_organize, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine the file extension
        _, file_extension = os.path.splitext(filename)

        # Find the appropriate subdirectory or use "Other" if not found
        target_folder = "Other"
        for folder, extensions in organized_folders.items():
            if file_extension.lower() in extensions:
                target_folder = folder
                break

        # Create the subdirectory if it doesn't exist within "Organized Files"
        target_dir = os.path.join(organized_files_directory, target_folder)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # Move the file to the appropriate subdirectory within "Organized Files"
        target_file_path = os.path.join(target_dir, filename)
        shutil.move(file_path, target_file_path)
        print(f"Moved '{filename}' to 'Organized Files/{target_folder}'")

# Function to handle the "Browse" button click event
def browse_button_click():
    directory_to_organize = filedialog.askdirectory()
    if directory_to_organize:
        directory_var.set(directory_to_organize)

# Function to handle the "Organize" button click event
def organize_button_click():
    directory_to_organize = directory_var.get()
    if os.path.exists(directory_to_organize) and os.path.isdir(directory_to_organize):
        organize_and_relocate(directory_to_organize)
        result_label.config(text="Organizing and relocating complete.")
    else:
        result_label.config(text="Invalid directory. Please provide a valid directory path.")

# Create the main window
root = tk.Tk()
root.title("File Organizer")

# Create and configure widgets
directory_var = tk.StringVar()
directory_label = tk.Label(root, text="Select a directory to organize:")
directory_label.pack()
directory_entry = tk.Entry(root, textvariable=directory_var)
directory_entry.pack()
browse_button = tk.Button(root, text="Browse", command=browse_button_click)
browse_button.pack()
organize_button = tk.Button(root, text="Organize", command=organize_button_click)
organize_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()

