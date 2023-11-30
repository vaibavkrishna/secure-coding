import os
import subprocess

def run_cppcheck(file_path, output_file):
    # Run cppcheck on the given file and append the output to the specified file
    command = ["cppcheck", file_path]
    with open(output_file, "a") as output:
        output.write(f"Running cppcheck on: {file_path}\n")
        subprocess.run(command, stdout=output, stderr=subprocess.PIPE)
        output.write("\n" + "-"*50 + "\n")  # Separator line

def process_files(directory, output_file):
    # Get the list of files in the directory
    files = os.listdir(directory)

    for file in files:
        # Construct the full path to the file
        file_path = os.path.join(directory, file)

        if os.path.isdir(file_path):
            # If the item is a directory, recursively process its contents
            process_files(file_path, output_file)
        elif file_path.endswith((".c", ".h")):
            # If the item is a C or C++ header file, run cppcheck
            print(f"Running cppcheck on: {file_path}")
            run_cppcheck(file_path, output_file)

# Define the output file path
output_file_path = os.path.join(os.getcwd(), "cppcheck_output.txt")

# Start processing files in the current working directory
current_directory = os.getcwd()
process_files(current_directory, output_file_path)

print(f"All cppcheck outputs saved to: {output_file_path}")
