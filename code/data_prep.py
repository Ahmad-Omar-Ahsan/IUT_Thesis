import os
from shutil import copyfile
dest = 'preprocessed_data'
for root, dirs, files in os.walk("./data", topdown=False):
    for name in files:
        file_name = name.split('.')
        file_path = os.path.join(root, name)
        if file_name[-1] == 'txt' and file_name[-2] == 'quantification':
            try:
                copyfile(file_path, os.path.join(dest, name))
            except:
                continue


