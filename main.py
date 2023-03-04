import os
import shutil

downloads_folder = os.path.expanduser("D:\Downloads") #the downloads folder path
images_folder = os.path.expanduser("D:\Downloads\Downloads_Images") #the new folder path

if not os.path.exists(images_folder):
    os.makedirs(images_folder) #Check if the folder name&path already exists. if not, Python will create the folder.

for file_name in os.listdir(downloads_folder):
    if file_name.endswith(".png") or file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
        file_path = os.path.join(downloads_folder, file_name)
        shutil.move(file_path, images_folder) #goes through all files in the Downloads folder, and moves files that ends with images extension to the new folder.
        
