#! coding: utf-8

from sys import argv
script, path, write_file = argv

from os import listdir
from os.path import isfile
from os.path import join

data = {}

for dir_entry in listdir(path):
    # Opens and reads directory entry if it is a file
    dir_entry_path = join(path, dir_entry)
    if isfile(dir_entry_path):
        with open(dir_entry_path, 'r') as my_file:
            data[dir_entry] = my_file.read()
