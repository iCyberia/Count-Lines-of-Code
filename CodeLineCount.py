import os
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return sum(1 for line in file)
    except:
        return 0

def count_files_and_lines(directory):
    total_files = 0
    total_lines = 0
    file_details = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = Path(root) / file
            if file_path.is_file():
                total_files += 1
                lines_in_file = count_lines_in_file(file_path)
                total_lines += lines_in_file
                file_details.append((file_path, lines_in_file))
    
    return total_files, total_lines, file_details

def browse_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path

if __name__ == "__main__":
    folder_path = browse_folder()
    if folder_path:
        total_files, total_lines, file_details = count_files_and_lines(folder_path)
        print(f"Total number of files: {total_files}")
        print(f"Total number of lines: {total_lines}")
        for file_path, lines in file_details:
            print(f"{file_path}: {lines} lines")
    else:
        print("No folder selected.")
