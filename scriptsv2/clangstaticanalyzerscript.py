import os
import subprocess

def run_clang_static_analyzer(file_path, output_file):
    cmd = ["scan-build", "clang", "--analyze", file_path]
    with open(output_file, "a") as output:
        subprocess.run(cmd, stdout=output, stderr=subprocess.STDOUT)

def find_files(directory, extension):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_list.append(os.path.join(root, file))
    return file_list

def main():
    # Set the output file for the Clang Static Analyzer results
    output_file = "clang_static_analysis_results.txt"

    # Find all C and header files in the current directory and its subdirectories
    current_directory = os.getcwd()
    c_files = find_files(current_directory, (".c", ".h"))

    # Run Clang Static Analyzer for each file
    for c_file in c_files:
        run_clang_static_analyzer(c_file, output_file)

if __name__ == "__main__":
    main()
