import random
import string
import tkinter as tk
from tkinter import filedialog

def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password):
    """Prompt the user to save the password in a file."""
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    
    if file_path:
        with open(file_path, 'w') as file:
            file.write(password)
        print("Password saved successfully!")
    else:
        print("No file selected. Password not saved.")

def main():
    # Generate a password
    password = generate_password()
    print("Generated Password:", password)
    
    # Prompt the user to save the password
    response = input("Copy the password and press Enter to save it: ")
    
    if response == '':
        save_password(password)
    else:
        print("Password not saved.")

if __name__ == "__main__":
    main()
