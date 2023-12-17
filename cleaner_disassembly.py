import os
import re
import sys

print ("Format for all files must be in numeric order. For scripts ex. 1.py, 2.py. For disassembly ex. 1.dism, 2.dism.");

dir_scripts = input("Please enter script directory: ");
if os.path.exists(dir_scripts) == False and os.path.isdir(dir_scripts) == False:
    sys.exit("Script directory is not a directory.");
 
dir_disms = input("Please enter disassembly directory: ");
if os.path.exists(dir_disms) == False and os.path.isdir(dir_disms) == False:
    sys.exit("Script directory is not a directory.");

ex_disms = input("Please enter disassembly file extension: ");

list_scripts = os.listdir(dir_scripts);
for file_name in list_scripts:
    match = re.search(r'\d+', file_name);
    if match:
        dism = os.path.join(dir_disms, str(match.group()) + "." + ex_disms);
        if os.path.exists(dism) == False:
            print("Mismatch between disassembly and script deleting: " + file_name);
            file_path = os.path.join(dir_scripts, file_name);
            os.remove(file_path);
    else:
        sys.exit("File does not have a numeric name.");