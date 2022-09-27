import os
import sys

if __name__ == '__main__':

    directory = "../LabGen"
    files = os.listdir(directory)
    py_files = [file for file in files if file.endswith(".py")]
    with open("all_files.py", "w") as f:
        for file in py_files:
            f.write(file + "\n")




