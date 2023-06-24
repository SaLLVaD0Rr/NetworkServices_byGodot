from PIL import Image
import os


def resize_images(directory, output_directory, width, height):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Iterate through the files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            # Open the image file
            image_path = os.path.join(directory, filename)
            img = Image.open(image_path)
            
            # Resize the image
            resized_img = img.resize((width, height))
            
            # Save the resized image to the output directory
            output_path = os.path.join(output_directory, filename)
            resized_img.save(output_path)
            
            print(f"Resized {filename} successfully.")


def main():
    directory = input("Enter the directory path containing the images: ")
    output_directory = input("Enter the output directory path for resized images: ")
    width = int(input("Enter the desired width: "))
    height = int(input("Enter the desired height: "))
    
    resize_images(directory, output_directory, width, height)


if __name__ == '__main__':
    main()
