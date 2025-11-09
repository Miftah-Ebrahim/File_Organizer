# 📁 File Organizer

A Python script that automatically organizes files into categorized folders based on their file types.

## 🎯 Features

- Automatically sorts files into categories (Images, Documents, Music, Videos, etc.)
- Handles duplicate filenames intelligently
- Simple command-line interface
- Error handling for file permissions
- Progress tracking and summary report

## 📋 Requirements

- Python 3.6 or higher
- No external libraries needed (uses only standard library)

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/Miftah-Ebrahim/File_Organizer/blob/main/File_Organizer.py
cd file-organizer-project
```

2. Run the script:
```bash
python file_organizer.py
```

## 💻 Usage

### Basic Usage
```bash
python file_organizer.py
```

When prompted, enter the folder path you want to organize, or press Enter to organize the current directory.

### Example
```
Enter the folder path to organize (or press Enter for current folder): /Users/yourname/Downloads

Organizing files in: /Users/yourname/Downloads
============================================================
Creating folders...
  ✓ Created: Images/
  ✓ Created: Documents/
  ...

Found 15 file(s) to organize

Moving files...
  → vacation.jpg → Images/ ✓
  → report.pdf → Documents/ ✓
  ...
```

## 📂 File Categories

| Category | File Types |
|----------|------------|
| **Images** | .jpg, .jpeg, .png, .gif, .bmp, .svg |
| **Documents** | .pdf, .docx, .doc, .txt, .xlsx, .pptx |
| **Music** | .mp3, .wav, .flac, .aac, .m4a |
| **Videos** | .mp4, .mkv, .avi, .mov, .wmv |
| **Archives** | .zip, .rar, .7z, .tar, .gz |
| **Code** | .py, .js, .html, .css, .java, .json |
| **Miscellaneous** | Everything else |

## ⚙️ Customization

To add new file categories, edit the `file_types` dictionary in the `FileOrganizer` class:
```python
self.file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Ebooks': ['.epub', '.mobi', '.pdf'],  # Add your own!
    # ...
}
```

## 🛡️ Safety Features

- **Duplicate Protection**: Files with the same name get numbered (e.g., `file_1.jpg`)
- **Permission Handling**: Gracefully handles files that can't be moved
- **Non-destructive**: Only moves files, never deletes them

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

## 🙏 Acknowledgments

- Built as a learning project to practice Python file handling
- Inspired by the need to organize messy Downloads folders!

---

⭐ If you found this helpful, please star this repository!