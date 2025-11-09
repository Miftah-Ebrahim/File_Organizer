"""
Automated File Organizer Script
A simple Python program to automatically organize files into folders by type.

Created by: [Miftah Ebrahim]
Date: November 2025
"""

import os
import shutil
from pathlib import Path

class FileOrganizer:
    """Organizes files into folders based on their file extensions."""
    
    def __init__(self, folder_path):
        """
        Set up the file organizer.
        
        folder_path: The folder containing files to organize
        """
        self.folder = Path(folder_path)
        
        # Check if folder exists
        if not self.folder.exists():
            raise ValueError(f"Folder not found: {folder_path}")
        
        # Dictionary to map file types to folder names
        self.file_types = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
            'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx'],
            'Music': ['.mp3', '.wav', '.flac', '.aac', '.m4a'],
            'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.webm'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.json'],
            'Miscellaneous': []  # For files that don't match any category
        }
        
        # Keep track of what we've done
        self.moved_files = {}
        self.error_count = 0
    
    
    def get_file_category(self, file_extension):
        """
        Figure out which folder a file should go into based on its extension.
        
        file_extension: The file extension like '.jpg' or '.pdf'
        Returns: The folder name like 'Images' or 'Documents'
        """
        # Make sure extension is lowercase for comparison
        file_extension = file_extension.lower()
        
        # Check each category to see if the extension matches
        for category, extensions in self.file_types.items():
            if file_extension in extensions:
                return category
        
        # If no match found, put it in Miscellaneous
        return 'Miscellaneous'
    
    
    def create_folders(self):
        """Create all the category folders if they don't already exist."""
        print("\nCreating folders...")
        
        for folder_name in self.file_types.keys():
            folder_path = self.folder / folder_name
            
            # Create folder if it doesn't exist
            if not folder_path.exists():
                folder_path.mkdir()
                print(f"  ✓ Created: {folder_name}/")
            else:
                print(f"  • Already exists: {folder_name}/")
    
    
    def move_file(self, file_path, category):
        """
        Move a file to its category folder.
        
        file_path: Path to the file to move
        category: Name of the destination folder
        Returns: True if successful, False if there was an error
        """
        destination_folder = self.folder / category
        destination_path = destination_folder / file_path.name
        
        try:
            # If a file with the same name already exists, add a number to it
            if destination_path.exists():
                base_name = file_path.stem  # filename without extension
                extension = file_path.suffix  # the .jpg or .pdf part
                counter = 1
                
                # Keep trying until we find a name that doesn't exist
                while destination_path.exists():
                    new_name = f"{base_name}_{counter}{extension}"
                    destination_path = destination_folder / new_name
                    counter += 1
                
                print(f"  ⚠ Renamed to {destination_path.name} (duplicate found)")
            
            # Actually move the file
            shutil.move(str(file_path), str(destination_path))
            
            # Track what we moved
            if category not in self.moved_files:
                self.moved_files[category] = 0
            self.moved_files[category] += 1
            
            return True
            
        except PermissionError:
            print(f"  ✗ Can't move {file_path.name} - permission denied")
            self.error_count += 1
            return False
            
        except Exception as e:
            print(f"  ✗ Error moving {file_path.name}: {e}")
            self.error_count += 1
            return False
    
    
    def organize_files(self):
        """Main function to organize all files in the folder."""
        print(f"\nOrganizing files in: {self.folder}")
        print("=" * 60)
        
        # Create the category folders first
        self.create_folders()
        
        # Get all files in the folder (but not subdirectories or hidden files)
        all_files = [f for f in self.folder.iterdir() 
                     if f.is_file() and not f.name.startswith('.')]
        
        # Don't organize the Python script itself
        all_files = [f for f in all_files if f.suffix != '.py']
        
        print(f"\nFound {len(all_files)} file(s) to organize\n")
        
        if len(all_files) == 0:
            print("No files to organize!")
            return
        
        # Move each file to its category folder
        print("Moving files...")
        for file_path in all_files:
            extension = file_path.suffix
            category = self.get_file_category(extension)
            
            print(f"  → {file_path.name} → {category}/", end="")
            
            if self.move_file(file_path, category):
                print(" ✓")
        
        # Show summary of what we did
        self.show_summary()
    
    
    def show_summary(self):
        """Print a summary of how many files were moved to each folder."""
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)
        
        total = 0
        
        # Show results for each category
        for category in sorted(self.moved_files.keys()):
            count = self.moved_files[category]
            print(f"{category:20s}: {count} file(s)")
            total += count
        
        print("-" * 60)
        print(f"Total files organized: {total}")
        
        if self.error_count > 0:
            print(f"Errors encountered: {self.error_count}")
        
        print("=" * 60)


# Main program starts here
def main():
    """Run the file organizer program."""
    
    print("=" * 60)
    print("FILE ORGANIZER")
    print("=" * 60)
    print("\nThis program will organize your files into folders by type.")
    print()
    
    # Ask user which folder to organize
    folder_input = input("Enter the folder path to organize (or press Enter for current folder): ")
    
    # Use current folder if nothing was entered
    if folder_input.strip() == "":
        folder_path = "."
    else:
        folder_path = folder_input.strip()
    
    try:
        # Create the organizer and run it
        organizer = FileOrganizer(folder_path)
        organizer.organize_files()
        
        print("\n Done! Your files have been organized.")
        
    except ValueError as e:
        print(f"\n Error: {e}")
        
    except KeyboardInterrupt:
        print("\n\n Cancelled by user.")
        
    except Exception as e:
        print(f"\n Something went wrong: {e}")


# This runs the program when you execute the script
if __name__ == "__main__":
    main()