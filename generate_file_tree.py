import os

# List of directories to ignore when generating the file tree
IGNORED_DIRS = [".git", "schema/items/weapons"]


def should_ignore_dir(dir_path, ignored_dirs, start_path):
    """
    Determines if a directory should be ignored based on the list of ignored directories.

    Args:
        dir_path (str): The full path of the directory to check.
        ignored_dirs (list): List of directory paths to ignore.
        start_path (str): The starting path of the directory tree.

    Returns:
        bool: True if the directory should be ignored, False otherwise.
    """
    relative_path = os.path.relpath(dir_path, start_path)
    for ignored in ignored_dirs:
        if relative_path == ignored or relative_path.startswith(f"{ignored}/"):
            return True
    return False


def generate_file_tree(start_path):
    """
    Generates a string representation of the file tree starting from the given path.

    Args:
        start_path (str): The root path from which to generate the file tree.

    Returns:
        str: A string representing the file tree.
    """
    file_tree = ""
    for root, dirs, files in os.walk(start_path):
        # Filter out directories that should be ignored
        dirs[:] = [
            d
            for d in dirs
            if not should_ignore_dir(os.path.join(root, d), IGNORED_DIRS, start_path)
        ]

        level = root.replace(start_path, "").count(
            os.sep
        )  # Determine the level of the current directory
        indent = " ┃ " * (level)  # Indentation based on the directory level
        base_name = os.path.basename(root)  # Get the base name of the current directory
        file_tree += f"{indent}┣ 📂{base_name}\n"  # Add the directory to the file tree
        sub_indent = " ┃ " * (level + 1)  # Indentation for files within the directory
        for f in files:
            file_tree += f"{sub_indent}┣ 📜{f}\n"  # Add files to the file tree
    return file_tree


def update_readme_with_file_tree(start_path, readme_path):
    """
    Updates the README file with the generated file tree.

    Args:
        start_path (str): The root path from which to generate the file tree.
        readme_path (str): The path to the README file to be updated.
    """
    # Generate the file tree string
    file_tree = f"```\n📦{start_path}\n" + generate_file_tree(start_path) + "```"

    # Read the current content of the README file
    with open(readme_path, "r") as readme_file:
        readme_content = readme_file.readlines()

    # Find the indices where the file tree should be inserted
    start_index = None
    end_index = None
    for i, line in enumerate(readme_content):
        if line.strip() == "# File Tree":
            start_index = i + 1
        if start_index and line.strip() == "```":
            end_index = i + 1

    # Update the README content with the new file tree
    if start_index is not None and end_index is not None:
        new_readme_content = (
            readme_content[:start_index]
            + [file_tree + "\n"]
            + readme_content[end_index:]
        )
    else:
        new_readme_content = readme_content + ["# File Tree\n", file_tree + "\n"]

    # Write the updated content back to the README file
    with open(readme_path, "w") as readme_file:
        readme_file.writelines(new_readme_content)


# Usage example
start_path = "scprp"  # The directory to generate the file tree from
readme_path = "README.md"  # The path to the README file to be updated
update_readme_with_file_tree(start_path, readme_path)
