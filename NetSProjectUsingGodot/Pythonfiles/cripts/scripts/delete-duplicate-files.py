import os
import hashlib
import tkinter as tk
from tkinter import filedialog

def calculate_hash(file_path):
    # Calculate the MD5 hash of the file
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buffer = file.read(4096)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = file.read(4096)
    return hasher.hexdigest()

def find_duplicate_files(directory):
    file_hashes = {}
    duplicates = []

    # Iterate over all files in the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = calculate_hash(file_path)

            # Check if the hash already exists in the dictionary
            if file_hash in file_hashes:
                duplicates.append((file_hashes[file_hash], file_path))
            else:
                file_hashes[file_hash] = file_path

    return duplicates

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Deleted file: {file_path}")
    except Exception as e:
        print(f"Error deleting file: {str(e)}")

# Create a Tkinter root window to display the directory selection dialog
root = tk.Tk()
root.withdraw()

# Prompt the user to select the directory using a dialog
directory_to_scan = filedialog.askdirectory(title="Select Directory to Scan for Duplicate Files")

# Check if a directory was selected
if directory_to_scan:
    # Find duplicate files in the selected directory
    duplicate_files = find_duplicate_files(directory_to_scan)

    # Print the list of duplicate files
    if duplicate_files:
        print("Duplicate files found:")
        for duplicate in duplicate_files:
            print(f"Original: {duplicate[0]}")
            print(f"Duplicate: {duplicate[1]}")
            print("-----------")
            delete_duplicate = input("Do you want to delete the duplicate file? (y/n): ")
            if delete_duplicate.lower() == 'y':
                delete_file(duplicate[1])
                print("-----------")
    else:
        print("No duplicate files found.")
else:
    print("No directory selected.")
