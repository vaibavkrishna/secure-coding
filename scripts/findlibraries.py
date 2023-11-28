import os
import re

def find_libraries_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # Use a regular expression to find library includes
        matches = re.findall(r'#include\s*<(.+?)>', content)
        return matches

def process_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(('.c', '.h')):
                file_path = os.path.join(root, file_name)
                libraries = find_libraries_in_file(file_path)
                if libraries:
                    print(f"Libraries in {file_path}: {', '.join(libraries)}")

if __name__ == "__main__":
    # Change the directory path accordingly
    start_directory = "/path/to/your/directory"
    process_directory(start_directory)
