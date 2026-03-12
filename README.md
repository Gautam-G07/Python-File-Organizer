# Python File Organizer

## Overview

This project is a simple Python automation script that organizes files in a folder into categorized directories based on their file extensions.
It helps keep directories clean by automatically moving files like PDFs, images, text files, presentations, and music into their respective folders.

The script scans a specified directory and sorts files into predefined folders.

---

## Features

* Automatically organizes files into folders
* Creates folders if they do not already exist
* Supports multiple file types
* Prevents errors if folders already exist
* Simple and lightweight automation script

---

## Supported File Types

| File Extension | Destination Folder |
| -------------- | ------------------ |
| `.txt`         | Text               |
| `.pdf`         | Pdfs               |
| `.pptx`        | ppts               |
| `.jpg`, `.png` | Images             |
| `.mp3`         | Music              |

---

## Technologies Used

* Python
* os module
* shutil module

---

## How It Works

1. The script scans all files inside the target directory.
2. It checks the extension of each file.
3. Based on the extension, the file is moved into the corresponding folder.
4. If the folder does not exist, the script automatically creates it.

---

## How to Run the Script

### 1. Clone the repository

```bash
git clone https://github.com/Gautam-G07/Python-File-Organizer.git
```

### 2. Navigate to the project directory

```bash
cd Python-File-Organizer
```

### 3. Run the script

```bash
python fileorganizer.py
```

---

## Example Folder Structure

Before running the script:

```
Documents
 ├── file1.pdf
 ├── notes.txt
 ├── presentation.pptx
 ├── song.mp3
 ├── image.jpg
```

After running the script:

```
Documents
 ├── Pdfs
 │   └── file1.pdf
 ├── Text
 │   └── notes.txt
 ├── ppts
 │   └── presentation.pptx
 ├── Music
 │   └── song.mp3
 ├── Images
 │   └── image.jpg
```

---

## Future Improvements

* Support for more file formats
* Automatic detection of file types
* GUI-based file organizer
* Custom folder configuration

---

## Author

Gautam G

