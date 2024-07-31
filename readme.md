# Project Title
Automated File Tree Generator

# Description
This project provides a Python script that generates a string representation of a file tree for a given directory and updates a README.md file with the generated file tree. The script allows for specifying directories to ignore during the file tree generation process.

# Features
- Generates a file tree representation of a specified directory.
- Ignores specified directories while generating the file tree.
- Automatically updates a README.md file with the generated file tree.

# Getting Started
# Prerequisites
- Python 3.x

# Installation
- Clone the repository:
```bash
git clone https://github.com/yourusername/automated-file-tree-generator.git
cd automated-file-tree-generator
```
- Install any required dependencies (if any).

# Usage
- Update the IGNORED_DIRS list in the script to specify any directories that should be ignored during the file tree generation process.
- Update the start_path and readme_path variables in the script to specify the directory to generate the file tree from and the path to the README.md file to be updated.
- Run the script:
```bash
python file_tree_generator.py
```

# Example
Assuming the following directory structure:
```css
scprp/
├── .git/
├── schema/
│   ├── items/
│   │   ├── weapons/
│   ├── other_items/
├── main.py
└── README.md
```
And IGNORED_DIRS set to [".git", "schema/items/weapons"], the generated file tree would look like this:
```css
📦scprp
 ┣ 📂schema
 ┃ ┣ 📂other_items
 ┣ 📜main.py
 ┣ 📜README.md
```
The README.md file will be updated to include this file tree under a section titled "File Tree".

# Script Details
## Functions
`should_ignore_dir(dir_path, ignored_dirs, start_path)`
Determines if a directory should be ignored based on the list of ignored directories.

- Args:
    - dir_path (str): The full path of the directory to check.
    - ignored_dirs (list): List of directory paths to ignore.
    - start_path (str): The starting path of the directory tree.
- Returns:
    - bool: True if the directory should be ignored, False otherwise.
`generate_file_tree(start_path)`
Generates a string representation of the file tree starting from the given path.
- Args:
    - start_path (str): The root path from which to generate the file tree.
- Returns:
    - str: A string representing the file tree.
`update_readme_with_file_tree(start_path, readme_path)`
Updates the README.md file with the generated file tree.
- Args:
    - start_path (str): The root path from which to generate the file tree.
    - readme_path (str): The path to the README.md file to be updated.