"""
To rename folders which are intially named like "n02085620-Chihuahua" to just "Chihuahua"
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Define the directory path
root_dir = os.environ.get("root_dir")

for folder in os.listdir(root_dir):
    directory_path = os.path.join(root_dir, folder)

    # List all folders in the directory
    folders = [
        f
        for f in os.listdir(directory_path)
        if os.path.isdir(os.path.join(directory_path, f))
    ]

    # Rename the folders
    for folder in folders:
        # Define the new name for the folder (you can modify this logic as needed)
        new_folder_name = folder.split("-")[1].replace("_", " ")

        # Get the full paths of the old and new folders
        old_folder_path = os.path.join(directory_path, folder)
        new_folder_path = os.path.join(directory_path, new_folder_name)

        # Rename the folder
        os.rename(old_folder_path, new_folder_path)

print("Folders renamed successfully.")
