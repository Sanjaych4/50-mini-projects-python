# Day 27: Display directories, subdirectories, files in a tree structure

import os

def print_tree(dir_path, padding=''):
    """
    Prints the directory tree structure recursively.
    """
    if not os.path.isdir(dir_path):
        print(f"{padding}{os.path.basename(dir_path)}")
        return
    print(f"{padding}[{os.path.basename(dir_path)}]")
    padding = padding + '  '
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        print_tree(item_path, padding)

# Example usage
print_tree(os.getcwd())

