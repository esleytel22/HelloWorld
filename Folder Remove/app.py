from pathlib import *
import glob
import shutil
import os

source = '/Users/cbonifacio.FILEBANKINC/Desktop/914277'
destination = '/Users/cbonifacio.FILEBANKINC/Desktop/temp'

list_of_folder = os.listdir(source)  #= ['A', 'B']
names = {}
for each_folder in list_of_folder:
    full_path = os.path.join(source, each_folder)
    os.chdir(full_path)  # change directory to the desired path

    for each_file in glob.glob('*'):
        with open(each_file) as f:
            print(f'{each_file} ---------- {each_folder}')
            shutil.copy(each_file, destination)
            #names[each_file] = sum(1 for line in f if line.strip())

    print(names)