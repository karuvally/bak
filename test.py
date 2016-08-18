#!/usr/bin/env python3
# test file

# import some serious stuff
import os
from os.path import join, getsize


# test function
def find_directory_size(source_directory_path):
    total_size = 0
    for root, sub_directories, files in os.walk(source_directory_path):
        for file in files:
            total_size += getsize(join(root, file))
    total_size = int(total_size / 1024)
    return total_size


directory_size = find_directory_size('/home/aswin/Music')
print(directory_size)