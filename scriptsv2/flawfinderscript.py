import os
import subprocess

def run_flawfinder(directory, output_file):
    # Run flawfinder on C source code files in the given directory
    command = ["flawfinder", directory]
    subprocess.run(command, stdout=output_file, stderr=subprocess.PIPE)

def process_folders(base_directory, output_file):
    # Get the list of folders in the base directory
    folders = [f for f in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, f))]

    for folder in folders:
        # Construct the full path to the folder
        folder_path = os.path.join(base_directory, folder)

        # Run flawfinder on the folder and append the output to the specified file
        output_file.write(f"Running flawfinder on: {folder_path}\n")
        run_flawfinder(folder_path, output_file)
        output_file.write("\n" + "-"*50 + "\n")  # Separator line

# Use the current working directory as the base directory
base_directory = os.getcwd()

# Define the output file path
output_file_path = os.path.join(base_directory, "flawfinder_output.txt")

# Open the output file in write mode (create or overwrite)
with open(output_file_path, "w") as output_file_obj:
    # Start processing folders in the base directory
    process_folders(base_directory, output_file_obj)

print(f"All flawfinder outputs saved to: {output_file_path}")
