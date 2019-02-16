import os

path = os.getcwd()

file_list = os.listdir(os.getcwd())

for file in file_list:
    if (file.startswith('hd')):
        os.rename(file, file[3:])