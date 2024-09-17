#!/usr/bin/env python3
import os
from colorama import Fore


files = os.listdir()


this_file = "rename.py"

def allow_write_mode():
    try:
        os.system("sudo chmod  755 ./*")
        print(Fore.GREEN + " > WRITE PRIVILEGES OBTAINED",Fore.RESET)
    except:
        print(Fore.RED + " > Error while tying to get write privileges",Fore.RESET)
        
def rename_file(file):

    try:
        new_file = file.split("(")
        name = file.split("(")[0].strip()
        ext = os.path.splitext(new_file[1])[1].strip()
        new_name = name + ext
        os.rename(file,new_name)
        print(Fore.YELLOW,f" > Renamed {file} into {new_name}",Fore.RESET)
    except: 
        print(Fore.RED,f" > Error while renaming {file}",Fore.RESET)
    

# per linux
allow_write_mode()

for file in files:
    if os.path.isfile(file) and file != "rename.py":
    	rename_file(file)
