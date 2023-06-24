import os
import shutil

def organize_files(source_directory):
    # Create folders for different file types
    image_folder = os.path.join(source_directory, 'Images')
    pdf_folder = os.path.join(source_directory, 'PDFs')

    # Create the folders if they don't exist
    os.makedirs(image_folder, exist_ok=True)
    os.makedirs(pdf_folder, exist_ok=True)

    # Get the list of files in the source directory
    files = os.listdir(source_directory)

    # Organize each file into the appropriate folder
    for file in files:
        file_path = os.path.join(source_directory, file)

        if os.path.isfile(file_path):
            # Get the file extension
            file_extension = os.path.splitext(file)[1].lower()

            # Move image files to the Images folder
            if file_extension in ['.jpg', '.jpeg', '.png', '.gif']:
                shutil.move(file_path, os.path.join(image_folder, file))
                print(f'Moved {file} to Images folder.')

            # Move PDF files to the PDFs folder
            elif file_extension == '.pdf':
                shutil.move(file_path, os.path.join(pdf_folder, file))
                print(f'Moved {file} to PDFs folder.')

            # Skip files with other extensions
            else:
                print(f'Skipped {file}. Not an image or PDF file.')


# Prompt the user to enter the directory path
source_directory = input("Enter the directory path to organize: ")

# Call the function to organize files
organize_files(source_directory)

