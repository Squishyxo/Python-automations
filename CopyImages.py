import os
import shutil

# Define the path to the root directory where the script should start searching for images
root_directory = "/"

# Define the path to the new folder where the images will be copied
new_folder_path = os.path.expanduser("~/Pictures/all_images")

# Create the new folder if it doesn't already exist
if not os.path.exists(new_folder_path):
    os.mkdir(new_folder_path)

# Loop through all files and directories under the root directory
for root, dirs, files in os.walk(root_directory):
    for file in files:
        # Check if the file is an image file
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            # Construct the paths to the original file and the copy
            original_file_path = os.path.join(root, file)
            copy_file_path = os.path.join(new_folder_path, file)
            # Copy the file to the new folder
            shutil.copy2(original_file_path, copy_file_path)
