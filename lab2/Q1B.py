# B.	
# Next, write another script, Q1B.py, that receives as parameter the name of a .py file in the current directory 
# (including the .py), e.g., x.py. Next, Q1B.py checks if the file contains a Python script, and if so, checks if the script
# contains a line that appends to a file called Q1B.out the string of the command that ran the script, if the script does not
# contain a line that appends to a file called Q1B.out the string of the command that ran the script then Q1B.py adds the line
# to the script. The line should append the command used to run the script and all its arguments to the file Q1B.out. 


import os
import sys

if __name__ == '__main__':
    directory = '/home/cse/Lab2/Solutions'
    files = os.listdir(directory)
    py_files = [file for file in files if file.endswith(".py")]
    for file in py_files:
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                if "Q1B.out" in line:
                    break
            else:
                with open(file, "a") as f:
                    f.write("with open('Q1B.out', 'a') as f:\n")
                    f.write("    f.write('" + " ".join(sys.argv) + "')\n")


                    
            