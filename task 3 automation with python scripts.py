import os
import shutil

# Define file categories and their extensions
file_categories = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    "Documents": ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    "Videos": ['.mp4', '.mkv', '.mov', '.avi', '.flv'],
    "Audio": ['.mp3', '.wav', '.flac', '.aac'],
    "Archives": ['.zip', '.rar', '.tar', '.gz'],
    "Others": []
}

# Function to create folders if they don't exist
def create_folders(base_path):
    for category in file_categories.keys():
        folder_path = os.path.join(base_path, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# Function to organize files
def organize_files(base_path):
    # List all files in the base folder
    for filename in os.listdir(base_path):
        file_path = os.path.join(base_path, filename)
        
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension
        file_extension = os.path.splitext(filename)[1].lower()
        
        # Check which category the file belongs to
        file_moved = False
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                category_folder = os.path.join(base_path, category)
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"Moved '{filename}' to '{category}' folder.")
                file_moved = True
                break
        
        # If no category matched, move to "Others"
        if not file_moved:
            others_folder = os.path.join(base_path, "Others")
            if not os.path.exists(others_folder):
                os.makedirs(others_folder)
            shutil.move(file_path, os.path.join(others_folder, filename))
            print(f"Moved '{filename}' to 'Others' folder.")

# Main function
def main():
    # Set the directory you want to organize
    folder_to_organize = input("Enter the full path of the folder you want to organize: ")
    
    # Check if the folder exists
    if not os.path.exists(folder_to_organize):
        print("The folder does not exist.")
        return
    
    # Create subfolders for organization
    create_folders(folder_to_organize)
    
    # Organize the files
    organize_files(folder_to_organize)
    
    print("Files have been organized.")

if __name__ == "__main__":
    main()